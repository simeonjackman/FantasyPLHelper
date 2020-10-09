name=fantasy_docker
image=fantasy_pl_helper:latest

## build docker
build:
	docker build --tag ${image} .

## really build docker
sudo-build:
	sudo docker build --tag ${image} .

## clean
clean: prune
	rm -f -r __pycache__

## remove all dangling iamges
prune:
	docker system prune

## run docker image
run:
	docker run --rm -it -d -p 5000:5000 \
		--name ${name} ${image}

## stop docker image
stop:
	docker stop ${name}
