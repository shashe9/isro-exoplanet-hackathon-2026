"""
Transit Least Squares detector.

This module converts a cleaned TESS light curve into a Candidate object.
"""

from transitleastsquares import transitleastsquares

from src.features.candidate import Candidate


class TLSDetector:

    def __init__(
        self,
        period_min: float = 0.5,
        period_max: float = 15.0,
        oversampling: int = 5,
    ):
        self.period_min = period_min
        self.period_max = period_max
        self.oversampling = oversampling

    def detect(self, time, flux):
        """
        Run Transit Least Squares.

        Currently returns the raw TLS result.

        Candidate conversion will be added next.
        """

        model = transitleastsquares(time, flux)

        results = model.power(
            period_min=self.period_min,
            period_max=self.period_max,
            oversampling_factor=self.oversampling,
            show_progress_bar=True,
        )

        return results