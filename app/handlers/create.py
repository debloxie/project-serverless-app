import json
import uuid
import time
import logging
from utils import db

# -----------------------------
# Structured JSON Logger Setup
# -----------------------------
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def log(action, status, **kwargs):
    """Helper for consistent structured logging."""
    entry = {
        "action": action,
        "status": status,
        "timestamp": int(time.time())
    }
    entry.update(kwargs)
    logger.info(entry)


# -----------------------------
# Main Lambda Router
# -----------------------------
def lambda_handler(event, context):
    http_method = event.get("httpMethod")
    path = event.get("path", "")

    log("router", "received", method=http_method, path=path)

    try:
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
        elif http_method == "GET" and path.endswith("/health"):
            return handle_health(event)

        else:
            log("router", "error", reason="unsupported_route")
            return {
                "statusCode": 400,
                "body": json.dumps({"message": "Unsupported route"})
            }

    except Exception as e:
        log("router", "exception", error=str(e))
        return {
            "statusCode": 500,
            "body": json.dumps({"message": "Internal server error"})
        }


# -----------------------------
# CREATE
# -----------------------------
def handle_create(event):
    body = json.loads(event.get("body") or "{}")
    item_id = body.get("id") or str(uuid.uuid4())

    item = {
        "id": item_id,
        "name": body.get("name", ""),
        "description": body.get("description", "")
    }

    log("create_item", "received", item=item)

    saved = db.create_item(item)

    log("create_item", "success", item_id=item_id)

    return {
        "statusCode": 201,
        "body": json.dumps(saved)
    }


# -----------------------------
# GET ONE
# -----------------------------
def handle_get(event):
    item_id = event.get("pathParameters", {}).get("id")

    log("get_item", "received", item_id=item_id)

    item = db.get_item(item_id)

    if not item:
        log("get_item", "not_found", item_id=item_id)
        return {
            "statusCode": 404,
            "body": json.dumps({"message": "Item not found"})
        }

    log("get_item", "success", item_id=item_id)

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }


# -----------------------------
# UPDATE
# -----------------------------
def handle_update(event):
    item_id = event.get("pathParameters", {}).get("id")
    body = json.loads(event.get("body") or "{}")

    updates = {
        "name": body.get("name", ""),
        "description": body.get("description", "")
    }

    log("update_item", "received", item_id=item_id, updates=updates)

    updated = db.update_item(item_id, updates)

    log("update_item", "success", item_id=item_id)

    return {
        "statusCode": 200,
        "body": json.dumps(updated)
    }


# -----------------------------
# DELETE
# -----------------------------
def handle_delete(event):
    item_id = event.get("pathParameters", {}).get("id")

    log("delete_item", "received", item_id=item_id)

    result = db.delete_item(item_id)

    log("delete_item", "success", item_id=item_id)

    return {
        "statusCode": 200,
        "body": json.dumps(result)
    }


# -----------------------------
# LIST ALL
# -----------------------------
def handle_list(event):
    log("list_items", "received")

    items = db.list_items()

    log("list_items", "success", count=len(items))

    return {
        "statusCode": 200,
        "body": json.dumps(items)
    }

#### ------------------------
# HEALTH HANDLER
#### -------------------------
def handle_health(event):
    log("health_check", "success")
    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "ok",
            "timestamp": int(time.time())
        })
    }
