from modules.choose_lines_by_index import choose_lines_by_index
import os
class config:
    OUTPUT_PREFIX = "../chunks"
    current_file = os.path.abspath(__file__)
    ORIGINAL_FILE = current_file[-4]
    
choose_lines_by_index([0,1,2], config)

choose_lines_by_index([0,3,4], config)

choose_lines_by_index([0,5,6], config)

choose_lines_by_index([0,7,8], config)

choose_lines_by_index([0,9,10], config)

choose_lines_by_index([0,11,12], config)

choose_lines_by_index([0,13,14,15], config)
choose_lines_by_index([0,13,16,17], config)
choose_lines_by_index([0,13,18,19], config)

choose_lines_by_index([0,20,21], config)

