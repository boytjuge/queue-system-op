from flask import Flask , Blueprint, render_template ,redirect , url_for , request ,jsonify,session # type: ignore
from flask_cors import CORS  # type: ignore
from routes.route_api import *
from routes.route_web import *
app = Flask(__name__,static_url_path='/queue-workflow-system/static')
cors = CORS(app)
app.config['SECRET_KEY'] = '*7r29dUydNma)-++12ksdKajhBXs9z*yTTgd'
app.config['JWT_SECRET_KEY'] = '*7r29dUydNma)-++12ksdKajhBXs9z*yTTgd'
app.config['APPLICATION_ROOT'] = '/queue-workflow-system'
app.register_blueprint(api_blueprint, url_prefix='/queue-workflow-system/api')
app.register_blueprint(web_blueprint, url_prefix='/queue-workflow-system/web')

#app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=10)

jwt = JWTManager(app)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('pages-error-404.html',error=error), 404


@app.errorhandler(500)
def page_error_request(error):
    return 'internal server error', 500


@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        'status': 'error',
        'message': 'Method Not Allowed',
        'error': 'Method Not Allowed'
    }), 405

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

# @app.before_request
# def make_session_permanent():
#     session.permanent = True
#     app.permanent_session_lifetime = timedelta(seconds=4)


if __name__ == '__main__':
    # from routes.route_service import create_socketio
    # create_socketio(app)
    app.run(host='127.0.0.1',port=5000,debug=True)