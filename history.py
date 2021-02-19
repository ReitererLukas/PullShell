from collections import deque

class History:
  def __init__(self,max_saved_items = 100):
    self.__history = deque()
    self.__max_saved_items = max_saved_items
    self.__counter = 0
    pass

  def add_to_history(self, command):
    if len(self.__history) >= self.__max_saved_items:
      self.__history.pop()
      pass
    self.__history.appendleft(command)
    pass
  
  def get_next(self):
    if self.__counter + 1 >= len(self.__history):
      self.reset_counter()
      pass
    else:
      self.__counter += 1
      pass
    return self.__history[self.__counter]
    pass

  def clear_history(self):
    self.__history.clear()
    self.__counter = 0
    pass

  def reset_counter(self):
    self.__counter = 0
    pass
  
  pass