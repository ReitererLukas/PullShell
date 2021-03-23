from __init__ import *

class Cli(IUI):
  def __init__(self):
    super().__init__()
    self.__is_question = False
    self.on_startup()
    pass

  def on_startup(self):
    self.controller = Controller(self)
    self.controller.load_paths_from_cfg()
    self.controller.register_commands()
    pass
  
  def run(self):
    while True:
      input_command = input(f'{self.controller.get_current_dir()}>')
      if input_command == 'q':
        break
      x = input_command.split(' ')

      self.controller.execute_command(x[0],x[1:])
      pass
    pass

  def ask_question(self, question):
    answer = input(f'{question} ')
    return answer
    pass

  def set_output(self, output):
    print(output)
    pass
  pass


if __name__ == "__main__":
  cli = Cli()
  cli.run()
  pass