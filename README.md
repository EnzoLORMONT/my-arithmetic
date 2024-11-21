# My Arithmetic Project

[![Coverage Status](https://coveralls.io/repos/github/EnzoLORMONT/my-arithmetic/badge.svg?branch=main)](https://coveralls.io/github/EnzoLORMONT/my-arithmetic?branch=main)

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

# my-arithmetic-enzo

[![PyPI - Version](https://img.shields.io/pypi/v/my-arithmetic-enzo.svg)](https://pypi.org/project/my-arithmetic-enzo)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/my-arithmetic-enzo.svg)](https://pypi.org/project/my-arithmetic-enzo)

-----

## Table of Contents

- [Installation](#installation)
- [License](#license)

## Installation

```console
pip install my-arithmetic-enzo
```

## License

`my-arithmetic-enzo` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.

