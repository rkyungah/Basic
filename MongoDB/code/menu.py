import conn
import datsearch as ds
import datinsert as ins


def dbInfo():
    print(conn.conn.database_names())   # DB이름 확인
    dbs = conn.conn.database_names()
    db_con = conn.conn

    print("DB의 collection들 확인")
    for one_db in dbs:
        db = conn.conn[one_db]   # db하나 선택
        print(db.collection_names())
        db_c = db.collection_names()
        for one_col in db_c:
            print("collection 들의 데이터 수 : {}".format(one_col))
            datcnt = db[one_col].count()
            print(datcnt)

### DB을 작업을 위해 메뉴 구현.
def menuPrint():
    print("DB정보(0), 검색(1), 삭제(2), 삽입(3), 변경(4) 선택해 주세요.")
    print("CSV 추가(5)", "확인(6)", "extra CSV 추가(7)")
    sel = int(input())
    return sel

from sklearn.datasets import load_iris
from pymongo import MongoClient


def irisinsert():
    iris_df = load_iris()
    client = MongoClient()

    irisdb = client.iris  # iris DB생성.
    # collection = irisdb['iriscol']  # collection 생성
    # irisdb.iriscol.drop()  # 먼저 지우기
    iris_col = irisdb.iriscol

    len_iris = iris_df.data.shape[0]  # iris데이터셋의 행의 수
    for i in range(0, (len_iris - 1)):
        data = {
            'id_': i,
            'sepallength': iris_df.data[i, 0],
            'sepalwidth': iris_df.data[i, 1],
            'petallength': iris_df.data[i, 2],
            'petalwidth': iris_df.data[i, 3],
            'species': i
        }
        iris_col.insert_one(data)


def irissearch():
    client = MongoClient()
    irisdb = client.iris  # iris DB생성.
    iris_col = irisdb.iriscol  # iriscol 컬렉션 지정.
    cur = iris_col.find()

    for item in cur:
        print(item)

import json
import pandas as pd

def csvInsert(csv_path, db_name, col_name, db_url='local_host',
              db_port=27017) :
    client = MongoClient(db_url, db_port)
    db = client[db_name]      # db 지정, 생성
    db_col = db[col_name] # db에 collection 지정, 생성
    # mongodb 형태로 변환
    data = pd.read_csv(csv_path)
    pyload = data.to_json(orient = 'records')
    lastData = json.loads(pyload)

    db_col.remove()             # 기존 데이터(도큐먼트) 삭제
    db_col.insert(lastData)     # 데이터에 도큐먼트를 넣어줌
    return db_col.count()       # 컬렉션 데이터 건 수


if __name__=="__main__":
    menuint = menuPrint()
    if menuint==0:
        dbInfo()        # DB에 관련된 정보를 보겠다.
    elif menuint==1:
        ds.Search()     # 전체 검색
    elif menuint==3:
        print("데이터를 추가합니다.")
        ins.datInsert()
    elif menuint == 5 :
        print('IRIS 데이터를 추가합니다.')
        irisinsert()
    elif menuint == 6 :
        print('IRIS 데이터를 확인')
        irissearch()
    elif menuint == 7 :
        print('csv 추가')
        csv_path = 'C://Users/202-017/PycharmProjects/seoul19/testMongo/20191105133144.csv'
        datacnt = csvInsert(csv_path, 'local', 'datedate', db_url = 'localhost', db_port=27017)
        print('데이터가 추가되었습니다. {}건'.format(datacnt))


# csvfile = open('C://Users/202-017/PycharmProjects/seoul19/testMongo/20191105133144.csv',
#                'r')
# reader = csv.DictReader(csvfile)
# header = ["index", "date","temperate","humidity","hr"]
# df = pd.DataFrame(data)
# records = csv.DictReader(df)
#
# output = []
#
# for each in reader :
#     row = {}
#     for field in header :
#         row[field] = each[field]
#     output.append(row)
#
#
# db.segment.insert(records)