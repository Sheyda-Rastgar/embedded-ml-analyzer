def format_bytes(num_bytes: int) -> str:
    """
    Format a byte count into a human-readable string (B, KB, MB, GB).
    """
    if num_bytes < 0:
        raise ValueError("num_bytes must be non-negative.")

    units = ["B", "KB", "MB", "GB", "TB"]
    value = float(num_bytes)

    for unit in units:
        if value < 1024.0 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)} {unit}"
            return f"{value:.2f} {unit}"
        value /= 1024.0

    return f"{num_bytes} B"