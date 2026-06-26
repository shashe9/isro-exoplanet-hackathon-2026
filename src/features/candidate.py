from dataclasses import dataclass
from typing import Optional

import numpy as np


@dataclass
class Candidate:
    """
    Represents one transit candidate detected from a single TESS light curve.
    """

    # Identification
    target_id: str
    sector: int
    cadence_seconds: int

    # Detection results
    period: float
    duration: float

    # Transit depth
    depth_fraction: float
    depth_ppm: float

    # Detection confidence
    sde: float
    snr: float
    fap: float

    # Vetting metrics
    odd_even_mismatch: float
    transit_count: int

    # Folded light curve
    phase: Optional[np.ndarray] = None
    folded_flux: Optional[np.ndarray] = None