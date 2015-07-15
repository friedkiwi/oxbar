__author__ = 'yj'

# script to import the original bar listing from
# uglynewt's github repository to the oxbar bar.

BAR_LISTING = 'https://raw.githubusercontent.com/uglynewt/fridgeview/master/res/raw/contents'

import urllib2
import json


bar_listing = urllib2.urlopen(BAR_LISTING).read()


products = []
counter = 1

for line in bar_listing.split("\n"):
    if (len(line.split(":")) == 2):
        if (len(line.split(":")[1]) > 0) :
            name = line.split(":")[0]
            cost = line.split(":")[1]
            product = {}
            product["model"] = "bar.product"
            product["pk"] = counter
            product["fields"] = {}

            product["fields"]["name"] = name
            product["fields"]["product_price"] = cost
            product["fields"]["description"] = ""
            product["fields"]["product_type"] = "D"
            product["fields"]["is_vegan"] = False
            product["fields"]["is_vegetarian"] = False
            product["fields"]["contains_nuts"] = False
            product["fields"]["contains_milk"] = False

            products.append(product)

            counter = counter + 1


print json.dumps(products)