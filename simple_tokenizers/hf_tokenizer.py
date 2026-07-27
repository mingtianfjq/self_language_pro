from transformers import AutoTokenizer


class HFTokenizer:

    def __init__(self, model_path_or_name):

        self.tokenizer = AutoTokenizer.from_pretrained(model_path_or_name)

    def encode(self, text):
        return self.tokenizer.encode(text, add_special_tokens=False)

    def decode(self, token_ids):
        return self.tokenizer.decode(token_ids)

    @property
    def vocab_size(self):
        return len(self.tokenizer)

    @property
    def pad_token_id(self):
        return self.tokenizer.pad_token_id

    @property
    def unk_token_id(self):
        return self.tokenizer.unk_token_id

    @property
    def bos_token_id(self):
        return self.tokenizer.bos_token_id  

    @property
    def eos_token_id(self):
        return self.tokenizer.eos_token_id