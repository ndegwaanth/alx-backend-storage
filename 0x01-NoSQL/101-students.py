#!/usr/bin/python3
"""101-students.py"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score in desc order
    :param mongo_collection: pymongo collection object
    :return: list of students sorted by average score
    """
    students = list(mongo_collection.find())
    for student in students:
        total_score = 0
        for topic in student['topics']:
            total_score += topic['score']
        average_score = total_score / len(student['topics'])
        student['averageScore'] = average_score
    sort = sorted(students, key=lambda x: x['averageScore'], reverse=True)
    return sort
