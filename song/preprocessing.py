# 목표 : sql핸들링

"""
사용 데이터
관광지 -> 부산광역시_부산명소정보 서비스.xlsx
숙박 -> 부산지역 숙박분야 공공데이터(열린관광시설정보).xlsx
음식점 -> 부산광역시_부산맛집정보 서비스.xlsx
"""



import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# 전처리 결과를 Database에 넣는다.
class Preprocess:
    def __init__(self):
        tourist_attractions_data_1 = pd.read_excel("./selected_data/관광지/부산광역시_부산명소정보 서비스.xlsx", engine="openpyxl")
        want_columns_1 = ["구군", "여행지", "위도", "경도", "주소", "연락처", "상세내용"]
        self.tourist_attractions_data = tourist_attractions_data_1[want_columns_1]
        # t1, id 이렇게 2개의 데이터를 더 넣으면. 데이터를 가져올 때, 저장할 때 -> 조회용으로 테이블 명, id를 같이 쓴다.
        # temp_t1 = list()
        # temp_id = list()
        # for i in range(len(tourist_attractions_data_1)):
        #     temp_t1.append("t1")
        #     temp_id.append(i+1)
        # temp_df_t1 = pd.DataFrame(temp_t1, columns=["table_name"])
        # temp_df_id = pd.DataFrame(temp_id, columns=["id"])
        # self.want_data_1 = pd.concat([temp_df_id, self.want_data_1], axis=1)
        # self.want_data_1 = pd.concat([temp_df_t1, self.want_data_1], axis=1)
        # print(self.want_data_1)

        restaurant_data = pd.read_csv("./selected_data/음식점/부산광역시_부산맛집정보 서비스.csv")
        want_columns_2 = ["구군", "콘텐츠명", "위도", "경도", "주소", "연락처", "상세내용"]
        self.restaurant_data = restaurant_data[want_columns_2]

        accommodation_data = pd.read_excel("./selected_data/숙박/부산지역 숙박분야 공공데이터(열린관광시설정보).xlsx", engine="openpyxl")
        accommodation_data = accommodation_data[accommodation_data['폐업여부'] == "N"]
        accommodation_data.fillna("", inplace=True)
        accommodation_data.reset_index(drop=True, inplace=True)
        delete_list = ["여인숙", "여관", "모텔"]
        for delete_thing in delete_list:
            drop_index = accommodation_data[accommodation_data['업체명'].str.contains(delete_thing)].index
            accommodation_data = accommodation_data.drop(drop_index, axis=0)
        delete_list1 = "월"
        for delete_thing in delete_list1:
            drop_index = accommodation_data[accommodation_data['번지'].str.contains(delete_thing, na=False)].index
            accommodation_data = accommodation_data.drop(drop_index, axis=0)

        want_columns = ['업체명', '시군구명', '읍면동명', '리명', '번지', '위도', '경도', '전화번호', '주차가능여부']
        accommodation_data = accommodation_data[want_columns]
        accommodation_data.reset_index(inplace=True)

        new_list = list()
        for i in range(len(accommodation_data)):
            if accommodation_data.loc[i, "리명"] == "":
                a = "부산광역시 " + str(accommodation_data.loc[i, "시군구명"]) + " " + str(accommodation_data.loc[i, "읍면동명"]) + " " + str(accommodation_data.loc[i, "번지"])
            else:
                a = "부산광역시 " + str(accommodation_data.loc[i, "시군구명"]) + " " + str(accommodation_data.loc[i, "읍면동명"]) + " " + str(accommodation_data.loc[i, "리명"]) + " " + str(accommodation_data.loc[i, "번지"])
            new_list.append(a)

        new_df = pd.DataFrame(new_list, columns=["주소"])
        accommodation_data = pd.concat([new_df, accommodation_data], axis=1)
        want_columns = ['시군구명', '업체명', '주소', '번지', '위도', '경도', '전화번호', '주차가능여부']
        self.accommodation_data = accommodation_data[want_columns]

        # 최종 데이터
        """
        # ["구군", "콘텐츠명", "위도", "경도", "주소", "연락처", "상세내용"]
        self.tourist_attractions_data
        # ["구군", "콘텐츠명", "위도", "경도", "주소", "연락처", "상세내용"]
        self.restaurant_data
        # ['시군구명', '업체명', '주소', '번지', '위도', '경도', '전화번호', '주차가능여부']
        self.accommodation_data
        """
        # 여기에 이미지 데이터 넣으면 끝난다.




# 하나의 포멧으로 통일하셨음.-> 7~8 columns, 하나의 기본 포멧을 만들고, id에 따라 추가정보를 출력

class DataBase:
    def __init__(self, preprocess_object):
        # preprocess_object에서 전처리 결과물을 가지고
        # 데이터베이스에 적재 -> 만든 ERD에 맞춰서
        pass



if __name__ == "__main__":
    preprocessing_object = Preprocess()

