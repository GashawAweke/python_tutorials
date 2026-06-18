

# This is not Python's standard library.
import serial

# install: pip install pyserial
# PySerial allows Python to communicate with:

# * Arduino
# * ESP32
# * sensors
# * GPS modules
# * serial devices

# Communication happens over:

# ```text
# USB → Serial → Arduino
# ```


# `serial.Serial()`
# Creates a serial connection object.

# Constructor:

# ```python
# serial.Serial(
#     port,
#     baudrate,
#     timeout
# )
# ```

class SerialController:

    def __init__(
        self,
        port: str = "/dev/ttyACM0",
        baudrate: int = 9600
    ) -> None:

        self.arduino = serial.Serial(
            port,
            baudrate,
            timeout=1
        )

# Parameters:

# | Parameter | Meaning                |
# | --------- | ---------------------- |
# | port      | Device file            |
# | baudrate  | Communication speed    |
# | timeout   | Maximum read wait time |


# Common ports:

# Linux:

# ```text
# /dev/ttyACM0
# /dev/ttyUSB0
# ```

# Windows:

# ```text
# COM3
# COM4
# ```


# ===========================

# Common Serial Object Properties

# `.port`

# `.baudrate`

# `.is_open`: check connection status

class SerialController:

    def __init__(
        self,
        port: str = "/dev/ttyACM0",
        baudrate: int = 9600
    ) -> None:
        try:
            self.arduino = serial.Serial(
                port,
                baudrate,
                timeout=1
            )
            print("Connected")

        except serial.SerialException as e:
            print(f"Connection failed: {e}")
            raise


# call
controller = SerialController()


# `.close()`
# Closes serial connection.


# `.open()`
# Reopens connection.


# ======================

# `write()`

# `write()` sends bytes to the serial port.
# Serial communication sends bytes, not strings.


# Signature:
# write(data: bytes)


# This is invalid:
self.arduino.write("HELLO")

# This is correct:
self.arduino.write(
    "HELLO".encode()
)

# or

self.arduino.write(
    b"HELLO"
)


# ======================
#  `in_waiting`
# `in_waiting` is a property, not a method.
# No parentheses.
# It tells how many bytes are available for reading.


# The logic:

if self.arduino.in_waiting == 0:
    return None

# avoids blocking.

# Without it:

self.arduino.readline()

# may wait up to:

timeout = 1

# second.

# ======================

#  `readline()`
# Reads data until newline:
# ```text
# \n
# ```


# Arduino:

# ```cpp
# Serial.println("READY");
# ```

# sends:

# ```text
# READY\n
# ```

# Python:

line = self.arduino.readline()

print(line)  # b'READY\r\n'


# Then:
# Decode()
# ```python
# .decode("utf-8")
# .strip()
# ```

# becomes:

# ```python
# "READY"
# ```
