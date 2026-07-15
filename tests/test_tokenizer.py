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
    assert tokenizer.token_to_id['<PAD>'] == 0
    ids = tokenizer.encode("I love ChatGPT")
    assert ids == [3, 3, 3]