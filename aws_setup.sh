#!/bin/sh

main () {
    echo "Updating OS...";
    update_os
    echo "Installing necessary packages"
    install_necessary_packages;
}

update_os () {
    sudo yum update;
}

install_necessary_packages() {
    sudo yum install git-all;
    sudo yum install libffi-devel;
    sudo yum install nginx;
    sudo yum install gcc;
    sudo yum install postgresql95-server.x86_64;
    sudo yum install postgresql95-devel.x86_64;
}

main