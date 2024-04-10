import pika
import sys
import os

from consumer_interface import mqConsumerInterface

class mqConsumer(mqConsumerInterface):

 

    def __init__(

        self, binding_key: str, exchange_name: str, queue_name: str

    ) -> None:

        self.channel = None

        self.connection = None

        self.queue_name = queue_name

        self.binding_key = binding_key

        self.exchange_name = exchange_name

        self.setupRMQConnection()

 

    def setupRMQConnection(self) -> None:

        con_params = pika.URLParameters(os.environ["AMQP_URL"])

        self.connection = pika.BlockingConnection(parameters=con_params)

        self.channel = self.connection.channel()

        self.channel.queue_declare(queue=self.queue_name)

        self.exchange = self.channel.exchange_declare(exchange=self.exchange_name, exchange_type="topic")


        self.channel.queue_bind(

        queue= self.queue_name,

        routing_key= self.binding_key,

        exchange= self.exchange_name,

        )

        self.channel.basic_consume(

        self.queue_name, self.on_message_callback, auto_ack=False

        )

 

    def on_message_callback(

        self, channel, method_frame, header_frame, body

        ):

        print("Message is: " + body.decode() + "!")

        self.connection.close()

    def startConsuming(self):

        print(" [*] Waiting for messages. To exit press CTRL+C")

        self.channel.start_consuming()

    def __del__(self):
        try:
            if self.channel is not None:
                print("Closing RMQ channel on destruction")
                self.channel.close()
        except Exception as e:
            a = 2 # dont close it, inconsequential statement

        try:
            if self.connection is not None:
                self.connection.close()
        except Exception as e:
            a = 2 # dont close it, 

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: <script> SECTOR QUEUENAME")
        sys.exit(1)

    sector, queue_name = sys.argv[1], sys.argv[2]

   
    binding_key = f"#.{sector}.#"

    exchange_name = "stocks"  
    consumer = mqConsumer(binding_key=binding_key, exchange_name=exchange_name, queue_name=queue_name)
    consumer.startConsuming()
