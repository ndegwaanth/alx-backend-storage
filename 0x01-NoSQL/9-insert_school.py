#!/usr/bin/env python3
""" Insert a document in Python"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    insert new documet in a collection
    :mongo_collection: the database collection
    :return: new _id
    """
    result = mongo_collection.insert_one(kwargs).inserted_id
    return result
