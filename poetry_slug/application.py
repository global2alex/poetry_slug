import click

@click.group()
def Application():
  """
  Just a test, hello?
  """

@Application.command('compare', short_help='Number of greetings.')
def cli(count):
  """
  test2
  """
