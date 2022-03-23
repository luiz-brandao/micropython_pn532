"""
``pn532.uart``
====================================================

This module will let you communicate with a PN532 RFID/NFC shield or breakout
using UART.

* Author(s): Original Raspberry Pi code by Tony DiCola, CircuitPython by ladyada,
             refactor by Carter Nelson, MicroPython by Luiz Brandao

"""

import time

from pn532.pn532 import PN532, BusyError


class PN532_UART(PN532):
    """Driver for the PN532 connected over Serial UART"""

    def __init__(self, uart, *, reset=None, debug=False):
        """Create an instance of the PN532 class using Serial connection.
        Optional reset pin and debugging output.
        """
        self.debug = debug
        self._uart = uart
        super().__init__(debug=debug, reset=reset)

    def _wakeup(self):
        """Send any special commands/data to wake up PN532"""
        if self._reset_pin:
            self._reset_pin.value = True
            time.sleep(0.01)
        self.low_power = False
        self._uart.write(
            b"\x55\x55\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
        )  # wake up!
        self.SAM_configuration()

    def _wait_ready(self, timeout=1000):
        """Wait `timeout` milliseconds"""
        start = time.ticks_ms()
        while time.ticks_diff(time.ticks_ms(), start) < timeout:
            if self._uart.any() > 0:
                return True  # No Longer Busy
            time.sleep(0.01)  # lets ask again soon!
        # Timed out!
        return False

    def _read_data(self, count):
        """Read a specified count of bytes from the PN532."""
        frame = self._uart.read(count)
        if not frame:
            raise BusyError("No data read from PN532")
        if self.debug:
            print("Reading: ", [hex(i) for i in frame])
        return frame

    def _write_data(self, framebytes):
        """Write a specified count of bytes to the PN532"""
        while self._uart.any():
            self._uart.read()
        self._uart.write(framebytes)
