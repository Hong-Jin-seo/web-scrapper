import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. 웹 페이지 가져오기
url = "웹 페이지 주소"
response = requests.get(url)

if response.status_code == 200:
    print("웹 페이지 요청 성공!")
else:
    print("웹 페이지를 가져올 수 없습니다.")
    exit()

# 2. HTML 분석하기
soup = BeautifulSoup(response.text, 'html.parser')

# 3. 원하는 데이터 추출하기
# 'a' 태그 중에서 'api_txt_lines' 클래스를 가진 요소를 모두 찾습니다.
articles = soup.find_all('a', class_='nclicks(cnt_flashart)')

# 데이터를 저장할 빈 리스트를 만듭니다.
data = []

print("\n=== 기사 제목 목록 ===")
if not articles:
    print("추출할 기사가 없습니다. HTML 구조를 확인하세요.")
else:
    for article in articles:
        # <a> 태그 안에 있는 텍스트를 추출 (제목)
        title = article.get_text()
        # <a> 태그의 'href' 속성 값 추출 (링크)
        link = article.get('href')

        print(f"제목: {title}\n링크: {link}\n")
        
        # 추출한 제목과 링크를 딕셔너리 형태로 리스트에 추가합니다.
        data.append({'제목': title, '링크': link})

# 4. pandas 라이브러리를 사용해 CSV 파일로 저장하기
# data 리스트를 데이터프레임으로 변환
if data: # data 리스트에 데이터가 있는 경우에만 실행
    df = pd.DataFrame(data)
    df.to_csv('naver_news_articles.csv', index=False, encoding='utf-8-sig')
    print("데이터를 'naver_news_articles.csv' 파일에 저장했습니다.")
else:
    print("저장할 데이터가 없습니다.")