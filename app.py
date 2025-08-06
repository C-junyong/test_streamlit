import subprocess
import sys
import platform  # ✅ platform import 추가

# 필요한 패키지 설치 함수
def install_and_import(package):
    try:
        __import__(package)
    except ImportError:
        print(f"'{package}'가 설치되지 않아 설치를 진행합니다.")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"'{package}' 설치 완료!")

# 자동 설치
for pkg in ["streamlit", "pandas", "matplotlib"]:
    install_and_import(pkg)

# 패키지 임포트
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ✅ 한글 폰트 설정
if platform.system() == 'Windows':
    plt.rcParams['font.family'] = 'Malgun Gothic'
elif platform.system() == 'Darwin':
    plt.rcParams['font.family'] = 'AppleGothic'
else:
    plt.rcParams['font.family'] = 'NanumGothic'

plt.rcParams['axes.unicode_minus'] = False

# ✅ Streamlit 앱 시작
st.title("📊 학생 점수 분석 웹앱")

df = pd.DataFrame({
    "이름": ["철수", "영희", "민수", "지수"],
    "나이": [23, 21, 24, 22],
    "점수": [85, 90, 78, 92]
})

st.dataframe(df)

avg_score = df["점수"].mean()
st.write(f"👉 평균 점수: {avg_score:.2f}점")

fig, ax = plt.subplots()
ax.bar(df["이름"], df["점수"])
ax.set_title("학생별 점수")
st.pyplot(fig)
