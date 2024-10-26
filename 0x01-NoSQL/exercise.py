#!/usr/bin/env python3
"""Inserts a new document into a MongoDB collection."""

from pymongo.collection import Collection

def insert_school(mongo_collection: Collection, **kwargs) -> str:
    """
    Inserts a new document into the specified MongoDB collection.

    Parameters:
    - mongo_collection: A pymongo Collection object where the document will be inserted.
    - **kwargs: Key-value pairs representing the document fields and values.

    Returns:
    - The _id of the newly inserted document.
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
