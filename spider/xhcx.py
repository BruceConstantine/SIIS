import time
import requests
from functools import wraps
from bs4 import BeautifulSoup
from app import db


def cal_run_time(func):
    """
    计算函数体运行时间
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("函数运行时间： ", end - start)
        return result

    return wrapper


@cal_run_time
def splider(stu_num):
    xhcx_url = 'http://210.44.176.116/cjcx/xhcx_list.php'  # 进行学号查询要登录的url
    post_data = {
        'post_xingming': '',
        'post_xuehao': '%s' % stu_num,
        'Submit': '提交'
    }

    response = requests.post(
        url=xhcx_url,
        data=post_data,
    )

    return response


# /html/body/table/tbody/tr[1]/td/table/tbody/tr

@cal_run_time
def parse(response):
    soup = BeautifulSoup(response.text, "html5lib")
    # print(soup)
    # return soup
    td = soup.find_all("td", {"scope": "col", "valign": "middle"})
    print(len(td))


if __name__ == '__main__':
    parse(splider('1411'))
