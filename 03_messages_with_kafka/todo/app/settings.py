
from starlette.config import Config
from starlette.datastructures import Secret

try:
    config = Config(".env")
except FileNotFoundError:
    config = Config()

DATABASE_URL = config("DATABASE_URL", cast=Secret)
BOOTSTRAP_SERVER = config("BOOTSTRAP_SERVER", cast=str)
KAKFKA_ORDER_TOPIC=config("KAFKA_ORDER_TOPIC",cast=str)
KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT=config("KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT", cast=str)

print(f"DATABASE_URL: {DATABASE_URL}")
print(f"BOOTSTRAP_SERVER: {BOOTSTRAP_SERVER}")
print(f"KAFKA_ORDER_TOPIC: {KAKFKA_ORDER_TOPIC}")
print(f"KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT: {KAFKA_CONSUMER_GROUP_ID_FOR_PRODUCT}")

