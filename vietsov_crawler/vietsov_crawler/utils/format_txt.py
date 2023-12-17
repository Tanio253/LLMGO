import os
import json
PREFIX_FP = './json_files/'
file_paths = ["CSVC", "DADT", "DVTT", "GT", "NNL", "SPDV", "TDTS", "TT"]
def format_txt():
    for file_name in file_paths:
        input_path = os.path.join(PREFIX_FP, file_name, f"{file_name}.json")
        base_directory = os.getcwd()
        dir_name = file_name + "_txt"
        new_directory = os.path.join(base_directory, "txt_files", dir_name, "core")
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
        with open(input_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        id = 0
        for item in data:
            title = item['title']
            content = '\n'.join([content_block for content_block in item['content']])
            filename = os.path.join(new_directory, f"title-{id}.txt")
            with open(filename, 'w', encoding='utf-8') as text_file:
                text_file.write(title + "\n" + content)
            print(f"Created file: {filename}")
            id+=1
if __name__ == "__main__":
    format_txt()