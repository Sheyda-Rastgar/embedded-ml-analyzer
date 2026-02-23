import torch.nn as nn

from embedml.hardware_profiles import STM32_SMALL
from embedml.model_analyzer import ModelAnalyzer
from embedml.report import build_feasibility_report


model = nn.Sequential(
    nn.Linear(10, 64),
    nn.ReLU(),
    nn.Linear(64, 2),
)

analyzer = ModelAnalyzer(model)

total_params = analyzer.count_parameters()
float32_flash = analyzer.estimate_weight_memory(bytes_per_param=4)
int8_flash = analyzer.estimate_weight_memory(bytes_per_param=1)

report = build_feasibility_report(
    profile=STM32_SMALL,
    total_params=total_params,
    float32_weight_bytes=float32_flash,
    int8_weight_bytes=int8_flash,
)

print(report.to_text())