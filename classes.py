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