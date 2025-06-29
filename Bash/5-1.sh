# Compare two files and report if they are the same or different

diff "$1" "$2" > /dev/null

if [ $? -eq 0 ]; then
    echo "They are the same"
else
    echo "They are different"
fi