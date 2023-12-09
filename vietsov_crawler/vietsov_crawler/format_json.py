import json

# Your JSON data
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--file_path')
args = parser.parse_args()
with open(args.file_path,'r') as o:
    data = json.load(o)
    print(len(data))
# Writing the formatted JSON to a file
with open(f'formatted_{args.file_path}', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
