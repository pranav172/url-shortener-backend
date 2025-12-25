import redis

# redis_client = redis.Redis(
#     host="localhost",
#     port=6379,
#     decode_responses=True  # return strings, not bytes
# )
import os
redis_client = redis.Redis.from_url(
    os.getenv("redis://red-d569ebur433s73e1iof0:6379"),
    decode_responses=True
)
