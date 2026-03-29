import collections
import re


def count_pairs(vocab):
    pairs = collections.defaultdict(int)

    for word, freq in vocab.items():
        symbols = word.split()

        for i in range(len(symbols) - 1):
            pair = (symbols[i], symbols[i + 1])
            pairs[pair] += freq

    return pairs


def apply_merge(pair, vocab_in):
    vocab_out = {}

    pattern = re.escape(' '.join(pair))
    regex = re.compile(r'(?<!\S)' + pattern + r'(?!\S)')

    for word in vocab_in:
        merged_word = regex.sub(''.join(pair), word)
        vocab_out[merged_word] = vocab_in[word]

    return vocab_out