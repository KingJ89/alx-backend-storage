#!/usr/bin/env python3
"""Updates all topics of a school document based on the given name."""

from pymongo.collection import Collection
from typing import List

def update_topics(mongo_collection: Collection, name: str, topics: List[str]) -> None:
    """
    Updates the 'topics' field of documents in the collection where the 'name' field matches.

    Parameters:
    - mongo_collection (Collection): The pymongo collection object.
    - name (str): The name of the school whose topics need updating.
    - topics (List[str]): A list of topics to set for the school.
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
