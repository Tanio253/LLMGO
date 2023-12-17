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
choose_lines_by_index([0,7,10,11], config)
choose_lines_by_index([0,7,11,12], config)
#Resource
choose_lines_by_index([0,13,14], config)
#Certificate
choose_lines_by_index([0,15,16,17], config)
choose_lines_by_index([0,15,18,19], config)
choose_lines_by_index([0,15,20,21], config)
choose_lines_by_index([0,15,21,22], config)
#Product
for i in range(24, 42, 2):
    choose_lines_by_index([0,23,i,i+1], config)
choose_lines_by_index([0,23,41,42], config)
#Partner
choose_lines_by_index([0,43,44,45], config)

