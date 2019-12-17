"""
This file is run each day at 12:00 and
    - Scrapes the data from weerplaza (scrapeWeerPlaza.py)
    - Scrapes the actual weather of the day before (data_yesterday.py)

    This data will later be used to preform a quality check
"""


import scrapeWeerPlaza
import data_yesterday