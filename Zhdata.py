from bs4 import BeautifulSoup
from ZhURL import get_one_page
import re


def get_data(index):
    html = get_one_page(index)

    soup = BeautifulSoup(html, 'html.parser')

    div_all_book = soup.find_all('div', attrs={'class': 'rank_d_list borderB_c_dsh clearfix'})
    return div_all_book


def get_name(index, id):
    all_book = get_data(index)
    all = all_book[id].select('.rank_d_b_name')
    for name in all:
        name = re.sub('\s+', " ", name.get_text())
        return name


def get_reader(index, id):
    all_book = get_data(index)
    all = all_book[id].select('.rank_d_b_cate')
    for reader in all:
        autor = re.split('\\|', reader.get_text())
        autor1 = re.sub('\s+', " ", autor[0])
        return autor1


def get_info(index, id):
    all_book = get_data(index)
    all = all_book[id].select('.rank_d_b_info')
    for info in all:
        return info.get_text()


def get_last(index, id):
    all_book = get_data(index)
    all = all_book[id].select('.rank_d_b_last')
    for last in all:
        name = re.split('\n', last.get_text())
        return name[1]


def get_ticket(index, id):
    all_book = get_data(index)
    all = all_book[id].select('.rank_d_b_ticket')
    for ticket in all:
        return ticket.get_text()


def get_type(index, id):
    all_book = get_data(index)
    all = all_book[id].select('.rank_d_b_cate')
    for reader in all:
        type = re.split('\\|', reader.get_text())
        return type[1]


def get_status(index, id):
    all_book = get_data(index)
    all = all_book[id].select('.rank_d_b_cate')
    for reader in all:
        status = re.split('\\|', reader.get_text())
        return status[2]


def get_time(index, id):
    all_book = get_data(index)
    all = all_book[id].select('.rank_d_b_last')
    for last in all:
        time = re.split('\n', last.get_text())
        return time[2]


if __name__ == '__main__':
    print(get_name(0, 0))

