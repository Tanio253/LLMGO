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
#Resource
choose_lines_by_index([0,10,11], config)
#Certificate
choose_lines_by_index([0,12,13], config)
#Product
for i in range(15, 26, 2):
    choose_lines_by_index([0,14,i,i+1], config)
choose_lines_by_index([0,14,26,27], config)

#Partner
choose_lines_by_index([0,28,29,30], config)
choose_lines_by_index([0,28,31,32], config)

