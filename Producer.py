import stomp


class Producer:
   def __init__(self, host, port):
       self.conn = stomp.Connection([(host, port)])
       self.conn.connect(wait=True)


   def send_message(self, topic, message):
       self.conn.send(destination=f'/topic/{topic}', body=message)


   def disconnect(self):
       self.conn.disconnect()


if __name__ == "__main__":
   producer = Producer('192.168.0.102', 61613)
   topic = "topic1"
   message = "Tôi tên là"


   producer.send_message(topic, message)
   print(f"Sent: {message}")


   producer.disconnect()