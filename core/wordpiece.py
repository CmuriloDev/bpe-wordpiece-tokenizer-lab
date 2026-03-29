from transformers import AutoTokenizer


def test_wordpiece():

    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

    sentence = "The transformer's hyperparameters are unacceptably difficult to tune."

    tokens = tokenizer.tokenize(sentence)

    print("\n--- WordPiece Analysis ---")
    print(tokens)

    return tokens