from pylibftdi import USB_PID_LIST, SerialDevice
from ctypes import byref

USB_PID_LIST.append(0x6015)
BITMODE_CBUS = 0x20


dev = SerialDevice()

dev.baudrate = 46875

# programming voltage
dev.rts = 1

# reset
dev.ftdi_fn.ftdi_set_bitmode(0x40, BITMODE_CBUS)

dev.close()