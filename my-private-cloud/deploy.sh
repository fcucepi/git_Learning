#!/bin/bash
echo "creating folders..."
mkdir -p /mnt/data/photos/uploads
mkdir -p /mnt/data/config

echo ""
echo ""
echo "rm old docker containers..."
docker compose down
docker container prune

echo ""
echo ""
echo "starting docker containers..."
docker compose up -d

echo ""
echo ""
echo "This is your docker status"
docker ps -a
