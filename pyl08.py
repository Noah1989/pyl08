from pylibftdi import USB_PID_LIST, Device

USB_PID_LIST.append(0x6015)

dev = Device(mode='b')

dev.write('\x00');