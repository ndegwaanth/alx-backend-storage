#!/usr/bin/env python3
"""List all documents in Python"""


def list_all(mongo_collection):
    """
    List all documents in a collection
    :param mongo_collection: pymongo collection object
    :return: list of docs or an empty list if no of doc found
    """

    return list(mongo_collection.find())
