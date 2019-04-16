from argparse import ArgumentParser

class Application:
  def __init__(self):
    self.user_input = self.__parse_args__()

    if self.user_input.mass_compare:
      print("Mass Compare!")
    elif self.user_input.compare:
      print("Comapre Individual Files")

  def __parse_args__(self):
    parser = ArgumentParser(
      prog="python main.py",
      description="""
      This tool helps... maybe
      """,
    )
    parser.add_argument(
      "-c",
      "--compare",
      type=str,
      default=False,
      help="Yup, that's what this does."
    )
    parser.add_argument(
      "-m",
      "--mass-compare",
      action="store_true",
      help="... I have no idea... ???"
    )
    return parser.parse_args()
