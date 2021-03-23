from collections import deque


# verwaltet die Command-History von PullShell
class History:
    def __init__(self, max_saved_items: int = 100):
        self.__history: deque = deque()
        self.__max_saved_items: int = max_saved_items
        self.__counter: int = 0
        pass

    # fügt einen neuen Command in die PullShull ein
    def add_to_history(self, command: str):
        if len(self.__history) >= self.__max_saved_items:
            self.__history.pop()
            pass
        self.__history.appendleft(command)
        pass

    # returnt das nächste Element in der History
    def get_next(self) -> str:
        # falls es am Maximum ist, wird der counter reseted
        self.reset_counter() if self.__counter + 1 >= len(self.__history) else self.increment_counter()

        # wenn history 0 groß ist wird "" retured
        return self.__history[self.__counter] if len(self.__history) != 0 else ""
        pass
    
    # returnt das vorherige Element in der History
    def get_previous(self) -> str:
        # falls es am Minimum ist, wird der counter aufs maximum gesetzt
        self.set_counter_to_max() if self.__counter == 0 else self.decrement_counter()

        # wenn history 0 groß ist wird "" retured
        return self.__history[self.__counter] if len(self.__history) != 0 else ""
        pass
    
    # cleared die History
    def clear_history(self):
        self.__history.clear()
        self.__counter = 0
        pass

    # setzt den Counter auf 0
    def reset_counter(self):
        self.__counter = 0
        pass
    
    # erhöht den Counter um 1
    def increment_counter(self):
        self.__counter += 1
        pass
    
    # vermindert den Counter um 1
    def decrement_counter(self):
        self.__counter -= 1
        pass

    # setzt den Counter zur Länge von der History
    def set_counter_to_max(self):
        self.__counter = len(self.__history) - 1 if len(self.__history) != 0 else 0
        pass

    pass
