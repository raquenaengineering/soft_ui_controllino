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

        # ANALOG INPUTS #                       # all those could be defined to None as initial value, as they always come from the micrcontroller side.

        self.val_A0 = False                     #  NOTE:
        self.val_A1 = False                     # THESE VARIABLES ARE CURRENTLY UNUSED
        self.val_A2 = False                     # NEED TO FIND A WAY TO LINK THEM BY REFERENCE WITH THE VALUES OF THE ARRAY
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

        self.digital_out_vals = [
            self.status_D0,
            self.status_D1,
            self.status_D2,
            self.status_D3,
            self.status_D4,
            self.status_D5,
            self.status_D6,
            self.status_D7,
            self.status_D8,
            self.status_D9,
            self.status_D10,
            self.status_D11
        ]

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

        self.relays_vals = [
            self.status_R0,
            self.status_R1,
            self.status_R2,
            self.status_R3,
            self.status_R4,
            self.status_R5,
            self.status_R6,
            self.status_R7,
            self.status_R8,
            self.status_R9
        ]



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
        analog_vals_stream = self.receive_data()

        # self.val_A0 = analog_vals               # need to implement for each analog value!!!


        for i in range(len(self.analog_vals)):    # analog vals declared as independent variables and also as array to iterate.
            bytes = analog_vals_stream[2*i:2*i+2]
            # self.analog_vals[i] = int.from_bytes(bytes, byteorder="big", signed=False)
            analog_val = int.from_bytes(bytes, byteorder="big", signed=False)
            volt_val = round(config.controllino_config.supply_voltage * (analog_val / 1024),2)
            self.analog_vals[i] = volt_val

            # print("analog vals")
            # for val in analog_vals_stream:
            #     print(val)

            # logging.debug("bytes for conversion = " + str(bytes))
            # logging.debug("analog_val " + str(i) + " " + str(self.analog_vals[i]))
            # logging.debug(self.analog_vals[i])


    def receive_data(self):
        data = self.serial_port.read(22)       # 10 analog values, 2 bytes per value, define as a variable ???!!!
        return(data)

    def set_digital_output(self, pin, val):
        """
        Sends the right command to set on or off a certain digital output
        The command list comes from the config file, so actually they can be changed if needed
        :param pin: the pin number you wanna set
        :param val: either True or False, meaning On or Off
        :return:
        """
        if(pin == 0):
            if(val == True):
                self.send_command(commands.cmd_pin_d0_on)
            else:
                self.send_command(commands.cmd_pin_d0_off)

        elif(pin == 1):
            if(val == True):
                self.send_command(commands.cmd_pin_d1_on)
            else:
                self.send_command(commands.cmd_pin_d1_off)

        elif(pin == 2):
            if(val == True):
                self.send_command(commands.cmd_pin_d2_on)
            else:
                self.send_command(commands.cmd_pin_d2_off)

        elif(pin == 3):
            if(val == True):
                self.send_command(commands.cmd_pin_d3_on)
            else:
                self.send_command(commands.cmd_pin_d3_off)

        elif(pin == 3):
            if(val == True):
                self.send_command(commands.cmd_pin_d3_on)
            else:
                self.send_command(commands.cmd_pin_d3_off)

        elif(pin == 4):
            if(val == True):
                self.send_command(commands.cmd_pin_d4_on)
            else:
                self.send_command(commands.cmd_pin_d4_off)

        elif(pin == 5):
            if(val == True):
                self.send_command(commands.cmd_pin_d5_on)
            else:
                self.send_command(commands.cmd_pin_d5_off)

        elif(pin == 6):
            if(val == True):
                self.send_command(commands.cmd_pin_d6_on)
            else:
                self.send_command(commands.cmd_pin_d6_off)

        elif(pin == 7):
            if(val == True):
                self.send_command(commands.cmd_pin_d7_on)
            else:
                self.send_command(commands.cmd_pin_d7_off)

        elif(pin == 8):
            if(val == True):
                self.send_command(commands.cmd_pin_d8_on)
            else:
                self.send_command(commands.cmd_pin_d8_off)

        elif(pin == 9):
            if(val == True):
                self.send_command(commands.cmd_pin_d9_on)
            else:
                self.send_command(commands.cmd_pin_d9_off)

        elif(pin == 10):
            if(val == True):
                self.send_command(commands.cmd_pin_d10_on)
            else:
                self.send_command(commands.cmd_pin_d10_off)

        elif(pin == 11):
            if(val == True):
                self.send_command(commands.cmd_pin_d11_on)
            else:
                self.send_command(commands.cmd_pin_d11_off)

    def set_relay(self, pin, val):                              # seems too similar to set_digital_outupt, unify??? !!!
        """
        Sends the right command to set on or off a certain digital output
        The command list comes from the config file, so actually they can be changed if needed
        :param pin: the pin number you wanna set
        :param val: either True or False, meaning On or Off
        :return:
        """
        if(pin == 0):
            if(val == True):
                self.send_command(commands.cmd_pin_R0_on)
            else:
                self.send_command(commands.cmd_pin_R0_off)

        elif(pin == 1):
            if(val == True):
                self.send_command(commands.cmd_pin_R1_on)
            else:
                self.send_command(commands.cmd_pin_R1_off)

        elif(pin == 2):
            if(val == True):
                self.send_command(commands.cmd_pin_R2_on)
            else:
                self.send_command(commands.cmd_pin_R2_off)

        elif(pin == 3):
            if(val == True):
                self.send_command(commands.cmd_pin_R3_on)
            else:
                self.send_command(commands.cmd_pin_R3_off)

        elif(pin == 4):
            if(val == True):
                self.send_command(commands.cmd_pin_R4_on)
            else:
                self.send_command(commands.cmd_pin_R4_off)

        elif(pin == 5):
            if(val == True):
                self.send_command(commands.cmd_pin_R5_on)
            else:
                self.send_command(commands.cmd_pin_R5_off)

        elif(pin == 6):
            if(val == True):
                self.send_command(commands.cmd_pin_R6_on)
            else:
                self.send_command(commands.cmd_pin_R6_off)

        elif(pin == 7):
            if(val == True):
                self.send_command(commands.cmd_pin_R7_on)
            else:
                self.send_command(commands.cmd_pin_R7_off)

        elif(pin == 8):
            if(val == True):
                self.send_command(commands.cmd_pin_R8_on)
            else:
                self.send_command(commands.cmd_pin_R8_off)

        elif(pin == 9):
            if(val == True):
                self.send_command(commands.cmd_pin_R9_on)
            else:
                self.send_command(commands.cmd_pin_R9_off)

    def test_digital_outputs(self):
        n_io_pins = 12
        for i in range(5):
            for i in range(n_io_pins):                         # number of IO pins #
                self.set_digital_output(i,True)
            time.sleep(1)
            for i in range(n_io_pins):
                self.set_digital_output(i, False)
            time.sleep(1)

    def test_relays(self):                              # number of relays #
        n_relays = 10
        for i in range(5):
            for i in range(n_relays):
                self.set_relay(i, True)
            time.sleep(1)
            for i in range(n_relays):
                self.set_relay(i, False)
            time.sleep(1)


if __name__ == '__main__':

    print("Running controllino maxi test")
    c = controllino_maxi()

    # c.send_command(b'?')

    # c.test_digital_outputs()
    c.test_relays()




