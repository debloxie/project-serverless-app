import json
import uuid
from utils import db


def lambda_handler(event, context):
    http_method = event.get("httpMethod")
    path = event.get("path", "")

    # Route based on method + path
    if http_method == "POST" and path.endswith("/items"):
        return handle_create(event)
    elif http_method == "GET" and "/items/" in path:
        return handle_get(event)
    elif http_method == "PUT" and "/items/" in path:
        return handle_update(event)
    elif http_method == "DELETE" and "/items/" in path:
        return handle_delete(event)
    elif http_method == "GET" and path.endswith("/items"):
        return handle_list(event)
    else:
        return {
            "statusCode": 400,
            "body": json.dumps({"message": "Unsupported route"})
        }


def handle_create(event):
    body = json.loads(event.get("body") or "{}")
    item_id = body.get("id") or str(uuid.uuid4())
    item = {
        "id": item_id,
        "name": body.get("name", ""),
        "description": body.get("description", "")
    }
    saved = db.create_item(item)
    return {
        "statusCode": 201,
        "body": json.dumps(saved)
    }


def handle_get(event):
    item_id = event.get("pathParameters", {}).get("id")
    item = db.get_item(item_id)
    if not item:
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Item not found"})
        }
    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }


def handle_update(event):
    item_id = event.get("pathParameters", {}).get("id")
    body = json.loads(event.get("body") or "{}")
    updates = {
        "name": body.get("name", ""),
        "description": body.get("description", "")
    }
    updated = db.update_item(item_id, updates)
    return {
        "statusCode": 200,
        "body": json.dumps(updated)
    }


def handle_delete(event):
    item_id = event.get("pathParameters", {}).get("id")
    result = db.delete_item(item_id)
    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }


def handle_list(event):
    items = db.list_items()
    return {
        "statusCode": 200,
        "body": json.dumps(items)
    }
