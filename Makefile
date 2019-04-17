STACK_NAME		:= $(shell basename "$$(pwd)")
DOMAINNAME		:= testnet.dapla.net
VIRTUAL_HOST		:= $(STACK_NAME).$(DOMAINNAME)
IMAGE_NAME		:= dmsapi
NETWORK_NAME		:= public

export VIRTUAL_HOST
export DOMAINNAME
export STACK_NAME
export IMAGE_NAME
export NETWORK_NAME

.SILENT:
.DEFAULT: all
.PHONY: all clean deploy test $(VIRTUAL_HOST)

all: clean deploy

clean:
	@docker stack rm $(STACK_NAME)

distclean: clean
	@docker volume ls | awk '/$(STACK_NAME)/ { system("docker volume rm "$$2) }'
	@docker image rm $(IMAGE_NAME)

deploy: image networks volumes config secrets
	@docker stack deploy -c docker-stack.yml $(STACK_NAME)

image:
	@docker image build -t $(IMAGE_NAME) .

test: $(VIRTUAL_HOST)

networks:
	@-docker network create -d overlay --scope swarm $(NETWORK_NAME)

config: ;
secrets: ;
volumes: ;

$(VIRTUAL_HOST):
	@curl -sSLk $@
