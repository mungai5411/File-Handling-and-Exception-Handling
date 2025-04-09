def modify_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        modified_content = content.upper()
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"File '{input_filename}' successfully modified and saved as '{output_filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{input_filename}' does not exist.")
    except IOError:
        print(f"Error: Could not read/write to '{input_filename}' or '{output_filename}'.")
