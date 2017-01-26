import click
 
@click.command()
@click.help_option('-h', '--help')
@click.version_option('2.0', '-v', '--version', message='%(prog)s v%(version)s')
def cli():
    """This does almost nothing"""
 
if __name__ == '__main__':
    cli()