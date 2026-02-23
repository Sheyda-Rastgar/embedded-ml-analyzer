# Embedded ML Analyzer

**Analyze whether your ML model fits embedded constraints before deployment.**

Embedded ML Analyzer is a lightweight, constraint-aware feasibility planner for embedded machine learning systems.

It is designed to help engineers answer a critical design-time question:

Will this model architecture fit on my target hardware before I train or convert it?

---

## Motivation

In many embedded ML workflows, hardware feasibility is evaluated late in the pipeline:

- After model training
- After quantization
- After conversion to formats such as TFLite or ONNX
- Or during deployment validation

At that stage, redesigning the model architecture can be expensive and time-consuming.

There are already strong tools in the ecosystem that provide:

- Post-conversion profiling
- Runtime memory inspection
- Operator-level memory tracing
- Deployment metrics within specific frameworks

However, most of these tools operate after export or inside a specific toolchain.

Embedded ML Analyzer explores a different perspective:

A lightweight, PyTorch-first feasibility planning step that evaluates architectural constraints early — before training or conversion.

---

## What This Tool Is (v0.1)

Version 0.1 focuses on early architectural feasibility checks.

Current capabilities:

- Parameter counting
- Weight memory estimation (float32 and int8)
- Hardware profile-based flash feasibility checks
- Structured feasibility reporting
- Minimal command-line interface
- Human-readable memory formatting

### Current Scope

- Works directly with PyTorch models (torch.nn.Module)
- Focuses primarily on weight storage estimation
- Uses simplified activation assumptions (to be refined in future versions)

The goal at this stage is to validate the core feasibility workflow while keeping the architecture clean and extensible.

---

## What This Tool Is Not (Yet)

- It is not a full runtime memory profiler.
- It does not replace TFLite or ONNX profiling tools.
- It does not compute exact peak memory arena allocation.
- It does not automatically optimize or modify models.

This project focuses on architectural feasibility planning rather than runtime instrumentation.

---

## Example Workflow

### Input

- A PyTorch model architecture
- A predefined hardware profile (e.g., STM32_SMALL)

### Output

- Total parameter count
- Estimated weight memory (float32 / int8)
- Feasibility result for the selected hardware
- A structured textual report

The CLI allows selecting different hardware profiles to compare feasibility outcomes.

---

## Hardware Profiles

The project currently includes predefined example profiles:

- STM32_SMALL (128 KB RAM, 512 KB Flash)
- ESP32_CLASS (320 KB RAM, 4 MB Flash)

Support for custom hardware profile definitions is planned for future versions.

---

## Installation (Development Mode)

1. Create and activate a virtual environment.
2. Install dependencies (currently PyTorch).
3. Run the example script or CLI module from the project root.

The project follows a src-based layout and is intended to be installed in editable mode during development.

---

## Project Structure (High-Level)

The architecture is intentionally modular:

- Hardware profiles: define memory constraints
- Model analyzer: extracts architectural statistics from PyTorch models
- Reporting layer: formats feasibility results
- CLI layer: provides a simple user interface

This separation allows incremental feature expansion without tightly coupling analysis and presentation logic.

---

## Project Status

This project is in early development (v0.1).

The current focus is:

- Validating the architectural feasibility workflow
- Keeping the internal structure extensible
- Building a solid foundation for future memory estimation features

### Planned Improvements

- Improved activation memory estimation
- Peak RAM approximation
- Layer-wise memory breakdown
- Bottleneck identification
- Actionable architectural suggestions
- Custom hardware profile loading
- Improved CLI ergonomics

---

## Why This Matters

Embedded ML systems operate under strict memory constraints.

Being able to reason about feasibility before training reduces iteration cost and enables more informed architectural decisions.

This project is an ongoing exploration of that early-stage design space.

Feedback and technical discussion are welcome.