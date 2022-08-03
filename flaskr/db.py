import click
from flask import current_app, g
from flask_pymongo import PyMongo
from fake_sample import random_sample


def get_db():
    if 'db' not in g:
        g.db = PyMongo(current_app).db

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    samples = random_sample()
    insert_result = db.mobile_calls.insert_many(samples)
    print(f'top 10 username for testing\n{", ".join(list(set([s["username"] for s in samples]))[:10])}')
    print(f'{len(insert_result.inserted_ids)} calls inserted!')


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
