#!/usr/bin/env python

import os
import json
import csv

from covid19es import location
from covid19es import population
from covid19es import Countries
from covid19es.eshelper import ES


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

countries = Countries()

for i in c_csvdata:
    # The data format looks like this:
    #
    #['Province/State', 'Country/Region', 'Lat', 'Long', one row per day
    # We want one document per day

    # In theory all of these files are sorted the same, we will check this
    # someday
    rec = next(r_csvdata)
    deaths = next(d_csvdata)


    country = i[1]
    province = i[0]
    location = {"lat": i[2], "lon": i[3]}


    # Now the dates
    for idx in range(4, len(i)):

        countries.add(i[1])
        countries.add_province(i[0])

        # Our date format looks like 1/22/20
        # We need yyyyMMdd
        [month, day, year] = first_line[idx].split('/')
        year = int("20%s" % year)
        month = int(month)
        day = int(day)
        # We need leading zeros
        day = "%d%02d%02d" % (year, month, day)

        if i[idx] == '':
            i[idx] = '0'
        c = int(i[idx])

        if rec[idx] == '':
            rec[idx] = '0'
        r = int(rec[idx])

        if deaths[idx] == '':
            deaths[idx] = '0'
        d = int(deaths[idx])

        countries.add_data(day, c, d, r, location)


es = ES('covid19-country')
es.add(countries.get_bulk_country())

es = ES('covid-19')
es.add(countries.get_bulk_province())
