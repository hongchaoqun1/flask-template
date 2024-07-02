from flask import jsonify
from . import main
from ..model import Staff
from ..utils import json_response
from app import db


@main.route('/hello')
def hello_world():  # put application's code here
    staff = Staff(username='admin')
    db.session.add(staff)
    db.session.commit()
    return json_response("Hello, World!")
