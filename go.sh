#!/bin/sh
CLEAN="clean"
HELP="help"

if [ $1 = $HELP ]; then
    echo "OPTIONS:"
    echo ""
    echo "To run the application:     Simply type the following command:"
    echo "                            >> ./go.sh "
    echo "To delete previously  "
    echo "generated results     :     Please type the following command:"
    echo "                            >> ./go.sh clean"
fi

if [ $1 = $CLEAN ]; then
    echo "Deleting Result.txt"
    rm -r ./output/Result.txt
elif [ -z $1 ]; then
    sudo apt-get install python3.4
    python3.4 ./src/Record_Linkage.py
fi
