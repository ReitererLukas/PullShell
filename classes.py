from collections import deque

class Path:
  def __init__(self, path, alias = None):
    self.path = path
    self.alias = alias
    pass

  def __str__(self):
    if self.alias == None:
      return f"{self.path}"
      pass
    else:
      return f"{self.path} as {self.alias}"
      pass
    pass

  def getAlias(self):
    return '' if self.alias == None else self.alias

  def getPath(self):
    return self.path
  pass

class History:
  def __init__(self,saved_items = 100):
    self.__history = deque()
    self.saved_items = saved_items
    self.counter = 0
    pass

  def add_to_history(self, command):
    if len(self.__history) >= self.saved_items:
      self.__history.pop()
      pass
    self.__history.appendleft(command)
    pass
  
  def get_next(self):
    if counter + 1 >= len(self.__history):
      reset_counter()
      pass
    else:
      self.counter += 1
      pass
    return history[self.counter]
    pass

  def reset_counter(self):
    self.counter = 0
    pass
  
  pass