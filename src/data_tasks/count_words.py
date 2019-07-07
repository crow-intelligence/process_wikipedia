from bounter import bounter
from smart_open import smart_open

counts = bounter(size_mb=1024)
for line in smart_open('data/interim/wiki.txt'):
    l = line.strip().split()
    counts.update(l)

freq_dist = dict(list(counts.items()))

with open('data/interim/word_freqs.tsv', 'w') as outfile:
    for k, v in freq_dist.items():
        o = k + '\t' + str(v) + '\n'
        outfile.write(o)
