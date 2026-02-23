import argparse
import torch.nn as nn

from embedml.hardware_profiles import ESP32_CLASS, STM32_SMALL
from embedml.model_analyzer import ModelAnalyzer
from embedml.report import build_feasibility_report


def build_demo_model() -> nn.Module:
    return nn.Sequential(
        nn.Linear(10, 64),
        nn.ReLU(),
        nn.Linear(64, 2),
    )


def get_profile(name: str):
    profiles = {
        "STM32_SMALL": STM32_SMALL,
        "ESP32_CLASS": ESP32_CLASS,
    }
    if name not in profiles:
        valid = ", ".join(sorted(profiles.keys()))
        raise SystemExit(f"Unknown profile '{name}'. Valid profiles: {valid}")
    return profiles[name]


def main() -> None:
    parser = argparse.ArgumentParser(description="Embedded ML feasibility planner (v0.1)")
    parser.add_argument("--profile", default="STM32_SMALL")
    args = parser.parse_args()

    profile = get_profile(args.profile)
    model = build_demo_model()

    analyzer = ModelAnalyzer(model)
    total_params = analyzer.count_parameters()
    float32_flash = analyzer.estimate_weight_memory(bytes_per_param=4)
    int8_flash = analyzer.estimate_weight_memory(bytes_per_param=1)

    report = build_feasibility_report(
        profile=profile,
        total_params=total_params,
        float32_weight_bytes=float32_flash,
        int8_weight_bytes=int8_flash,
    )

    print(report.to_text())


if __name__ == "__main__":
    main()