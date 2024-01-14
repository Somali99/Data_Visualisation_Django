from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class Gdp(models.Model):
    gdp1980 = models.FloatField(null = False, default = 0)
    gdp1981 = models.FloatField(null = False, default = 0)
    gdp1982 = models.FloatField(null = False, default = 0)
    gdp1983 = models.FloatField(null = False, default = 0)
    gdp1984 = models.FloatField(null = False, default = 0)
    gdp1985 = models.FloatField(null = False, default = 0)
    gdp1986 = models.FloatField(null = False, default = 0)
    gdp1987 = models.FloatField(null = False, default = 0)
    gdp1988 = models.FloatField(null = False, default = 0)
    gdp1989 = models.FloatField(null = False, default = 0)
    gdp1990 = models.FloatField(null = False, default = 0)
    gdp1991 = models.FloatField(null = False, default = 0)
    gdp1992 = models.FloatField(null = False, default = 0)
    gdp1993 = models.FloatField(null = False, default = 0)
    gdp1994 = models.FloatField(null = False, default = 0)
    gdp1995 = models.FloatField(null = False, default = 0)
    gdp1996 = models.FloatField(null = False, default = 0)
    gdp1997 = models.FloatField(null = False, default = 0)
    gdp1998 = models.FloatField(null = False, default = 0)
    gdp1999 = models.FloatField(null = False, default = 0)
    gdp2000 = models.FloatField(null = False, default = 0)
    gdp2001 = models.FloatField(null = False, default = 0)
    gdp2002 = models.FloatField(null = False, default = 0)
    gdp2003 = models.FloatField(null = False, default = 0)
    gdp2004 = models.FloatField(null = False, default = 0)
    gdp2005 = models.FloatField(null = False, default = 0)
    gdp2006 = models.FloatField(null = False, default = 0)
    gdp2007 = models.FloatField(null = False, default = 0)
    gdp2008 = models.FloatField(null = False, default = 0)
    gdp2009 = models.FloatField(null = False, default = 0)
    gdp2010 = models.FloatField(null = False, default = 0)
    gdp2011 = models.FloatField(null = False, default = 0)
    gdp2012 = models.FloatField(null = False, default = 0)
    gdp2013 = models.FloatField(null = False, default = 0)
    gdp2014 = models.FloatField(null = False, default = 0)
    gdp2015 = models.FloatField(null = False, default = 0)
    gdp2016 = models.FloatField(null = False, default = 0)
    gdp2017 = models.FloatField(null = False, default = 0)
    gdp2018 = models.FloatField(null = False, default = 0)
    gdp2019 = models.FloatField(null = False, default = 0)
    gdp2020 = models.FloatField(null = False, default = 0)
    gdp2021 = models.FloatField(null = False, default = 0)
    gdp2022 = models.FloatField(null = False, default = 0)
    gdp2023 = models.FloatField(null = False, default = 0)
    gdp2024 = models.FloatField(null = False, default = 0)
    gdp2025 = models.FloatField(null = False, default = 0)
    gdp2026 = models.FloatField(null = False, default = 0)
    gdp2027 = models.FloatField(null = False, default = 0)
    gdp2028 = models.FloatField(null = False, default = 0)
    
    
class Population(models.Model):
    pop1950 = models.IntegerField(null = False, default = 0)
    pop1951 = models.IntegerField(null = False, default = 0)
    pop1952 = models.IntegerField(null = False, default = 0)
    pop1953 = models.IntegerField(null = False, default = 0)
    pop1954 = models.IntegerField(null = False, default = 0)
    pop1955 = models.IntegerField(null = False, default = 0)
    pop1956 = models.IntegerField(null = False, default = 0)
    pop1957 = models.IntegerField(null = False, default = 0)
    pop1958 = models.IntegerField(null = False, default = 0)
    pop1959 = models.IntegerField(null = False, default = 0)
    pop1960 = models.IntegerField(null = False, default = 0)
    pop1961 = models.IntegerField(null = False, default = 0)
    pop1962 = models.IntegerField(null = False, default = 0)
    pop1963 = models.IntegerField(null = False, default = 0)
    pop1964 = models.IntegerField(null = False, default = 0)
    pop1965 = models.IntegerField(null = False, default = 0)
    pop1966 = models.IntegerField(null = False, default = 0)
    pop1967 = models.IntegerField(null = False, default = 0)
    pop1968 = models.IntegerField(null = False, default = 0)
    pop1969 = models.IntegerField(null = False, default = 0)
    pop1970 = models.IntegerField(null = False, default = 0)
    pop1971 = models.IntegerField(null = False, default = 0)
    pop1972 = models.IntegerField(null = False, default = 0)
    pop1973 = models.IntegerField(null = False, default = 0)
    pop1974 = models.IntegerField(null = False, default = 0)
    pop1975 = models.IntegerField(null = False, default = 0)
    pop1976 = models.IntegerField(null = False, default = 0)
    pop1977 = models.IntegerField(null = False, default = 0)
    pop1978 = models.IntegerField(null = False, default = 0)
    pop1979 = models.IntegerField(null = False, default = 0)
    pop1980 = models.IntegerField(null = False, default = 0)
    pop1981 = models.IntegerField(null = False, default = 0)
    pop1982 = models.IntegerField(null = False, default = 0)
    pop1983 = models.IntegerField(null = False, default = 0)
    pop1984 = models.IntegerField(null = False, default = 0)
    pop1985 = models.IntegerField(null = False, default = 0)
    pop1986 = models.IntegerField(null = False, default = 0)
    pop1987 = models.IntegerField(null = False, default = 0)
    pop1988 = models.IntegerField(null = False, default = 0)
    pop1989 = models.IntegerField(null = False, default = 0)
    pop1990 = models.IntegerField(null = False, default = 0)
    pop1991 = models.IntegerField(null = False, default = 0)
    pop1992 = models.IntegerField(null = False, default = 0)
    pop1993 = models.IntegerField(null = False, default = 0)
    pop1994 = models.IntegerField(null = False, default = 0)
    pop1995 = models.IntegerField(null = False, default = 0)
    pop1996 = models.IntegerField(null = False, default = 0)
    pop1997 = models.IntegerField(null = False, default = 0)
    pop1998 = models.IntegerField(null = False, default = 0)
    pop1999 = models.IntegerField(null = False, default = 0)
    pop2000 = models.IntegerField(null = False, default = 0)
    pop2001 = models.IntegerField(null = False, default = 0)
    pop2002 = models.IntegerField(null = False, default = 0)
    pop2003 = models.IntegerField(null = False, default = 0)
    pop2004 = models.IntegerField(null = False, default = 0)
    pop2005 = models.IntegerField(null = False, default = 0)
    pop2006 = models.IntegerField(null = False, default = 0)
    pop2007 = models.IntegerField(null = False, default = 0)
    pop2008 = models.IntegerField(null = False, default = 0)
    pop2009 = models.IntegerField(null = False, default = 0)
    pop2010 = models.IntegerField(null = False, default = 0)
    pop2011 = models.IntegerField(null = False, default = 0)
    pop2012 = models.IntegerField(null = False, default = 0)
    pop2013 = models.IntegerField(null = False, default = 0)
    pop2014 = models.IntegerField(null = False, default = 0)
    pop2015 = models.IntegerField(null = False, default = 0)
    pop2016 = models.IntegerField(null = False, default = 0)
    pop2017 = models.IntegerField(null = False, default = 0)
    pop2018 = models.IntegerField(null = False, default = 0)
    pop2019 = models.IntegerField(null = False, default = 0)
    pop2020 = models.IntegerField(null = False, default = 0)
    pop2021 = models.IntegerField(null = False, default = 0)
    pop2022 = models.IntegerField(null = False, default = 0)
    pop2023 = models.IntegerField(null = False, default = 0)


class Country(models.Model):
    name = models.CharField(max_length = 45, null = False, default = "Not Available")
    pop = models.ForeignKey(Population, on_delete=models.CASCADE, null = True)
    gdp = models.ForeignKey(Gdp, on_delete=models.CASCADE, null = True)
    population = models.FloatField(null = True, default = 0)
    yearly_change = models.FloatField(null = True, default = 0)
    net_change = models.FloatField(null = True, default = 0)
    density = models.FloatField(null = True, default = 0)
    land_area = models.FloatField(null = True, default = 0)
    net_migrants = models.FloatField(null = True, default = 0)
    fertility_rate = models.FloatField(null = True, default = 0)
    median_age = models.FloatField(null = True, default = 0)
    population_urban = models.FloatField(null = True, default = 0)
    world_share = models.FloatField(null = True, default = 0)

    def __str__(self):
        return self.name
    
    @classmethod
    def clear_data_and_import(cls)->int:
        """Clears data instances and imports from a file.
        Returns:
            int: 0 for Success, other values are errors handled.
        """
        
        #removing data to start again
        cls.objects.all().delete()
        Gdp.objects.all().delete()
        Population.objects.all().delete()
        
        # Read gdp data from 1950 to 2028 (5 years of predictions) 
        try:
            with open(file= "/home/amnesia2/Documents/Django/Data_Visualisation/data/population/world_population_2023.csv", mode='r', encoding='utf-8-sig') as f1:#  this file url is made for production not distribution
                for line in f1:
                    try:
                        country = Country()
                        country.name, country.population, country.yearly_change, country.net_change, country.density, country.land_area, country.net_migrants, country.fertility_rate, country.median_age, country.population_urban, country.world_share= line.strip().split(',')
                        country.save()
                    except ValueError:
                        return 8
                f1.close()
        except FileNotFoundError:
            return 7
        
        # Read population details file in 2023
        try:
            with open(file= "/home/amnesia2/Documents/Django/Data_Visualisation/data/population/gdp.csv", mode='r', encoding='utf-8-sig') as f2:#  this file url is made for production not distribution
                for line in f2:
                    gdp = Gdp()
                    try:
                        # Parse the line and create a new gdp instance
                        name, gdp.gdp1980, gdp.gdp1981, gdp.gdp1982, gdp.gdp1983, gdp.gdp1984, gdp.gdp1985, gdp.gdp1986, gdp.gdp1987, gdp.gdp1988, gdp.gdp1989, gdp.gdp1990, gdp.gdp1991, gdp.gdp1992, gdp.gdp1993, gdp.gdp1994, gdp.gdp1995, gdp.gdp1996, gdp.gdp1997, gdp.gdp1998, gdp.gdp1999, gdp.gdp2000, gdp.gdp2001, gdp.gdp2002, gdp.gdp2003, gdp.gdp2004, gdp.gdp2005, gdp.gdp2006, gdp.gdp2007, gdp.gdp2008, gdp.gdp2009, gdp.gdp2010, gdp.gdp2011, gdp.gdp2012, gdp.gdp2013, gdp.gdp2014, gdp.gdp2015, gdp.gdp2016, gdp.gdp2017, gdp.gdp2018, gdp.gdp2019, gdp.gdp2020, gdp.gdp2021, gdp.gdp2022, gdp.gdp2023, gdp.gdp2024, gdp.gdp2025, gdp.gdp2026, gdp.gdp2027, gdp.gdp2028 = line.strip().split(',')
                        gdp.save()
                        try:
                            country = Country.objects.get(name = name)
                        except ObjectDoesNotExist:
                            return 6
                        country.gdp = gdp
                        country.save()
                    except ValueError:
                        return 5
                f2.close()
        except FileNotFoundError:
            return 4
        # Read population evolution file from 1950 2023
        try:
            with open(file= "/home/amnesia2/Documents/Django/Data_Visualisation/data/population/world_population_1950_2023.csv", mode='r', encoding='utf-8-sig') as f3:# this file url is made for production not distribution
                for line in f3:
                    pop = Population()
                    try:
                        # Parse the line and create a new population instance 
                        name, pop.pop1950, pop.pop1951, pop.pop1952, pop.pop1953, pop.pop1954, pop.pop1955, pop.pop1956, pop.pop1957, pop.pop1958, pop.pop1959, pop.pop1960, pop.pop1961, pop.pop1962, pop.pop1963, pop.pop1964, pop.pop1965, pop.pop1966, pop.pop1967, pop.pop1968, pop.pop1969, pop.pop1970, pop.pop1971, pop.pop1972, pop.pop1973, pop.pop1974, pop.pop1975, pop.pop1976, pop.pop1977, pop.pop1978, pop.pop1979, pop.pop1980, pop.pop1981, pop.pop1982, pop.pop1983, pop.pop1984, pop.pop1985, pop.pop1986, pop.pop1987, pop.pop1988, pop.pop1989, pop.pop1990, pop.pop1991, pop.pop1992, pop.pop1993, pop.pop1994, pop.pop1995, pop.pop1996, pop.pop1997, pop.pop1998, pop.pop1999, pop.pop2000, pop.pop2001, pop.pop2002, pop.pop2003, pop.pop2004, pop.pop2005, pop.pop2006, pop.pop2007, pop.pop2008, pop.pop2009, pop.pop2010, pop.pop2011, pop.pop2012, pop.pop2013, pop.pop2014, pop.pop2015, pop.pop2016, pop.pop2017, pop.pop2018, pop.pop2019, pop.pop2020, pop.pop2021, pop.pop2022, pop.pop2023 = line.strip().split(',')
                        pop.save()
                        try:
                            country = Country.objects.get(name = name)
                        except ObjectDoesNotExist:
                            print(name)
                            return 3
                        country.pop = pop
                        country.save()
                    except ValueError:
                        return 2
                f3.close()
        except FileNotFoundError:
            return 1
        return 0 # success


class Region(models.Model):
    name = models.CharField(max_length = 45, null = False, default = "Not Available")
    gdp = models.ForeignKey(Gdp, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.name
    
    @classmethod
    def clear_data_and_import(cls)->int:
        """Clears data instances and imports from a file.
        Returns:
            int: 0 for Success, other values are errors handled.
        """
        
        #removing data to start again
        cls.objects.all().delete()
        
        # Read gdp data from 1950 to 2028 (5 years of predictions) 
        try:
            with open(file= "/home/amnesia2/Documents/Django/Data_Visualisation/data/population/regional_gdp.csv", mode='r', encoding='utf-8-sig') as f:#  this file url is made for production not distribution
                for line in f:
                    region = Region()
                    gdp = Gdp()
                    try:
                        # Parse the line and create a new gdp instance
                        region.name, gdp.gdp1980, gdp.gdp1981, gdp.gdp1982, gdp.gdp1983, gdp.gdp1984, gdp.gdp1985, gdp.gdp1986, gdp.gdp1987, gdp.gdp1988, gdp.gdp1989, gdp.gdp1990, gdp.gdp1991, gdp.gdp1992, gdp.gdp1993, gdp.gdp1994, gdp.gdp1995, gdp.gdp1996, gdp.gdp1997, gdp.gdp1998, gdp.gdp1999, gdp.gdp2000, gdp.gdp2001, gdp.gdp2002, gdp.gdp2003, gdp.gdp2004, gdp.gdp2005, gdp.gdp2006, gdp.gdp2007, gdp.gdp2008, gdp.gdp2009, gdp.gdp2010, gdp.gdp2011, gdp.gdp2012, gdp.gdp2013, gdp.gdp2014, gdp.gdp2015, gdp.gdp2016, gdp.gdp2017, gdp.gdp2018, gdp.gdp2019, gdp.gdp2020, gdp.gdp2021, gdp.gdp2022, gdp.gdp2023, gdp.gdp2024, gdp.gdp2025, gdp.gdp2026, gdp.gdp2027, gdp.gdp2028 = line.strip().split(',')
                        gdp.save()
                        region.gdp = gdp
                        region.save()
                    except ValueError:
                        return -2
                f.close()
        except FileNotFoundError:
            return -1
        return 0
    