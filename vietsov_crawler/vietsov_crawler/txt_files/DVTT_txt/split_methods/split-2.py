from modules.choose_lines_by_index import choose_lines_by_index
import os
class config:
    OUTPUT_PREFIX = "../chunks"
    current_file = os.path.abspath(__file__)
    ORIGINAL_FILE = current_file[-4]
    
choose_lines_by_index([0,1,2], config)

choose_lines_by_index([0,3,4], config)

choose_lines_by_index([0,5,6], config)

choose_lines_by_index([0,7,8], config)

choose_lines_by_index([0,9,10,11], config)
choose_lines_by_index([0,9,12,13], config)
choose_lines_by_index([0,9,14,15], config)
choose_lines_by_index([0,9,15,16], config)

choose_lines_by_index([0,17,18], config)

choose_lines_by_index([0,19,20,21], config)
choose_lines_by_index([0,19,22,23], config)
choose_lines_by_index([0,19,24,25], config)
choose_lines_by_index([0,19,26,27], config)
choose_lines_by_index([0,19,28,29], config)

choose_lines_by_index([0,30,31,32], config)
choose_lines_by_index([0,30,33,34], config)
choose_lines_by_index([0,30,35,36], config)
choose_lines_by_index([0,30,37,38], config)
choose_lines_by_index([0,30,39,40], config)
choose_lines_by_index([0,30,40,41], config)

