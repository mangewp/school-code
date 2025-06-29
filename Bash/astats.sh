#!/bin/bash

# Default log file path
LOGFILE="/home/ruizhao/CYBR3350/HW4/access_log"

# Help message
usage() {
  echo "Usage: $0 <request> [<file>]"
  echo
  echo "Reports selected information about Apache."
  echo "If no filename is given, we use /home/ruizhao/CYBR3350/HW4/access_log"
  echo
  echo "Request:"
  echo "  -h            Print this long message"
  echo "  IPs           Print a sorted list of all unique IP addresses that have accessed the server, and a total count at the end"
  echo "  Users         Print all unique user names whose web pages have been accessed, and a total count at the end"
}

# Check args
if [ $# -lt 1 ]; then
  usage
  exit 1
fi

REQUEST=$1
if [ $# -eq 2 ]; then
  LOGFILE=$2
fi

case $REQUEST in
  -h)
    usage
    exit 0
    ;;

  IPs|ips)
    if [ ! -f "$LOGFILE" ]; then
      echo "Error: Log file '$LOGFILE' not found."
      exit 1
    fi
    awk '{print $1}' "$LOGFILE" | sort -V | uniq | tee /tmp/astats_ips.$$ | wc -l | awk '{print "Total unique IPs:", $1}'
    rm -f /tmp/astats_ips.$$
    ;;

  Users|users)
    if [ ! -f "$LOGFILE" ]; then
      echo "Error: Log file '$LOGFILE' not found."
      exit 1
    fi
    awk '{print $7}' "$LOGFILE" \
      | grep '/~' \
      | sed -E 's|^/\~([^/]+)/.*|\1|' \
      | sort | uniq | tee /tmp/astats_users.$$ | wc -l | awk '{print "Total unique users:", $1}'
    rm -f /tmp/astats_users.$$
    ;;

  *)
    echo "Unknown request: $REQUEST"
    usage
    exit 1
    ;;
esac
