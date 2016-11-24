from flask import Flask, request
from flask_restful import Resource, Api
import json

class mirror(Resource):

    def post(self, provider_slug):
        return json.loads(request.data.decode('utf-8'))

    def put(self, provider_slug):

        return json.loads(request.data.decode('utf-8'))