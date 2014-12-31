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
        self.parser.add_argument('value', type=str, location='json')
        self.parser.add_argument('parseId', type=str, location='json')
        self.parser.add_argument('type', type=str, location='json')

        super(TagList, self).__init__()
    def get(self):
        return [x for x in mongo.db.tags.find()]
    def post(self):
        args = self.parser.parse_args()
        #looks to see if expected input exists
        if not args['value']:
            abort(400)
        jo = args
        #checks to make sure this tag doesn't exist
        queryJSON = mongo.db.tags.find_one({"value": jo['value']})
        #if it doesn't exist, insert it into DB
        if not queryJSON:
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

class RemoveTag(restful.Resource):
    #deleting tags by Value
    def __init__(self, *args, **kwargs):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('value', type=str, location='json')
    def post(self):
        args = self.parser.parse_args()
        #looks to see if expected input exists
        if not args['value']:
            abort(400)
        tag = mongo.db.tags.find_one_or_404({"value": args['value']})
        mongo.db.tags.remove({"_id": tag['_id']})
        return '', 204

class TagSearch(restful.Resource):
    #baseline search by regex
    def get(self, word):
        return mongo.db.tags.find({'value': {'$regex': word}})

class TagJQuery(restful.Resource):
    def __init__(self, *args, **kwargs):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('term', type=str, location='args')

        super(TagJQuery, self).__init__()


    def get(self):
        args = self.parser.parse_args()
        values = mongo.db.tags.find({'value': {'$regex': args['term']}})
        return values


class Root(restful.Resource):
    def get(self):
        return {
            'status': 'OK',
            'mongo': str(mongo.db),
        }
api.add_resource(Root, '/')
api.add_resource(TagList, '/tags/')
api.add_resource(Tag, '/tags/<ObjectId:tag_id>')
api.add_resource(RemoveTag,'/removeTag/')
api.add_resource(TagSearch, '/tags/search/<word>')
api.add_resource(TagJQuery, '/frontend/jquery')
