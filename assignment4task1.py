def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("File content:\n")
            for line in file:
                print(line, end='')  # end='' prevents double newlines
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
# Call the function with the desired file name
read_file("sample.txt")
