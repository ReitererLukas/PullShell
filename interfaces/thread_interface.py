from abc import abstractmethod


# Interface for Threads
class IThread:

    # setzt einen Output
    @abstractmethod
    def set_output(self, output: str, mode: bool = True):
        pass

    # stellt eine Frage
    @abstractmethod
    def ask_question(self, question: str) -> str:
        pass

    pass
