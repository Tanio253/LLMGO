import os
def choose_lines_and_save(lines, li):
    content_block = ''.join(lines[l] for l in li)
    return content_block
    
def remove_endline(li):
    return li.strip()

def save_to_file(lines, id, config):
    output_filename = os.path.join(config.OUTPUT_PREFIX, f"title-{config.ORIGINAL_FILE}-{id}.txt")
    with open(output_filename, 'w', encoding='utf-8') as output_file:
        output_file.write(lines)
    
    
    