#!/bin/bash

script1() {
    echo "Running Script 1"
    docker image build -t chi_vio .
    # docker run --env-file .env -dp5000:5000 --name chi_vio_container chi_vio
    docker run -dp5000:5000 --name chi_vio_container chi_vio
}

script2() {
    echo "Running Script 2"
    docker-compose -f docker-compose.yaml up -d --build
}

script3() {
    echo "Running Script 3"
    waitress-serve --port=5000 run:app
}

script4() {
    echo "Running Script 4"
}

echo "Please Select:"
options=("Script 1" "Script 2" "Script 3" "Script 4" "Quit")


select opt in "${options[@]}"; do
    case $REPLY in
        1)
            script1
            break
            ;;
        2)
            script2
            break
            ;;
        3)
            script3
            break
            ;;

        4)
            script4
            break
            ;;
        5)
            echo "Quit"
            break
            ;;
        *)
            echo "無效"
            ;;
    esac
done

echo "Finished"
