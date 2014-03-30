from pylibftdi import USB_PID_LIST, Device

USB_PID_LIST.append(0x6015)

dev = Device(mode='b')

# baudrate seems to be divided by 4 internally
dev.baudrate = 46875

dev.write('U');