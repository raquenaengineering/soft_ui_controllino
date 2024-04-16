# # # import sys
# # # from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QRadioButton
# # # from PyQt5.QtGui import QPixmap, QFont
# # #
# # #
# # # class ImageWidget(QWidget):
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #         self.setWindowTitle("Image Widget with Radio Buttons")
# # #
# # #         layout = QVBoxLayout(self)
# # #
# # #         # Create a frame to hold the image
# # #         frame = QFrame(self)
# # #         layout.addWidget(frame)
# # #
# # #         # Set frame style and geometry
# # #         frame.setStyleSheet(
# # #             "QFrame { background-image: url('docu/controllino.png'); background-repeat: no-repeat; background-position: center; }")
# # #         frame.setFixedSize(400, 300)  # Set the size of the frame to match the image size
# # #
# # #         # Radio Button 1
# # #         radio_button1 = QRadioButton("Radio Button 1", frame)
# # #         radio_button1.move(50, 50)  # Adjust button position as needed
# # #         radio_button1.setChecked(True)
# # #         radio_button1.setFixedSize(50, 10)  # Set the size of the radio button
# # #
# # #         # Radio Button 2
# # #         radio_button2 = QRadioButton("Radio Button 2", frame)
# # #         radio_button2.move(250, 200)  # Adjust button position as needed
# # #         radio_button2.setFixedSize(50, 10)  # Set the size of the radio button
# # #
# # #
# # # if __name__ == "__main__":
# # #     app = QApplication(sys.argv)
# # #     widget = ImageWidget()
# # #     widget.show()
# # #     sys.exit(app.exec_())
# #
# #
# # # import sys
# # # from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFrame
# #
# #
# # import sys
# # from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QFrame
# # from PyQt5.QtCore import Qt
# #
# #
# # class ExampleWidget(QWidget):
# #     def __init__(self):
# #         super().__init__()
# #         self.initUI()
# #
# #     def initUI(self):
# #         self.setWindowTitle('Example Widget')
# #         # self.setGeometry(100, 100, 300, 200)
# #
# #         # Create a frame to surround the inner widget
# #         frame = QFrame(self)
# #         frame.setFrameShape(QFrame.Box)  # Set the frame shape to Box
# #         frame.setLineWidth(1)  # Set the line width of the frame
# #
# #         # Create a layout for the frame
# #         layout = QVBoxLayout(frame)
# #
# #         # Create a label widget to be placed inside the frame
# #         # label = QLabel('This is inside the frame', frame)
# #         # label.setAlignment(Qt.AlignCenter)  # Align the text in the center
# #
# #         # Add the label widget to the layout
# #         # layout.addWidget(label)
# #
# #         # Set the layout of the frame
# #         # frame.setLayout(layout)
# #
# #         # Set the size and position of the frame
# #         frame.setGeometry(50, 50, 200, 100)
# #
# #
# # def main():
# #     app = QApplication(sys.argv)
# #     ex = ExampleWidget()
# #     ex.show()
# #     sys.exit(app.exec_())
# #
# #
# # if __name__ == '__main__':
# #     main()
#
#
# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QVBoxLayout
# from PyQt5.QtCore import Qt
#
#
# class ExampleWidget(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle('Radio Button Example')
#         self.setGeometry(100, 100, 300, 200)
#
#         # Create a vertical layout
#         layout = QVBoxLayout(self)
#
#         # Create a radio button
#         self.radio_button = QRadioButton('Change Background Color', self)
#         self.radio_button.toggled.connect(self.on_radio_toggled)
#
#         # Add the radio button to the layout
#         layout.addWidget(self.radio_button)
#
#         # Set the layout for the main window
#         self.setLayout(layout)
#
#     def on_radio_toggled(self, checked):
#         if checked:
#             self.radio_button.setStyleSheet("QRadioButton::indicator:checked {background-color: red;}")
#         else:
#             self.radio_button.setStyleSheet("QRadioButton::indicator:checked {background-color: none;}")
#
#
# def main():
#     app = QApplication(sys.argv)
#     ex = ExampleWidget()
#     ex.show()
#     sys.exit(app.exec_())
#
#
# if __name__ == '__main__':
#     main()

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class Led(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setMinimumSize(20, 20)  # Set minimum size to ensure the widget is visible

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable anti-aliasing for smoother circle
        painter.setBrush(QColor(0, 0, 0))  # Set brush color to black
        painter.setPen(QColor(0, 0, 0))  # Set pen color to black
        radius = min(self.width(), self.height()) / 2
        painter.drawEllipse(self.width() / 2 - radius, self.height() / 2 - radius, radius * 2, radius * 2)


def main():
    app = QApplication(sys.argv)
    led = Led()
    led.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
