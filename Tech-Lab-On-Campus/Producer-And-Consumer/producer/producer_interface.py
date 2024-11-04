import pika
import os
import sys
from solution.producer_sol import mqProducer  # pylint: disable=import-error


class mqProducerInterface:
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.connection = None
        self.channel = None
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange=self.exchange_name, exchange_type='direct')

    def publishOrder(self, message: str) -> None:
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body=message
        )
        self.channel.close()
        self.connection.close()


class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        super().__init__(routing_key, exchange_name)


def main() -> None:
    producer = mqProducer(routing_key="Tech Lab Key", exchange_name="Tech Lab Exchange")
    producer.publishOrder("Success! Producer And Consumer Section Complete.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
