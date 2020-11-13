#! python3
#                   ## Webscraping with Beautiful Soup adjusted for Windows ##
# The code below determines whether or not an item is in stock at Pricesmart's
# San Fernando branch by evaluating the style attribute of an i tag within a p tag.
# It first locates the span tag that contains the text=<Store Location>. From here
# it determines the parent p tag and finally extracts the style attribute of the i
# tag contained within. Required packages shown in the import section below. Install
# if not already installed 
#
#
# Import Libraries
from tkinter import *
import tkinter.messagebox
import requests
import pandas as pd
import bs4

# Item Numbers removed from code and stored locally to text file 
# Read in list of items from text file and convert to list
# Adjust path to file as required
data = pd.read_csv('/Users/admin/Desktop/PS.txt', header=None, usecols=[0], dtype='str')
items = data[0].tolist()

# Iterate through list to create search url
for item in items:
    # Define URL for each item
    url = ('https://www.pricesmart.com/site/tt/en/pdp/{}'.format(item))

    # Get HTML response
    response = requests.get(url)

    # Parse HTML response using BeautifulSoup
    responseSoup = bs4.BeautifulSoup(response.text, 'html.parser')

    ## Extract required Elements from Soup ##
    # Extract product name from id="product-display-name"
    productName = responseSoup.select('#product-display-name')[0].getText().strip().replace("'", "")
    if productName != "" :
        # Find and extract P Element for San Fernando store. Change store location as required
        storeContainer = responseSoup.find(name='span', attrs={"class": "product-container-inner"}, text='San Fernando')
        parentElementP = storeContainer.find_parent('p')
        # Extract Style attribute for child i tag - proxy for stock status
        stockCheck = parentElementP.select('i')[0].get('style')

        # Define string for tkinter pop-up message
        tkmessage = "{} back in stock!".format(productName)

        # Apply logic to stock check using style attribute as proxy
        if stockCheck != 'color:red':
             # Display pop-up window if item is in stock
             root=Tk()
             root.withdraw()
             tkinter.messagebox.showinfo('Pricesmart Py', tkmessage)
