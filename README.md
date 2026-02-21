
Analyze whether your ML model fits embedded constraints before deployment.


# Embedded ML Analyzer

Embedded ML Analyzer is a constraint-aware analysis tool that estimates whether a neural network model can fit on a resource-constrained embedded target before deployment.

It focuses on practical deployment constraints such as RAM usage, flash usage, activation memory, and rough feasibility checks.

## Why this exists

Many embedded ML projects fail late because hardware constraints are discovered after model development. This tool aims to catch those issues early by providing clear, repeatable estimates.

## Scope (v0.1)

Version 0.1 focuses on:

- Counting model parameters
- Estimating parameter storage size (float32 and int8)
- Approximating activation memory (simple estimates)
- Checking feasibility against predefined hardware profiles
- Producing a clear fit / not-fit result

Initial support:
- PyTorch models

## Example use case

Input:
- A PyTorch model
- A hardware profile (for example: 128 KB RAM, 512 KB flash)

Output estimates:
- Parameter count
- Estimated flash usage for weights
- Estimated RAM usage for activations (approximate)
- Overall feasibility result and the likely bottleneck

