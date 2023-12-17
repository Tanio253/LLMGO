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
choose_lines_by_index([0,7,12,13], config)
choose_lines_by_index([0,7,14,15], config)
choose_lines_by_index([0,7,16,17], config)
#Resource
choose_lines_by_index([0,18,19,20], config)
choose_lines_by_index([0,18,21,22], config)
choose_lines_by_index([0,18,23,24], config)
choose_lines_by_index([0,18,25,26], config)
choose_lines_by_index([0,18,27,28], config)
choose_lines_by_index([0,18,28,29], config)
#Certificate
choose_lines_by_index([0,30,31], config)
#Product
for i in range(33, 42, 2):
    choose_lines_by_index([0,32,i,i+1], config)
choose_lines_by_index([0,32,42,43], config)

#Partner
choose_lines_by_index([0,44,45], config)

