import pymongo

import config
from util import deal
import json 
import re

client = pymongo.MongoClient(config.mongo_dsn)
db = client['trumpz']
from random import randrange


class Doc():
    collection = 'default'
    counter = None
    def __init__(self):
        pass

    def save():
        pass 
    
    def insert(self, doc):
        """
        Inserts a JSON document into the collection.
        """
        data = {}
        try:
	    data = json.loads(doc)

        except:
            raise ValueError,"We were expecting a JSON document"

        if '_id' not in data:
            data['_id'] = self.get_next_in_sequence()

        self.add(data)

    def add(self, data):
        """
        Adds a data structure to the collection
        """
	db[self.collection].insert(data)

    def recent_n(self,number):
        return list(db[self.collection].find().limit(number))
 
    def get_next_in_sequence(self):
        doc = db['counters'].find_and_modify(
            query = { "_id": self.counter}, 
            update = {"$inc":{"seq":1}},
            new=True)
        return int(doc['seq'])

    def pick_one(self):
        """
        Pick the most recent animal, vegetable, etc
        """
        return db[self.collection].find_one()

    def show_all(self):
        return list(db[self.collection].find().limit(50))

    def show(self, start=None):
	if start is not None:
	    return list(db[self.collection].find({'_id':{'$gt':start}}).limit(50))
	else:
	    return list(db[self.collection].find().limit(50))

    def by_id(self, id):
        return db[self.collection].find_one({"_id": id})
    
    def by_name(self, name):
        return db[self.collection].find_one({'name':name})
    
    def match_name(self, name):
	regx = re.compile(name)
	return list(db[self.collection].find({'name': {'$regex' : regx}}))

class Card(Doc):
    collection = 'deck'
    counter = 'card'
    def pick_n(self, n):
        """
        """
        numbers = [] 
        items = {}

        total = db[self.collection].count()
        while len(numbers) < n:
            my_random = randrange(0,total)
            if my_random not in numbers:
	        items[my_random] = db[self.collection].find().limit(-1).skip(my_random).next()        
		numbers.append(my_random)

        return items.values()


class Hand(Doc):
    collection = 'hand'
    counter = 'hand'

    def __init__(self,player=None,cards=None):
        p = Player(player)
        
        

class Player(Doc):
    counter = 'player'
    collection = 'player'
    def __init__(self,name):
        return self.by_name(name)

class Game(Doc):
    counter = 'game' 
    collection = 'game'

    def start(self, player1, player2):
        # select N hand*2 from deck at random
        # deal them into two piles
        # each pile gets a Hand document
        c = Card()
        cards = c.pick_n(config.handsize*2)
        pile1, pile2 = deal(cards)
        
        h = Hand(player=player1, cards=pile1)
        h2 = Hand(player=player2, cards=pile2)

