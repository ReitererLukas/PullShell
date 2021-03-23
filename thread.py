from threading import Thread
from PyQt5 import QtCore
from PyQt5.QtCore import QThread
from threading import Event

from __init__ import *


# Thread Klasse für andere UIs und CLIs
class MyThread(Thread, IThread):
    def __init__(self, controller: Controller, command: str):
        super().__init__(self)
        self.__controller = controller
        self.__command = command
        pass
    
    # wird bei Thread.start() ausgeführt
    def run(self):
        self.__controller.execute_command(
            self.__command[0], self.__command[1:])
        pass

    pass


# Thread Klasse für PyQT UI
class My_QThread(QThread, IThread):

    # wird benutzt um den Output rauszuschreiben
    output_signal = QtCore.pyqtSignal(str, bool)
    # wird benutzt um eine Frage zu stellen
    ask_question_signal = QtCore.pyqtSignal(str)

    waiting_for_answer_event = Event()  # Events for passive Waiting

    def __init__(self, ui: IUI, controller: Controller, command: str):
        QThread.__init__(self)
        self.__controller = controller
        self.__controller.set_thread(self)
        self.__command = command
        self.__ui = ui

        # cleared event, damit man es neu starten kann
        self.waiting_for_answer_event.clear()
        pass

    # sendet ein Signal an die GUI um den Output Threadsicher auszugeben
    # overrided method of UI_Interface
    def set_output(self, output: str, mode: bool = True):
        self.output_signal.emit(output, mode)
        pass

    # sendet ein Signal an die GUI um eine Frage zu öffnen
    # overrided method of UI_Interface
    def ask_question(self, question: str) -> str:
        self.ask_question_signal.emit(question)
        # wartet, dass die Frage beantwortet wurd
        self.waiting_for_answer_event.wait()
        return self.__ui.get_answer()
        pass

    # wird bei Thread.start() ausgeführt
    def run(self):
        self.__controller.execute_command(
            self.__command[0], self.__command[1:])
        pass

    pass
