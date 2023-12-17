from modules.choose_lines_by_index import choose_lines_by_index
import os
class config:
    OUTPUT_PREFIX = "../chunks"
    current_file = os.path.abspath(__file__)
    ORIGINAL_FILE = current_file[-4]
    
choose_lines_by_index([0,1,2], config)

choose_lines_by_index([0,3,4], config)

choose_lines_by_index([0,5,6], config)

choose_lines_by_index([0,7,8,9], config)
choose_lines_by_index([0,7,10,11], config)
choose_lines_by_index([0,7,11,12], config)

choose_lines_by_index([0,13,14], config)

choose_lines_by_index([0,15,16], config)

choose_lines_by_index([0,17,18,19], config)
choose_lines_by_index([0,17,20,21], config)
choose_lines_by_index([0,17,22,23], config)
choose_lines_by_index([0,17,24,25], config)
choose_lines_by_index([0,17,26,27], config)
choose_lines_by_index([0,17,28,29], config)

choose_lines_by_index([0,30,31], config)

