#!/usr/bin/env python3
""" Change school topics"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    :param mongo_collection: pymongo collection object
    :param name: string, school name to update
    :param topics: list of strings, list of topics approached in the school
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
