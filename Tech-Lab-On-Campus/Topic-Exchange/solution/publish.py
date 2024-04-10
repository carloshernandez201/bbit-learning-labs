import pika
import sys
import os

from producer_interface import mqProducerInterface

 

class mqProducer(mqProducerInterface):

    def __init__(self,  routing_key: str, exchange_name: str) -> None:

        self.routing_key = routing_key

        self.exchange_name = exchange_name

       

        self.channel = None

        self.connection = None

 

        self.setupRMQConnection()

 

    def setupRMQConnection(self) -> None:

        con_params = pika.URLParameters(os.environ["AMQP_URL"])

        self.connection = pika.BlockingConnection(parameters=con_params)

 

        self.channel = self.connection.channel()

 

        self.exchange = self.channel.exchange_declare(
            exchange=self.exchange_name,
            exchange_type='topic'  
        )
 

    def publishOrder(self, message: str) -> None:

        # Basic Publish to Exchange

        self.channel.basic_publish(

            exchange=self.exchange_name,

            routing_key=self.routing_key,

            body=message,

        )

 

        # Close Channel

        #self.channel.close()

 

        # Close Connection

        #self.connection.close()
if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: <script> TICKER PRICE SECTOR")
        sys.exit(1)
    ticker, price, sector = sys.argv[1], sys.argv[2], sys.argv[3]

    routing_key = f"{sector}.{ticker}"

    message = f"{ticker} is ${price}"

    exchange_name = "stocks"
    producer = mqProducer(routing_key=routing_key, exchange_name=exchange_name)
    producer.publishOrder(message=message)

    print(f"Published message: {message} with routing key: {routing_key}")