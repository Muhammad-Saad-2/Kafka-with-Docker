from aiokafka import AIOKafkaProducer
import asyncio

async def send_order(order_id: int):
    producer = AIOKafkaProducer(bootstrap_servers='kafka:9092')
    await producer.start()
    try:
        await producer.send_and_wait("order_topic", order_id.to_bytes(4, 'big'))
    finally:
        await producer.stop()

if __name__ == "__main__":
    asyncio.run(send_order(1))
