from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


def uni_link():
    school_list = []
    for num in range(1, 21):
        link = 'https://www.niche.com/colleges/search/best-colleges/?page=' + str(num)
        html = urlopen(link)
        soup = BeautifulSoup(html, "lxml")
        schools = soup.findAll('a', {'search-result__link'})
        for school in schools:
            school_d = {}
            if len(school) == 2:
                school_name = school.find('h2', {'search-result__title'}).getText()
                school_link = school['href']
                school_d['name'] = school_name
                school_d['link'] = school_link
            school_list.append(school_d)
    return school_list


def uni_table(school_list):
    list = []
    for school in school_list:
        school_dic = {}
        name = school['name']
        url = school['link']
        school_dic['name'] = name
        school_dic['link'] = url
        html = urlopen(url)
        soup = BeautifulSoup(html, "lxml")
        score_lists = soup.findAll('ol', {'ordered__list__bucket'})
        for score_list in score_lists:
            scores = score_list.findAll('li', {'ordered__list__bucket__item'})
            for score in scores:
                item = score.find('div', {'profile-grade__label'}).getText().replace(" ", "_")
                value = score.find('div', {'niche__grade'}).getText()
                # header.append(item)
                school_dic[item] = value
        try:
            description = soup.find('span', {'bare-value'}).getText()
            school_dic['des'] = description
        except:
            school_dic['des'] = ''

        address = soup.find('div', {'profile__address'})
        address_list = address.findAll('div')
        address_str = address_list[2].getText()
        address_city = address_list[3].getText().split(', ')[0]
        address_state = address_list[3].getText().split(', ')[1].split(' ')[0]
        address_zip = address_list[3].getText().split(', ')[1].split(' ')[1]
        school_dic['street'] = address_str
        school_dic['city'] = address_city
        school_dic['state'] = address_state
        school_dic['zip'] = address_zip

        admission = soup.find(id='admissions')
        rates = admission.findAll('span')
        rate_list = []
        for rate in rates:
            rate_list.append(rate.getText())
        accept_rate_index = rate_list.index("Acceptance Rate")
        sat_index = rate_list.index("SAT Range")
        ACT_index = rate_list.index("ACT Range")
        fee_index = rate_list.index("Application Fee")
        school_dic['Accept_Rate'] = rate_list[accept_rate_index+1]
        school_dic['SAT'] = rate_list[sat_index+1]
        school_dic['ACT'] = rate_list[ACT_index+1]
        school_dic['Application_fee'] = rate_list[fee_index+1]

        cost = soup.find(id='cost')
        try:
            price = cost.find('div', {'scalar__value'}).find('span').getText()
            school_dic['Price_per_year'] = price
        except:
            school_dic['Price_per_year'] = ''

        major_div = soup.find(id='majors')
        majors = major_div.find('ul', {'popular-entities-list'}).findAll('li')
        major_rank = ""
        for major in majors:
            major_name = major.find('h6').getText()
            major_rank += major_name + '; '
        school_dic['major_rank'] = major_rank
        # header.append('major_rank')
        # print(header)
        list.append(school_dic)
        print(school_dic)
    return list


school_list = uni_link()
school_list_clean = list(filter(None,school_list))
print(school_list_clean)

list = uni_table(school_list_clean)
header = ['name', 'link', 'Academics', 'Value', 'Diversity', 'Campus', 'Athletics', 'Party_Scene', 'Professors',
          'Location', 'Dorms', 'Campus_Food', 'Student_Life', 'Safety', 'des', 'street', 'city', 'state', 'zip', 'Accept_Rate',
          'SAT', 'ACT', 'Application_fee', 'Price_per_year', 'major_rank']
table = pd.DataFrame(list, columns=header)

print(table)
table.to_csv('school_info.csv',index=None)
