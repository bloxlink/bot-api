from os import environ as env

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8002
AUTH = env.get("BOT_API_AUTH", "")
DEBUG_MODE = env.get("PROD") != "TRUE"

REDIS_HOST = env.get("REDIS_HOST")
REDIS_PORT = 6379
REDIS_PASSWORD = env.get("REDIS_PASSWORD", "")
MONGO_URL = env.get("MONGO_URL", "")