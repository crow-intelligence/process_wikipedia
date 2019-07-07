with open('data/interim/word_freqs.tsv', 'r') as f:
    word_freq = {}
    for l in f:
        wd, freq = l.strip().split('\t')
        freq = int(freq)
        if freq > 50:
            word_freq[wd] = freq

vocabulary = list(word_freq.keys())
# 2841167242 -> no filter
# 2795371170 -> 20
# 2776104024 -> 50

with open('data/interim/vocabulary.txt', 'w') as f:
    for wd in vocabulary:
        f.write(wd + '\n')
