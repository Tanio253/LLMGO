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
choose_lines_by_index([0,5,6], config)
#Mission
choose_lines_by_index([0,7,8,9], config)
choose_lines_by_index([0,7,9,10], config)
#Resource
choose_lines_by_index([0,11,12,13], config)
choose_lines_by_index([0,11,13,14], config)

choose_lines_by_index([0,15,16,17], config)

choose_lines_by_index([0,18,19,20], config)
choose_lines_by_index([0,18,21,22], config)
choose_lines_by_index([0,18,23,24], config)
choose_lines_by_index([0,18,25,26], config)


