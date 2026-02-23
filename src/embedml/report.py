from dataclasses import dataclass

from .utils import format_bytes


@dataclass
class FeasibilityReport:
    profile_name: str
    total_params: int
    float32_weight_bytes: int
    int8_weight_bytes: int
    fits_float32: bool
    fits_int8: bool

    def to_text(self) -> str:
        lines = [
            f"Target profile: {self.profile_name}",
            f"Total parameters: {self.total_params}",
            "",
            f"Float32 weights: {format_bytes(self.float32_weight_bytes)} | fits: {self.fits_float32}",
            f"Int8 weights:    {format_bytes(self.int8_weight_bytes)} | fits: {self.fits_int8}",
        ]
        return "\n".join(lines)


def build_feasibility_report(
    profile,
    total_params: int,
    float32_weight_bytes: int,
    int8_weight_bytes: int,
) -> FeasibilityReport:
    result_f32 = profile.check_fit(required_ram=0, required_flash=float32_weight_bytes)
    result_i8 = profile.check_fit(required_ram=0, required_flash=int8_weight_bytes)

    return FeasibilityReport(
        profile_name=profile.name,
        total_params=total_params,
        float32_weight_bytes=float32_weight_bytes,
        int8_weight_bytes=int8_weight_bytes,
        fits_float32=result_f32["fits"],
        fits_int8=result_i8["fits"],
    )