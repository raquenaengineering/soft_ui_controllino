
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

from PyQt5 import QtGui

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

class led(QWidget):

	def __init__(self):
		super().__init__()
		painter = QtGui.QPainter()
		pen = QtGui.QPen



class controllino_led(QWidget):

	def __init__(self, led_text = "", text_pos = "right"):
		super().__init__()
		# widget #
		# self.setContentsMargins(0,0,0,0)
		# layout #
		self.layout_main = QHBoxLayout()
		self.layout_main.setContentsMargins(0,0,0,0)
		self.setLayout(self.layout_main)
		# led #
		self.led = QRadioButton()
		# self.led.setContentsMargins(0,0,0,0)
		# label #
		self.label = QLabel(led_text)
		# self.label.setContentsMargins(0,0,0,0)

		self.label.setStyleSheet('QLabel'						# use one line per style property. 
								 '{'	
								 'font: 7pt Helvetica MS;'
								 'font-weight: bold;'
								 '}')

		self.led.setStyleSheet('QRadioButton{font: 0pt Helvetica MS;} '
							   'QRadioButton::indicator '
							   '{ width: 16px; height: 16px;};'
							   'QRadioButton::indicator:checked '
							   '{ color: green;};'
							   )

		if(text_pos == "right"):
			self.layout_main.addWidget(self.led)
			self.layout_main.addWidget(self.label)

		elif(text_pos == "left"):
			self.layout_main.addWidget(self.label)
			self.layout_main.addWidget(self.led)



class controllino_leds_group(QWidget):
	"""
	There are 3 groups of LEDs, analog, digital and relay, which are fairly similar, so
	all 3 will inherit from this class, which will be used to set the common parameters:
	- FRAME, CONTENTMARGINS
	"""

	def __init__(self):

		m = 3									# variable to control content margin

		super().__init__()
		self.setContentsMargins(0,0,0,0)

		self.layout_main = QHBoxLayout()					# first create a main layout
		self.layout_main.setContentsMargins(0,0,0,0)
		self.setLayout(self.layout_main)

		self.frame = QFrame()
		self.frame.setFrameShape(QFrame.Box)
		self.frame.setLineWidth(1)
		self.frame.setContentsMargins(1,1,1,1)
		# self.frame.setContentsMargins(m,m,m,m)
		self.layout_main.addWidget(self.frame)				# second add the frame to the main layout

		self.layout_frame = QHBoxLayout()					# third create a layout for inside the frame
		self.layout_frame.setContentsMargins(0,0,0,0)
		self.frame.setLayout(self.layout_frame)				# fourth add it to the frame.


		self.layout_A = QVBoxLayout()
		self.layout_frame.addLayout(self.layout_A)

		self.layout_B = QVBoxLayout()
		self.layout_frame.addLayout(self.layout_B)


class controllino_leds_analog(controllino_leds_group):

	def __init__(self):
		super().__init__()


		# left #
		self.led_a0 = controllino_led("A0", "left")
		self.led_a0.led.setDisabled(True)
		self.layout_A.addWidget(self.led_a0)
		self.led_a1 = controllino_led("A1", "left")
		self.led_a1.led.setDisabled(True)
		self.layout_A.addWidget(self.led_a1)
		self.led_a2 = controllino_led("A2", "left")
		self.led_a2.led.setDisabled(True)
		self.layout_A.addWidget(self.led_a2)
		self.led_a3 = controllino_led("A3", "left")
		self.led_a3.led.setDisabled(True)
		self.layout_A.addWidget(self.led_a3)
		self.led_a4 = controllino_led("A4", "left")
		self.led_a4.led.setDisabled(True)
		self.layout_A.addWidget(self.led_a4)
		self.led_a5 = controllino_led("A5", "left")
		self.led_a5.led.setDisabled(True)
		self.layout_A.addWidget(self.led_a5)

		# right #
		self.led_a6 = controllino_led("A6", "right")
		self.led_a6.led.setDisabled(True)
		self.layout_B.addWidget(self.led_a6)
		self.led_a7 = controllino_led("A7", "right")
		self.led_a7.led.setDisabled(True)
		self.layout_B.addWidget(self.led_a7)
		self.led_a8 = controllino_led("A8", "right")
		self.led_a8.led.setDisabled(True)
		self.layout_B.addWidget(self.led_a8)
		self.led_a9 = controllino_led("A9", "right")
		self.led_a9.led.setDisabled(True)
		self.layout_B.addWidget(self.led_a9)
		self.led_a10 = controllino_led("IN1", "right")
		self.led_a10.led.setDisabled(True)
		self.layout_B.addWidget(self.led_a10)
		self.led_a11 = controllino_led("IN2", "right")
		self.led_a11.led.setDisabled(True)
		self.layout_B.addWidget(self.led_a11)

class controllino_leds_digital(controllino_leds_group):

	def __init__(self):
		super().__init__()

		# left #
		self.led_d0 = controllino_led("D0", "left")
		self.layout_A.addWidget(self.led_d0)
		self.led_d1 = controllino_led("D1", "left")
		self.layout_A.addWidget(self.led_d1)
		self.led_d2 = controllino_led("D2", "left")
		self.layout_A.addWidget(self.led_d2)
		self.led_d3 = controllino_led("D3", "left")
		self.layout_A.addWidget(self.led_d3)
		self.led_d4 = controllino_led("D4", "left")
		self.layout_A.addWidget(self.led_d4)
		self.led_d5 = controllino_led("D5", "left")
		self.layout_A.addWidget(self.led_d5)

		# right #
		self.led_d6 = controllino_led("D6", "right")
		self.layout_B.addWidget(self.led_d6)
		self.led_d7 = controllino_led("D7", "right")
		self.layout_B.addWidget(self.led_d7)
		self.led_d8 = controllino_led("D8", "right")
		self.layout_B.addWidget(self.led_d8)
		self.led_d9 = controllino_led("D9", "right")
		self.layout_B.addWidget(self.led_d9)
		self.led_d10 = controllino_led("D10", "right")
		self.layout_B.addWidget(self.led_d10)
		self.led_d11 = controllino_led("D11", "right")
		self.layout_B.addWidget(self.led_d11)

class controllino_leds_relays(controllino_leds_group):

	def __init__(self):
		super().__init__()

		#  left #
		self.led_r0 = controllino_led("R0", "left")
		self.layout_A.addWidget(self.led_r0)
		self.led_r1 = controllino_led("R1", "left")
		self.layout_A.addWidget(self.led_r1)
		self.led_r2 = controllino_led("R2", "left")
		self.layout_A.addWidget(self.led_r2)
		self.led_r3 = controllino_led("R3", "left")
		self.layout_A.addWidget(self.led_r3)
		self.led_r4 = controllino_led("R4", "left")
		self.layout_A.addWidget(self.led_r4)

		# right #
		self.led_r5 = controllino_led("R5", "right")
		self.layout_B.addWidget(self.led_r5)
		self.led_r6 = controllino_led("R6", "right")
		self.layout_B.addWidget(self.led_r6)
		self.led_r7 = controllino_led("R7", "right")
		self.layout_B.addWidget(self.led_r7)
		self.led_r8 = controllino_led("R8", "right")
		self.layout_B.addWidget(self.led_r8)
		self.led_r9 = controllino_led("R9", "right")
		self.layout_B.addWidget(self.led_r9)


class controllino_leds_widget(QWidget):

	def __init__(self):
		super().__init__()

		# self.setMaximumWidth(240)
		# self.setMaximumHeight(120)

		self.setAutoFillBackground(True)
		self.setContentsMargins(0,0,0,0)

		self.layout_main = QHBoxLayout()
		self.layout_main.setContentsMargins(0,0,0,0)
		self.setLayout(self.layout_main)


		self.img_controllino = QLabel("There should be the image of the controllino here")
		# self.frame_main.addWidget(self.img_controllino)

		self.pixmap_controllino = QPixmap("docu/controllino.png")
		self.img_controllino.setPixmap(self.pixmap_controllino)

		# Analog #
		self.analog_leds = controllino_leds_analog()
		self.layout_main.addWidget(self.analog_leds)

		# Digital #
		self.digital_leds = controllino_leds_digital()
		self.layout_main.addWidget(self.digital_leds)

		# Relays #
		self.relays_leds = controllino_leds_relays()
		self.layout_main.addWidget(self.relays_leds)


class controllino_maxi_image_with_leds(QWidget):

	def __init__(self):
		super().__init__()

		# self.setFixedSize(1024,768)						# just for testing

		# picture of the controllino representing the status of the IO pins #

		self.pixmap_controllino = QPixmap("docu/controllino_744x570.png")
		self.pic_size = self.pixmap_controllino.size()


		# main layout #
		self.layout_main = QHBoxLayout()
		self.setLayout(self.layout_main)

		# image container #
		self.img_controllino = QLabel("There should be the image of the controllino here")
		self.img_controllino.setFixedSize(self.pic_size)
		self.layout_main.addWidget(self.img_controllino)
		self.img_controllino.setPixmap(self.pixmap_controllino)

		#

		self.leds = controllino_leds_widget()
		self.leds.setParent(self.img_controllino)
		self.leds.show()
		self.leds.setGeometry(19 ,217, 316, 124)

		# self.button_over_image = QPushButton()
		# self.button_over_image.setParent(self.img_controllino)
		# self.button_over_image.show()
		# self.button_over_image.setGeometry(14,120,100,100)


	# def __init__(self):
	#     super().__init__()
	#
	#     self.layout_main = QHBoxLayout()
	#     self.frame = QFrame()
	#     self.layout_main.addWidget(self.frame)
	#     self.frame.setGeometry(120,120,120,120)
	#     self.frame.setFixedSize(120,120)
	#     # self.frame.drawFrame()
	#     self.frame.setStyleSheet("border :3px solid blue;")
	#     self.layout_frame = QVBoxLayout()
	#     self.frame.setLayout(self.layout_frame)
	#     self.button1 = QPushButton()
	#     self.layout_frame.addWidget(self.button1)
	#     self.button2 = QPushButton()
	#     self.layout_frame.addWidget(self.button2)





class MainWindow(QMainWindow):
	"""
	Main window to contain the her02 class widget.
	"""

	# constructor #
	def __init__(self):

		super().__init__()

		self.controllino_image  = controllino_maxi_image_with_leds()
		self.setCentralWidget(self.controllino_image)

		# self.setFixedHeight(560)

		font = self.font()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	app.setStyle("Fusion")  # required to use it here
	window = MainWindow()
	window.show()
	app.exec_()