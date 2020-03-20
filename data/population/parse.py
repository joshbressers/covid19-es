#!/usr/bin/env python

import csv

with open('WPP2019_TotalPopulationBySex.csv', 'r') as csvfile:
    csvdata = csv.reader(csvfile)

    first_line = next(csvdata)

    for i in csvdata:
        # LocID,Location,VarID,Variant,Time,MidPeriod,PopMale,PopFemale,PopTotal,PopDensity
        #
        # I want Location, VarID, Time, and PopTotal
        # i[1], [2], i[4], i[8]
        # The VarID is for expected population growth, we don't care, but
        # we only want the "normal" data
        if i[4] == '2020' and i[2] == '2':
            name = i[1]
            year = int(i[4])
            population = int(float(i[8]) * 1000)
            print("%s %d %d" % (i[1], year, population))
