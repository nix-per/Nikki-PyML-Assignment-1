# Q25. Write a program that copies the contents of one text file to another

try:
    source_file = "source.txt"
    destination_file = "destination.txt"

    with open(source_file, 'r') as f_source:
        content = f_source.read()
    
    with open(destination_file, 'w') as f_dest:
        f_dest.write(content)
    
    print(f"Contents from '{source_file}' copied to '{destination_file}' successfully.")

except FileNotFoundError:
    print("Error: One of the files does not exist. Please check the file paths.")
except IOError as e:
    print(f"IOError occurred: {e}")
except Exception as e:
    print(f"Unexpected error occurred: {e}")
