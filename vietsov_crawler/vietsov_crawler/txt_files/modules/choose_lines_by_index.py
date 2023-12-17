from modules.helpers import (
    choose_lines_and_save, 
    save_to_file
)
import os

def choose_lines_by_index(li, config, id = None):
    input_filename = f"../core/title-{config.ORIGINAL_FILE}.txt"
    if not os.path.exists(config.OUTPUT_PREFIX):
        os.makedirs(config.OUTPUT_PREFIX)
    
    if id is None:
        existing_files = os.listdir(config.OUTPUT_PREFIX)
        
        txt_file_name = [filename for filename in existing_files if filename.endswith('.txt')]
        if txt_file_name:
            if any(f"title-{config.ORIGINAL_FILE}-" in t for t in txt_file_name):
                existing_ids = [int(t.split(f"title-{config.ORIGINAL_FILE}-")[1].replace(".txt", '')) for t in txt_file_name if f"title-{config.ORIGINAL_FILE}-" in t]
                id = max(existing_ids, default=-1) + 1
            else:
                id = 0
        else: 
            id = 0
    
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    content_block = choose_lines_and_save(lines, li)
    save_to_file(content_block, id , config)
    
    