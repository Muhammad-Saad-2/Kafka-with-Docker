from aiokafka import AIOKafkaConsumer
import asyncio

async def consume_orders():
    consumer = AIOKafkaConsumer(
        'order_topic',
        bootstrap_servers='kafka:9092',
        group_id="order_group")
    await consumer.start()
    try:
        async for msg in consumer:
            order_id = int.from_bytes(msg.value, 'big')
            print(f"Consumed order with ID: {order_id}")
    finally:
        await consumer
