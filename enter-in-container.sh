#!/bin/bash

# This script is used to enter in a container. Options: aws_labs_sqlserver, aws_labs_kafka, aws_labs_zookeeper, aws_labs_api, aws_labs_producer

if [ "$1" = "aws_labs_sqlserver" ]; then
    docker exec -it aws_labs_sqlserver bash
elif [ "$1" = "aws_labs_kafka" ]; then
    docker exec -it aws_labs_kafka bash
elif [ "$1" = "aws_labs_zookeeper" ]; then
    docker exec -it aws_labs_zookeeper bash
elif [ "$1" = "aws_labs_api" ]; then
    docker exec -it aws_labs_api bash
elif [ "$1" = "aws_labs_producer" ]; then
    docker exec -it aws_labs_producer bash
else
    echo "Invalid container name"
    echo "Options: aws_labs_sqlserver, aws_labs_kafka, aws_labs_zookeeper, aws_labs_api, aws_labs_producer"
fi