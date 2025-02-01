import redis
import json
from django.conf import settings

class RedisHandler:
    def __init__(self):
        self.redis_client = redis.StrictRedis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=settings.REDIS_DB,
            decode_responses=True
        )

    def set_cache_with_transaction(self, key, value):
        try:
            with self.redis_client.pipeline() as pipe:
                pipe.multi()
                pipe.set(key, json.dumps(value))
                pipe.execute()
        except redis.RedisError as e:
            print(f"Redis transaction failed: {e}")

    def get_cache(self, key):
        try:
            cached_data = self.redis_client.get(key)
            if cached_data:
                return json.loads(cached_data)
            return None
        except redis.RedisError as e:
            print(f"Failed to get cache: {e}")
            return None

    def delete_cache(self, key):
        try:
            self.redis_client.delete(key)
        except redis.RedisError as e:
            print(f"Failed to delete cache: {e}")