from pymongo import MongoClient
import json

link = "mongodb+srv://ndegwaanth:<password>@cluster0.9eytvzr.mongodb.net/Database1?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(link)

print(client.list_database_names())

db = client.Database1
print(db.list_collection_names())

todo1 = [
    {
        'age': 37,
        'fullnames': 'Mary Onyango',
        'city': [ 'Chicago' ],
        'hobbies': [ 'Programming', 'Reading' ]
    },
    {
        'name': 'Mike Smith',
        'age': 35,
        'city': 'San Francisco'
    },
    {
        'name': 'Anthony',
        'Address': { 'street': 'USA' },
        'hobbies': [ 'Codding' ]
    }
]

todos = db.todos
test = db.test
todos.insert_many(todo1)
test.insert_many(todo1)

print(test.find_one({'fullnames':'Mary Onyango', 'age': 37}))
# print(test.find_many())

data = test.find()

# for i in data:
#     print((i))

print(test.count_documents({}))
