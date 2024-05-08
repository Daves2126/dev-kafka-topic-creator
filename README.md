# Kafka Topic Creator

This repository is created to automate the topic creation process on Kafka for development environments, making it easier and more efficient.

## How to Use

To use this tool, follow these steps:

1. Ensure you have Docker installed on your system.
2. Create a topics.txt file
3. Add your desired topics to the topics.txt file following the structure: `<topicName>:<partitions>:<replicationFactor>`
4. Run the provided Docker Compose example.

### Docker Compose Example

```yaml
kafka_init:
  image: egonzalezt/dev-kafka-topic-creator:latest
  volumes:
    - ./topics.txt:/scripts/topics.txt:ro
  environment:
    - FILE_PATH=/scripts/topics.txt
    - BOOTSTRAP_SERVERS=kafka:9092
  depends_on:
    - kafka
  networks:
    - kafka
```

### Notes

* Make sure to replace `./topics.txt` with the actual path to your topics.txt file.
* Adjust the `BOOTSTRAP_SERVERS` environment variable if your Kafka broker is not running on `kafka:9092`.
* Adjust the `FILE_PATH` if you change the location of the file on the volume bind

## topics.txt Structure

The topics.txt file should have the following structure:

```txt
<topicName>:<partitions>:<replicationFactor>
<topicName>:<partitions>:<replicationFactor>
<topicName>:<partitions>:<replicationFactor>
...
```

Replace `<topicName>`, `<partitions>`, and `<replicationFactor>` with your desired values for each topic.

This tool will read this file and automatically create topics with the specified configurations on your Kafka broker.

Feel free to contribute to this repository or report any issues you encounter!

## License
CoplandFileManager is licensed under the [Apache 2.0 license](./LICENSE).
