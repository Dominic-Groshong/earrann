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


    images
    type of home
    style (1 story, 2 story, etc.)
    year built
    lot acerage
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

    data = {
        'MLS': soup.find(text=re.compile('^MLS')),
        'Address': {
            'Street': soup.find(text=re.compile('^Address')),
            'City': soup.find(text=re.compile('^City')),
            'County': soup.find(text=re.compile('^County')),
            'State': soup.find(text=re.compile('^State')),
            'ZIP': soup.find(text=re.compile('^State')),
        },
        'Bedrooms': soup.find(text=re.compile('^Bedrooms')),
        'Bathrooms': soup.find(text=re.compile('^Bathrooms')),
        'Price': soup.find(text=re.compile('^Price')),
        'Comments': soup.find(text=re.compile('^Comments')),
    }

    #img_urls = []
    # img_urls.append(site_url + soup.find(id="showhome_mainphoto").get('src'))

    # for image in soup.findAll(text=re.compile('(?<=photourl = \').*?(?=\';)')):
    #     image.find(string=re.compile('(?<=photourl = \').*?(?=\';)'))
    #     print(image)
    #     # img_urls.append(site_url + image.get('src'))

    print(data)


# Run Program
search_soup()
