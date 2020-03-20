#!/usr/bin/env python

import os
import json
import glob
import csv
import re

from covid19es import location
from covid19es import population
from covid19es.eshelper import ES
from covid19es import Countries

# Dates are hard
last_year4 = re.compile(r'(\d+)\/(\d+)\/(\d{4}) (\d+)\:(\d+)')
last_year2 = re.compile(r'(\d+)\/(\d+)\/(\d{2}) (\d+)\:(\d+)')

es = ES()
countries = Countries()

csv_data = glob.glob("data/daily/*.csv")

for f in csv_data:
    with open(f, 'r') as csvfile:
        csvdata = csv.reader(csvfile)

        first_line = next(csvdata)


        for i in csvdata:
            # The data format looks like this:
            #
            #Province/State,Country/Region,Last Update,Confirmed,Deaths,Recovered,Latitude,Longitude

            countries.add(i[1])
            countries.add_province(i[0])

            # Some of the data is missing long/lat details
            if len(i) == 8:
                # Elasticsearch geopoint format
                loc = {"lat": i[6], "lon": i[7]}
            else:
                loc = None

            # Now the dates, this is from the filename f
            [month, day, year] = f.split('/')[-1].split('.')[0].split('-')
            day = "%s%s%s" % (year, month, day)

            countries.add_data(day, i[3], i[4], i[5], loc)


es.add(countries.get_bulk_country())

es = ES('covid19-province')
es.add(countries.get_bulk_province())
