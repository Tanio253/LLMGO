from modules.choose_lines_by_index import choose_lines_by_index
import os
class config:
    OUTPUT_PREFIX = "../chunks"
    current_file = os.path.abspath(__file__)
    ORIGINAL_FILE = current_file[-4]
    
choose_lines_by_index([0,1], config)
choose_lines_by_index([0,2], config)

choose_lines_by_index([0,3,4], config)
choose_lines_by_index([0,3,5], config)
choose_lines_by_index([0,3,6], config)
choose_lines_by_index([0,3,7], config)
choose_lines_by_index([0,3,8], config)

choose_lines_by_index([0,9,10], config)
choose_lines_by_index([0,9,11], config)
choose_lines_by_index([0,9,12], config)
choose_lines_by_index([0,9,13], config)
choose_lines_by_index([0,9,14], config)

choose_lines_by_index([0,15,16,17], config)
choose_lines_by_index([0,15,16,18], config)
choose_lines_by_index([0,15,16,19], config)
choose_lines_by_index([0,15,16,20], config)

choose_lines_by_index([0,15,21,22], config)
choose_lines_by_index([0,15,21,22], config)
choose_lines_by_index([0,15,21,23], config)

choose_lines_by_index([0,15,25,26], config)
choose_lines_by_index([0,15,25,27], config)
choose_lines_by_index([0,15,25,28], config)

choose_lines_by_index([0,30, 31, 32, 33], config)


