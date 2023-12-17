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
choose_lines_by_index([0,11,14,15], config)
choose_lines_by_index([0,11,16,17], config)
choose_lines_by_index([0,11,18,19], config)
choose_lines_by_index([0,11,20,21], config)
choose_lines_by_index([0,11,21,22], config)
#Certificate
choose_lines_by_index([0,23,24], config)
#Product
choose_lines_by_index([0,25,26,27], config)
choose_lines_by_index([0,25,28,29], config)
#Partner
choose_lines_by_index([0,30,31], config)


