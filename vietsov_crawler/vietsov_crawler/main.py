from utils import (
    format_json,
    format_txt,
)
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--format')
args = parser.parse_args()
if __name__ == "__main__":
    if args.format=="json":
        format_json.format_json()
    if args.format=='txt':
        format_txt.format_txt()
    
