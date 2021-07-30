from torch import nn
from transformers import AutoTokenizer, AutoModel


class BERTMetric(nn.Module):
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained()
        print("s")