from ..simple_tokenizers import HFTokenizer


def test_encode_decode():

    tokenizer = HFTokenizer(
        "./assets/asset_tokenizers"
    )

    text = "I love AI"

    ids = tokenizer.encode(text)

    result = tokenizer.decode(ids)
    print(tokenizer.encode("aaaaaaaa  sdv  rfga   adg"))

    assert result.strip() == text