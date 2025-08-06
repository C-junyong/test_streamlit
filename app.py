import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import urllib.request
import os

# ✅ 1. 폰트 GitHub에서 직접 다운로드 (캐시로 저장)
font_url = "https://github.com/naver/nanumfont/blob/master/ttf/NanumGothic.ttf?raw=true"
font_path = "NanumGothic.ttf"

if not os.path.exists(font_path):
    urllib.request.urlretrieve(font_url, font_path)

# ✅ 2. matplotlib에 한글 폰트 적용
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams["font.family"] = font_name
plt.rcParams["axes.unicode_minus"] = False

# ✅ 3. Streamlit 앱 구성
st.title("📊 학생 점수 분석 앱")

df = pd.DataFrame({
    "이름": ["철수", "영희", "민수", "지수"],
    "점수": [85, 90, 78, 92]
})

st.dataframe(df)

st.subheader("👉 평균 점수")
st.write(df["점수"].mean())

fig, ax = plt.subplots()
ax.bar(df["이름"], df["점수"])
ax.set_title("학생별 점수")
st.pyplot(fig)
