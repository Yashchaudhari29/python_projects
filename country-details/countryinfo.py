
from countryinfo import CountryInfo
name= input("Enter name of the country : ")

country= CountryInfo(name)
country_name= country.alt_spellings()
print(country_name)

#for printing the capital of country

capital=country.capital()
print(capital)

#for printing currency of country

currency=country.currencies()
print(currency)

#for printing language of country

lang=country.languages()
print(lang)

#for printing timezone of country

t_zone= country.timezones()
print(t_zone)

#for printing area of country

c_area=country.area()
print(c_area,"kilometer per square")

#for printing the border nations of country

c_border = country.borders()
print(c_border)

#for printing the calling code of country

c_call= country.calling_codes()
print(c_call)

#to print the wikipedia link of any coutry

c_wiki=country.wiki()
print(c_wiki)

# to print the populations of the country

c_pop=country.population()
print(c_pop)

# for printing whole country details

c_info=country.info()
for x,y in c_info.items():
    print(f'{x} --> {y}')
