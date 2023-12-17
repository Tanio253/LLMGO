from modules.choose_lines_by_index import choose_lines_by_index
import os
import os

class Config:
    OUTPUT_PREFIX = "../chunks"
    
    def __init__(self, ORIGINAL_FILE):
        self.ORIGINAL_FILE = ORIGINAL_FILE


config_instance = Config(ORIGINAL_FILE=0)


for i in range(1604):
    config_instance.ORIGINAL_FILE = i
    input_filename = f"../core/title-{config_instance.ORIGINAL_FILE}.txt"
    with open(input_filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    for j in range(2,len(lines)-2, 3):
        choose_lines_by_index([0,1,j,j+1,j+2], config_instance)


