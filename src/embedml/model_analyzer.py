import torch.nn as nn


class ModelAnalyzer:
    """
    Utility class for static analysis of PyTorch models.

    Provides parameter counting and weight memory estimation
    for deployment feasibility checks.
    """

    def __init__(self, model: nn.Module):
        self.model = model

    def count_parameters(self) -> int:
        return sum(p.numel() for p in self.model.parameters() if p.requires_grad)

    def estimate_weight_memory(self, bytes_per_param: int = 4) -> int:
        return self.count_parameters() * bytes_per_param