"""
File: webcrawler.py
Name: Tracy Lee
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male number: 10895302
Female number: 7942376
---------------------------
2000s
Male number: 12976700
Female number: 9208284
---------------------------
1990s
Male number: 14145953
Female number: 10644323
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'
        
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        male_total = 0
        female_total = 0
        male_num_str = ""
        female_num_str = ""
        table = soup.find('tbody')
        tr_tags = table.find_all("tr")
        for tr_tag in tr_tags:
            if tr_tag.find("td",{"colspan":"4"}):
                break
            tds = tr_tag.find_all('td')
            male_str = tds[2].text
            for male_num in male_str:
                if male_num == ",":
                    pass
                else:
                    male_num_str += male_num
            male_total += int(male_num_str)
            male_num_str = ''

            female_str = tds[4].text
            for female_num in female_str:
                if female_num == ",":
                    pass
                else:
                    female_num_str += female_num
            female_total += int(female_num_str)
            female_num_str = ''
        print("Male Number: " + str(male_total))
        print("Female Number: " + str(female_total))


if __name__ == '__main__':
    main()
