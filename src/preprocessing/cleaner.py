"""
Light curve preprocessing utilities.

This module prepares raw TESS light curves for transit detection.
"""

from lightkurve import LightCurve


def clean_lightcurve(
    lightcurve: LightCurve,
    normalize: bool = True,
    flatten: bool = True,
    window_length: int = 401
) -> LightCurve:
    """
    Clean a TESS light curve.

    Steps
    -----
    1. Remove NaNs
    2. Remove bad quality cadences
    3. Normalize flux
    4. Flatten long-term stellar trends

    Parameters
    ----------
    lightcurve : LightCurve

    normalize : bool
        Normalize the flux.

    flatten : bool
        Remove long-term trends.

    window_length : int
        Savitzky-Golay filter window length.

    Returns
    -------
    LightCurve
    """

    lc = lightcurve.remove_nans()

    # Keep only good-quality cadences if quality column exists
    if hasattr(lc, "quality"):
        mask = lc.quality == 0
        lc = lc[mask]

    if normalize:
        lc = lc.normalize()

    if flatten:
        lc = lc.flatten(window_length=window_length)

    return lc