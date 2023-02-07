# ddns_bot

A simple Python script to call a Telegram Private Bot and send an IP address based on a Docker Cronjob.

It runs every X time (as configured in _crontab_ file - innitially for each 30min) and sends a Telegram message everytime IP changes as recorded inside `last_ip.txt` file.


# DockerHub:
https://hub.docker.com/r/abelroes/ddnsbot


## Requisites:

- [Docker & Docker-Compose](https://docs.docker.com/compose/install/)



## Running:

Create a `.env` file in project's root directory with yours specific variables.
See `.env.local` for reference.


```shell
docker build -t ddns_bot .
docker-compose up -d
```

## Stopping:

```shell
docker-compose down
```

## Logs:

```shell
docker ps
# see your container name than substitute
docker logs ddnsbot-ddnsbot-1
```

## References:

- [Telegram's Bot API](https://core.telegram.org/bots/api) documentation.
- Nils Schröder's [Medium article](https://nschdr.medium.com/running-scheduled-python-tasks-in-a-docker-container-bf9ea2e8a66c) for docker+cronjob.
