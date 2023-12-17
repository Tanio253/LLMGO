import json
import os
PREFIX_FP = './json_files/'
file_paths = ["CSVC", "DADT", "DVTT", "GT", "NNL", "SPDV", "TDTS", "TT"]
def format_json():
    for file_name in file_paths:
        input_path = os.path.join(PREFIX_FP, file_name, f"{file_name}.json")
        output_path = os.path.join(PREFIX_FP, file_name, f"formatted_{file_name}.json")
        with open(input_path, 'r') as input_file:
            data = json.load(input_file)

        with open(output_path, 'w', encoding='utf-8') as output_file:
            json.dump(data, output_file, ensure_ascii=False, indent=2)
            
if __name__ == "__main__":
    format_json()
    

