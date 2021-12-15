from flask.cli import FlaskGroup
from src import app

# extending the Flask CLI with our own 
cli = FlaskGroup(app)

if __name__ == '__main__':
    cli()