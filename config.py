
class ui_config():
    update_period = 500                    # period in ms in which the ui is updated / INDEPENDENT ON UPDATES OF THE CONTROLLINO CLASS!!!


class serial_config():

    baudrate = 115200                       # typical baudrate, can be changed, but do in both firm and soft
    port = "COM4"                           # use device manager to figure out the assigned port before running script.

class socket_config():
    ip = "192.168.4.200"                    # needs to be set up at the firmware side, any free ip will do
    port = 8881                             # any free port should do, BUT: CHECK STANDARDS FOR BETTER CHOICE!


class controllino_config():
    supply_voltage = 12                     # Voltage supplied to the controllino, usually 12 or 24 V