import argparse
from pathlib import Path
from multiprocessing import cpu_count
import pdb
mapping = {
        "。":".",
        "，":",",
        "！":"!",
        "：":":",
        "；":":",
        "？":"?",
        "～":"~",
        "\"":"\'",
        "“":"\'",


        }

def clean(text):
    text = text.lower()
    text = ''.join([mapping[c] if c in mapping else c for c in text])
    return text

def preprocess(args):
    # Generate new meta.csv
    out = []
    text = []
    with open(Path(args.data_dir, '000001-010000.txt'), encoding='utf-8') as f:
        lines = f.readlines()
    lines = lines[1::2]
    for i, line in enumerate(lines):
        idx = '%06.f'%(i+1)
        line = line.replace('\t', '').strip()
        text.append(line)
        out.append('|'.join([idx, line, line]))

    Path(args.output_dir).mkdir(exist_ok=True)
    new_meta = Path(args.output_dir, 'bzn_meta.csv')
    with open(new_meta, 'w') as f:
        for x in out:
            f.write(x + '\n')

    # Calculate all symbols appear in the dataset
    symbols = set()
    for line in text:
        symbols = symbols | set(line)
    symbols = ''.join(sorted(list(symbols)))
    symbol_text = Path(args.output_dir, "bzn_symbols.txt")
    with open(symbol_text, 'w') as f:
        f.write(symbols)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='BZN dataset')
    parser.add_argument('--data-dir', type=str, help='Directory to raw dataset')
    parser.add_argument('--output-dir', default='bzn_tmp/', type=str, help='Directory to store output', required=False)
    parser.add_argument('--n-jobs', default=cpu_count(), type=int, help='Number of jobs used for feature extraction', required=False)
    args = parser.parse_args()
    preprocess(args)
