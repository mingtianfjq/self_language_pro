

import json


PAD_TOKEN = "<PAD>"
BOS_TOKEN = "<BOS>"
EOS_TOKEN = "<EOS>"
UNK_TOKEN = "<UNK>"

SPECIAL_TOKENS = [PAD_TOKEN, BOS_TOKEN, EOS_TOKEN, UNK_TOKEN]






class WordTokenizer:

    def __init__(self):

        self.token_to_id = {}
        self.id_to_token = {}

        for idx, token in enumerate(SPECIAL_TOKENS):
            self.token_to_id[token] = idx
            self.id_to_token[idx] = token
    
    def fit(self, corpus):
        tokens = set()
        for text in corpus:
            for token in text.split():
                tokens.add(token)
        
        sorted_tokens = sorted(tokens)
        start_idx = len(SPECIAL_TOKENS)
        for idx, token in enumerate(sorted_tokens):
            self.token_to_id[token] = idx + start_idx
            self.id_to_token[idx + start_idx] = token

    def encode(self, text):
        tokens = text.split()
        ids = []
        unknown_token_id = self.token_to_id[UNK_TOKEN]
        for token in tokens:
            ids.append(self.token_to_id.get(token, unknown_token_id))
        
        return ids
    
    def decode(self, ids):
        tokens = []
        for idx in ids:
            tokens.append(self.id_to_token[idx])

        return ' '.join(tokens)

    def save(self, file_path):
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(self.token_to_id, file, ensure_ascii=False, indent=2)

    @classmethod
    def load(cls, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            token_to_id = json.load(file)

        tokenizer = cls()
        tokenizer.token_to_id = {token: int(idx) for token, idx in token_to_id.items()}
        tokenizer.id_to_token = {
            int(idx): token for token, idx in tokenizer.token_to_id.items()
        }
        return tokenizer