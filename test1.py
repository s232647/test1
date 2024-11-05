# 분류 모델 웹앱 만들기
import streamlit as st

# 1.기계학습 모델 파일 로드
import joblib
model = joblib.load('logistic_regression_model.pkl') 

# 2.모델 설명
st.title('_______')
col1, col2,col3 = st.columns( ____ )      # 몇 개의 컬럼으로 나눌까?
with col1:
      st.subheader('모델 설명 ')
      st.write(' - 기계학습 알고리즘 : 로지스틱 회귀 ')
      st.write(' - 학습 데이터 출처 : https://www.kaggle.com/')
      st.write(' - 훈련    데이터 : *건')
      st.write(' - 테스트 데이터 : *건')
      st.write(' - 모델 정확도 : 0.89')
# 3.데이터시각화
with col2:
      st.subheader('데이터시각화1')
      st.image('____________' )   # 이미지 불러오기
with col3:
      st.subheader('데이터시각화2')
      st.image('____________')    # 이미지 불러오기

# 4. 모델 활용
st.subheader('모델 활용')
st.write('**** 공부시간을 입력하세요.. 인공지능이 당신의 합격/불합격 분류 결과를 알려드립니다!')

a = st.number_input(' _________ ', value=0)   # 사용자 입력

if st.button('합불분류'):              # 사용자가 '합불분류' 버튼을 누르면
        input_data = [[ a ]]          # 사용자가 입력한 a,b,c 를 input_data에 저장하고
        p = model._______(input_data)      # model이 분류한 값을 p에 저장한다
        if p[0] == 1 :
              st.success('인공지능 분류 결과는 ___입니다')
        else:
              st.success('인공지능 분류 결과를 ____입니다')

              
