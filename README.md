# survetric
Testing peer to peer programming using python and pygame.

![survetric](https://raw.githubusercontent.com/Forbrig/survetric/master/survetric.png)

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

You will need to set manually the ip address and port that you peer will run:

```
my_ip = "0.0.0.0" # localhost
my_port = "8081"
```

To run the application type in terminal _(on source folder)_:

```
$ python3 pygame.py
```

Run a new peer in other terminal and port (also change the color if you want):

```
player_ = player("red")
my_port = "8082"
```

To connect the second peer to the first type on terminal the _ip:port_:

```
$ 0.0.0.0:8081
```

Connect the first to the seccond:

```
$ 0.0.0.0:8082
```

The next peer that connect will know in the net will know the peers list from the the one he connect and then connect to the list:

```
player_ = player("green")
my_port = "8083"
```

```
$ 0.0.0.0:8081
```

Check out the bully election to know who is electd to be the main peer. When he desconnect the peers will vote to know who will be the next bully.

## Authors

* **Vitor G. Forbrig** - [Forbrig](https://github.com/Forbrig)
