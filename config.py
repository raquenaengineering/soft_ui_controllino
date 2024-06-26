
class ui_config():
    update_period = 200                    # period in ms in which the ui is updated / INDEPENDENT ON UPDATES OF THE CONTROLLINO CLASS!!!

class comm_config():
    comm_type = "socket"                    # serial or socket communication, ideally will also set modifications in firmware to block the other comm. method.
    # Minimum time when using a wireless connection, minimum 150ms for consistent communicaion
    # Minimum time direct conn. 18ms
    t_wait_between_request_and_read = 0.150   # time to wait after sending a data request command and reading the data

class serial_config():

    baudrate = 115200                       # typical baudrate, can be changed, but do in both firm and soft
    port = "COM4"                           # use device manager to figure out the assigned port before running script.

class socket_config():
    ip = "192.168.0.128"                    # needs to be set up at the firmware side, any free ip will do
    port = 8881                             # any free port should do, BUT: CHECK STANDARDS FOR BETTER CHOICE!


class controllino_config():
    supply_voltage = 12                     # Voltage supplied to the controllino, usually 12 or 24 V
    analog_val_measured_at_supply = 9.59   # maybe controllino broken --> measured val and supply not matching, so need to compensate.
    led_logic_high = 8.43                   # LEDs connected to the analog pins, need to have at least this voltage to turn on.
    led_logic_low = 5.65                    # LEDs conneted to analog pin turn off when they go below this voltage.