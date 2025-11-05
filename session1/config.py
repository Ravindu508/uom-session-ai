from dataclasses import dataclass, field

@dataclass(frozen=True)
class LabConfig:
    """
    Configuration for the lab.
    """
    sample_rate: int = field(default=1000)
    duration_s: float = field(default=2.0)
    noise_std: float = field(default=0.15)
    median_window: int = field(default=11)
    cache_size: int = field(default=256)