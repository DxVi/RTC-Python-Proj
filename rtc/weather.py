#libraries beautiful soup and requests
# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
 

def weather_scrape():
    #ok
    # page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.05361000000005&lon=-118.24549999999999#.XwJ6mm0zZEY')
 
    # soup = BeautifulSoup(page.content, 'html.parser')
    # week = soup.find(id='seven-day-forecast-body')

    # items = week.find_all(class_ = 'tombstone-container')
#-----------------------------------------
    # print('-----start------------')                                
    #print(items[0])

    #print(items[0].find(class_ = 'period-name').get_text())
    #print(items[0].find(class_ = 'short-desc').get_text())
    #x = items[0].find(class_ = 'temp')  
    #print(x)
    #if (x == None):
    #  print('high surf advisory')
    #print(items[0].find(class_ = 'temp'))
    #.get_text())
#-----------------------------------------
    #ok
    # period_names = [item.find(class_ = 'period-name').get_text() for item in items if item.find(class_ = 'temp') != None]
    # short_descs = [item.find(class_ = 'short-desc').get_text() for item in items if item.find(class_ = 'temp') != None]
    # temps = [item.find(class_ = 'temp').get_text() for item in items if item.find(class_ = 'temp') != None]
#-----------------------------------------
    #print(period_names)
    #print(short_descs)
    #print(temps)
#-----------------------------------------
    #ok
    # weather_stuff = pd.DataFrame(
    # {'period':period_names,
    # 'short_descs':short_descs,
    # 'temps':temps,
    # })

    # print(weather_stuff)
    # print('---------------end----')

    textvar="weather.py => Hello from weather_scrape function"
    return textvar