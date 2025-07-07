#!/bin/bash

while getopts "e:f:" opt; do
    case $opt in
    e)      
    args=($OPTARG) 
    if [ ${#args[@]} -ne 2 ]; then
        echo "Error: Option -e requires exactly two numeric arguments in quotes. Example: -e \"2 3\""
        exit 1
    fi
      ./6-1.sh "${args[0]}" "${args[1]}"
    ;;
    f)
    
    if ! [[ $OPTARG =~ ^[0-9]+$ ]]; then
        echo "Error: Option -f requires a single numeric argument."
        exit 1
    fi
        ./6-2.sh "$OPTARG"
    ;;
    \?)
        echo "Error: Invalid option -$OPTARG"
        exit 1
    ;;
    :)
        echo "Error: Option -$OPTARG requires an argument."
        exit 1
    ;;
    esac
done
