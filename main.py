import controller

def on_startup():
  controller.load_from_cfg()
  pass

if __name__ == "__main__":
  on_startup()
  while True:
    input_command = input('>')
    if input_command == 'q':
      break
    x = input_command.split(' ')

    controller.execute_command(x[0],x[1:])

    pass
  pass