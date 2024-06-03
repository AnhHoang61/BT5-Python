# import pika
#
# def callback(ch, method, properties, body):
#     print(f" [x] Received {body}")
#
# # Kết nối tới RabbitMQ server
# connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672))
# channel = connection.channel()
#
# # Khai báo một exchange
# channel.exchange_declare(exchange='logs', exchange_type='fanout')
#
# # Khai báo một hàng đợi tạm thời
# result = channel.queue_declare(queue='', exclusive=True)
# queue_name = result.method.queue
#
# # Ràng buộc hàng đợi với exchange
# channel.queue_bind(exchange='logs', queue=queue_name)
#
# # Nhận thông điệp từ hàng đợi
# channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
#
# print(' [*] Waiting for messages. To exit press CTRL+C')
# channel.start_consuming()

import stomp


class Consumer(stomp.ConnectionListener):
    def __init__(self, host, port, topics):
        self.conn = stomp.Connection([(host, port)])
        self.conn.set_listener('', self)
        self.conn.connect(wait=True)
        for topic in topics:
            self.conn.subscribe(destination=f'/topic/{topic}', id=1, ack='auto')

    def on_message(self, frame):
        print(f"Received: {frame.body}")

    def disconnect(self):
        self.conn.disconnect()


if __name__ == "__main__":
    topics = ["topic1", "topic2"]
    consumer = Consumer('192.168.0.102', 61613, topics)
    print("Subscribed to topics:", topics)

    try:
        while True:
            pass  # Keep the script running to receive messages
    except KeyboardInterrupt:
        consumer.disconnect()
        print("Disconnected")
