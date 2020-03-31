#!/usr/bin/env python

import iso3166

def get_country_name(country_name):

    country2 = get_code(country_name)
    if country2 == '':
        return ''
    else:
        return iso3166.countries_by_alpha2[country2].name

def get_code(country_name):

    # This will be the code we return
    code = ''

    # first we capitalize
    cu = country_name.upper()

    # Then we see if it's in the library
    if cu in iso3166.countries_by_name:
        code = iso3166.countries_by_name[cu].alpha2
    else:

        if cu == 'CHANNEL ISLANDS':
            code = 'GB'
        elif cu == 'SAINT MARTIN':
            code = 'SX'
        elif cu == 'MAINLAND CHINA':
            code = 'CN'
        elif cu == 'SOUTH KOREA':
            code = 'CR'
        elif cu == 'TAIWAN':
            code = 'TW'
        elif cu == 'MACAU':
            code = 'MO'
        elif cu == 'VIETNAM':
            code = 'VN'
        elif cu == 'RUSSIA':
            code = 'RU'
        elif cu == 'UK':
            code = 'GB';
        elif cu == 'US':
            code = 'US'
        elif cu == 'IRAN':
            code = 'IR'
        elif cu == 'OTHERS':
            # These are cruise ships
            code = ''
        elif cu == 'CRUISE SHIP':
            code = ''
        elif cu == 'DIAMOND PRINCESS':
            code = ''
        elif cu == 'MS ZAANDAM':
            code = ''
        elif cu == 'CZECH REPUBLIC':
            code = 'CZ'
        elif cu == 'PALESTINE':
            code = 'PS'
        elif cu == 'WEST BANK AND GAZA':
            code = 'PS'
        elif cu == 'ST. MARTIN':
            code = 'MF'
        elif cu == 'BRUNEI':
            code = 'BN'
        elif cu == 'MOLDOVA':
            code = 'MD'
        elif cu == 'SAINT BARTHELEMY':
            code = 'BL'
        elif cu == 'VATICAN CITY':
            code = 'VA'
        elif cu == 'KOREA, SOUTH':
            code = 'KR'
        elif cu == 'UNITED KINGDOM':
            code = 'GB'
        elif cu == 'TAIWAN*':
            code = 'TW'
        elif cu == 'BOLIVIA':
            code = 'BO'
        elif cu == 'CONGO (KINSHASA)':
            code = 'CG'
        elif cu == 'REPUBLIC OF THE CONGO':
            code = 'CG'
        elif cu == 'COTE D\'IVOIRE':
            code = 'CI'
        elif cu == 'REUNION':
            code = 'RE'
        elif cu == 'OCCUPIED PALESTINIAN TERRITORY':
            code = 'PS'
        elif cu == 'IVORY COAST':
            code = 'CI'
        elif cu == 'VENEZUELA':
            code = 'VE'
        elif cu == 'CURACAO':
            code = 'CW'
        elif cu == 'REPUBLIC OF IRELAND':
            code = 'IE'
        elif cu == 'CONGO (BRAZZAVILLE)':
            code = 'CG'
        elif cu == ' AZERBAIJAN':
            code = 'AZ'
        elif cu == 'NORTH IRELAND':
            code = 'GB'
        elif cu == 'IRAN (ISLAMIC REPUBLIC OF)':
            code = 'IR'
        elif cu == 'REPUBLIC OF KOREA':
            code = 'KR'
        elif cu == 'HONG KONG SAR':
            code = 'HK'
        elif cu == 'TAIPEI AND ENVIRONS':
            code = 'TW'
        elif cu == 'MACAO SAR':
            code = 'MO'
        elif cu == 'REPUBLIC OF MOLDOVA':
            code = 'MD'
        elif cu == 'TANZANIA':
            code = 'TZ'
        elif cu == 'THE BAHAMAS':
            code = 'BS'
        elif cu == 'BAHAMAS, THE':
            code = 'BS'
        elif cu == 'THE GAMBIA':
            code = 'GM'
        elif cu == 'GAMBIA, THE':
            code = 'GM'
        elif cu == 'CAPE VERDE':
            code = 'CV'
        elif cu == 'EAST TIMOR':
            code = 'TL'
        elif cu == 'SYRIA':
            code = 'SY'
        elif cu == 'LAOS':
            code = 'LA'
        elif cu == 'BURMA':
            code = 'MM'
        else:
            raise NameError("\'%s\'" % cu)

    return code
