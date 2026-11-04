import pandas as pd
import streamlit as st

st.title("② 자료와 그래프")
st.info("이 페이지에서는 자료를 표와 그래프로 표현합니다. 값을 추가하며 평균·중앙값의 변화를 확인하고, 같은 자료를 여러 그래프로 비교해 보세요.")

st.subheader("1. 자료 추가와 대표값")
st.write("기존 자료: 4, 5, 5, 6, 7")
new_value = st.number_input("추가할 자료", value=10)
data = pd.DataFrame({"값": [4, 5, 5, 6, 7, new_value]})
left, right = st.columns(2)
with left:
    st.metric("평균", f"{data['값'].mean():.2f}", delta=f"{data['값'].mean()-5.4:+.2f}", delta_color="off")
with right:
    st.metric("중앙값", f"{data['값'].median():.2f}", delta=f"{data['값'].median()-5:+.2f}", delta_color="off")
st.write("추가할 값을 10에서 100으로 바꿔 보세요. 평균과 중앙값 중 무엇이 더 많이 변하나요?")
st.dataframe(data, hide_index=True)
st.bar_chart(data)

st.subheader("2. 같은 자료를 세 가지 그래프로 보기")
a = st.slider("일차함수의 기울기", -5, 5, 2)
x = list(range(-5, 6))
function = pd.DataFrame({"x": x, "y": [a * value for value in x]})
line, bar, scatter = st.tabs(["선 그래프", "막대그래프", "산점도"])
with line:
    st.line_chart(function.set_index("x"))
with bar:
    st.bar_chart(function.set_index("x"))
with scatter:
    st.scatter_chart(function, x="x", y="y")

with st.expander("CSV 파일로 자료 가져오기"):
    file = st.file_uploader("숫자가 들어 있는 CSV 파일", type="csv")
    if file is not None:
        try:
            uploaded = pd.read_csv(file)
            st.dataframe(uploaded.head(100), hide_index=True)
            numbers = uploaded.select_dtypes(include="number")
            if numbers.empty:
                st.warning("숫자 열이 있는 파일을 넣어 주세요.")
            else:
                st.bar_chart(numbers.head(100))
        except (ValueError, UnicodeError, pd.errors.ParserError):
            st.error("UTF-8 형식의 CSV 파일인지 확인해 주세요.")
