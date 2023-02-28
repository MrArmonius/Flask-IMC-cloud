import click
import mysql.connector
from flask import current_app, g


def get_db():
    host_arg = "mysql_server"
    print("Host choosed: ", host_arg)
    if 'db' not in g:
        g.db = mysql.connector.connect(
            host=host_arg,
            database=current_app.config['DATABASE'],
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
        lines = f.read().decode('utf-8')
        print(lines)
        split_line = lines.split('\n')
        print("size: ", len(split_line))
        with db.cursor() as cursor:
            for line in split_line:
                if line != "":
                    cursor.execute(line, multi=True)
 #   db.commit()
        
def execute_db(query_db):
    db = get_db()
    with db.cursor() as cursor:
        cursor.execute(query_db)
    db.commit()

def get_all_database():
    db = get_db()
    return_value = []
    with db.cursor() as cursor:
        cursor.execute("SELECT * FROM data_tp1;")
        return_value = cursor.fetchall()
    return return_value
    

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
