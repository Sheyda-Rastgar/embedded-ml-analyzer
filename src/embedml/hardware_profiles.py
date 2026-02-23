from dataclasses import dataclass


@dataclass
class HardwareProfile:
    name: str
    ram_bytes: int
    flash_bytes: int

    # Evaluate memory feasibility against hardware limits.
    def check_fit(self, required_ram: int, required_flash: int) -> dict:
        ram_ok = required_ram <= self.ram_bytes
        flash_ok = required_flash <= self.flash_bytes

        return {
            "profile": self.name,
            "ram_ok": ram_ok,
            "flash_ok": flash_ok,
            "fits": ram_ok and flash_ok,
            "required_ram": required_ram,
            "required_flash": required_flash,
            "available_ram": self.ram_bytes,
            "available_flash": self.flash_bytes,
        }


# Predefined hardware profiles

STM32_SMALL = HardwareProfile(
    name="STM32_SMALL",
    ram_bytes=128 * 1024,
    flash_bytes=512 * 1024,
)

ESP32_CLASS = HardwareProfile(
    name="ESP32_CLASS",
    ram_bytes=320 * 1024,
    flash_bytes=4 * 1024 * 1024,
)