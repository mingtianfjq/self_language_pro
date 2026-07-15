from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tokenizers import WordTokenizer

def test_world_tokenizer():
    tokenizer = WordTokenizer()
    text = ['test 1 language model',
            'test 2 language model']
    tokenizer.fit(text)
    test_text = 'test language model'
    ids = tokenizer.encode(test_text)
    recoverd_text = tokenizer.decode(ids)
    assert recoverd_text == test_text