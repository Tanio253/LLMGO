from modules.choose_lines_by_index import choose_lines_by_index
import os
class config:
    OUTPUT_PREFIX = "../chunks"
    current_file = os.path.abspath(__file__)
    ORIGINAL_FILE = current_file[-4]
choose_lines_by_index([0,1], config)
for i in range(3, 17):
    choose_lines_by_index([0,2,i], config)



