import streamlit as st
import pandas as pd
import numpy as np

# 1. 페이지 설정 (브라우저 탭 이름과 아이콘)
st.set_page_config(page_title="My First App", page_icon="🚀")

# 2. 앱 제목과 간단한 소개
st.title("📊 배포고고")
st.write("이 앱은 GitHub과 Streamlit Cloud를 통해 배포되었습니다.")

# 3. 사이드바 만들기
st.sidebar.header("조절판")
name = st.sidebar.text_input("당신의 이름을 입력하세요", "방문객")
data_size = st.sidebar.slider("데이터 개수 선택", 10, 100, 50)

# 4. 데이터 생성 및 시각화
st.subheader(f"👋 반갑습니다, {name}님!")
chart_data = pd.DataFrame(
    np.random.randn(data_size, 3),
    columns=['에너지', '속도', '효율']
)

# 라인 차트 출력
st.line_chart(chart_data)

# 데이터 표 출력 (선택 사항)
if st.checkbox("데이터 표 보기"):
    st.dataframe(chart_data)