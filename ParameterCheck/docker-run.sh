#!/bin/bash

CONTAINER_NAME="strands-agent-parameter-check"

echo "=== Docker Build & Run Script ==="

# Check and remove existing container
if docker ps -a --format "table {{.Names}}" | grep -q "^${CONTAINER_NAME}$"; then
    echo "Removing existing container '${CONTAINER_NAME}'..."
    docker rm -f ${CONTAINER_NAME}
    echo "Container removed"
else
    echo "No existing container found"
fi

# Build image
echo "Building Docker image..."
docker build -t ${CONTAINER_NAME} .

if [ $? -eq 0 ]; then
    echo "Build completed"
    
    # Run container
    echo "Starting container..."
    # For Linux
    # docker run -d --name ${CONTAINER_NAME} --env-file ./.env -v $(pwd)/requested-template:/app/requested-template -v $(pwd)/output:/app/output ${CONTAINER_NAME}
    
    # For Docker Desktop for Windows
    win_path=$(pwd | sed -E 's|^/([a-z])|\U\1:|')
    echo $win_path
    # docker run -d --name ${CONTAINER_NAME} --env-file ./.env -v $win_path/requested-template:/app/requested-template -v $win_path/output:/app/output ${CONTAINER_NAME}
    docker run -itd --name ${CONTAINER_NAME} --env-file ./.env -v $win_path/requested-template:/app/requested-template -v $win_path/output:/app/output ${CONTAINER_NAME}

    if [ $? -eq 0 ]; then
        echo "Container '${CONTAINER_NAME}' started successfully"
        docker ps --filter "name=${CONTAINER_NAME}"
    else
        echo "Error: Failed to start container"
        exit 1
    fi
else
    echo "Error: Build failed"
    exit 1
fi