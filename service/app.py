import os, json, time
from flask import Flask, render_template, Response
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS
from db import Doc, Card, Hand, Player, Game 
import datetime
import config


app = Flask(__name__)
api = Api(app)
cors = CORS(app)

cj = None

@app.route('/')
def welcome():
    return render_template('index.html') 

    
class Deck(Resource):
    """
    Look at all the cards
    """
    def get(self, id=None):
        c = Card()
        return c.show(start=int(id))


class Search(Resource):
    """Search for name text match on card"""
    def get(self, text):
	c= Card()
	return c.by_name(text)	

class StorableResource(Resource):
    host = config.host
    obj = Doc
    
    def get(self, id):
        o = self.obj()
        return o.by_id(int(id))

    def post(self):
        """
        Add a new find to the collection.
        """
        
        parser = reqparse.RequestParser()
        parser.add_argument('data',type=str)
        args = parser.parse_args()
        
        data = {}        

        input = args['data']

        # we roundtrip the data into python and back to JSON
        # in the real world, we would validate the data structure here.

        try:
            data = json.loads(input)
        except ValueError, e:
            return {'error', e.message}, 500

        o = self.obj()
        data['_id'] = o.get_next_in_sequence()

        o.insert(json.dumps(data))
        return {'success':data['_id']}, 200

    def request(self,url):
        """Request JSON from a URL, return parsed objects"""
        if url.startswith('/'):
            url = self.host + url
        return json.loads(urllib.urlopen(url).read())

class ThisCard(StorableResource):
    obj = Card


class Random(Resource):
    def get(self):
        c = Card()
        return c.pick_n(1)

class ThisHand(StorableResource):
    obj = Hand
    def post(self):
        pass

class Game(StorableResource):
    def post(self):
        """Spin up a new game"""
        deck = self.request('deck')
        parser = reqparse.RequestParser()
        parser.add_argument('player1',type=str)
        parser.add_argument('player2',type=str)
        args = parser.parse_args()
        print deck 

class PlayerDetails(StorableResource):
    """
    
    """
    obj = Player  
 

class Scoreboard(Resource):
    """
    """
    def get(self):
        pass 


api.add_resource(Deck, '/deck/','/deck/from/<id>')
api.add_resource(ThisCard, '/card/<id>', '/card/', '/card')
api.add_resource(Random,'/random/')
api.add_resource(PlayerDetails, '/user/', '/user/<id>')
api.add_resource(Scoreboard, '/scoreboard/')
api.add_resource(Search, '/search/<text>')
api.add_resource(ThisHand, '/hand/', '/hand/<id>')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
