import torch.nn as nn

from embedml.model_analyzer import ModelAnalyzer
from embedml.hardware_profiles import STM32_SMALL


# Simple test model
model = nn.Sequential(
    nn.Linear(10, 64),
    nn.ReLU(),
    nn.Linear(64, 2),
)

analyzer = ModelAnalyzer(model)

total_params = analyzer.count_parameters()

float32_flash = analyzer.estimate_weight_memory(bytes_per_param=4)
int8_flash = analyzer.estimate_weight_memory(bytes_per_param=1)

result_f32 = STM32_SMALL.check_fit(required_ram=0, required_flash=float32_flash)
result_i8 = STM32_SMALL.check_fit(required_ram=0, required_flash=int8_flash)

print("Total parameters:", total_params)
print("Float32 weights (bytes):", float32_flash, "| fits:", result_f32["fits"])
print("Int8 weights (bytes):", int8_flash, "| fits:", result_i8["fits"])