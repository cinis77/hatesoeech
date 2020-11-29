import threading

from flask import Flask

from utils.config_parser import Config
from gevent.pywsgi import WSGIServer

from web.views.api_controller import api_controller
from web.views.web_controller import web_controller

PORT = Config.getint_or_else("API", "Port", 4000)

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.secret_key = b'_1327567464166'
app.config["PORT"] = PORT
app.config["HOST"] = "0.0.0.0"
app.config["THREADED"] = True
app.config["DEBUG"] = False
app.register_blueprint(api_controller)

if Config.getboolean_or_else("API", "GUI", False):
    app.register_blueprint(web_controller)


class WebApp(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        http_server = WSGIServer(('0.0.0.0', PORT), app)
        http_server.serve_forever()
