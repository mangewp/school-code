#!/bin/bash

while true; do
  echo
  read -p "Choose an option (e for exponent, f for factorial, q to quit): " choice

  case $choice in
    e)
      read -p "Enter two numbers (base and exponent), separated by space: " base exponent
      if [[ ! $base =~ ^[0-9]+$ || ! $exponent =~ ^[0-9]+$ ]]; then
        echo "Error: Both inputs must be numeric."
        continue
      fi
      ./6-1.sh "$base" "$exponent"
      ;;
    f)
      read -p "Enter one number to compute factorial: " num
      if [[ ! $num =~ ^[0-9]+$ ]]; then
        echo "Error: Input must be a numeric value."
        continue
      fi
      ./6-2.sh "$num"
      ;;
    q)
      echo "Goodbye"
      break
      ;;
    *)
      echo "Error: Invalid option. Choose e, f, or q."
      ;;
  esac
done
