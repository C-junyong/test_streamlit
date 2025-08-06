import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import platform

# 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

st.title("📊 학생 점수 분석 웹앱")

df = pd.DataFrame({
    "이름": ["철수", "영희", "민수", "지수"],
    "나이": [23, 21, 24, 22],
    "점수": [85, 90, 78, 92]
})

st.dataframe(df)

avg = df["점수"].mean()
st.write(f"👉 평균 점수: {avg:.2f}점")

fig, ax = plt.subplots()
ax.bar(df["이름"], df["점수"])
ax.set_title("학생별 점수")
st.pyplot(fig)
