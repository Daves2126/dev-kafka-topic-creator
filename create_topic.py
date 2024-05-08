import sys
import os
from confluent_kafka.admin import AdminClient, NewTopic
def create_topics_from_file(file_path, bootstrap_servers):
    print(f"Creating topics from file: {file_path}")
    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers, 'client.id': 'admin-client', 'security.protocol': 'PLAINTEXT'})
    cluster_metadata = admin_client.list_topics(timeout=10)
    if cluster_metadata.topics is None:
        print("No topics found in Kafka cluster. Waiting for Kafka to be available...")
        cluster_metadata = admin_client.list_topics(timeout=10)
        if cluster_metadata.topics is None:
            print("Kafka cluster is not available. Exiting...")
            sys.exit(1)
    new_topics = []
    with open(file_path, 'r') as file:
        for line in file:
            topic_info = line.strip().split(':')
            if len(topic_info) != 3:
                print(f"Invalid format in line: {line.strip()}. Expected format: <topicName>:<partitions>:<replicationFactor>")
                continue
            topic_name, partitions, replication_factor = topic_info
            if not partitions.isdigit() or not replication_factor.isdigit():
                print(f"Invalid partitions or replication factor in line: {line.strip()}. Partitions and replication factor must be integers.")
                continue
            if topic_name not in cluster_metadata.topics:
                print(f"Creating topic: {topic_name} with {partitions} partitions and replication factor: {replication_factor}")
                new_topics.append(NewTopic(topic=topic_name, num_partitions=int(partitions), replication_factor=int(replication_factor)))
            else:
                print(f"Topic: {topic_name} already exists in Kafka cluster. Skipping...")
    if new_topics:
        print(f"Creating a total of {len(new_topics)} topics in Kafka cluster...")
        res = admin_client.create_topics(new_topics)
        for topic, f in res.items():
            f.result()
if __name__ == "__main__":
    file_path = os.environ.get("FILE_PATH")
    bootstrap_servers = os.environ.get("BOOTSTRAP_SERVERS")
    if file_path is None or bootstrap_servers is None:
        print("Please provide FILE_PATH and BOOTSTRAP_SERVERS environment variables.")
        sys.exit(1)
    create_topics_from_file(file_path, bootstrap_servers)