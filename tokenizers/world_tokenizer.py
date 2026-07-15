class WordTokenizer:

    def __init__(self):

        self.token_to_id = {}
        self.id_to_token = {}
    
    def fit(self, corpus):
        tokens = set()
        for text in corpus:
            for token in text.split():
                tokens.add(token)
        
        sorted_tokens = sorted(tokens)
        for idx, token in enumerate(sorted_tokens):
            self.token_to_id[token] = idx
            self.id_to_token[idx] = token

    def encode(self, text):
        tokens = text.split()
        ids = []
        for token in tokens:
            ids.append(self.token_to_id[token])
        
        return ids
    
    def decode(self, ids):
        tokens = []
        for idx in ids:
            tokens.append(self.id_to_token[idx])

        return ' '.join(tokens)