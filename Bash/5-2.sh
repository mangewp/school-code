# Check if exactly two arguments are provided

if [ $# -ne 2 ]; then
    echo "Error: Exactly two file names must be provided."
    exit 1
fi

# Check if both files exist
if [ ! -f "$1" ]; then
    echo "Error: File '$1' does not exist."
    exit 1
fi

if [ ! -f "$2" ]; then
    echo "Error: File '$2' does not exist."
    exit 1
fi

# Compare the files
diff "$1" "$2" > /dev/null

if [ $? -eq 0 ]; then
    echo "They are the same"
else
    echo "They are different"
fi