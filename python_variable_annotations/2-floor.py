#!/usr/bin/env python3
"""
Bu modul real ədədi aşağı yuvarlayan floor funksiyasını ehtiva edir.
"""

import math


def floor(n: float) -> int:
    """
    Verilən real ədədi aşağı yuvarlayaraq tam ədəd qaytarır.

    Args:
        n (float): Yuvarlanacaq real ədəd.

    Returns:
        int: n-in aşağı yuvarlanmış tam dəyəri.
    """
    return math.floor(n)
