


# standard imports #

import sys
import time
import logging
logging.basicConfig(level = logging.WARNING)

# qt imports #
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QComboBox,
    QLineEdit,
    QPushButton,
    QMenuBar,
    QToolBar,
    QStatusBar,
    QDialog,
    QFileDialog,
    QMessageBox,														# Dialog with extended functionality.
    QShortcut,
    QCheckBox,
    QRadioButton,
    QFrame,
    QSystemTrayIcon,
    QTextEdit,
    QMenu,
    QAction,
    QWidget
)

from PyQt5 import *

from PyQt5.QtGui import (
    QIcon,
    QPalette,
    QPixmap,
    QKeySequence,
    QColor,
    QFont
)

from PyQt5.QtCore import(
    Qt,
    QThreadPool,
    QRunnable,
    QObject,
    QSize,
    pyqtSignal,															# those two are pyqt specific.
    pyqtSlot,
    QTimer																# nasty stuff
)

# pip installed imports #

from pyqt_led import Led as QLed


# local project imports #

import controllino_maxi
from controllino_maxi_image_with_leds import controllino_maxi_image_with_leds


import config

# # submodule imports #
# # from pyqt_common_resources.pyqt_custom_palettes import dark_palette
#
# import pyqt_common_resources.pyqt_custom_palettes as pyqt_custom_palettes
#




class controllino_single_digital_out_widget(QWidget):
    """
    As the representation of a single digital output may change,
    but many single digital outputs will be used, instead of changing
    each of them every time, a single implementation will be done, and
    several instances of this class will be used for the ui.
    """
    def __init__(self, name):

        super().__init__()

        button_size = 50

        self.layout_main = QHBoxLayout()
        self.setLayout(self.layout_main)

        self.label_pin = QLabel(name)
        self.layout_main.addWidget(self.label_pin)

        self.label_state = QLabel("-")							# should represent the state ON/OFF, once read from controllino.
        self.layout_main.addWidget(self.label_state)

        self.button_on = QPushButton("ON")
        self.button_on.setMaximumWidth(button_size)
        self.layout_main.addWidget(self.button_on)

        self.button_off = QPushButton("OFF")
        self.button_off.setMaximumWidth(button_size)
        self.layout_main.addWidget(self.button_off)

class controllino_digital_outputs_widget(QWidget):
    """
    Used to improve modularity of UI
    Will group all digital outuputs of the controllino
    Internal: This class will only be instanced once inside the controllino maxi ui class.
    """
    def __init__(self):

        super().__init__()

        self.layout_main = QHBoxLayout()
        self.setLayout(self.layout_main)

        self.layout_pins_A = QVBoxLayout()					# pins are divided in 2 colmuns, A and B, each 6 pins.
        self.layout_main.addLayout(self.layout_pins_A)

        # PINS D0-D5 #
        self.pin_d0 = controllino_single_digital_out_widget("D0");
        self.layout_pins_A.addWidget(self.pin_d0)
        self.pin_d1 = controllino_single_digital_out_widget("D1");
        self.layout_pins_A.addWidget(self.pin_d1)
        self.pin_d2 = controllino_single_digital_out_widget("D2");
        self.layout_pins_A.addWidget(self.pin_d2)
        self.pin_d3 = controllino_single_digital_out_widget("D3");
        self.layout_pins_A.addWidget(self.pin_d3)
        self.pin_d4 = controllino_single_digital_out_widget("D4");
        self.layout_pins_A.addWidget(self.pin_d4)
        self.pin_d5 = controllino_single_digital_out_widget("D5");
        self.layout_pins_A.addWidget(self.pin_d5)

        self.layout_pins_B = QVBoxLayout()
        self.layout_main.addLayout(self.layout_pins_B)

        # PINS D6-D11 #
        self.pin_d6 = controllino_single_digital_out_widget("D6");
        self.layout_pins_B.addWidget(self.pin_d6)
        self.pin_d7 = controllino_single_digital_out_widget("D7");
        self.layout_pins_B.addWidget(self.pin_d7)
        self.pin_d8 = controllino_single_digital_out_widget("D8");
        self.layout_pins_B.addWidget(self.pin_d8)
        self.pin_d9 = controllino_single_digital_out_widget("D9");
        self.layout_pins_B.addWidget(self.pin_d9)
        self.pin_d10 = controllino_single_digital_out_widget("D10");
        self.layout_pins_B.addWidget(self.pin_d10)
        self.pin_d11 = controllino_single_digital_out_widget("D11");
        self.layout_pins_B.addWidget(self.pin_d11)

class controllino_single_analog_in_widget(QWidget):
    """
    Similar case as "controllino_single_digital_out_widget" please refer to its docu.
    """
    def __init__(self, name):
        super().__init__()
        # self.setContentsMargins(0,0,0,0)
        self.layout_main = QHBoxLayout()
        self.layout_main.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout_main)

        self.label_pin = QLabel(name)
        self.layout_main.addWidget(self.label_pin)

        self.text_analog_val = QLineEdit("-")
        self.text_analog_val.setEnabled(False)
        self.layout_main.addWidget(self.text_analog_val)

class controllino_all_analog_in_widget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout_main = QHBoxLayout()
        self.setLayout(self.layout_main)



        self.layout_pins_A = QVBoxLayout()
        self.layout_main.addLayout(self.layout_pins_A)

        # self.pene = QLabel("PENE")
        # self.layout_pins_A.addWidget(self.pene)

        self.pin_A0 = controllino_single_analog_in_widget("A0")
        self.layout_pins_A.addWidget(self.pin_A0)
        self.pin_A1 = controllino_single_analog_in_widget("A1")
        self.layout_pins_A.addWidget(self.pin_A1)
        self.pin_A2 = controllino_single_analog_in_widget("A2")
        self.layout_pins_A.addWidget(self.pin_A2)
        self.pin_A3 = controllino_single_analog_in_widget("A3")
        self.layout_pins_A.addWidget(self.pin_A3)
        self.pin_A4 = controllino_single_analog_in_widget("A4")
        self.layout_pins_A.addWidget(self.pin_A4)
        self.pin_A5 = controllino_single_analog_in_widget("A5")
        self.layout_pins_A.addWidget(self.pin_A5)

        self.layout_pins_B = QVBoxLayout()
        self.layout_main.addLayout(self.layout_pins_B)

        self.pin_A6 = controllino_single_analog_in_widget("A6")
        self.layout_pins_B.addWidget(self.pin_A6)
        self.pin_A7 = controllino_single_analog_in_widget("A7")
        self.layout_pins_B.addWidget(self.pin_A7)
        self.pin_A8 = controllino_single_analog_in_widget("A8")
        self.layout_pins_B.addWidget(self.pin_A8)
        self.pin_A9 = controllino_single_analog_in_widget("A9")
        self.layout_pins_B.addWidget(self.pin_A9)
        self.pin_IN0 = controllino_single_analog_in_widget("IN0")
        self.layout_pins_B.addWidget(self.pin_IN0)
        self.pin_IN1 = controllino_single_analog_in_widget("IN1")
        self.layout_pins_B.addWidget(self.pin_IN1)

class controllino_single_relay_widget(controllino_single_digital_out_widget):		# in the future may have its own implementation, now it will be used in the same way a digital OUT would be.
    def __init__(self, name):
        super().__init__(name)

class controllino_relays_widget(QWidget):
    def __init__(self):

        super().__init__()

        self.layout_main = QHBoxLayout()
        self.setLayout(self.layout_main)

        self.layout_relays_A = QVBoxLayout()					# pins are divided in 2 colmuns, A and B, each 6 pins.
        self.layout_main.addLayout(self.layout_relays_A)

        # PINS R0-R4 #
        self.pin_R0 = controllino_single_digital_out_widget("R0");
        self.layout_relays_A.addWidget(self.pin_R0)
        self.pin_R1 = controllino_single_digital_out_widget("R1");
        self.layout_relays_A.addWidget(self.pin_R1)
        self.pin_R2 = controllino_single_digital_out_widget("R2");
        self.layout_relays_A.addWidget(self.pin_R2)
        self.pin_R3 = controllino_single_digital_out_widget("R3");
        self.layout_relays_A.addWidget(self.pin_R3)
        self.pin_R4 = controllino_single_digital_out_widget("R4");
        self.layout_relays_A.addWidget(self.pin_R4)

        self.layout_relays_B = QVBoxLayout()
        self.layout_main.addLayout(self.layout_relays_B)

        # PINS R5-R9 #
        self.pin_R5 = controllino_single_digital_out_widget("R5");
        self.layout_relays_B.addWidget(self.pin_R5)
        self.pin_R6 = controllino_single_digital_out_widget("R6");
        self.layout_relays_B.addWidget(self.pin_R6)
        self.pin_R7 = controllino_single_digital_out_widget("R7");
        self.layout_relays_B.addWidget(self.pin_R7)
        self.pin_R8 = controllino_single_digital_out_widget("R8");
        self.layout_relays_B.addWidget(self.pin_R8)
        self.pin_R9 = controllino_single_digital_out_widget("R9");
        self.layout_relays_B.addWidget(self.pin_R9)

class controllino_maxi_widget(QWidget):

    def __init__(self):
        """
        Constructor, creates and arranges all widgets, also binds actions and signals
        """
        super().__init__()

        # controllino object, where the actual data is stored and communication implemented #
        self.controllino = controllino_maxi.controllino_maxi()

        #### LAYOUT ####

        ### general top layout ###
        self.setContentsMargins(0,0,0,0)
        self.layout_main = QVBoxLayout()
        self.layout_control = QHBoxLayout()
        self.layout_main.addLayout(self.layout_control)
        self.setLayout(self.layout_main)

        # # Analog pins #
        self.analog_inputs = controllino_all_analog_in_widget()
        self.layout_control.addWidget(self.analog_inputs)

        # Digital outputs #
        self.digital_outputs = controllino_digital_outputs_widget()
        self.layout_control.addWidget(self.digital_outputs)

        # Relays #
        self.relays = controllino_relays_widget()
        self.layout_control.addWidget(self.relays)

        self.button_reset = QPushButton("RESET")
        self.button_reset.setMinimumHeight(30)
        self.button_reset.clicked.connect(self.controllino.reset)

        self.layout_main.addWidget(self.button_reset)

        # picture of the controllino representing the status of the IO pins #

        # self.leds = controllino_leds_widget()
        # self.layout_control.addWidget(self.leds)

        # - IMPLEMENTATION OF THE LEDS AT THE CONTROLLINO IMAGE:
        # 	- 1. A CHANGE IS MADE EITHER VIA THE BUTTONS, OR PRESSING ONTO AN LED.
        # 	- 2. IF CHANGE TO TOGGLE SWITCHES, THE TOGGLE CHANGES, WITH THE "SHOULD" VALUE.
        # 	- 3. THE REQUIRED COMMAND TO REQUEST THE VALUES IS SENT.
        # 	- 4. THE ACTUAL VALUES ("IS" VALUES) OF THE OUTPUTS ARE RETURNED.
        # 	- 5. THE LEDS ARE UPDATE WITH THOSE VALUES.


        self.img_controllino = controllino_maxi_image_with_leds()
        self.layout_control.addWidget(self.img_controllino)




        # signal connection #
        self.connect_digital_buttons_signals()
        self.connect_relay_buttons_signals()


        # timers #
        self.timer_update_ui = QTimer()
        self.timer_update_ui.setInterval(config.ui_config.update_period)				# interval set  via config file
        self.timer_update_ui.timeout.connect(self.on_timer_update_ui)
        self.timer_update_ui.start()

        # initial update with the remote values #
        self.update_ui_all_vals()

        self.set_shortcuts()


    def connect_digital_buttons_signals(self):
        # digital on/off 0-3
        self.digital_outputs.pin_d0.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 0, val = True))				# NOTE: required to use a lambda in case the method we are calling requires input parameters !
        self.digital_outputs.pin_d0.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 0, val = False))

        self.digital_outputs.pin_d1.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 1, val = True))
        self.digital_outputs.pin_d1.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 1, val = False))

        self.digital_outputs.pin_d2.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 2, val = True))
        self.digital_outputs.pin_d2.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 2, val = False))

        self.digital_outputs.pin_d3.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 3, val = True))
        self.digital_outputs.pin_d3.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 3, val = False))

        # digital on/off 4-7
        self.digital_outputs.pin_d4.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 4, val = True))				# NOTE: required to use a lambda in case the method we are calling requires input parameters !
        self.digital_outputs.pin_d4.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 4, val = False))

        self.digital_outputs.pin_d5.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 5, val = True))
        self.digital_outputs.pin_d5.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 5, val = False))

        self.digital_outputs.pin_d6.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 6, val = True))
        self.digital_outputs.pin_d6.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 6, val = False))

        self.digital_outputs.pin_d7.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 7, val = True))
        self.digital_outputs.pin_d7.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 7, val = False))

        # digital on/off 8-11
        self.digital_outputs.pin_d8.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 8, val = True))				# NOTE: required to use a lambda in case the method we are calling requires input parameters !
        self.digital_outputs.pin_d8.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 8, val = False))

        self.digital_outputs.pin_d9.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 9, val = True))
        self.digital_outputs.pin_d9.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 9, val = False))

        self.digital_outputs.pin_d10.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 10, val = True))
        self.digital_outputs.pin_d10.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 10, val = False))

        self.digital_outputs.pin_d11.button_on.clicked.connect(lambda: self.controllino.set_digital_output(pin = 11, val = True))
        self.digital_outputs.pin_d11.button_off.clicked.connect(lambda: self.controllino.set_digital_output(pin = 11, val = False))


        # those are for the controllino image side # TO BE FINISHED!!! #
        self.img_controllino.leds.digital_leds.led_d0.led.clicked.connect(lambda: self.controllino.set_digital_output(pin = 0, val = True))
        self.img_controllino.leds.digital_leds.led_d0.led.clicked.connect(
            lambda: self.controllino.set_digital_output(pin = 0,
                                                        val = self.img_controllino.leds.digital_leds.led_d0.led.state))


    def connect_relay_buttons_signals(self):
        # relay on/off 0-3
        self.relays.pin_R0.button_on.clicked.connect(lambda: self.controllino.set_relay(pin = 0, val = True))				# NOTE: required to use a lambda in case the method we are calling requires input parameters !
        self.relays.pin_R0.button_off.clicked.connect(lambda: self.controllino.set_relay(pin = 0, val = False))

        self.relays.pin_R1.button_on.clicked.connect(lambda: self.controllino.set_relay(pin = 1, val = True))
        self.relays.pin_R1.button_off.clicked.connect(lambda: self.controllino.set_relay(pin = 1, val = False))

        self.relays.pin_R2.button_on.clicked.connect(lambda: self.controllino.set_relay(pin = 2, val = True))
        self.relays.pin_R2.button_off.clicked.connect(lambda: self.controllino.set_relay(pin = 2, val = False))

        self.relays.pin_R3.button_on.clicked.connect(lambda: self.controllino.set_relay(pin = 3, val = True))
        self.relays.pin_R3.button_off.clicked.connect(lambda: self.controllino.set_relay(pin = 3, val = False))


        self.relays.pin_R4.button_on.clicked.connect(lambda: self.controllino.set_relay(pin = 4, val = True))
        self.relays.pin_R4.button_off.clicked.connect(lambda: self.controllino.set_relay(pin = 4, val = False))

        self.relays.pin_R5.button_on.clicked.connect(lambda: self.controllino.set_relay(pin = 5, val = True))
        self.relays.pin_R5.button_off.clicked.connect(lambda: self.controllino.set_relay(pin = 5, val = False))

        self.relays.pin_R6.button_on.clicked.connect(lambda: self.controllino.set_relay(pin = 6, val = True))
        self.relays.pin_R6.button_off.clicked.connect(lambda: self.controllino.set_relay(pin = 6, val = False))

        self.relays.pin_R7.button_on.clicked.connect(lambda: self.controllino.set_relay(pin = 7, val = True))
        self.relays.pin_R7.button_off.clicked.connect(lambda: self.controllino.set_relay(pin = 7, val = False))


        self.relays.pin_R8.button_on.clicked.connect(lambda: self.controllino.set_relay(pin = 8, val = True))
        self.relays.pin_R8.button_off.clicked.connect(lambda: self.controllino.set_relay(pin = 8, val = False))

        self.relays.pin_R9.button_on.clicked.connect(lambda: self.controllino.set_relay(pin = 9, val = True))
        self.relays.pin_R9.button_off.clicked.connect(lambda: self.controllino.set_relay(pin = 9, val = False))

    def on_timer_update_ui(self):
        logging.debug("timer")
        self.update_ui_all_vals()


    def update_ui_all_vals(self):
        self.update_ui_analog_vals()
        self.update_ui_digital_vals()
        self.update_ui_relay_vals()

    def update_ui_analog_vals(self):
        # THIS FOR NOW IS ONLY A MOCKUP !!! --> NEED TO IMPLEMENT UPDATE ALL VALUES

        self.controllino.request_analog_inputs()

        self.analog_inputs.pin_A0.text_analog_val.setText(str(self.controllino.analog_vals[0]))
        self.analog_inputs.pin_A1.text_analog_val.setText(str(self.controllino.analog_vals[1]))
        self.analog_inputs.pin_A2.text_analog_val.setText(str(self.controllino.analog_vals[2]))
        self.analog_inputs.pin_A3.text_analog_val.setText(str(self.controllino.analog_vals[3]))

        self.analog_inputs.pin_A4.text_analog_val.setText(str(self.controllino.analog_vals[4]))
        self.analog_inputs.pin_A5.text_analog_val.setText(str(self.controllino.analog_vals[5]))
        self.analog_inputs.pin_A6.text_analog_val.setText(str(self.controllino.analog_vals[6]))
        self.analog_inputs.pin_A7.text_analog_val.setText(str(self.controllino.analog_vals[7]))

        self.analog_inputs.pin_A8.text_analog_val.setText(str(self.controllino.analog_vals[8]))
        self.analog_inputs.pin_A9.text_analog_val.setText(str(self.controllino.analog_vals[9]))

        time.sleep(.1)

    def update_ui_digital_vals(self):
        logging.debug("updating ui digital vals")
        self.controllino.request_digital_outputs()
        # VECTORIZE THIS !!! #
        self.img_controllino.leds.digital_leds.led_d0.led.setChecked(self.controllino.digital_out_vals[0])
        self.img_controllino.leds.digital_leds.led_d1.led.setChecked(self.controllino.digital_out_vals[1])
        self.img_controllino.leds.digital_leds.led_d2.led.setChecked(self.controllino.digital_out_vals[2])
        self.img_controllino.leds.digital_leds.led_d3.led.setChecked(self.controllino.digital_out_vals[3])
        self.img_controllino.leds.digital_leds.led_d4.led.setChecked(self.controllino.digital_out_vals[4])
        self.img_controllino.leds.digital_leds.led_d5.led.setChecked(self.controllino.digital_out_vals[5])

        self.img_controllino.leds.digital_leds.led_d6.led.setChecked(self.controllino.digital_out_vals[6])
        self.img_controllino.leds.digital_leds.led_d7.led.setChecked(self.controllino.digital_out_vals[7])
        self.img_controllino.leds.digital_leds.led_d8.led.setChecked(self.controllino.digital_out_vals[8])
        self.img_controllino.leds.digital_leds.led_d9.led.setChecked(self.controllino.digital_out_vals[9])
        self.img_controllino.leds.digital_leds.led_d10.led.setChecked(self.controllino.digital_out_vals[10])
        self.img_controllino.leds.digital_leds.led_d11.led.setChecked(self.controllino.digital_out_vals[11])

    def update_ui_relay_vals(self):
        logging.debug("updating ui relay vals")
        self.controllino.request_relay_outputs()
        # VECTORIZE THIS !!! #
        self.img_controllino.leds.relays_leds.led_r0.led.setChecked(self.controllino.relays_vals[0])
        self.img_controllino.leds.relays_leds.led_r1.led.setChecked(self.controllino.relays_vals[1])
        self.img_controllino.leds.relays_leds.led_r2.led.setChecked(self.controllino.relays_vals[2])
        self.img_controllino.leds.relays_leds.led_r3.led.setChecked(self.controllino.relays_vals[3])
        self.img_controllino.leds.relays_leds.led_r4.led.setChecked(self.controllino.relays_vals[4])

        self.img_controllino.leds.relays_leds.led_r5.led.setChecked(self.controllino.relays_vals[5])
        self.img_controllino.leds.relays_leds.led_r6.led.setChecked(self.controllino.relays_vals[6])
        self.img_controllino.leds.relays_leds.led_r7.led.setChecked(self.controllino.relays_vals[7])
        self.img_controllino.leds.relays_leds.led_r8.led.setChecked(self.controllino.relays_vals[8])
        self.img_controllino.leds.relays_leds.led_r9.led.setChecked(self.controllino.relays_vals[9])



    def set_shortcuts(self):
        reset_shortcut = QShortcut(' ', self)
        reset_shortcut.activated.connect(self.controllino.reset)


class MainWindow(QMainWindow):
    """
    Main window to contain the her02 class widget.
    """

    # constructor #
    def __init__(self):

        super().__init__()

        self.controllino_widget = controllino_maxi_widget()
        # self.controllino_widget  = controllino_leds_widget()
        self.setCentralWidget(self.controllino_widget)
        # stylesheet, so I don't get blind with tiny characters #
        self.setWindowTitle("CONTROLLINO WIDGET")

        # self.controllino_pic = controllino_maxi_image_with_buttons()
        # self.setCentralWidget(self.controllino_pic)


        self.setFixedHeight(768)

        font = self.font()
        font.setPointSize(24)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # required to use it here
    # app.palette = pyqt_custom_palettes.dark_palette()
    # app.setPalette(app.palette)
    # app.setPalette(dark_palette)
    window = MainWindow()

    window.show()
    app.exec_()