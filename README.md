# My Arithmetic Project

![Pipeline](https://gitlab.univ-lr.fr/elormont/my-arithmetic-enzo/badges/main/pipeline.svg)

![Coverage](https://gitlab.univ-lr.fr/elormont/my-arithmetic-enzo/badges/main/coverage.svg)

# Deployer un Runner Gitlab sur docker

Faire un dossier config qui appartient à root.

Et voici la configuration à mettre :

```toml
concurrent = 1
check_interval = 0
shutdown_timeout = 0

[session_server]
  listen_address = "0.0.0.0:8093"
  advertise_address = "127.0.0.1:8093"
  session_timeout = 1800

[[runners]]
  name = "my-runner"
  url = "https://gitlab.univ-lr.fr/"
  token = "YOUR_TOKEN"
  executor = "docker"
  [runners.docker]
    tls_verify = false
    image = "alpine:latest"
    privileged = true
    disable_cache = false
    volumes = ["/var/run/docker.sock:/var/run/docker.sock", "/cache"]
    shm_size = 0
  [runners.cache]
```

`docker run -d --name gitlab-runner --restart always -v ./config:/etc/gitlab-runner -v /var/run/docker.sock:/var/run/docker.sock gitlab/gitlab-runner:latest`