import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager
import urllib.request
import os

# ✅ GitHub Raw URL에서 한글 폰트 다운로드 (최초 한 번만)
font_url = "https://raw.githubusercontent.com/naver/nanumfont/master/ttf/NanumGothic.ttf"
font_path = "NanumGothic.ttf"

if not os.path.exists(font_path):
    urllib.request.urlretrieve(font_url, font_path)

# ✅ 한글 폰트 적용
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams["font.family"] = font_name
plt.rcParams["axes.unicode_minus"] = False

# ✅ Streamlit 앱
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
ax.set_title("학생별 점수")  # 한글 정상 표시됨
st.pyplot(fig)
