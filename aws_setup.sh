#!/bin/sh

main () {
    echo "U P D A T I N G  O S . . ."
    update_os
    echo "I N S T A L L I N G  N E C E S S A R Y  P A C K A G E S . . ."
    install_necessary_packages
    echo "I N S T A L L I N G  T R A C K E R C I Z E . . ."
    install_trackercise
}

update_os () {
    sudo yum update;
}

install_necessary_packages() {
    sudo yum install git-all
    sudo yum install libffi-devel
    sudo yum install nginx
    sudo yum install gcc
    sudo yum install postgresql95-server.x86_64
    sudo yum install postgresql95-devel.x86_64
}

install_trackercise() {
    git clone https://github.com/pbraunstein/trackercise.git
}

main