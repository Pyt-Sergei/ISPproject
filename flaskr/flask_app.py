from flask import Flask


def create_app():
    # create and configure the app
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config.update(
        broker_url='redis://localhost:6379',
        result_backend='redis://localhost:6379',
    )

    return app


app = create_app()
