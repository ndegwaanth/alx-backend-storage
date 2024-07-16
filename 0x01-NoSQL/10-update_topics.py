#!/usr/bin/env python3
""" Change school topics"""


def update_topic(mongo_collection, name, topics):
    """"
    changes all topics of a school document
    :param:mongo_collection: database collection
    :param:name: (string) will be school name to update
    :param:topics: list of topics approached in the school
    """
    mongo_collection.update_many({
        "name": name}, {"topics": topics})
