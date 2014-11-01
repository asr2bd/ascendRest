__name__ = 'ascendrest'
import json
from flask import request, abort
from flask.ext import restful
from flask.ext.restful import reqparse
from flask_rest_service import app, api, mongo
from bson.objectid import ObjectId

class TagList(restful.Resource):
    def __init__(self, *args, **kwargs):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('tag', type=str)
        super(TagList, self).__init__()
    def get(self):
        return [x for x in mongo.db.tags.find()]
    def post(self):
        args = self.parser.parse_args()
        #looks to see if expected input exists
        if not args['tag']:
            abort(400)

        jo = json.loads(args['tag'])
        #checks to make sure this tag doesn't exist
        queryJSON = mongo.db.tags.find_one({"name": jo['name']})
        #if it doesn't exist, insert it into DB
        if not queryJSON['name']:
            tag_id = mongo.db.tags.insert(jo)
            return mongo.db.tags.find_one({"_id": tag_id})
        else:
            abort(400)

class Tag(restful.Resource):
    #returning and deleting tags by ID
    def get(self, tag_id):
        return mongo.db.tags.find_one_or_404({"_id": tag_id})

    def delete(self, tag_id):
        mongo.db.tags.find_one_or_404({"_id": tag_id})
        mongo.db.tags.remove({"_id": tag_id})
        return '', 204

class TagSearch(restful.Resource):
    #baseline search by regex
    def get(self, word):
        return mongo.db.tags.find({'name': {'$regex': word}})

class Root(restful.Resource):
    def get(self):
        return {
            'status': 'OK',
            'mongo': str(mongo.db),
        }
api.add_resource(Root, '/')
api.add_resource(TagList, '/tags/')
api.add_resource(Tag, '/tags/<ObjectId:tag_id>')
api.add_resource(TagSearch, '/tags/search/<word>')