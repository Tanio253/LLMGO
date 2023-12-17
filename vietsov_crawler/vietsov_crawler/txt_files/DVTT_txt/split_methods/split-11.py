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
choose_lines_by_index([0,7,10,11], config)
#Resource
choose_lines_by_index([0,12,13], config)
#Certificate
choose_lines_by_index([0,14,15], config)
#Product
choose_lines_by_index([0,16,17,18], config)
choose_lines_by_index([0,16,18,19], config)

#Partner
choose_lines_by_index([0,20,21], config)


