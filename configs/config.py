from dataclasses import dataclass


@dataclass
class ModelConfig:
    """Configuration for the language model."""

    vocab_size: int = 32000
    max_seq_len: int = 2048

    hidden_size: int = 512
    intermediate_size: int = 1536

    num_layers: int = 8
    num_heads: int = 8

    dropout: float = 0.0

    rope_theta: float = 10000.0