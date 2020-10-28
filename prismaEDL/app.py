from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    from prismaEDL.views import main
    app.register_blueprint(main)

    app.config['PRISMA_API_KEY'] = os.environ.get('PRISMA_API_KEY')

    return app


if __name__ == '__main__':
    create_app().run()
