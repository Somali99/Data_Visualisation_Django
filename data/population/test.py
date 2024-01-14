list_population = []
def read_population_file():
    global list_population
    with open(file="/home/amnesia2/Documents/Django/Data_Visualisation/data/population/world_population_2023.csv", mode='r', encoding='utf-8-sig') as f:
        for line in f:
            country = {}
            country['name'], country['population'], country['yearly_change'], country['net_change'], country['density'], country['land_area'], country['net_migrants'], country['fertility_rate'], country['median_age'], country['population_urban'], country['world_share'] = line.strip().split(',')
            list_population.append(country)
list_gdp = []
def read_gdp_file():
    global list_gdp
    with open(file="/home/amnesia2/Documents/Django/Data_Visualisation/data/population/gdp.csv", mode='r', encoding='utf-8-sig') as f:
        for line in f:
            country = {}
            country['name'], country['gdp1980'], country['gdp1981'], country['gdp1982'], country['gdp1983'], country['gdp1984'], country['gdp1985'], country['gdp1986'], country['gdp1987'], country['gdp1988'], country['gdp1989'], country['gdp1990'], country['gdp1991'], country['gdp1992'], country['gdp1993'], country['gdp1994'], country['gdp1995'], country['gdp1996'], country['gdp1997'], country['gdp1998'], country['gdp1999'], country['gdp2000'], country['gdp2001'], country['gdp2002'], country['gdp2003'], country['gdp2004'], country['gdp2005'], country['gdp2006'], country['gdp2007'], country['gdp2008'], country['gdp2009'], country['gdp2010'], country['gdp2011'], country['gdp2012'], country['gdp2013'], country['gdp2014'], country['gdp2015'], country['gdp2016'], country['gdp2017'], country['gdp2018'], country['gdp2019'], country['gdp2020'], country['gdp2021'], country['gdp2022'], country['gdp2023'], country['gdp2024'], country['gdp2025'], country['gdp2026'], country['gdp2027'], country['gdp2028'] = line.strip().split(',')
            list_gdp.append(country)
joined_list = []
def join():
    global list_gdp, list_population, joined_list
    joined_list = [d['name'] for d in list_population if any(d['name'] == g['name'] for g in list_gdp)]

def main():
    read_population_file()
    read_gdp_file()
    join()
    print(len(joined_list))

if __name__ == '__main__':
    main()
