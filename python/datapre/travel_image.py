import requests
from bs4 import BeautifulSoup

import pandas as pd
import numpy as np

# 관광지 (문화시설 제외)
url_sgp = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
          '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&areaCode=39&sigunguCode=3&listYN=Y'

url_jj = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
         '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&areaCode=39&sigunguCode=4&listYN=Y'

url_gg = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=31&sigunguCode='

url_gb = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=35&sigunguCode='

url_gn = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=36&sigunguCode='

url_seoul = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=1&sigunguCode='

url_ic = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=2&sigunguCode='

url_dj = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=3&sigunguCode='

url_dg = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=4&sigunguCode='

url_gj = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=5&sigunguCode='

url_bs = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=6&sigunguCode='

url_us = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=7&sigunguCode='

url_sj = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=8&sigunguCode=1'

url_gw = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=32&sigunguCode='

url_cb = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=33&sigunguCode='

url_cn = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=34&sigunguCode='

url_jb = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=37&sigunguCode='

url_jn = 'http://api.visitkorea.or.kr/openapi/service/rest/KorService/areaBasedList?serviceKey=k9ex5ipQp8k' \
          '%2Baiet3GfC015PcRbjkuEv%2Bq8XD2ScEoT0CMfyyZgG5%2BjRCpsuFqQ2LFtwGcZdiDuigKZLvnn7yg%3D%3D&pageNo=1&numOfRows' \
         '=2000&MobileApp=AppTest&MobileOS=ETC&arrange=O&contentTypeId=12&listYN=Y&areaCode=38&sigunguCode='

urls = [
    url_sgp,
    url_jj,
]

# 서울
#for i in range(1, 26):
#    urls.append(url_seoul + str(i))

# 인천
#for i in range(1, 11):
#    urls.append(url_ic + str(i))

# 대전
#for i in range(1, 6):
#    urls.append(url_dj + str(i))

# 대구
#for i in range(1, 9):
#    urls.append(url_dg + str(i))

# 광주
#for i in range(1, 6):
#    urls.append(url_gj + str(i))

# 부산
#for i in range(1, 17):
#    urls.append(url_bs + str(i))

# 울산
#for i in range(1, 6):
#    urls.append(url_us + str(i))

# 세종
#urls.append(url_sj)

# 경기
#for i in range(1, 32):
#    urls.append(url_gg+str(i))

# 강원도
#for i in range(1, 19):
#    urls.append(url_gw + str(i))

# 충북
#for i in range(1, 13):
#    urls.append(url_cb + str(i))

# 충남
#for i in range(1, 17):
#    if i != 10:
#        urls.append(url_cn + str(i))

# 경북
#for i in range(1, 24):
#    if i != 18:
#        urls.append(url_gb+str(i))

# 전체 파일은 나중에 한번에 구동하여 다시 써야 함

# 경남
for i in range(1, 22):
    if i != 11:
        urls.append(url_gn + str(i))

# 전북
for i in range(1, 15):
    urls.append(url_jb + str(i))

# 전남
for i in range(1, 25):
    if i != 14 and i != 15:
        urls.append(url_jn + str(i))
print(urls)
df_image = pd.DataFrame(columns=['travel_name', 'travel_image'])

j = 0
for i in range(len(urls)):
    try:
        document = requests.get(urls[i])
        soup = BeautifulSoup(document.content, "lxml-xml")

        for travelElement in soup.findAll('item'):
            if travelElement.firstimage is None:
                break
            print(j, travelElement.title.string, travelElement.firstimage.string)
            df_image.loc[j] = [travelElement.title.string, travelElement.firstimage.string]
            j = j+1
    except Exception as e:
        print('에러 내용:', e)
        continue


print(df_image)

# df_image.to_csv('../preprocessing/image.csv', sep=',', mode='w', header=True, index=False, encoding='cp949')

df_image.to_csv('../preprocessing/image.csv', sep=',', mode='a', header=False, index=False, encoding='cp949')

