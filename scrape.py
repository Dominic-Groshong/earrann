#!/usr/bin/env python
import os
import sys
import re
import requests
from bs4 import BeautifulSoup


# Perameters
site_url = 'https://www.valleybrokers.com/762281'  # MLS sample to scrape


# Helper functions
def request_site(site_url):
    """Send a request and parse it through beautiful soup, returning a soup object

    Args:
        URL (string): Input url of webpage you want to scrape.
    """
    page = requests.get(site_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    return soup


def search_soup():
    """
    What data do we want to get from soup?
    ---------------------------------------
    mls number
    price
    # of bedrooms
    # of bathrooms
    images
    type of home
    style (1 story, 2 story, etc.)
    year built
    lot acerage
    address
    city
    county
    state
    zip
    comments(discription)
    directions
    inclusions
    tax year
    taxes
    square footage
    acreage
    garage
    water
    zoning
    listing agency
    """

    soup = request_site(site_url)

    mls = soup.find(text=re.compile('^MLS'))

    data = []

    for item in soup.find_all('div', class_="data"):
        data.append(item.prettify())

    print(data)


# Run Program
search_soup()
