import json

# Load JSON data from the file
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file_path')
args = parser.parse_args()
with open(args.file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Iterate through each content in the JSON data
for item in data:
    title = item['title']
    
    # Iterate through each content block in the 'content' array
    block = []
    for idx, content_block in enumerate(item['content']):
        block.append(content_block)
        # Create a new text file with a filename based on the title and index
    filename = f"{title}.txt"
    
    # Write the content block to the text file
    with open(filename, 'w', encoding='utf-8') as text_file:
        text_file.write('\n\n'.join(block))
            
    print(f"Created file: {filename}")
