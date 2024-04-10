# Comprehensive Messaging Queue System Project

This project, developed with the support of Bloomberg Finance L.P. and their learning lab program, showcases a comprehensive messaging queue system designed to facilitate seamless communication between different components of a larger application ecosystem. It leverages RabbitMQ to implement a robust producer-consumer model, ensuring efficient data processing and distribution.

## Project Components

- **MQ Producer Interface:** Responsible for publishing messages to specified exchanges with unique routing keys, allowing targeted message delivery to consumer services.

- **MQ Consumer Interface:** Subscribes to specific queues bound to exchange channels. It filters incoming messages based on binding keys, ensuring relevant message consumption. This interface also includes functionality for message acknowledgment and processing.

## Installation and Setup

To get started with this project, clone the repository to your local machine or development environment. Ensure that you have RabbitMQ installed and running, as it is crucial for the operation of the message queuing system.

### Dependencies

- RabbitMQ: Follow the official RabbitMQ documentation for installation instructions.
- Python 3.x: This project is developed using Python 3. Ensure you have it installed on your system.

## Running the Project
0.  This section will guide you to using the topic exchange to subscribe to whichever industry stocks you are interested in, by having the consumer only listen to queues within that specific industry. 

1. **Start the Consumer Services:**
   - Open two terminal windows.
   - In the first terminal, run the consumer service subscribing to whichever industry stocks you want

2. **Publish Messages:**
   - Open a third terminal window.
   - Utilize the provided `publish.py` script to send messages. First, publish a message categorized under tech stocks, followed by a healthcare message, and finally a message belonging to a different sector.

3. **Verify Message Routing:**
   - Ensure that messages are correctly routed to their respective consumer services based on the topic of interest. The first and second messages should reach the appropriate queues, while the third message should not be delivered to any queue.

## Common Issues and Troubleshooting

- Ensure each queue has a unique name to avoid binding multiple keys to a single queue accidentally. This can be achieved by passing an extra argument for the queue name in your implementation.

- Verify that RabbitMQ is running and accessible. Connection issues can often be resolved by reviewing RabbitMQ's configuration and ensuring that your project's connection settings are correctly aligned.

## License

This project is licensed under the Apache License, Version 2.0. See the LICENSE file for more details.

## Acknowledgments

Special thanks to Bloomberg Finance L.P. for their support and contributions to this project. Their expertise and resources have been invaluable in achieving our goals.

## Contact

For more information, contributions, or inquiries, please visit our tech lab on campus or reach out to the project coordinators directly. We welcome collaboration from all interested parties.

© 2024 Bloomberg Finance L.P.
