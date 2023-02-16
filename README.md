# vigilant-octo-etcd

This project is used to test etcd which is a distributed, reliable key-value store for the most critical data of a distributed system.

# Running

You can start etcd / prometheus / grafana with:

```shell
docker-compose up -d
```

You can run a python etcd_client with:

```shell
python -m venv venv
. venv/bin/activate
python ./etcd_client.py
```

# GUI

Grafana is available on `localhost:3000`. Login and password are `admin`. You can use the dashboard `etcd-clusters-as-service`

# Shutdown

You can shutdown all servers by doing: `docker-compose down`