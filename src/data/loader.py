"""
Data loading utilities for TESS light curves.

This module is responsible only for retrieving TESS light curves.
No preprocessing or transit detection should happen here.
"""

import lightkurve as lk


def search_tess_lightcurves(
    target: str,
    mission: str = "TESS",
    author: str = "SPOC"
):
    """
    Search available TESS light curves.

    Parameters
    ----------
    target : str
        Example: 'TIC 261136679'

    Returns
    -------
    SearchResult
    """
    return lk.search_lightcurve(
        target=target,
        mission=mission,
        author=author
    )


def download_lightcurve(search_result, index: int = 0):
    """
    Download one light curve from a SearchResult.

    Parameters
    ----------
    search_result : lightkurve.SearchResult

    index : int
        Which entry to download.

    Returns
    -------
    TessLightCurve
    """
    if len(search_result) == 0:
        raise ValueError("No light curves found.")

    return search_result[index].download()