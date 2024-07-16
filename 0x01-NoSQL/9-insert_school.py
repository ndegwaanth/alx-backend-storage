#!/usr/bin/env python3
""" Insert a document in Python"""
from pymongo import MongoClient


def insert_school(mongo_collection, **kwargs):
    """
    insert new documet in a collection
    :mongo_collection: the database collection
    :return: new _id
    """
    result_ = mongo_collection.insertOne(kwargs).inserted_id
    return result_
