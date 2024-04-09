


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


# # submodule imports #
# # from pyqt_common_resources.pyqt_custom_palettes import dark_palette
#
# import pyqt_common_resources.pyqt_custom_palettes as pyqt_custom_palettes
#


class controllino_maxi_widget(QWidget):

	def __init__(self):
		"""
        Constructor, creates and arranges all widgets.
        """
		super().__init__()

		#### LAYOUT ####

		### general top layout ###
		self.layout_main = QVBoxLayout()
		self.layout_control = QHBoxLayout()
		self.layout_main.addLayout(self.layout_control)

		# digital pins #
		self.layout_digital_pins = QHBoxLayout()
		self.layout_control.addLayout(self.layout_digital_pins)

		self.layout_control_buttons_1 = QVBoxLayout()
		self.layout_digital_pins.addLayout(self.layout_control_buttons_1)

		# buttons for the IO pins #
		self.button_D0 = QPushButton("D0")
		self.layout_control_buttons_1.addWidget(self.button_D0)
		self.button_D1 = QPushButton("D1")
		self.layout_control_buttons_1.addWidget(self.button_D1)
		self.button_D2 = QPushButton("D2")
		self.layout_control_buttons_1.addWidget(self.button_D2)
		self.button_D3 = QPushButton("D3")
		self.layout_control_buttons_1.addWidget(self.button_D3)
		self.button_D4 = QPushButton("D4")
		self.layout_control_buttons_1.addWidget(self.button_D4)
		self.button_D5 = QPushButton("D5")
		self.layout_control_buttons_1.addWidget(self.button_D5)

		self.layout_control_buttons_2 = QVBoxLayout()
		self.layout_digital_pins.addLayout(self.layout_control_buttons_2)

		# buttons for the IO pins #
		self.button_D6 = QPushButton("D6")
		self.layout_control_buttons_2.addWidget(self.button_D6)
		self.button_D7 = QPushButton("D7")
		self.layout_control_buttons_2.addWidget(self.button_D7)
		self.button_D8 = QPushButton("D8")
		self.layout_control_buttons_2.addWidget(self.button_D8)
		self.button_D9 = QPushButton("D9")
		self.layout_control_buttons_2.addWidget(self.button_D9)
		self.button_D10 = QPushButton("D10")
		self.layout_control_buttons_2.addWidget(self.button_D10)
		self.button_D11 = QPushButton("D11")
		self.layout_control_buttons_2.addWidget(self.button_D11)


		# Analog pins #
		# block A #
		self.layout_analog_pins = QHBoxLayout()
		self.layout_control.addLayout(self.layout_analog_pins)
		self.layout_analog_pins_A = QVBoxLayout()
		self.layout_analog_pins.addLayout(self.layout_analog_pins_A)

		# A0 #
		self.layout_analog_pin_0 = QHBoxLayout()
		self.layout_analog_pins_A.addLayout(self.layout_analog_pin_0)

		self.button_set_analog_pin_0 = QPushButton("A0")
		self.layout_analog_pin_0.addWidget(self.button_set_analog_pin_0)
		self.textbox_set_analog_pin_0 = QTextEdit()
		self.layout_analog_pin_0.addWidget(self.textbox_set_analog_pin_0)

		# A1 #
		self.layout_analog_pin_1 = QHBoxLayout()
		self.layout_analog_pins_A.addLayout(self.layout_analog_pin_1)

		self.button_set_analog_pin_1 = QPushButton("A1")
		self.layout_analog_pin_1.addWidget(self.button_set_analog_pin_1)
		self.textbox_set_analog_pin_1 = QTextEdit()
		self.layout_analog_pin_1.addWidget(self.textbox_set_analog_pin_1)

		# A2 #
		self.layout_analog_pin_2 = QHBoxLayout()
		self.layout_analog_pins_A.addLayout(self.layout_analog_pin_2)

		self.button_set_analog_pin_2 = QPushButton("A2")
		self.layout_analog_pin_2.addWidget(self.button_set_analog_pin_2)
		self.textbox_set_analog_pin_2 = QTextEdit()
		self.layout_analog_pin_2.addWidget(self.textbox_set_analog_pin_2)

		# A3 #
		self.layout_analog_pin_3 = QHBoxLayout()
		self.layout_analog_pins_A.addLayout(self.layout_analog_pin_3)

		self.button_set_analog_pin_3 = QPushButton("A3")
		self.layout_analog_pin_3.addWidget(self.button_set_analog_pin_3)
		self.textbox_set_analog_pin_3 = QTextEdit()
		self.layout_analog_pin_3.addWidget(self.textbox_set_analog_pin_3)

		# A4 #
		self.layout_analog_pin_4 = QHBoxLayout()
		self.layout_analog_pins_A.addLayout(self.layout_analog_pin_4)

		self.button_set_analog_pin_4 = QPushButton("A4")
		self.layout_analog_pin_4.addWidget(self.button_set_analog_pin_4)
		self.textbox_set_analog_pin_4 = QTextEdit()
		self.layout_analog_pin_4.addWidget(self.textbox_set_analog_pin_4)

		# A5 #
		self.layout_analog_pin_5 = QHBoxLayout()
		self.layout_analog_pins_A.addLayout(self.layout_analog_pin_5)

		self.button_set_analog_pin_5 = QPushButton("A5")
		self.layout_analog_pin_5.addWidget(self.button_set_analog_pin_5)
		self.textbox_set_analog_pin_5 = QTextEdit()
		self.layout_analog_pin_5.addWidget(self.textbox_set_analog_pin_5)

		# BLOCK B #
		self.layout_analog_pins = QHBoxLayout()
		self.layout_control.addLayout(self.layout_analog_pins)
		self.layout_analog_pins_B = QVBoxLayout()
		self.layout_analog_pins.addLayout(self.layout_analog_pins_B)

		# A6 #
		self.layout_analog_pin_6 = QHBoxLayout()
		self.layout_analog_pins_B.addLayout(self.layout_analog_pin_6)

		self.button_set_analog_pin_6 = QPushButton("A6")
		self.layout_analog_pin_6.addWidget(self.button_set_analog_pin_6)
		self.textbox_set_analog_pin_6 = QTextEdit()
		self.layout_analog_pin_6.addWidget(self.textbox_set_analog_pin_6)

		# A7 #
		self.layout_analog_pin_7 = QHBoxLayout()
		self.layout_analog_pins_B.addLayout(self.layout_analog_pin_7)

		self.button_set_analog_pin_7 = QPushButton("A7")
		self.layout_analog_pin_7.addWidget(self.button_set_analog_pin_7)
		self.textbox_set_analog_pin_7 = QTextEdit()
		self.layout_analog_pin_7.addWidget(self.textbox_set_analog_pin_7)

		# A8 #
		self.layout_analog_pin_2 = QHBoxLayout()
		self.layout_analog_pins_B.addLayout(self.layout_analog_pin_2)

		self.button_set_analog_pin_2 = QPushButton("A2")
		self.layout_analog_pin_2.addWidget(self.button_set_analog_pin_2)
		self.textbox_set_analog_pin_2 = QTextEdit()
		self.layout_analog_pin_2.addWidget(self.textbox_set_analog_pin_2)

		# A9 #
		self.layout_analog_pin_3 = QHBoxLayout()
		self.layout_analog_pins_B.addLayout(self.layout_analog_pin_3)

		self.button_set_analog_pin_3 = QPushButton("A3")
		self.layout_analog_pin_3.addWidget(self.button_set_analog_pin_3)
		self.textbox_set_analog_pin_3 = QTextEdit()
		self.layout_analog_pin_3.addWidget(self.textbox_set_analog_pin_3)

		# A10 #
		self.layout_analog_pin_4 = QHBoxLayout()
		self.layout_analog_pins_B.addLayout(self.layout_analog_pin_4)

		self.button_set_analog_pin_4 = QPushButton("A4")
		self.layout_analog_pin_4.addWidget(self.button_set_analog_pin_4)
		self.textbox_set_analog_pin_4 = QTextEdit()
		self.layout_analog_pin_4.addWidget(self.textbox_set_analog_pin_4)

		# A11 #
		self.layout_analog_pin_5 = QHBoxLayout()
		self.layout_analog_pins_B.addLayout(self.layout_analog_pin_5)

		self.button_set_analog_pin_5 = QPushButton("A5")
		self.layout_analog_pin_5.addWidget(self.button_set_analog_pin_5)
		self.textbox_set_analog_pin_5 = QTextEdit()
		self.layout_analog_pin_5.addWidget(self.textbox_set_analog_pin_5)



		# Relays #
		self.layout_relays = QHBoxLayout()
		self.layout_control.addLayout(self.layout_relays)


		# relays A #
		self.layout_relays_A = QVBoxLayout()
		self.layout_relays.addLayout(self.layout_relays_A)

		# R1 #
		self.layout_R1 = QHBoxLayout()
		self.layout_relays_A.addLayout(self.layout_R1)

		self.button_set_R1 = QPushButton("R1")
		self.layout_R1.addWidget(self.button_set_R1)
		self.textbox_set_R1 = QTextEdit()
		self.layout_R1.addWidget(self.textbox_set_R1)

		# R2 #
		self.layout_R2 = QHBoxLayout()
		self.layout_relays_A.addLayout(self.layout_R2)

		self.button_set_R2 = QPushButton("R2")
		self.layout_R2.addWidget(self.button_set_R2)
		self.textbox_set_R2 = QTextEdit()
		self.layout_R2.addWidget(self.textbox_set_R2)

		# relays B #
		self.layout_relays_B = QVBoxLayout()
		self.layout_relays.addLayout(self.layout_relays_B)

		# R5 #
		self.layout_R5 = QHBoxLayout()
		self.layout_relays_B.addLayout(self.layout_R5)

		self.button_set_R5 = QPushButton("R5")
		self.layout_R5.addWidget(self.button_set_R5)
		self.textbox_set_R5 = QTextEdit()
		self.layout_R5.addWidget(self.textbox_set_R5)

		# R6 #
		self.layout_R6 = QHBoxLayout()
		self.layout_relays_B.addLayout(self.layout_R6)

		self.button_set_R6 = QPushButton("R6")
		self.layout_R6.addWidget(self.button_set_R6)
		self.textbox_set_R6 = QTextEdit()
		self.layout_R6.addWidget(self.textbox_set_R6)


		# LEDs #

		self.layout_LED = QVBoxLayout()
		self.layout_control.addLayout(self.layout_LED)

		# self.label_led = QLabel("LEDs")
		# self.layout_LED.addWidget(self.label_led)

		self.led_D0 = QLed(self.layout_LED)
		self.layout_LED.addWidget(self.led_D0)
		self.led_D1 = QLed(self.layout_LED)
		self.layout_LED.addWidget(self.led_D1)
		self.led_D2 = QLed(self.layout_LED)
		self.layout_LED.addWidget(self.led_D2)
		self.led_D3 = QLed(self.layout_LED)
		self.layout_LED.addWidget(self.led_D3)



		self.img_controllino = QLabel("There should be the image of the controllino here")
		self.pixmap_controllino = QPixmap("docu/controllino.png")
		self.img_controllino.setPixmap(self.pixmap_controllino)
		# self.img_controllino.setStyleSheet("background-image: docu/controllino.png")
		self.layout_control.addWidget(self.img_controllino)




		self.setLayout(self.layout_main)




class MainWindow(QMainWindow):
	"""
	Main window to contain the her02 class widget.
	"""

	# constructor #
	def __init__(self):

		super().__init__()

		# self.setWindowIcon(QIcon("media/theion_logo_10mm.png"))


		# self.print_timer = QTimer()  # we'll use timer instead of thread
		# self.print_timer.timeout.connect(self.add_incoming_lines_to_log)
		# self.print_timer.start(LOG_WINDOW_REFRESH_PERIOD_MS)  # period needs to be relatively short

		#self.widget = QWidget()
		self.controllino_widget = controllino_maxi_widget()
		self.setCentralWidget(self.controllino_widget)
		# stylesheet, so I don't get blind with tiny characters #
		self.setWindowTitle("CONTROLLINO WIDGET")

		# self.setBaseSize(1200,400)
		# self.setFixedSize(1440,560)

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