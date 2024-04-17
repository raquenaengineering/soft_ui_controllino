


"""
To be able to synchronize easily any changes in the communication between the controllino and the UI,
- The command list will be implemented as a separate file.
- A script that autogenerates the expected commands on the firmware side will be created.
- The output of the script will be copied to the folder where the firmware is compiled (as a source file)
- So, it can be read and compiled with the firmware everytime there is a change.

ui side: controllino_command_list.py
    - class with a lot of variables?
        - probably best option
firmware side: command_list.h
    - defines
    - const chars? --> probably this option better.
"""

class controllino_command_list():

    # SPECIAL #

    cmd_reset = b' '                        # IMPOOOOOOOORTANT!

    # ANALOG INPUTS #

    cmd_request_analog_inputs = b'-'
    cmd_request_digital_outputs = b'_'
    cmd_request_relay_outputs = b','
    cmd_request_all = b';'


    # DIGITAL OUTPUTS #

    cmd_pin_d0_on = b'+'
    cmd_pin_d0_off = b'*'

    cmd_pin_d1_on = b'1'
    cmd_pin_d1_off = b'!'

    cmd_pin_d2_on = b'2'
    cmd_pin_d2_off = b'"'

    cmd_pin_d3_on = b'3'
    cmd_pin_d3_off = b'#'            # original command was '·', but is not an ASCII character


    cmd_pin_d4_on = b'4'
    cmd_pin_d4_off = b'$'

    cmd_pin_d5_on = b'5'
    cmd_pin_d5_off = b'%'

    cmd_pin_d6_on = b'6'
    cmd_pin_d6_off = b'&'

    cmd_pin_d7_on = b'7'
    cmd_pin_d7_off = b'/'


    cmd_pin_d8_on = b'8'
    cmd_pin_d8_off = b'('

    cmd_pin_d9_on = b'9'
    cmd_pin_d9_off = b')'

    cmd_pin_d10_on = b'0'
    cmd_pin_d10_off = b'='

    cmd_pin_d11_on = b"'"
    cmd_pin_d11_off = b'?'

    # RELAY OUTPUTS #

    cmd_pin_R0_on = b'q'
    cmd_pin_R0_off = b'Q'

    cmd_pin_R1_on = b'w'
    cmd_pin_R1_off = b'W'

    cmd_pin_R2_on = b'e'
    cmd_pin_R2_off = b'E'

    cmd_pin_R3_on = b'r'
    cmd_pin_R3_off = b'R'


    cmd_pin_R4_on = b't'
    cmd_pin_R4_off = b'T'

    cmd_pin_R5_on = b'y'
    cmd_pin_R5_off = b'Y'

    cmd_pin_R6_on = b'u'
    cmd_pin_R6_off = b'U'

    cmd_pin_R7_on = b'i'
    cmd_pin_R7_off = b'I'


    cmd_pin_R8_on = b'o'
    cmd_pin_R8_off = b'O'

    cmd_pin_R9_on = b'p'
    cmd_pin_R9_off = b'P'



    def __init__(self):             # not needed, this class is just a variable container.
        pass


if __name__ == "__main__":
    # ccl = controllino_command_list()
    # for param in vars(ccl):
    #     print(param)

    for param in vars(controllino_command_list):
        print(param)