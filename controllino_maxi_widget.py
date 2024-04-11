


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

	QSystemTrayIcon,
	QTextEdit,
	QMenu,
	QAction,
	QWidget
)

from PyQt5 import *

from PyQt5.QtGui import (
	QIcon,
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


		self.layout_main = QHBoxLayout()
		self.setLayout(self.layout_main)

		self.label_pin = QLabel(name)
		self.layout_main.addWidget(self.label_pin)

		self.label_state = QLabel("-")							# should represent the state ON/OFF, once read from controllino.
		self.layout_main.addWidget(self.label_state)

		self.button_on = QPushButton("ON")
		self.layout_main.addWidget(self.button_on)

		self.button_off = QPushButton("OFF")
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
		self.layout_main = QHBoxLayout()
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

class controllino_maxi_image_with_buttons(QWidget):

	def __init__(self):
		super().__init__()

		# picture of the controllino representing the status of the IO pins #

		self.layout_main = QHBoxLayout()
		# self.layout_main.set
		self.setLayout(self.layout_main)


		self.img_controllino = QLabel("There should be the image of the controllino here")
		self.layout_main.addWidget(self.img_controllino)

		self.pixmap_controllino = QPixmap("docu/controllino.png")
		self.img_controllino.setPixmap(self.pixmap_controllino)
		# self.img_controllino.setStyleSheet("background-image: docu/controllino.png")

		self.button_over_image = QPushButton()

class controllino_led_widget(QWidget):
	def __init__(self):
		super().__init__()
		# LEDs #
		self.layout_LED = QVBoxLayout()
		self.setLayout(self.layout_LED)

		self.label_led = QLabel("LEDs")
		self.layout_LED.addWidget(self.label_led)

		self.led_D0 = QLed(self.layout_LED)
		self.layout_LED.addWidget(self.led_D0)
		self.led_D1 = QLed(self.layout_LED)
		self.layout_LED.addWidget(self.led_D1)
		self.led_D2 = QLed(self.layout_LED)
		self.layout_LED.addWidget(self.led_D2)
		self.led_D3 = QLed(self.layout_LED)
		self.layout_LED.addWidget(self.led_D3)

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

		# picture of the controllino representing the status of the IO pins #

		self.img_controllino = controllino_maxi_image_with_buttons()
		self.layout_control.addWidget(self.img_controllino)




		# signal connection #
		self.connect_digital_buttons_signals()
		self.connect_relay_buttons_signals()


		# timers #
		self.timer_update_ui = QTimer()
		self.timer_update_ui.setInterval(config.ui_config.update_period)				# interval set  via config file
		self.timer_update_ui.timeout.connect(self.on_timer_update_ui)
		self.timer_update_ui.start()


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
		print("on_timer_update_ui timed out")
		self.update_ui_analog_vals()


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

	# # MOVED TO THE CONTROLLINO CLASS ITSELF
	# # IS IT REALLY REQUIRED HERE ??? !!!
	# def set_pin_val(self, pin, val):
	# 	"""
	# 	:param pin: the pin number you wanna set
	# 	:param val: either True or False, meaning On or Off
	# 	:return:
	# 	"""
	# 	pass
	# 	# self.controllino.send_command(cmd_pin_d0_on)



class MainWindow(QMainWindow):
	"""
	Main window to contain the her02 class widget.
	"""

	# constructor #
	def __init__(self):

		super().__init__()

		self.controllino_widget = controllino_maxi_widget()
		self.setCentralWidget(self.controllino_widget)
		# stylesheet, so I don't get blind with tiny characters #
		self.setWindowTitle("CONTROLLINO WIDGET")

		# self.controllino_pic = controllino_maxi_image_with_buttons()
		# self.setCentralWidget(self.controllino_pic)


		self.setFixedHeight(560)

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