from modules.choose_lines_by_index import choose_lines_by_index
import os
class config:
    OUTPUT_PREFIX = "../chunks"
    current_file = os.path.abspath(__file__)
    ORIGINAL_FILE = current_file[-5] + current_file[-4]
#Addr    
choose_lines_by_index([0,1,2], config)
#Contact
choose_lines_by_index([0,3,4], config)
#About
choose_lines_by_index([0,5,6,7], config)
choose_lines_by_index([0,5,8,9], config)
choose_lines_by_index([0,5,10,11], config)
choose_lines_by_index([0,5,11,12], config)


