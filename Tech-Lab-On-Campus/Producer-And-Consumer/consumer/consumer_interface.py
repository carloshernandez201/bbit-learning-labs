import pika

class mqConsumerInterface:
    def __init__(self, binding_key: str, exchange_name: str, queue_name: str) -> None:
        self.binding_key = binding_key
        self.exchange_name = exchange_name
        self.queue_name = queue_name
        self.connection = None
        self.channel = None
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')
        self.channel.queue_declare(queue=self.queue_name)
        self.channel.queue_bind(exchange=self.exchange_name, queue=self.queue_name, routing_key=self.binding_key)
        self.channel.basic_consume(queue=self.queue_name, on_message_callback=self.on_message_callback, auto_ack=False)

    def on_message_callback(self, channel, method_frame, header_frame, body) -> None:
        print(f"Received message: {body.decode()}")
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)

    def startConsuming(self) -> None:
        print(" [*] Waiting for messages. To exit press CTRL+C")
        self.channel.start_consuming()
    
    def __del__(self) -> None:
        print("Closing RMQ connection on destruction")
        if self.channel:
            self.channel.close()
        if self.connection:
            self.connection.close()
