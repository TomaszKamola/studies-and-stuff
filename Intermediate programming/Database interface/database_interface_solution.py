from pprint import pp   # For more user-friendly prints
from pymongo import MongoClient
from bson.objectid import ObjectId
from collections import OrderedDict


# Connection configuration
CONNECTION_STRING = 'mongodb+srv://TomaszKamola:xgQpu7YBi3qPE2VD@cluster0.gvodfaa.mongodb.net/test'

client = MongoClient(CONNECTION_STRING)
db = client['Test']
sample_collection = db['Test']

# Find all objects in collection
for item in sample_collection.find():
    pp(item)

# Find object by ID
query1 = sample_collection.find_one(
    { "_id": ObjectId("6404466ad48a0b23e8b2f43d") }
)
pp(query1)

# Add single object to collection
insertion1 = sample_collection.insert_one(
    {
      "title": "Ratatouille",
      "genres": [ "Animated", "Comedy", "Drama" ],
      "runtime": 111,
      "rated": "G",
      "year": 2007,
      "directors": [ "Brad Bird" ],
      "cast": [ "Will Arnett", "Patton Oswalt", "Lou Romano", "Ian Holm" ],
      "type": "movie"
    }
)

# Add many objects to collection
insertion2 = sample_collection.insert_many([
    {
      "title": "Shrek",
      "genres": [ "Animated", "Comedy" ],
      "runtime": 90,
      "rated": "PG",
      "year": 2001,
      "directors": [ "Vicky Jenson", "Andrew Adamson" ],
      "cast": [ "Mike Myers", "Cameron Diaz", "Eddie Murphy", "John Lithgow" ],
      "type": "movie"
    },
    {
      "title": "Requiem For A Dream",
      "genres": [ "Psychological", "Drama" ],
      "runtime": 102,
      "rated": "R",
      "year": 2000,
      "directors": [ "Darren Aronofsky" ],
      "cast": [ "Jared Leto", "Jannifer Connely" ],
      "type": "movie"
    }
])

## Delete object
deletion1 = { "_id": ObjectId("6404466ad48a0b23e8b2f43d") }
sample_collection.delete_one(deletion1)

## Update object
record = { "title": "Movie12345" }
newdata = { "$set": { "title": "Movie123" } }
sample_collection.update_one(record, newdata)


## Create new database along with Schema and collection
CONNECTION_STRING = "mongodb+srv://TomaszKamola:xgQpu7YBi3qPE2VD@cluster0.gvodfaa.mongodb.net/"

db = MongoClient(CONNECTION_STRING)['BookStore']

book_schema = {
    'title': {
        'type': 'string',
        'minlength': 1,
        'required': True
    },
    'isbn_code': {
        'type': 'string',
        'minlength': 13,
        'required': True
    },
    'author': {
        'type': 'string',
        'minlength': 1,
        'required': True
    },
    'genres': {
        'type': 'array',
        'minlength': 1,
        'required': True
    },
    'year': {
        'type': 'int',
        'minlength': 4,
        'required': True
    },
    'in_store': {
        'type': 'bool',
        'required': True
    },
    'price': {
        'type': 'double',
        'required': True
    }
}

collection = 'BookData'
validator = {
    '$jsonSchema': {
        'bsonType': 'object',
        'properties': {}
    }
}
required = []

for key in book_schema:
    field = book_schema[key]
    properties = {'bsonType': field['type']}
    minimum = field.get('minlength')

    if type(minimum) == int:
        properties['minLength'] = minimum

    if field.get('required') is True:
        required.append(key)

    validator['$jsonSchema']['properties'][key] = properties

if len(required) > 0:
    validator['$jsonSchema']['required'] = required

query = [
    ('collMod', collection),
    ('validator', validator)
]

try:
    db.create_collection(collection)
    db.command(OrderedDict(query))
except Exception as e:
    print(e)


## Add object compatible with validation (for check)
bookdata = db['BookData']

try:
    insert_correct1 = bookdata.insert_one(
        {
        'title': "Alice's Adventures in Wonderland",
        'isbn_code': '978-3-16-148410-0',
        'author': 'Lewis Carroll',
        'genres': ['Fantasy', 'Literary nonsense'],
        'year': 1865,
        'in_store': True,
        'price': 13.95
        }
    )
    insert_correct2 = bookdata.insert_one(
        {
        'title': "Nineteen Eighty-Four",
        'isbn_code': '978-3-22-338412-1',
        'author': 'George Orwell',
        'genres': ['Dystopian', 'political fiction', 'social science fiction'],
        'year': 1949,
        'in_store': True,
        'price': 12.50
        }
    )
    insert_correct3 = bookdata.insert_one(
        {
        'title': "The Emperor's New Clothes",
        'isbn_code': '978-1-13-222525-3',
        'author': 'Hans Christian Andersen',
        'genres': ['Literary folktale'],
        'year': 1837,
        'in_store': False,
        'price': 17.99
        }
    )
except Exception as e:
    print(e)

for book in bookdata.find():
    pp(book)

# Output:
"""
{'_id': ObjectId('6408f9a595ad8341e105847b'),
 'title': "Alice's Adventures in Wonderland",
 'isbn_code': '978-3-16-148410-0',
 'author': 'Lewis Carroll',
 'genres': ['Fantasy', 'Literary nonsense'],
 'year': 1865,
 'in_store': True,
 'price': 13.95}
{'_id': ObjectId('6408f9a695ad8341e105847c'),
 'title': 'Nineteen Eighty-Four',
 'isbn_code': '978-3-22-338412-1',
 'author': 'George Orwell',
 'genres': ['Dystopian', 'political fiction', 'social science fiction'],
 'year': 1949,
 'in_store': True,
 'price': 12.5}
{'_id': ObjectId('6408f9a695ad8341e105847d'),
 'title': "The Emperor's New Clothes",
 'isbn_code': '978-1-13-222525-3',
 'author': 'Hans Christian Andersen',
 'genres': ['Literary folktale'],
 'year': 1837,
 'in_store': False,
 'price': 17.99}
"""

# Add object incompatible with validation (for check)
try:
    insert_incorrect1 = bookdata.insert_one(
        {
        'title': "",
        'isbn_code': '978-0-0',
        'author': 'Random Author 1',
        'genres': ['Fantasy', 'Literary nonsense'],
        'year': 2000,
        'in_store': True,
        'price': 22.33
        }
    )
    insert_incorrect2 = bookdata.insert_one(
        {
        'title': "Nineteen Eighty-Four",
        'isbn_code': '978-3-22-111111-1',
        'author': 'Random Author 2',
        'genres': 'Generic',
        'year': 2001,
        'in_store': 'Yes',
        'price': '12.50'
        }
    )
except Exception as e:
    print(e)

for book in bookdata.find():
    pp(book)

# Output:
""" 
Document failed validation, full error: {'index': 0, 'code': 121, 'errInfo': {'failingDocumentId': ObjectId('6408fce305c181b14806c2c9'), 
'details': {'operatorName': '$jsonSchema', 'schemaRulesNotSatisfied': [{'operatorName': 'properties', 'propertiesNotSatisfied': 
[{'propertyName': 'title', 'details': [{'operatorName': 'minLength', 'specifiedAs': {'minLength': 1}, 'reason': 'specified string length was not satisfied', 
'consideredValue': ''}]}, {'propertyName': 'isbn_code', 'details': [{'operatorName': 'minLength', 'specifiedAs': {'minLength': 13}, 
'reason': 'specified string length was not satisfied', 'consideredValue': '978-0-0'}]}]}]}}, 'errmsg': 'Document failed validation'}

{'_id': ObjectId('6408fcbc86b0c8febfc27527'),
 'title': "Alice's Adventures in Wonderland",
 'isbn_code': '978-3-16-148410-0',
 'author': 'Lewis Carroll',
 'genres': ['Fantasy', 'Literary nonsense'],
 'year': 1865,
 'in_store': True,
 'price': 13.95}
{'_id': ObjectId('6408fcbd86b0c8febfc27528'),
 'title': 'Nineteen Eighty-Four',
 'isbn_code': '978-3-22-338412-1',
 'author': 'George Orwell',
 'genres': ['Dystopian', 'political fiction', 'social science fiction'],
 'year': 1949,
 'in_store': True,
 'price': 12.5}
{'_id': ObjectId('6408fcbd86b0c8febfc27529'),
 'title': "The Emperor's New Clothes",
 'isbn_code': '978-1-13-222525-3',
 'author': 'Hans Christian Andersen',
 'genres': ['Literary folktale'],
 'year': 1837,
 'in_store': False,
 'price': 17.99}
"""
# Non of incompatible object was added.
