# import random
from concurrent.futures import ThreadPoolExecutor
from itertools import filterfalse
from os import listdir
from os.path import isfile,join

with open('data/interim/vocabulary.txt', 'r') as f:
    vocabulary = f.read().split('\n')

in_path = 'data/interim/slices'
out_path = 'data/processed'
corpus = [f for f in listdir(in_path) if isfile(join(in_path, f))]
# corpus = random.sample(corpus, 1)


def not_vocabulary_word(wd):
    if wd in vocabulary:
        return False
    else:
        return True


def filter_line(line):
    line = line.strip().split()
    line = [wd.strip() for wd in line]
    return filterfalse(not_vocabulary_word, line)


def clean_file(f):
    with open(join(in_path, f), 'r') as infile:
        with open(join(out_path, f), 'w') as outfile:
            for l in infile:
                line = list(filter_line(l))
                line = ' '.join(line)
                outfile.write(line + '\n')


with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(clean_file, corpus)
