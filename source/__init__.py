import os


from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE='address',
        DATABASE_USER='address',
        DATABASE_PASSWD='address',
    )

    from . import db
    db.init_app(app)

    from . import index
    app.register_blueprint(index.bp)


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app