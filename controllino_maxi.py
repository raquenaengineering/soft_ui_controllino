# standard imports #
import logging
logging.basicConfig(level = logging.DEBUG)
import time

# pip installed imports #
import serial
import socket

# project local imports #
import config
from controllino_command_list import controllino_command_list as commands


class controllino_communication_interface():

    def __init__(self, connection_type = "serial"):
        self.connection_type = connection_type
        if self.connection_type == "serial":
            port = config.serial_config.port
            baudrate = config.serial_config.baudrate
            self.serial_connection = serial.Serial(port, baudrate)
        elif self.connection_type == "socket":
            print("socket initialization started")
            host = config.socket_config.ip
            port = config.socket_config.port
            self.socket_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket_connection.connect((host, port))
            print("socket initialization finished")
        else:
            raise ValueError("Invalid connection type. Choose 'serial' or 'socket'.")

    def write(self, data):
        if self.connection_type == "serial":
            # self.serial_connection.write(data.encode())
            self.serial_connection.write(data)
        elif self.connection_type == "socket":
            self.socket_connection.sendall(data)
        else:
            raise ValueError("Invalid connection type.")

    def read(self, buffer_size=1024):
        if self.connection_type == "serial":
            return self.serial_connection.read(buffer_size)
        elif self.connection_type == "socket":
            return self.socket_connection.recv(buffer_size)
        else:
            raise ValueError("Invalid connection type.")

    def close(self):
        if self.connection_type == "serial":
            self.serial_connection.close()
        elif self.connection_type == "socket":
            self.socket_connection.close()
        else:
            raise ValueError("Invalid connection type.")

class controllino_maxi():

    def __init__(self):

        # communication variables #     # THIS SHOULD GO OUT, OPTION TO DO IT WITH SERIAL OR SOCKET AVAILABLE, OR
        # JUST TO GIVE AN OBJECT AS AN INPUT WHICH HAS READ AND WRITE METHODS !!!

        # self.serial_port = serial.Serial(port = config.serial_config.port,
        #                                  baudrate = config.serial_config.baudrate)

        self.comm_iface = controllino_communication_interface(config.comm_config.comm_type)                             # so we can use indistinctly serial or socket, refer to config file.




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

        # IMPORTANT NOTE ABOUT ANALOG VALS !!! #
        # The LEDs at the analog pins go from ON to OFF 8.43V (APPROXIMATED TO 8.4V)
        # The LEDs at the analog pins go from OFF to ON 5.65V (APPROXIMATED TO 5.6V)

        self.val_AL0 = False                     #  NOTE:
        self.val_AL1 = False                     # THESE VARIABLES ARE CURRENTLY UNUSED
        self.val_AL2 = False                     # NEED TO FIND A WAY TO LINK THEM BY REFERENCE WITH THE VALUES OF THE ARRAY
        self.val_AL3 = False

        self.val_AL4 = False
        self.val_AL5 = False
        self.val_AL6 = False
        self.val_AL7 = False

        self.val_AL8 = False
        self.val_AL9 = False

        self.analog_logic_vals = [
            self.val_AL0,
            self.val_AL1,
            self.val_AL2,
            self.val_AL3,
            self.val_AL4,
            self.val_AL5,
            self.val_AL6,
            self.val_AL7,
            self.val_AL8,
            self.val_AL9
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
        # self.serial_port.write(command)
        logging.info("writing command " + str(command))
        self.comm_iface.write(command)


    def reset(self):
        self.send_command(commands.cmd_software_reset)

    def all_outputs_off(self):
        # print("all outputs off method triggered")
        self.send_command(commands.cmd_all_off)

    # def request_digital_outputs(self):
    #     logging.debug("request_relay_outputs")
    #     # # self.send_command(commands.cmd_request_analog_inputs)
    #     # self.send_command(b'_')
    #     # digital_vals_stream = self.receive_digital_data()
    #     # logging.debug(digital_vals_stream)
    #     #
    #     # for i in range(len(self.digital_out_vals)):
    #     #     byte = digital_vals_stream[i]
    #     #     if(byte == 0):
    #     #         self.digital_out_vals[i] = False
    #     #     else:
    #     #         self.digital_out_vals[i] = True
    #     #
    #     # # print(self.digital_out_vals)
    #     #
    #     # # there is no return values, as they get stored in class internal variables. (digital_out_vals)
    #     # return(True)


    def request_digital_outputs(self):
        logging.debug("request_digital_outputs")
        # self.send_command(commands.cmd_request_analog_inputs)
        self.send_command(commands.cmd_request_digital_outputs)
        digital_vals_stream = self.receive_digital_data()
        logging.info(digital_vals_stream)

        try:

            for i in range(len(self.digital_out_vals)):
                byte = digital_vals_stream[i]
                if(byte == 0):
                    self.digital_out_vals[i] = False
                else:
                    self.digital_out_vals[i] = True

        except:

            logging.warning("Incoming data misformed")

        # print(self.digital_out_vals)

        # there is no return values, as they get stored in class internal variables. (digital_out_vals)
        return(True)

    def receive_digital_data(self):
        data = self.comm_iface.read(14)  # 12 digital values + eol
        return (data)

    def request_analog_inputs(self):
        logging.debug("request_analog_inputs")
        # self.send_command(commands.cmd_request_analog_inputs)
        self.send_command(commands.cmd_request_analog_inputs)
        analog_vals_stream = self.receive_analog_data()

        # self.val_A0 = analog_vals               # need to implement for each analog value!!!


        try:

            for i in range(len(self.analog_vals)):    # analog vals declared as independent variables and also as array to iterate.
                bytes = analog_vals_stream[2*i:2*i+2]
                # self.analog_vals[i] = int.from_bytes(bytes, byteorder="big", signed=False)
                analog_val = int.from_bytes(bytes, byteorder="big", signed=False)
                volt_val = round(config.controllino_config.supply_voltage * (analog_val / 1024),2)
                self.analog_vals[i] = volt_val
                # USE HERE VOLT VAL TO ALSO UPDATE THE LEDS ON/OFF!!!!

                # !!! the analog values don't correspond to real voltage values, hence a correction factor is used
                # Best option would be use this correction factor when assigning volt_val level, but first
                # I would like to speak with the manufacturer (maybe my controllino is broken).
                correction_factor = config.controllino_config.analog_val_measured_at_supply/config.controllino_config.supply_voltage

                if self.analog_logic_vals[i] == True:
                    if(volt_val < config.controllino_config.led_logic_low*correction_factor):
                        self.analog_logic_vals[i] = False
                elif self.analog_logic_vals[i] == False:
                    if(volt_val > config.controllino_config.led_logic_high*correction_factor):
                        self.analog_logic_vals[i] = True

                # logging.debug("Analog logic vals:")
                # logging.debug(self.analog_logic_vals)


                # print("analog vals")
                # for val in analog_vals_stream:
                #     print(val)

                # logging.debug("bytes for conversion = " + str(bytes))
                # logging.debug("analog_val " + str(i) + " " + str(self.analog_vals[i]))
                # logging.debug(self.analog_vals[i])

        except:
            logging.warning("Incoming data misformed")


    def receive_analog_data(self):
        data = self.comm_iface.read(22)       # 10 analog values, 2 bytes per value, define as a variable ???!!!
        return(data)

    def request_relay_outputs(self):
        logging.debug("request_relay_outputs")
        self.send_command(commands.cmd_request_relay_outputs)
        relay_vals_stream = self.receive_relays_data()
        # logging.debug(relay_vals_stream)

        try:
            for i in range(len(self.relays_vals)):
                byte = relay_vals_stream[i]
                if(byte == 0):
                    self.relays_vals[i] = False
                else:
                    self.relays_vals[i] = True
        except:
            logging.warning("Incoming data misformed")


        # there is no return values, as they get stored in class internal variables. (digital_out_vals)
        return(True)

    def receive_relays_data(self):
        data = self.comm_iface.read(12)  # 10 digital values + eol
        return (data)


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

        self.request_digital_outputs()

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
                self.send_command(commands.cmd_pin_r0_on)
            else:
                self.send_command(commands.cmd_pin_r0_off)

        elif(pin == 1):
            if(val == True):
                self.send_command(commands.cmd_pin_r1_on)
            else:
                self.send_command(commands.cmd_pin_r1_off)

        elif(pin == 2):
            if(val == True):
                self.send_command(commands.cmd_pin_r2_on)
            else:
                self.send_command(commands.cmd_pin_r2_off)

        elif(pin == 3):
            if(val == True):
                self.send_command(commands.cmd_pin_r3_on)
            else:
                self.send_command(commands.cmd_pin_r3_off)

        elif(pin == 4):
            if(val == True):
                self.send_command(commands.cmd_pin_r4_on)
            else:
                self.send_command(commands.cmd_pin_r4_off)

        elif(pin == 5):
            if(val == True):
                self.send_command(commands.cmd_pin_r5_on)
            else:
                self.send_command(commands.cmd_pin_r5_off)

        elif(pin == 6):
            if(val == True):
                self.send_command(commands.cmd_pin_r6_on)
            else:
                self.send_command(commands.cmd_pin_r6_off)

        elif(pin == 7):
            if(val == True):
                self.send_command(commands.cmd_pin_r7_on)
            else:
                self.send_command(commands.cmd_pin_r7_off)

        elif(pin == 8):
            if(val == True):
                self.send_command(commands.cmd_pin_r8_on)
            else:
                self.send_command(commands.cmd_pin_r8_off)

        elif(pin == 9):
            if(val == True):
                self.send_command(commands.cmd_pin_r9_on)
            else:
                self.send_command(commands.cmd_pin_r9_off)

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




