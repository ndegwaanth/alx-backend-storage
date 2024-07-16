#!/usr/bin/env python3
""" Insert a document in Python"""


def insert_school(mongo_collection, **kwargs):
    """
    insert new documet in a collection
    :mongo_collection: the database collection
    :return: new _id
    """
    result = mongo_collection.insertOne(kwargs)
    return result.inserted_id
