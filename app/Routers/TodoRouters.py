from flask import Blueprint, request, json

todo = Blueprint('todo', __name__)

# http://localhost:5000/api/login  method = GET

@todo.route('/api', methods=['GET'])
def get_all():
    return 'ok'