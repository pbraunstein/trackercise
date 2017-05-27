#!/bin/bash

main() {
    echo "P U L L I N G  R E C E N T  C H A N G E S . . ."
    git pull

    echo "U P G R A D I N G  N O D E  P A C K A G E S . . ."
    upgrade_node_pacakages

    echo "B U I L D I N G  A N D  B U N D L I N G . . ."
    build_and_bundle

    echo "S E T T I N G  U P  N G I N X . . ."
    setup_nginx
}

upgrade_node_packages() {
    cd ./app/static && npm install
}

build_and_bundle() {
    npm run buildProduction
}

setup_nginx() {
    cd ../../
    sudo cp nginx.conf /etc/nginx/nginx.conf
}

main
