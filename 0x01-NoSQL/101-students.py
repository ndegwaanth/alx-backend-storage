#!/usr/bin/env python3
"""101-students.py"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score in descending order.

    :param mongo_collection: pymongo collection object
    :return: list of students sorted by average score
    """
    students = list(mongo_collection.find())  # Fetch all students
    for student in students:
        total_score = 0
        for topic in student['topics']:
            total_score += topic['score']
        average_score = total_score / len(student['topics'])
        student['averageScore'] = average_score  # Add averageScore field
    sorted_students = sorted(students,
                             key=lambda x: x['averageScore'],
                             reverse=True)  # Sort by averageScore
    return sorted_students
