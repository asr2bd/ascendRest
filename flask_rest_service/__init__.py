__name__ = 'ascendrest'
import os
from flask import Flask
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from flask.ext.restful.utils import cors
from flask import make_response
from bson.json_util import dumps

app = Flask(__name__)

MONGO_URL = os.environ.get('MONGO_URL')
if not MONGO_URL:
    import CONFIG
    MONGO_URL = CONFIG.MONGO_URI

app.config['MONGO_URI'] = MONGO_URL
mongo = PyMongo(app)

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

def options (self):
    pass

DEFAULT_REPRESENTATIONS = {'application/json': output_json}

api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS
api.decorators = [cors.crossdomain(origin='*', headers=['accept', 'Content-Type'])]

import flask_rest_service.resources

#this file initializes the application, the connection to mongo, and makes sure what
#mongo spits out is JSON instead of binary