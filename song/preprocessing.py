# 목표 : sql핸들링

import pandas as pd
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

# 전처리 결과를 Database에 넣는다.
class Preprocess:
    def __init__(self):
        tourist_attractions_data_1 = pd.read_excel("./selected_data/관광지/부산광역시_부산명소정보 서비스.xlsx", engine="openpyxl")
        want_columns_1 = ["구군", "여행지", "위도", "경도", "주소", "연락처", "홈페이지", "휴무일", "운영 및 시간", "편의시설"]
        self.want_data_1 = tourist_attractions_data_1[want_columns_1]
        print(self.want_data_1)

        """
        tourist_attractions_data_2 = pd.read_csv("./selected_data/관광지/전국관광지정보표준데이터.csv")
        want_columns_2 = ["관광지명", "위도", "경도", "소재지도로명주소", "공공편익시설정보", "운동및오락시설정보", "휴양및문화시설정보"]
        self.want_data_2 = tourist_attractions_data_2[want_columns_2]
        # "구" 데이터가 필요
        gu_list = ['강서구', '금정구', '남구', '동구', '동래구', '부산진구', '북구', '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구']
        temp_list = list()
        for i in range(len(tourist_attractions_data_2)):
            for gu in gu_list:
                if gu in tourist_attractions_data_2.loc[i, "소재지도로명주소"]:
                    temp_list.append(gu)
        # 데이터 가져와서 전처리 및 합치기
        # 전처리 결과 물을 변수에 저장
        temp_df = pd.DataFrame(temp_list, columns=["구군"])
        self.want_data_2 = pd.concat([self.want_data_2, temp_df], axis=1)
        want_columns_2 = ["구군", "관광지명", "위도", "경도", "소재지도로명주소", "공공편익시설정보", "운동및오락시설정보", "휴양및문화시설정보"]
        """

class DataBase:
    def __init__(self, preprocess_object):
        # preprocess_object에서 전처리 결과물을 가지고
        # 데이터베이스에 적재 -> 만든 ERD에 맞춰서
        pass



if __name__ == "__main__":
    preprocessing_object = Preprocess()

