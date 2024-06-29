      
def main(source_file, destination_file):
    """This function copies the content from the source file to the destination file."""
    try:
        with open(source_file, 'r') as source:
            content = source.read()
        
        with open(destination_file, 'w') as destination:
            destination.write(content)
        
        print(f"Content copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"Error: The file {source_file} does not exist.")
    except IOError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    source = '3.1-sample.txt'
    destination = '3.1-destination.txt'
    
    main(source, destination)
