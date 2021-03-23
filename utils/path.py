# fasst Pfade und Aliasse zusammen
class Path:
  def __init__(self, path: str, alias: str = None):
    self.path: str = path
    self.alias: str = alias
    pass

  def __str__(self) -> str:
    if self.alias == None:
      return f"{self.path}"
      pass
    else:
      return f"{self.path} as {self.alias}"
      pass
    pass

  def getAlias(self) -> str:
    return '' if self.alias == None else self.alias

  def getPath(self) -> str:
    return self.path
  pass

