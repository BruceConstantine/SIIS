import time
import requests
from functools import wraps
from bs4 import BeautifulSoup
from app import db
from app.models import Student, Score, Major, Class, Course


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

    # print(response.text)

    return response


@cal_run_time
def parse(response, year):
    soup = BeautifulSoup(response.text, "html5lib")
    td = soup.find_all("td", {"scope": "col", "valign": "middle"})
    td_length = len(td)
    n, i = 0, 1
    while n < td_length:
        stu_number = td[n + 1].get_text().strip()
        stu = Student.query.filter_by(number=stu_number).first()
        print('stu obj is ',stu)
        if stu is not None or stu_number[0:4] != year:
            print('continue')
            n += 14
            continue
        # print(stu_number, '---  ', stu)
        stu_name = td[n + 2].get_text().strip()
        stu_sex = td[n + 3].get_text().strip()
        stu_grade = td[n + 4].get_text().strip()
        stu_major = td[n + 6].get_text().strip()
        stu_class = td[n + 7].get_text().strip()
        stu_level = td[n + 9].get_text().strip()
        stu_length_of_schooling = td[n + 10].get_text().strip()
        print("第%d次循环" % i)
        print(stu_number, stu_name, stu_sex, stu_grade, stu_major, stu_class, stu_level, stu_length_of_schooling)
        marjor = Major.query.filter_by(name=stu_major).first()
        class_ = Class.query.filter_by(name=stu_major).first()
        # 判断marjor和class之前存在与否
        if marjor is None:
            try:
                marjor = Major(name=stu_major)
                db.session.add(marjor)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print("There is an error %r" % e)
                break
        if class_ is None:
            try:
                class_ = Class(name=stu_class)
                db.session.add(class_)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                print("There is an error %r" % e)
                break
        print('##--> marjor', marjor.id)
        print('##--> class_', class_.id)
        student = Student(
            number=stu_number,
            name=stu_name,
            sex=stu_sex,
            grade=stu_grade,
            marjor_id=marjor.id,
            class_id=class_.id,
            level=stu_level,
            length_of_schooling=stu_length_of_schooling
        )
        try:
            db.session.add(student)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("There is an error %r" % e)
            break
        i, n = i + 1, n + 14


def test():
    marjor = Major.query.filter_by(name='test').first()
    print(marjor)
    if not marjor:
        print('OK')
    else:
        print('Not OK')


if __name__ == '__main__':
    test()
    # parse(splider('1411'))
