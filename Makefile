# Variables
IMAGE_NAME = muhammadshoukat/house-prediction
TAG = latest

# Commands
build:
    docker build -t $(IMAGE_NAME):$(TAG) .

push:
    docker push $(IMAGE_NAME):$(TAG)

all: build push
