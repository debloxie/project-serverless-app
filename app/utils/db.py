import os
import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = os.environ.get("TABLE_NAME", "")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(TABLE_NAME)


def create_item(item: dict):
    table.put_item(Item=item)
    return item


def get_item(item_id: str):
    response = table.get_item(Key={"id": item_id})
    return response.get("Item")


def update_item(item_id: str, updates: dict):
    # Simple overwrite for demo
    item = {"id": item_id, **updates}
    table.put_item(Item=item)
    return item


def delete_item(item_id: str):
    table.delete_item(Key={"id": item_id})
    return {"deleted": True, "id": item_id}


def list_items():
    response = table.scan()
    return response.get("Items", [])
