import torch.nn as nn

from embedml.model_analyzer import ModelAnalyzer
from embedml.hardware_profiles import STM32_SMALL


# Simple test model
model = nn.Sequential(
    nn.Linear(10, 64),
    nn.ReLU(),
    nn.Linear(64, 2)
)

analyzer = ModelAnalyzer(model)

total_params = analyzer.count_parameters()
weight_memory = analyzer.estimate_weight_memory(bytes_per_param=4)

result = STM32_SMALL.check_fit(
    required_ram=0,  # Activation not considered yet
    required_flash=weight_memory
)

print("Total parameters:", total_params)
print("Estimated weight memory (bytes):", weight_memory)
print("Feasible on STM32_SMALL:", result["fits"])