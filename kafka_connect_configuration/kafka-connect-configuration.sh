#!/bin/bash

sleep 15.0s

usr/bin/kafka-topics --create --topic "$KAFKA_TOPIC" --partitions 1 --replication-factor 1 --if-not-exists --zookeeper "$ZOOKEEPER_HOSTS"

usr/bin/connect-standalone /etc/kafka/connect-standalone-sftp.properties /etc/kafka/connect-sftp-csv.properties