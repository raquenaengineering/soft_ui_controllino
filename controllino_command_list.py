


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


    cmd_pin_d0_on = b'+'
    cmd_pin_d0_off = b'*'

    cmd_pin_d1_on = b'1'
    cmd_pin_d1_off = b'!'

    cmd_pin_d2_on = b'2'
    cmd_pin_d2_off = b'"'

    cmd_pin_d3_on = b'3'
    cmd_pin_d3_off = b'-'            # problematic, not an ASCII character.


    # ANALOG INPUTS #

    cmd_request_analog_inputs = '-'

    def __init__(self):             # not needed, this class is just a variable container.
        pass


if __name__ == "__main__":
    # ccl = controllino_command_list()
    # for param in vars(ccl):
    #     print(param)

    for param in vars(controllino_command_list):
        print(param)