from threading import Event
from thread import My_QThread
from PyQt5 import QtWidgets as qt
from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import sys

from __init__ import *


class MainWindow(qt.QMainWindow, IUI):
    answer_signal = QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()
        # damit man bei onEnter weiß, ob eine Frage aktiv ist oder nicht
        self.__is_question = False
        self.on_startup() # set ups program
        self.initUI() # init UI
        pass

    # overrided method of UI_Interface
    def on_startup(self):
        self.__controller = Controller() # inits Controller
        self.__controller.load_paths_from_cfg() # ladet alle Paths
        self.__controller.register_commands() # registriert alle Commands
        pass

    # overrided method of UI_Interface
    def set_output(self, output: str,mode: bool):
        # wenn mode = False, dann weiß man, dass es keinen Output gibt
        if not mode:
            self.get_new_line()
            return
            pass
        
        hbox = self.get_hbox_of_widget()
        hbox.setContentsMargins(0, 5, 0, 0)

        lab1 = self.get_label_widget(f"{self.__controller.get_current_dir()}>")
        lab1.setStyleSheet('color:black')  # text of lab1 shouldn't be visible
        hbox.addWidget(lab1)
        hbox.addWidget(self.get_label_widget(output), stretch=1)

        # calls a new line
        self.get_new_line()
        pass

    # overrided method of UI_Interface
    def ask_question(self, question: str):
        hbox = self.get_hbox_of_widget()

        hbox.addWidget(self.get_label_widget(question))
        inp: qt.QLineEdit = self.get_line_edit_widget()
        hbox.addWidget(inp, stretch=1)
        inp.setFocus()
        self.__is_question = True
        pass

    # overrided method of UI_Interface
    def get_answer(self) -> str:
        return self.__last_question_answer

    # init funktion für die UI
    def initUI(self):
        self.__scroll = qt.QScrollArea()
        self.__widget = qt.QWidget()
        self.__vbox = qt.QVBoxLayout()

        self.__widget.setStyleSheet(
            'background-color:black;color:white;font-size:13px;border:0px')
        self.__vbox.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.__vbox.setContentsMargins(0, 0, 0, 0)
        self.__activ_lineEdit = None
        self.get_new_line()

        self.__widget.setLayout(self.__vbox)

        # Scroll Area Properties
        self.__scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.__scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.__scroll.setWidgetResizable(True)
        self.__scroll.setWidget(self.__widget)

        self.setCentralWidget(self.__scroll)
        self.__scroll.scroll(0, self.__widget.height())

        self.setGeometry(600, 100, 677, 343)
        self.setWindowTitle('PullShell')
        self.show()
        pass

    @QtCore.pyqtSlot()
    def on_enter(self):
        if self.__is_question:
            self.__is_question = False
            self.__last_question_answer = self.__activ_lineEdit.text()
            self.__thread.waiting_for_answer_event.set()
            pass
        else:
            # splittet commands nach command und arguments 
            x = self.__activ_lineEdit.text().split(' ')
            self.__thread = My_QThread(self, self.__controller, x)

            # connect all signals from the thread
            self.__thread.ask_question_signal.connect(self.ask_question)
            self.__thread.output_signal.connect(self.set_output)
        
            self.__thread.start() # starts thread
            
        pass

    def handle_process(self):
        # managed Loading Bars, progress, etc
        # for the future
        pass

    # returnt eine neue Line (=Label+LineEdit)
    def get_new_line(self):
        if self.__activ_lineEdit is not None:
            self.__activ_lineEdit.setReadOnly(True)
            pass
        hbox = self.get_hbox_of_widget()

        hbox.addWidget(self.get_label_widget(f"{self.__controller.get_current_dir()}>"))
        hbox.addWidget(self.get_line_edit_widget(), stretch=1)
        # muss gemacht werden, nachdem das Widget angezeigt wird
        self.__activ_lineEdit.setFocus()
        pass

    
    def get_hbox_of_widget(self) -> qt.QHBoxLayout:
        widget = qt.QWidget()
        hbox = qt.QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)

        widget.setLayout(hbox)
        self.__vbox.addWidget(widget)
        return hbox
        pass

    # returnt ein passend designtes LineEdit
    def get_line_edit_widget(self) -> qt.QLineEdit:
        inp = qt.QLineEdit()
        inp.returnPressed.connect(self.on_enter)
        inp.setFocus(Qt.FocusReason.MouseFocusReason)
        self.__activ_lineEdit = inp
        return inp
        pass

    # returnt ein passend designtes Label
    def get_label_widget(self, text: str = "") -> qt.QLabel:
        lab = qt.QLabel(text)
        lab.setTextInteractionFlags(Qt.TextInteractionFlag.TextSelectableByMouse)
        return lab
        pass
    
    pass


def main():
    app = qt.QApplication(sys.argv)
    main = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
