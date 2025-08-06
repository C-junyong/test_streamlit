import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 한글 폰트 설정 (Streamlit Cloud 호환)
plt.rcParams['font.family'] = 'NanumGothic'
plt.rcParams['axes.unicode_minus'] = False

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
