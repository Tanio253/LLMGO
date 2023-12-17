from modules.choose_lines_by_index import choose_lines_by_index
import os
class config:
    OUTPUT_PREFIX = "../chunks"
    current_file = os.path.abspath(__file__)
    ORIGINAL_FILE = current_file[-4]
    
choose_lines_by_index([0,1,2,3,4], config)
choose_lines_by_index([0,1,2,3,5], config)
choose_lines_by_index([0,1,2,3,6], config)
choose_lines_by_index([0,1,2,3,7], config)
choose_lines_by_index([0,1,2,3,8], config)
choose_lines_by_index([0,1,2,3,9], config)
choose_lines_by_index([0,1,2,3,10], config)

