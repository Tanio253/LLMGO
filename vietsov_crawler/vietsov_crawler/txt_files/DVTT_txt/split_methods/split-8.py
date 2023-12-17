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
choose_lines_by_index([0,7,8,9], config)
choose_lines_by_index([0,7,9,10], config)
#Resource
choose_lines_by_index([0,11,12,13], config)
choose_lines_by_index([0,11,14,15], config)
choose_lines_by_index([0,11,16,17], config)
choose_lines_by_index([0,11,18,19], config)
#Certificate
choose_lines_by_index([0,20,21], config)
#Product
for i in range(23, 46, 2):
    choose_lines_by_index([0,22,i,i+1], config)
choose_lines_by_index([0,22,46,47], config)

#Partner
choose_lines_by_index([0,48,49], config)

