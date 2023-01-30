import json
import os
from pathlib import Path

import redis  # type: ignore
from dotenv import load_dotenv
from fastapi.encoders import jsonable_encoder

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

pool = redis.ConnectionPool(
    host=os.getenv('REDIS_HOST'),
    port=os.getenv('REDIS_PORT'),
    db=os.getenv('REDIS_DB'),
    decode_responses=True,
)
redis_client = redis.Redis(connection_pool=pool)


def cache_get_list(key):
    res = redis_client.get(key)
    if res:
        return json.loads(res)
    return None


def cache_get_item(key, key_id):
    key = f'{key}:{key_id}'
    res = redis_client.get(key)
    if res:
        return json.loads(res)
    return None


def cache_set_list(key, items):
    redis_client.set(key, json.dumps(jsonable_encoder(items)))


def cache_set_item(key, item):
    key = f'{key}:{item["id"]}'
    redis_client.set(key, json.dumps(jsonable_encoder(item)))


def cache_delete_list(key):
    redis_client.delete(key)


def cache_delete_item(key, key_id):
    key = f'{key}:{key_id}'
    redis_client.delete(key)
