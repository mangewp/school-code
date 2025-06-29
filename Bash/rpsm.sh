#!/bin/bash

version="1.0"

usage() {
    echo "Usage: ./rpsm.sh <options> <directory>"
    echo "Reports selected information about specified directory tree."
    echo "Options:"
    echo "-h Print this help message, i.e., \"Usage: ./rpsm.sh … … (except -h and -v)\""
    echo "-v Print script version information, i.e., $version"
    echo "-u Find and list all files (just file names) with setuid set, all owners"
    echo "-g Find and list all files (just file names) with setgid set, all owners"
    echo "-w Find and list all files (just file names) that are world-writable"
    echo "-b Find and list all files (just file names) whose size is at least 10M"
    echo "-d Report directory disk usage"
    echo "-i Report information about the file system"
    echo "-a All of the above (except -h and -v)"
    exit 1
}

if [[ $# -eq 0 ]]; then
    usage
fi

while getopts ":hvugwbida" opt; do
    case $opt in
        h) usage ;;
        v) echo "$version"; exit 0 ;;
        u) uflag=1 ;;
        g) gflag=1 ;;
        w) wflag=1 ;;
        b) bflag=1 ;;
        d) dflag=1 ;;
        i) iflag=1 ;;
        a) aflag=1 ;;
        \?) echo "Invalid option: -$OPTARG" >&2; usage ;;
    esac
done

shift $((OPTIND-1))

# After options, $1 should be the directory
directory="$1"
if [[ -z "$directory" ]] && [[ -z "$aflag" ]] && [[ -z "$dflag" ]] && [[ -z "$iflag" ]]; then
    usage
fi

if [[ -n "$aflag" ]]; then
    uflag=1; gflag=1; wflag=1; bflag=1; dflag=1; iflag=1
fi

# Print filesystem info
if [[ -n "$iflag" ]]; then
    df -T "$directory" 2>/dev/null | awk 'NR==1{print $1, $2, $6, $7}; NR>1{print $1, $2, $6, $7}'
fi

# Print disk usage
if [[ -n "$dflag" ]]; then
    du -sh "$directory"/* 2>/dev/null | sort -n
fi

# Setuid files
if [[ -n "$uflag" ]]; then
    echo "Setuid files:"
    find "$directory" -type f -perm -4000 -ls 2>/dev/null | awk '{print $5, $11}'
fi

# Setgid files
if [[ -n "$gflag" ]]; then
    echo "Setgid files:"
    find "$directory" -type f -perm -2000 -ls 2>/dev/null | awk '{print $5, $11}'
fi

# World-writable files
if [[ -n "$wflag" ]]; then
    echo "World-writable files:"
    find "$directory" -type f -perm -0002 -ls 2>/dev/null | awk '{print $5, $11}'
fi

# Big files
if [[ -n "$bflag" ]]; then
    echo "Files >=10M:"
    find "$directory" -type f -size +10M -ls 2>/dev/null | awk '{print $11}'
fi

exit 0
