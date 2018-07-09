from service import app
from service.routes import api_blueprint


if __name__ == '__main__':
    app.register_blueprint(api_blueprint)
    app.run()
