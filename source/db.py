import click
import mysql.connector
from flask import current_app, g


def get_db():
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE'],
            user=current_app.config['DATABASE_USER'],
            passwd=current_app.config['DATABASE_PASSWD']
        )

    return g.db 


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        with db.cursor() as cursor:
            cursor.execute(f.read().decode('utf8'), multi=True)
    db.commit()
        
def execute_db(query_db):
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute(query_db)
    db.commit()
    

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)