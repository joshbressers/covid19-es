
from covid19es import location
from covid19es import population

class Countries:
    def __init__(self):
        self.countries = {}
        self.current = None

    def add(self, name):
        country = Country(name)
        if name in self.countries:
            self.countries[name].append(country)
        else:
            self.countries[name] = [country]
        self.current = country

    def add_province(self, name):

        self.current.add_province(name)

    def add_data(self, day, c, d, r, g):
        self.current.add_data(day, c, d, r, g)

    def get_bulk_country(self):

        results = []

        for key in self.countries:
            for i in self.countries[key]:
                results.append(i.get_bulk_country())

        return results

    def get_bulk_province(self):

        results = []

        for key in self.countries:
            for i in self.countries[key]:
                results.extend(i.get_bulk_province())

        return results

class Province:
    def __init__(self, name):
        self.province = name

    def add_data(self, date, confirmed, deaths, recovered, geo):

        self.day = date
        self.confirmed = confirmed
        self.deaths = deaths
        self.recovered = recovered

        self.location = geo

    def get_bulk(self):

        bulk = {
                "_op_type": "index",
                "_index":   "covid19-province"
               }

        # Only add location data if it exists
        if self.location is not None:
            bulk["location"] = self.location

        bulk["confirmed"] = self.confirmed
        bulk["deaths"] = self.deaths
        bulk["recovered"] = self.recovered
        bulk["province"] = self.province
        bulk["day"] = self.day

        return bulk

class Country:
    def __init__(self, name):

        self.provinces = []

        self.confirmed = 0
        self.deaths = 0
        self.recovered = 0

        self.country2 = location.get_code(name)
        self.country = location.get_country_name(name)
        self.population = population.get_population(self.country2)

    def add_province(self, name):

        self.provinces.append(Province(name))

    def add_data(self, day, confirmed, deaths, recovered, geo):

        if confirmed == '':
            confirmed = 0
        else:
            confirmed = int(confirmed)

        if deaths == '':
            deaths = 0
        else:
            deaths = int(deaths)

        if recovered == '':
            recovered = 0
        else:
            recovered = int(recovered)

        self.confirmed = self.confirmed + int(confirmed)
        self.deaths = self.deaths + int(deaths)
        self.recovered = self.recovered + int(recovered)
        self.day = day

        self.provinces[-1].add_data(day, confirmed, deaths, recovered, geo)

    def get_bulk_country(self):

        bulk = {
                "_op_type": "index",
                "_index":   "covid19-country"
               }

        bulk["confirmed"] = self.confirmed
        bulk["deaths"] = self.deaths
        bulk["recovered"] = self.recovered
        bulk["day"] = self.day
        bulk["country2"] = self.country2
        bulk["country"] = self.country
        bulk["population"] = self.population

        return bulk

    def get_bulk_province(self):

        results = []

        for i in self.provinces:
            r = i.get_bulk()

            r["country2"] = self.country2
            r["country"] = self.country

            results.append(r)

        return results
