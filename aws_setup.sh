#!/bin/sh

main () {
    echo "I N S T A L L I N G  N E C E S S A R Y  P A C K A G E S . . ."
    install_necessary_packages
    echo "I N S T A L L I N G  N V M . . ."
    install_nvm
    echo "I N S T A L L I N G  N O D E . . ."
    install_node
    echo "C R E A T I N G  V I R T U A L E N V . . . "
    create_virtualenv
    echo "I N S T A L L I N G  P Y T H O N  R E Q U I R E M E N T S . . ."
    install_python_requirements
}

install_necessary_packages() {
    sudo yum install libffi-devel
    sudo yum install nginx
    sudo yum install gcc
    sudo yum install postgresql95-server.x86_64
    sudo yum install postgresql95-devel.x86_64
}

install_nvm() {
    curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.33.1/install.sh | bash
}

install_node() {
    source ~/.bashrc
    nvm install 6.9.5
}

create_virtualenv() {
    virtualenv venv
}

install_python_requirements() {
    source ./venv/bin/activate
}

main