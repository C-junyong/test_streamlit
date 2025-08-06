import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 학생 점수 분석 앱 (Plotly 버전)")

df = pd.DataFrame({
    "이름": ["철수", "영희", "민수", "지수"],
    "점수": [85, 90, 78, 92]
})

st.dataframe(df)

fig = px.bar(df, x="이름", y="점수", title="학생별 점수")
st.plotly_chart(fig)
