#!/usr/bin/env python

import os
import json
import csv

from covid19es import location
from covid19es import population
from covid19es.eshelper import ES

index_name = 'cov-ts'

es = ES(index_name)

all_data = []

c_fh = open("data/time_series/time_series_19-covid-Confirmed.csv", 'r')
r_fh = open("data/time_series/time_series_19-covid-Recovered.csv", 'r')
d_fh = open("data/time_series/time_series_19-covid-Deaths.csv", 'r')

c_csvdata = csv.reader(c_fh)
r_csvdata = csv.reader(r_fh)
d_csvdata = csv.reader(d_fh)

first_line = next(c_csvdata)

# We need to skip the first line
next(r_csvdata)
next(d_csvdata)


for i in c_csvdata:
    # The data format looks like this:
    #
    #['Province/State', 'Country/Region', 'Lat', 'Long', one row per day
    # We want one document per day

    # In theory all of these files are sorted the same, we will check this
    # someday
    rec = next(r_csvdata)
    deaths = next(d_csvdata)

    base = {
        "province": i[0],
        "country": i[1],
        # Elasticsearch geopoint format
        "location": {"lat": i[2], "lon": i[3]}
    }


    base["country2"] = location.get_code(i[1])
    base["population"] = population.get_population(base["country2"])


    # Now the dates
    for idx in range(4, len(i)):

        json_data = base.copy()
        # Our date format looks like 1/22/20
        # We need yyyyMMdd
        [month, day, year] = first_line[idx].split('/')

        year = int("20%s" % year)
        month = int(month)
        day = int(day)

        # We need leading zeros
        json_data['day'] = "%d%02d%02d" % (year, month, day)

        if i[idx] == '':
            i[idx] = '0'
        json_data['confirmed'] = int(i[idx])

        if rec[idx] == '':
            rec[idx] = '0'
        json_data['recovered'] = int(rec[idx])

        if deaths[idx] == '':
            deaths[idx] = '0'
        json_data['deaths'] = int(deaths[idx])


        bulk = {
                "_op_type": "index",
                "_index":   index_name,
               }

        bulk.update(json_data)

        all_data.append(bulk)

es.add(all_data)
