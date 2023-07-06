"""test tb"""

import sqlite3
import pandas as pd








class DataBaseClass:
    pd.set_option("display.max_column", None)
    pd.set_option("display.max_row", None)
    db = sqlite3.connect("test.db")
    df = pd.read_sql("select * from test", db)

    def inputandreturn(self, a):
        dict_value = {}
        dict_num = {}
        cnt_ = 0
        df_1_pd = self.df[self.df['시군구명'] == f"{a}"]
        df_1_pd.reset_index(inplace=True)
        num_list = df_1_pd[['이미지','업체명', '주소', '시군구명', '전화번호', '위도', '경도', ]]
        list_column = ["이미지", "업체명", "주소", "시군구명", "전화번호", "위도", "경도"]
        # return num_list.values
        # print(num_list)
        for i in num_list.values:
            for value in zip(list_column, i):
                dict_value[value[0]] = value[1]
                a = dict_value.copy()
                dict_num[f"{cnt_}"] = a
            cnt_ += 1
        return dict_num


a = DataBaseClass()
test = a.inputandreturn("강서구")
for i in range(len(test)):
    print(test[f'{i}'])

