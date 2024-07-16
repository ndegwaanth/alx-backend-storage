#!/usr/bin/env python3
"""Where can I learn Python?"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns a list of schools having a specific topic.

    :param mongo_collection: pymongo collection object
    :param topic: string, topic searched
    :return: list of schools matching the topic
    """
    return list(mongo_collection.find({"topics": topic}))
