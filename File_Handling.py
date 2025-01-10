# Script to read a text file, count words, and write results to a new file
def file_handling(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
            word_count = len(content.split())
        
        with open(output_file, 'w') as file:
            file.write(f"Word count: {word_count}\n")
        
        print(f"Word count written to {output_file}")
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")

# Provide the input and output file paths
file_handling('Python Tasks\input.txt', 'Python Tasks\output.txt')
