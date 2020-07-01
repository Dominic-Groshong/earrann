#!/usr/bin/env python
import os
import sys
import re
import requests
from bs4 import BeautifulSoup


class MLS():

    base_url = 'https://www.valleybrokers.com/'  # MLS sample to scrape

    def __init__(self, mls_number):
        """
        Takes in MLS number adds it to url.

        Args:
            mls_number (int): MLS number of house to scrape.
        """
        self.url = self.base_url + str(mls_number)

    def get_soup(self):
        page = requests.get(self.url)
        self.soup = BeautifulSoup(page.content, 'html.parser')

    def search_soup(self):
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

        self.get_soup()

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
sample = MLS(762281)
sample.get_soup()
