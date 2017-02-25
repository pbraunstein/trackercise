#!/bin/sh

main () {
    echo "I N S T A L L I N G  N E C E S S A R Y  P A C K A G E S . . ."
    install_necessary_packages
}

install_necessary_packages() {
    sudo yum install libffi-devel
    sudo yum install nginx
    sudo yum install gcc
    sudo yum install postgresql95-server.x86_64
    sudo yum install postgresql95-devel.x86_64
}

main