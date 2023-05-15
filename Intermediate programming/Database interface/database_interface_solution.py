from pprint import pp   # For more user-friendly prints
from pymongo import MongoClient
from bson.objectid import ObjectId
from collections import OrderedDict


## 1
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


### 2
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


## 3
from pprint import pp   # for better output reading
from pymongo import MongoClient
from datetime import date


# Connection configuration
CONNECTION_STRING = "mongodb+srv://TomaszKamola:xgQpu7YBi3qPE2VD@cluster0.gvodfaa.mongodb.net/"
db = MongoClient(CONNECTION_STRING)['BookStore']
bookdata = db['BookData']


class DatabaseActions:

    def __init__(self, collection):
        self.collection = collection
        self.keys = [
            'title',
            'isbn_code',
            'author',
            'genres',
            'year',
            'in_store',
            'price'
        ]

    @staticmethod
    def info():
        info = """ 
Oto operacje, które możesz wykonać:
    add - dodawanie wpisu do kolekcji

        Składnia polecenia:
        add <klawisz enter>
        [
            Tytuł: <(string)>, 
            Kod ISBN: <(string)>, 
            Autor: <(string)>, 
            Gatunki: <gatunek1, gatunek2, ... (lista)>, 
            Rok: <(int)>, 
            W magazynie: <True | False (bool)>, 
            Cena: <(float)>
        ]

        Przykład:
        add <klawisz enter>
        
            Tytuł: Książka XYZ, 
            Kod ISBN: 978-3-16-122470-0, 
            Autor: Autor XYZ, 
            Gatunki: Horror, 
            Rok: 1999, 
            W magazynie: True, 
            Cena: 13.99

    del - usuwanie wpisu z kolekcji

        Składnia polecenia:
        del <parametr> <wartość>

        Przykład:
        del author George Orwell
        
    set - zmiana parametrów wpisu

        Składnia polecenia:
        set <parametr> <wartość> -> ustaw wartość parametru dla wszystkich wpisów
        set <parametr> <wartość> where <parametr> <wartość> -> ustaw wartość parametru dla wpisów z określonym parametrem

        Przykład:
        set price 0.0
        set title XYZ where title Anne Of Green Gables

    get - zwracanie kolekcji/wpisu

        Składnia polecenia:
        get -> zwraca całą kolekcję
        get <parametr> <wartość> -> zwraca wpis o określonym parametrze

        Przykład:
        get genres Powieść
        get genres Powieść, Horror
        get year 1998
        """

        return info
    
    def get(self, parameter=None, value=None):
        if parameter is None and value is None:
            print("Obecny stan kolekcji:\n")
            result = [item for item in self.collection.find()]

            if len(result) < 1:
                return "Kolekcja pusta."
            
            else:
                return result

        if parameter is not None and value is not None:
            result = [item for item in self.collection.find({ parameter: value })]

            if len(result) < 1:
                return "Nie istnieje wpis o podanych parametrach."
            
            else:
                return result

        else:
            raise TypeError("Oba argumenty powinny być None lub odpowiednie dla pól obiektu")
        
    def add(self, input_list):
        if isinstance(input_list, list):
            values = [value for value in input_list]

            if len(self.keys) == len(values):
                insert_data = {key: value for key, value in zip(self.keys, values)}

                try:
                    insert_data['year'] = int(insert_data['year'])
                except Exception as e:
                    print(f"{e}: Rok musi być liczbą.")

                try:
                    insert_data['price'] = float(insert_data['price'])
                except Exception as e:
                    print(f"{e}: Cena musi być liczbą zmiennoprzecinkową.")

                try:
                    insert = insert_data['in_store'].capitalize()
                    if insert in ['True', 'False']:
                        if insert == 'True':
                            insert_data['in_store'] = True
                        else:
                            insert_data['in_store'] = False
                except Exception as e:
                    print(f"{e}: W magazynie musi być prawdą lub fałszem.")

                if not isinstance(insert_data['title'], str):
                    raise TypeError(f"Wartość {insert_data['title']}(tytuł) musi być typu string")
                
                if not isinstance(insert_data['isbn_code'], str):
                    raise TypeError(f"Wartość {insert_data['isbn_code']}(ISBN) musi być typu string")
                
                if len(insert_data['isbn_code']) < 13:
                    raise TypeError(f"Wartość {insert_data['isbn_code']}(ISBN) musi mieć minimum 13 znaków")
                
                if not isinstance(insert_data['author'], str):
                    raise TypeError(f"Wartość {insert_data['author']}(autor) musi być typu string")
                
                if not isinstance(insert_data['genres'], list):
                    raise TypeError(f"Wartość {insert_data['genres']}(gatunki) musi być listą")
                
                if not isinstance(insert_data['year'], int):
                    raise TypeError(f"Wartość {insert_data['year']}(rok) musi być typu int")
                
                if insert_data['year'] > date.today().year:
                    raise ValueError(f"Rok {insert_data['year']} jeszcze nie nastąpił")
                
                if not isinstance(insert_data['in_store'], bool):
                    raise TypeError(f"Wartość {insert_data['in_store']}(w magazynie) musi być typu bool (True/False)")
                        
                if not isinstance(insert_data['price'], float):
                    raise TypeError(f"Wartość {insert_data['price']}(cena) musi być typu float")
                
                else:
                    self.collection.insert_one(insert_data)

                    print('\nPomyślnie dodano obiekt:\n')
                    [pp(item) for item in self.collection.find().sort('_id', -1).limit(1)]

            else:
                raise TypeError("Podałeś niepoprawną ilość parametrów dla nowego obiektu!")
            
        else:
            raise TypeError("Polecenie 'add' przyjmuje wyłącznie listę")
        
    def delete(self, parameter, value):
        if parameter not in self.keys:
            raise NameError(f"Nazwa parametru {parameter} nie jest rozpoznawalna")
        
        else:
            if parameter == 'title' and not isinstance(value, str):
                raise TypeError(f"Parametr {parameter} musi być typu string")

            if parameter == 'isbn_code' and not isinstance(value, str):
                raise TypeError(f"Parametr {parameter} musi być typu string")

            if parameter == 'author' and not isinstance(value, str):
                raise TypeError(f"Parametr {parameter} musi być typu string")

            if parameter == 'genres' and (not isinstance(value, str) and not isinstance(value, list)):
                raise TypeError(f"Parametr {parameter} musi być typu string albo list")

            if parameter == 'year' and not isinstance(value, int):
                raise TypeError(f"Parametr {parameter} musi być typu int")

            if parameter == 'in_store' and not isinstance(value, bool):
                raise TypeError(f"Parametr {parameter} musi być typu bool")

            if parameter == 'price' and not isinstance(value, float):
                raise TypeError(f"Parametr {parameter} musi być typu float")

            else:
                result = self.get(parameter, value)

                if result is None:
                    raise ValueError("Obiekt o podanych parametrach nie istnieje")
                
                else:
                    self.collection.delete_many({ parameter: value })

                    print('\nPomyślnie usunięto obiekty:\n')
                    for item in result:
                        pp(item)
                    

    def set(self, parameter1, value1, parameter2=None, value2=None):
        if parameter1 not in self.keys and parameter1 != 'where':
            raise NameError(f"Nazwa parametru {parameter1} nie jest rozpoznawalna")
        
        else:
            if parameter1 == 'title' and not isinstance(value1, str):
                raise TypeError(f"Parametr {parameter1} musi być typu string")

            if parameter1 == 'isbn_code' and not isinstance(value1, str):
                raise TypeError(f"Parametr {parameter1} musi być typu string")

            if parameter1 == 'author' and not isinstance(value1, str):
                raise TypeError(f"Parametr {parameter1} musi być typu string")

            if parameter1 == 'genres' and (not isinstance(value1, str) and not isinstance(value1, list)):
                raise TypeError(f"Parametr {parameter1} musi być typu string albo list")

            if parameter1 == 'year' and not isinstance(value1, int):
                raise TypeError(f"Parametr {parameter1} musi być typu int")

            if parameter1 == 'in_store' and not isinstance(value1, bool):
                raise TypeError(f"Wartość {parameter1}(w magazynie) musi być typu bool (True/False)")

            if parameter1 == 'price' and not isinstance(value1, float):
                raise TypeError(f"Parametr {parameter1} musi być typu float")

            else:
                if parameter2 is None and value2 is None:
                    self.collection.update_many(
                        {}, 
                        { "$set": 
                            { parameter1: value1 } 
                        }, 
                        upsert=False, 
                        array_filters=None
                    )

                if parameter2 is not None and value2 is not None:
                    self.collection.update_many(
                        { parameter2: value2 },
                        { "$set": 
                            { parameter1: value1 } 
                        }, 
                        upsert=False, 
                        array_filters=None
                    )

                getted = self.get(parameter1, value1)

                if not isinstance(getted, list):
                    print(getted)
                
                else:
                    print('\nPomyślnie zmieniono obiekty:\n')
                    for item in getted:
                        pp(item)



if __name__ == "__main__":

    collection = DatabaseActions(bookdata)
    
    info = DatabaseActions.info()
    print("Witaj w programie do obsługi bazy danych BookStore!")
    print("Aby wyświetlić instrukcje wpisz help\n")

    def split_data(input_data):
        splitted = input_data.replace("'", "").replace('"', '').split(" ")
        output = []

        if 'where' in splitted:
            values_to_set = []
            values_to_get = []

            for i in range(len(splitted)):
                if i >= splitted.index('where'):
                    values_to_get.append(splitted[i])
                else:
                    values_to_set.append(splitted[i])

            key = values_to_set[1]
            values = values_to_set[2:]
            merged_values = ' '.join(values)
            output.append(key)
            if key == 'genres' and len(values) >= 2:
                values = [value.replace(",", "") for value in values]
                output.append(values)
            elif key == 'genres' and len(values) < 2:
                output.append(values[0])
            elif key == 'year':
                output.append(int(values[-1]))
            elif key == 'price':
                output.append(float(values[-1]))
            elif key == 'in_store':
                if values[-1] in ['True', 'true']:
                    output.append(True)
                else:
                    output.append(False)
            else:
                output.append(merged_values)

            key = values_to_get[1]
            values = values_to_get[2:]
            merged_values = ' '.join(values)
            output.append(key)
            if key == 'genres' and len(values) >= 2:
                values = [value.replace(",", "") for value in values]
                output.append(values)
            elif key == 'genres' and len(values) < 2:
                output.append(values[0])
            elif key == 'year':
                output.append(int(values[-1]))
            elif key == 'price':
                output.append(float(values[-1]))
            elif key == 'in_store':
                if values[-1] in ['True', 'true']:
                    output.append(True)
                else:
                    output.append(False)
            else:
                output.append(merged_values)

            return output

        elif 'where' not in splitted:
            key = splitted[1]
            values = splitted[2:]
            merged_values = ' '.join(values)
            output.append(key)
            if key == 'genres' and len(values) >= 2:
                values = [value.replace(",", "") for value in values]
                print(values, " len >= 2")
                output.append(values)
            elif key == 'genres' and len(values) < 2:
                output.append(values[0])
            elif key == 'year':
                output.append(int(values[-1]))
            elif key == 'price':
                output.append(float(values[-1]))
            elif key == 'in_store':
                if values[-1] in ['True', 'true']:
                    output.append(True)
                else:
                    output.append(False)
            else:
                output.append(merged_values)

        return output
    

    while True:
        try:
            commands = ['add', 'del', 'set', 'get', 'help', 'end']
            input_data = input("Wpisz polecenie: >>>")
            input_list = input_data.split()

            if len(input_data) < 1:
                print("Nie wpisano polecenia.")
                continue
            
            if input_list[0] not in commands:
                print("Polecenie nie istnieje.")

            else:
                if input_list[0] == 'add':
                    data_add = [
                        input('Tytuł: '),
                        input('Kod ISBN: '),
                        input('Autor: '),
                        input('Gatunki: ').replace(" ", "").split(","),
                        input('Rok wydania: '),
                        input('W magazynie: '),
                        input('Cena: ')
                    ]

                    collection.add(data_add)

                if input_list[0] == 'del':
                    if len(input_list) <= 2:
                        print("Niepoprawne parametry.")

                    else:
                        values = split_data(input_data)
                        collection.delete(values[0], values[1])

                if input_list[0] == 'set':
                    if len(input_list) <= 2:
                        print("Niepoprawne parametry.")

                    else:
                        values = split_data(input_data)

                        print(values)
                        if len(values) > 2:
                            if isinstance(values[1], str) and values[0] == 'genres':
                                values[1] = [values[1]]
                            
                            if isinstance(values[3], str) and values[2] == 'genres':
                                values[3] = [values[3]]
                                
                            collection.set(values[0], values[1], values[2], values[3])
                            
                        else:
                            if isinstance(values[1], str) and values[0] == 'genres':
                                values[1] = [values[1]]

                            collection.set(values[0], values[1])

                if input_list[0] == 'get':
                    if len(input_list) > 1:
                        values = split_data(input_data)
                        print(values)
                        pp(collection.get(values[0], values[1]))

                    else:
                        pp(collection.get())

                if input_list[0] == 'help':
                    print(info)

                if input_list[0] == 'end':
                    print('Program zamknięty.')
                    break
                
            continue
        
        except Exception as e:
            print(e)
            continue
