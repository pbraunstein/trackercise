#!/bin/bash

main () {
    echo "S T A R T I N G  N G I N X . . ."
    sudo /etc/init.d/nginx start
    echo "S T A R T I N G  G U N I C O R N . . ."
    nohup gunicorn manage:app &
}

main
