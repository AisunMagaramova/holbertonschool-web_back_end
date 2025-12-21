#!/usr/bin/env python3
"""log stats from collection
"""
from pymongo import MongoClient

METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """Provides stats about Nginx logs stored in MongoDB"""
    if option:
        value = mongo_collection.count_documents({"method": option})
        print(f"\tmethod {option}: {value}")
        return

    total = mongo_collection.count_documents({})
    print(f"{total} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(mongo_collection, method)

    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    nginx_collection = client.logs.nginx
    log_stats(nginx_collection)
