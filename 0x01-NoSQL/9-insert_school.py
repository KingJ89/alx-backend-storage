#!/usr/bin/env python3
"""inserts a new document in thecollection"""

def insert_school(mongo_collection, **kwargs):
    """
    mongo_collection will be the collection object
    Returns the new _id
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
