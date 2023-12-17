from modules.choose_lines_by_index import choose_lines_by_index
import os
class config:
    OUTPUT_PREFIX = "../chunks"
    current_file = os.path.abspath(__file__)
    ORIGINAL_FILE = current_file[-4]
#Addr    
choose_lines_by_index([0,1,2], config)
#Contact
choose_lines_by_index([0,3,4], config)
#About
choose_lines_by_index([0,5,6], config)
#Mission
choose_lines_by_index([0,7,8], config)
#Resource
choose_lines_by_index([0,9,10,11], config)
choose_lines_by_index([0,9,12,13], config)
choose_lines_by_index([0,9,14,15], config)
choose_lines_by_index([0,9,16,17], config)
choose_lines_by_index([0,9,18,19], config)
#Certificate
choose_lines_by_index([0,20,21], config)
#Product
choose_lines_by_index([0,22,23,24], config)
choose_lines_by_index([0,22,25,26], config)
choose_lines_by_index([0,22,27,28], config)
choose_lines_by_index([0,22,29,30], config)
choose_lines_by_index([0,22,31,32], config)
choose_lines_by_index([0,22,32,33], config)
#Partner
choose_lines_by_index([0,34,35], config)

