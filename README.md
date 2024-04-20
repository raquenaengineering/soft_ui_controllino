# soft_ui_controllino
Software UI written in Pyqt for easy control of the controllino IO pins.

Here a little Demo:
![Controllino UI Widget View](https://github.com/raquenaengineering/soft_ui_controllino/blob/main/docu/readme_media/controllino_widget_ui.PNG)

## NOTES: ##
-  implement widget and controllino as two differentiated classes
    - the controllino widget creates an instance of the controllino class to function.
  
- the controllino class should be able to use at least two different methods to communicate:
    - Serial port based.
    - IP socket based. 
    
- to implement de different communication options, the methods
send_command and receive_data are the only ones which should require reimplementation
- Ideally it would be possible to integrate the widget and controllino class with
    - serial widget.
    - socket widget. 
- ¡¡¡Check the status of serial and socket widget, and fix them!!!