from flask import Blueprint, request, jsonify,session
import json
# model 
from flask_socketio import SocketIO , emit , Namespace
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity,create_refresh_token
import jwt
from datetime import datetime, timedelta


api_blueprint = Blueprint('api', __name__)