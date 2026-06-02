"""
live_nav_fetch.py
Day 1 — Fetch live NAV data from mfapi.in for key mutual fund schemes.
Parses JSON responses and saves each as a raw CSV in data/raw/.
"""

import os
import time
import requests
import pandas as pd
