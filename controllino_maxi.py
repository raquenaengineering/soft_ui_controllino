
from controllino_command_list import controllino_command_list as commands

class controllino_maxi():

    def __init__(self):

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
        pass

    def request_data(self):
        self.send_command()

    def receive_data(self):
        pass













