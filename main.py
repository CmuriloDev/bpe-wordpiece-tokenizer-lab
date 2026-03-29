from core.bpe import count_pairs, apply_merge
from core.wordpiece import test_wordpiece


def run_bpe():

    vocab = {
        'l o w </w>': 5,
        'l o w e r </w>': 2,
        'n e w e s t </w>': 6,
        'w i d e s t </w>': 3
    }

    print("=== BPE Training ===")

    for step in range(5):

        stats = count_pairs(vocab)

        if not stats:
            break

        best = max(stats, key=stats.get)

        vocab = apply_merge(best, vocab)

        print(f"\nStep {step + 1}")
        print(f"Best pair: {best}")
        print("Updated vocab:", vocab)

    return vocab


if __name__ == "__main__":
    run_bpe()
    test_wordpiece()