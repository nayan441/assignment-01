
def main(source_file):
    """This function will print count of upper case character in source file."""
    try:
        with open(source_file, 'r') as source:
            content = source.read()
        uppercase_count = sum(1 for char in content if char.isupper())
        print(uppercase_count)  
        
    except FileNotFoundError:
        print(f"Error: The file {source_file} does not exist.")
    except IOError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    source = '3.1-sample.txt'
    
    main(source)