from flask import Flask
from .Routers.TodoRouters import todo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# # app.config.from_object('app.settings')
app.register_blueprint(todo)
