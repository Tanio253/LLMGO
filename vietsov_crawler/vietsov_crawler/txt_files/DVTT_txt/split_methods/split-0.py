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
choose_lines_by_index([0,7,9,10], config)
choose_lines_by_index([0,7,11,12], config)
choose_lines_by_index([0,7,12,13], config)

choose_lines_by_index([0,14,15,16], config)

choose_lines_by_index([0,17,18], config)

choose_lines_by_index([0,19,20,21], config)
choose_lines_by_index([0,19,22,23], config)
choose_lines_by_index([0,19,24,25], config)
choose_lines_by_index([0,19,26,27], config)
choose_lines_by_index([0,19,28,29], config)
choose_lines_by_index([0,19,30,31], config)
choose_lines_by_index([0,19,32,33], config)
choose_lines_by_index([0,19,34,35], config)
choose_lines_by_index([0,19,36,37], config)
choose_lines_by_index([0,19,37,38], config)

choose_lines_by_index([0,39,40], config)