from controller import Controller

def on_startup():
  controller = Controller()
  controller.load_paths_from_cfg()
  controller.register_commands()
  return controller
  pass

if __name__ == "__main__":
  controller = on_startup()
  while True:
    input_command = input(f'{controller.get_current_dir()}>')
    if input_command == 'q':
      break
    x = input_command.split(' ')

    controller.execute_command(x[0],x[1:])

    pass
  pass