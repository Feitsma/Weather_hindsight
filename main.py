"""
This file is run each day at 12:00 and
    - Scrapes the data from weerplaza (scrape_weerplaza.py)
    - Scrapes the actual weather of the day before (data_yesterday.py)

    - Preform a quality check of the data (data_processing.py)
"""


import scrape_weerplaza
import data_yesterday

import data_processing
