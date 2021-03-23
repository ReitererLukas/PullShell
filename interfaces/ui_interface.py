from abc import abstractmethod


# Interface for UI
class IUI:

    # setups the program
    @abstractmethod
    def on_startup(self):
        pass

    # is called to print the output
    @abstractmethod
    def set_output(self, output: str, mode: bool):
        pass

    # stellt eine Frage
    @abstractmethod
    def ask_question(self, question: str) -> str:
        pass

    # liefert die Antwort zurück
    @abstractmethod
    def get_answer(self) -> str:
        pass

    pass
