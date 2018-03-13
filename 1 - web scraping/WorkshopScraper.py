import requests
from bs4 import BeautifulSoup
import csv, time

# set your start date and end date in format YYYY/M/D
startDate = "2017/1/1"
endDate = "2017/12/31"

# define function to use later in the while loop
def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""

# initial GET request
url = "https://www.wunderground.com/history/airport/WSAP/"+startDate+"/DailyHistory.html"
response = requests.get(url)
content = response.content

# convert contents to nested data structure
soup = BeautifulSoup(content, "lxml")

with open("WeatherScrape4.csv", "w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['Date', 'Mean Temp (C)', 'Max Temp (C)', 'Min Temp (C)', 'Precipitation (in)', 'Wind Speed (m/s)'])

    endDate = time.strptime(endDate, "%Y/%m/%d")
    date = time.strptime(startDate, "%Y/%m/%d")
    dateString = startDate

    while date <= endDate:
        print(dateString)

        # parse HTML
        meantemp = soup.find_all('tr')[2].find_all('td')[1].find_all(attrs={"class":"wx-value"})[0].text
        maxtemp = soup.find_all('tr')[3].find_all('td')[1].find_all(attrs={"class":"wx-value"})[0].text
        mintemp = soup.find_all('tr')[4].find_all('td')[1].find_all(attrs={"class":"wx-value"})[0].text
        precip = soup.find_all('tr')[13].find_all('td')[1].find_all(attrs={"class":"wx-value"})[0].text
        wind = soup.find_all('tr')[17].find_all('td')[1].find_all(attrs={"class":"wx-value"})[0].text

        # write resutls
        csv_writer.writerow([dateString, meantemp, maxtemp, mintemp, precip, wind])

        # find next link
        nextlink = soup.find('div', attrs={'class':'daily-history-select'}).find_all('a')[1].get('href')
        url = 'https://www.wunderground.com'+nextlink

        # GET request next link
        response = requests.get(url)
        content = response.content
        soup = BeautifulSoup(content, "lxml")

        # update date
        first = "/history/airport/WSAP/"
        last = "/DailyHistory.html"
        dateString = find_between(nextlink, first, last)
        date = time.strptime(dateString, "%Y/%m/%d")

print("Scrape complete!")
