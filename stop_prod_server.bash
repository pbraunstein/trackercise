#!/bin/bash

main () {
    echo "S T O P P I N G  G U N I C O R N . . ."
    kill $(ps aux | grep '[g]unicorn' | awk '{print $2}')
    echo "S T O P P I N G  N G I N X . . ."
    kill $(ps aux | grep '[n]ginx' | awk '{print $2}')
}

main