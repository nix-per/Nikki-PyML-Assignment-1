try:
    with open("String.txt", "r") as f:                         # Attempt to open the file in read mode
        a = f.read()
    print("The contents of the file 'String.txt' are:")
    print(a)
  
except FileNotFoundError:                                      # If the file is not present
    print("Error: The file 'String.txt' does not exist.")
  
except IOError as e:
    print(f"Error: An I/O error occurred while accessing the file. {e}")
