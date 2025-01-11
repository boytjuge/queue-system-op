from flask import Blueprint, request, jsonify,session,render_template,url_for,redirect

# model 
from flask_socketio import SocketIO , emit , Namespace
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity,create_refresh_token
import jwt
from datetime import datetime, timedelta
import json

web_blueprint = Blueprint('web', __name__)


@web_blueprint.route('/login',methods=['get'])
def login():
    return render_template('login.html')