from modules.choose_lines_by_index import choose_lines_by_index
import os
class config:
    OUTPUT_PREFIX = "../chunks"
    current_file = os.path.abspath(__file__)
    ORIGINAL_FILE = current_file[-4]
    
for i in range(2, 15, 2):
    choose_lines_by_index([0,1,i,i+1], config)
choose_lines_by_index([0,1,15,16], config)

