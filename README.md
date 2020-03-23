# survetric
Testing peer to peer programming using python and pygame.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* To run will need to have **python3** (or equivalent) on your machine.
* _bottle_;
* _pygame_;

```
$ pip3 install bottle
$ pip3 install pygame
```

### Running

You will need to set manually the ip address and port that yhe peer will run:

```
my_ip = "0.0.0.0" # localhost
my_port = "8081"
```

To run the application type in terminal _(on source folder)_:

```
$ python3 pygame.py
```

Run a new peer in other terminal and port:

```
my_port = "8082"
```


To connect the peers type on terminal the _ip:port_ that you want to connect:

```
$ 0.0.0.0:8081
```

## Authors

* **Vitor G. Forbrig** - [Forbrig](https://github.com/Forbrig)
