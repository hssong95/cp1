from flask import Flask, render_template, Blueprint, request
from markupsafe import escape
from werkzeug.datastructures import MultiDict
import pandas as pd
import numpy as np
import crawling


from flask import Flask

cp1 = Flask(__name__)

#표지
@cp1.route('/')
def index():
    head = '외식 산업 예비 창업자를 위한 데이터 시각화 및 분석 프로그래밍'
    head2 = 'CP1'
    return render_template('index.html', head=head, head2=head2)

#조회 페이지 지정
@cp1.route('/news/')
def news():
   
   return  render_template('news.html')

#앞에서 조회 페이지를 받아와 기사를 띄움(news_show 함수로 연결)
@cp1.route('/news/request', methods=['POST'])
def news_redirect():
    page_num= request.form.get("page_num")
    return news_show(int(page_num))

#crawling 모듈의 news_crawl함수에 페이지수 변수 주어 결과물 데이터 프레임으로 받아옴
@cp1.route('/news/<num>')
def news_show(num):
    data = crawling.news_crawl(int(num))
    data.content = data.content.str[:20]


    return data.to_html()

@cp1.route('/policy')
def policy_index():
    return render_template('policy.html')

@cp1.route('/policy/request', methods=['POST'])
def policy_redirect():
    policy_type = request.form.get('policy_type')

    if policy_type == '정책자금':
        keyword = 'found'
    elif policy_type == '성장지원':
        keyword= 'grow'
    elif policy_type == '재기지원':
        keyword= 'comeback'
    elif policy_type == '창업지원':
        keyword= 'startup'
    elif policy_type == '전통시장활성화':
        keyword= 'market'
    elif policy_type == '보증지원':
        keyword= 'grnty'
    else:
        return '잘못된 키워드 입니다.'    
        
    data = crawling.policy_info(keyword)
    return data.to_html()


#vscode 에서 바로 실행 + 디버그 모드
if __name__ == "__main__":
    cp1.run(debug=True)