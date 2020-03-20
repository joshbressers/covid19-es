
import csv
from covid19es import location

class Countries:
    def __init__(self):
        self.countries = {}

        with open('data/population/WPP2019_TotalPopulationBySex.csv', 'r') as csvfile:
            csvdata = csv.reader(csvfile)

            first_line = next(csvdata)

            for i in csvdata:
                # LocID,Location,VarID,Variant,Time,MidPeriod,PopMale,
                # PopFemale,PopTotal,PopDensity
                #
                # I want Location, VarID, Time, and PopTotal
                # i[1], [2], i[4], i[8]
                # The VarID is for expected population growth, we don't
                # care about most, we only want the "normal" data
                if i[4] == '2020' and i[2] == '2':
                    name = i[1]
                    year = int(i[4])
                    population = int(float(i[8]) * 1000)

                    try:
                        country2 = location.get_code(name)
                        self.countries[country2] = population
                    except:
                        # The names aren't all normalized

                        if name == 'China, Hong Kong SAR':
                            self.countries['HK'] = population
                        elif name == 'China, Macao SAR':
                            self.countries['MO'] = population
                        elif name == 'State of Palestine':
                            self.countries['PS'] = population
                        elif name == 'China, Taiwan Province of China':
                            self.countries['TW'] = population


    def get(self, name):

        if name in self.countries:
            return self.countries[name]
        else:
            return -1

the_countries = Countries()

def get_population(country):

    global the_countries

    return the_countries.get(country)
