#!/usr/bin/env python3
"""Where can I learn Python?"""


def school_by_topic(mongo_collection, topic):
    """
    return the list of school having specific topic
    :param:mongo_collection:database collection
    :param:topic:(string) will be topic searched
    :return: list of school
    """
    return list(mongo_collection.find({"topic": topic}))
