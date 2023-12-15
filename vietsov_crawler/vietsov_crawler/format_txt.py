import os
import json
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('--file_path', required=True, help='Directory name to store text files')
args = parser.parse_args()

# Get the current working directory
base_directory = os.getcwd()

# Create a new directory in the base directory
dir_name = args.file_path[:-5] + "_parse_txt"
new_directory = os.path.join(base_directory, dir_name)

# Check if the directory already exists; if not, create it
if not os.path.exists(new_directory):
    os.makedirs(new_directory)

# Load JSON data from the file  # Change this to your actual JSON file name
with open(args.file_path, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
id = -1
# Iterate through each content in the JSON data
for item in data:
    title = item['title']
    id+=1
    for idx, content_block in enumerate(item['content']):
        # if len(title)>20: title = title[:20]
        # if '/' in title: title = title.replace('/', ' ')
        filename = os.path.join(new_directory, f"{id}-{idx}.txt")
        with open(filename, 'w', encoding='utf-8') as text_file:
            text_file.write(title + "\n" + content_block)
        print(f"Created file: {filename}")
    
    # Write the content block to the text file
            
