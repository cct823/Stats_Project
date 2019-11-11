import pandas as pd
from urllib.request import urlopen
from bs4 import BeautifulSoup


def city_link():
    city_state = []
    '''get the city and state column'''
    school_info = pd.read_csv('rschool_info.csv')
    # select 5 for test
    city = list(school_info['city'])
    state = list(school_info['state'])

    '''replace the  ' ' in the city name to '+' because the link need it.'''
    for i in range(len(city)):
        city[i] = city[i].lower().replace(' ', '+')

    '''combine the city and state for link use.'''
    # if len(city) == len(state):
    for i in range(len(city)):
        city_state.append(city[i] + '-' + state[i].lower())

    '''remove duplicate in the list, cuz schools may in the same city.'''
    city_state=list(set(city_state))
    print(len(city_state))

    city_list = []
    # why if i put city_d = {} outside the loop, the data will be all the same?

    '''get the city name, link, then save as dictionary.
       Then add it to the list, return the list. '''

    for item in city_state:
        city_d = {}
        name = item.split('-')[0].replace('+', ' ').title()
        link = 'https://www.areavibes.com/' + item + '/livability/'
        city_d['city_name'] = name
        city_d['link'] = link

        city_list.append(city_d)

    return city_list

# {'city_name': 'Swarthmore', 'link': 'https://www.areavibes.com/swarthmore-pa/livability/'}

def city_data(city_list):
    DictList = []
    fail_link = []
    for city in city_list:
        # print(city)
        city_dic = {}
        name = city['city_name']
        url = city['link']
        city_dic['Name'] = name
        city_dic['Link'] = url
        try:
            html = urlopen(url)
        except:
            fail_link.append(str(url))
            continue
        soup = BeautifulSoup(html, "lxml")

        '''First Section: Livability scores, 8 elements'''
        Livability = soup.findAll('nav', {'category-menu'}) # the class has all elements
        for items in Livability:
            item = items.findAll('a')  # find all a to get the different categories
            for elements in item: # in each categories, get the name and score
                # element = elements['href']
                type = elements.find('em').getText()
                score = elements.find('i').getText()
                city_dic[type] = score  # add everything to the dictionary


            '''Second Section: Population and median home value'''
            '''This is searching from all span, how can i search the span under line 75'''
            '''line 75 not soup.findall, should be scorehero.find'''
            # scorehero = soup.findAll('div', {'score-hero-info'})
            # for items in scorehero:
            item = soup.findAll('span')
            pop = item[1].getText().split(':')[0]
            pop_num = item[1].getText().split(':')[1]

            median = item[2].getText().split(':')[0]
            median_num = item[2].getText().split(':')[1]
            # ranking = item[3].getText().split(' ').rstrip()  #  too many spaces w
            city_dic[pop] = pop_num
            city_dic[median] = median_num
            # city_dic['Rank'] = ranking

            '''Third Section: Real Estate Listings doesn't work?'''


            '''Fourth Section: Cost of living'''
            '''Add the comment after the ranking from first section, because the dictionary name will be the same when
            removing the city name Swarthmore Cost of Living -> Cost of Living'''

            living = soup.findAll('div', {'liv-header'})
            for infos in living:
                living_cate = infos.find('strong').getText()
                living_num = infos.find('small').getText()
                living_cate = living_cate.replace( name + ' ','').replace(' ','_')+'_Info'
                if living_cate == 'Amenities_Info':  # I don't want this, useless description in excel.
                    continue
                city_dic[living_cate] = living_num



        DictList.append(city_dic)
        # print(city_dic)
        # break

    # print(len(list))
    # print(fail_link)
    return DictList


city_list = city_link()
city_data = city_data(city_list)
column_name = ['Name', 'Link', 'Livability', 'Amenities', 'Cost of Living', 'Crime', 'Employment', 'Housing', 'Schools',
               'Weather', 'Population', 'Median home value', 'Cost_of_Living_Info', 'Crime_Info', 'Employment_Info',
               'Housing_Info', 'Schools_Info']

table = pd.DataFrame(city_data, columns=column_name)
print(table)
table.to_csv('city_info.csv')