from bs4 import BeautifulSoup
from MyURL import get_one_page
import re


def get_data(index):
    html = get_one_page(index)

    soup = BeautifulSoup(html, 'html.parser')

    div_all_movie = soup.select('.board-wrapper dd')
    return div_all_movie


def get_name(index, id):
    all_movie = get_data(index)
    all = all_movie[id].find('a', attrs={'class': 'image-link'})
    return all.get('title')


def get_star(index, id):
    all_movie = get_data(index)
    all = all_movie[id].find('p', attrs={'class': 'star'})
    mo = r'[\u4e00-\u9fa5]+'
    star = re.findall(mo, all.get_text())
    star1 = ''
    for i in range(0, len(star)):
        star1 = star1 + str(star[i])
    return star1


def get_time(index, id):
    all_movie = get_data(index)
    all = all_movie[id].find('p', attrs={'class': 'releasetime'})
    time = all.get_text()
    regx = '^.*?：([0-9-]+).*'
    res = re.match(regx, time)
    return res.group(1)


def get_country(index, id):
    all_movie = get_data(index)
    all = all_movie[id].find('p', attrs={'class': 'releasetime'})
    country = all.get_text()
    regx = '^.*?\((.*)\)'
    res = re.match(regx, country)
    if res:
        return res.group(1)


def get_score(index, id):
    all_movie = get_data(index)
    all = all_movie[id].find('p', attrs={'class': 'score'})
    i_int = all.find('i', attrs={'class': 'integer'})
    i_fra = all.find('i', attrs={'class': 'fraction'})
    score = i_int.get_text() + i_fra.get_text()
    return float(score)


if __name__ == '__main__':
    print(get_star(0, 0))

