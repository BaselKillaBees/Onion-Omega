# gpiohelper.py
# Found on https://community.onion.io/topic/40/simple-python-wrapper-and-demo

class GPIOHelper(object):

    exportPath = "/sys/class/gpio/gpiochip0/subsystem/export"
    pinDirectionPath = "/sys/class/gpio/gpio$/direction"
    pinValuePath = "/sys/class/gpio/gpio$/value"
    pins = [0, 1, 6, 7, 8, 12, 13, 14, 23, 26, 21, 20, 19, 18]

    def __init__(self):
            for pin in self.pins:
                fd = open(self.exportPath, 'w')
                fd.write(str(pin))
                fd.close()

    def setPin(self, pin, value):
            # Set direction as out
            fd = open(self.pinDirectionPath.replace("$", str(pin)), 'w')
            fd.write("out")
            fd.close()
                
            # Set value
            fd = open(self.pinValuePath.replace("$", str(pin)), 'w')
            fd.write(str(value))
            fd.close()
            
    def getPin(self, pin):
            # Set direction as in
            fd = open(self.pinDirectionPath.replace("$", str(pin)), 'w')
            fd.write("in")
            fd.close()
            
            # Get value
            fd = open(self.pinValuePath.replace("$", str(pin)), 'r')
            out = fd.read()
            fd.close()
            
            return int(out)

