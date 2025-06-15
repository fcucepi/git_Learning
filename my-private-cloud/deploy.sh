#!/bin/bash
echo "creating folders..."
mkdir -p /mnt/data/photos/uploads
mkdir -p /mnt/data/config

echo "starting docker containers..."
docker compose up -d

echo "deployment completed"
echo "- Immich is available at: http://localhost:2299"
echo "- FileBrowser is available at: http://localhost:8080"
