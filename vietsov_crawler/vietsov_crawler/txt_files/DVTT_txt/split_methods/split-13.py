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
#Facility
for i in range(9,22,2):
    choose_lines_by_index([0,8,i,i+1],config)


