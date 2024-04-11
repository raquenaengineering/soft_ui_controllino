# standard imports #
import logging
logging.basicConfig(level = logging.DEBUG)
import time

# pip installed imports #
import serial

# project local imports #
import config
from controllino_command_list import controllino_command_list as commands


class controllino_maxi():

    def __init__(self):

        # communication variables #     # THIS SHOULD GO OUT, OPTION TO DO IT WITH SERIAL OR SOCKET AVAILABLE, OR
        # JUST TO GIVE AN OBJECT AS AN INPUT WHICH HAS READ AND WRITE METHODS !!!

        self.serial_port = serial.Serial(port = config.serial_config.port,
                                         baudrate = config.serial_config.baudrate)



        ## PIN VARIABLES ##

        # RELAYS #
        self.status_R0 = False
        self.status_R1 = False
        self.status_R2 = False
        self.status_R3 = False

        self.status_R4 = False
        self.status_R5 = False
        self.status_R6 = False
        self.status_R7 = False

        self.status_R8 = False
        self.status_R9 = False

        # DIGITAL OUTPUTS #

        self.status_D0 = False
        self.status_D1 = False
        self.status_D2 = False
        self.status_D3 = False

        self.status_D4 = False
        self.status_D5 = False
        self.status_D6 = False
        self.status_D7 = False

        self.status_D8 = False
        self.status_D9 = False
        self.status_D10 = False
        self.status_D11 = False

        # ANALOG INPUTS #                       # all those could be defined to None as initial value, as they always come from the micrcontroller side.

        self.val_A0 = False
        self.val_A1 = False
        self.val_A2 = False
        self.val_A3 = False

        self.val_A4 = False
        self.val_A5 = False
        self.val_A6 = False
        self.val_A7 = False

        self.val_A8 = False
        self.val_A9 = False

        self.analog_vals = [
            self.val_A0,
            self.val_A1,
            self.val_A2,
            self.val_A3,
            self.val_A4,
            self.val_A5,
            self.val_A6,
            self.val_A7,
            self.val_A8,
            self.val_A9
        ]

        # DIGITAL_INPUTS #
        self.status_IN0 = False
        self.status_IN1 = False


    def send_command(self, command):
        """
        To comunicate with the controllino, we need to send commands to it,
        Most of the commands will be used to interact with the IO pins
        But there will also be some special commands to request data.
        :param command:
        :return:
        """
        self.serial_port.write(command)

    def request_analog_inputs(self):
        logging.debug("request_analog_inputs")
        self.send_command(b'-')
        analog_vals = self.receive_data()
        print("analog vals")
        for val in analog_vals:
            print(val)
        # self.val_A0 = analog_vals               # need to implement for each analog value!!!


        for i in range(len(self.analog_vals)):    # analog vals declared as independent variables and also as array to iterate.
            print("i = " + str(i))
            bytes = analog_vals[2*i:2*i+2]
            print("bytes for conversion = " + str(bytes))
            self.analog_vals[i] = int.from_bytes(bytes, byteorder="big", signed=False)

        bytes = self.analog_vals[2:4]

        self.val_A0 = int.from_bytes(bytes, byteorder = "big", signed = False)
        self.val_A1 = int.from_bytes(bytes, byteorder = "big", signed = False)




    def receive_data(self):
        data = self.serial_port.read(22)       # 10 analog values, 2 bytes per value, define as a variable ???!!!
        return(data)




if __name__ == '__main__':

    print("Running controllino maxi test")
    c = controllino_maxi()

    for i in range(10):
        c.send_command(b"+")
        time.sleep(1)
        c.request_analog_inputs()
        time.sleep(1)
        c.send_command(b"*")
        time.sleep(1)
        c.request_analog_inputs()
        time.sleep(1)






