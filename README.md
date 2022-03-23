# PN532 driver for MicroPython
MicroPython driver for PN532 NFC/RFID breakout boards. Based on the [CircuitPython driver by Adafruit](https://github.com/adafruit/Adafruit_CircuitPython_PN532).

### Compatibility
This driver has only been tested with the ESP32 using the [Grove NFC breakout board](https://wiki.seeedstudio.com/Grove_NFC/) in the default UART mode. 

Please let me know if you get this module successfully working with other hardware.

### Differences in the API from the CircuitPython version

- The timeout is expressed in milliseconds instead of seconds.
- The module name is different.
- Only UART is available
- _I2C and SPI are not available._ 

