import flask
from flask_restful import Resource, Api, reqparse

import logging
import logging.handlers

import datetime


# Set up circular logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler('/var/log/http.log', maxBytes=65536, backupCount=5)
logger.addHandler(handler)

# Create Flask App
app = flask.Flask(__name__)
api = Api(app)


# Default page
@app.route('/')
def default_page():
    logger.debug('retrieve logs')
    with open('/var/log/http.log', encoding="utf-8") as f:
        s = f.read()
        return s


# Simple resource class
class TestItem(Resource):
    #
    # REST API
    #
    def get(self, id=None):
        ''' Get Resource '''

        # TODO: return something meaningful
        return self.get_test_data(id)

    def post(self, id=None):
        ''' Create Resource '''
        if id is not None:
            abort(400, 'Object id should be null in POST')
        # TODO: create resource here
        return True

    def put(self, id=None):
        ''' Update Resource '''
        if id is None:
            abort(400, 'Object id should not be null in PUT')
        # TODO: update resource here
        return True

    def delete(self, id):
        ''' Delete Resource '''
        if id == 'null' or id is None:
            abort(400, 'Object id should not be null in DELETE')
        # TODO: delete resource here
        return {'deleted': id}

    #
    # Internal methods
    #
    def get_test_data(self, id):
        logger.debug('GET test data')
        test_object = {
            'id': id,
            'test_key': 'test value'
        }
        return test_object


# Register resources
api.add_resource(TestItem, '/test/<string:id>')
