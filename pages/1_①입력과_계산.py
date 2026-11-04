import streamlit as st

st.title("① 여러 가지 입력")
st.info("이 페이지에서는 여러 입력 기능과 버튼을 사용합니다. 값을 입력하고 선택지를 바꾸며 계산 결과와 피드백을 확인해 보세요.")

st.subheader("1. 글과 숫자 입력")
title = st.text_input("계산기 제목", "나의 계산기")
st.write(title)
left, right = st.columns(2)
with left:
    a = st.number_input("첫 번째 수", value=3)
with right:
    b = st.number_input("두 번째 수", value=5)
operation = st.selectbox("계산 방법", ["더하기", "곱하기"])
st.write("결과:", a + b if operation == "더하기" else a * b)

st.subheader("2. 슬라이더와 체크박스")
side = st.slider("정사각형 한 변의 길이", 1, 10, 4)
st.metric("넓이", side * side)
if st.checkbox("넓이 공식 보기"):
    st.latex(r"S=a^2")

st.subheader("3. 하나 선택하기")
choice = st.radio("2³의 값은?", [6, 8, 9], horizontal=True)
st.write("선택한 값:", choice)

st.subheader("4. 여러 개 선택하기")
selected = st.multiselect("소수를 모두 선택하세요", [1, 2, 3, 4, 5, 9])
st.write("선택한 수:", selected)

st.subheader("5. 버튼과 조건문")
st.latex(r"2x+3=11")
answer = st.number_input("x의 값", value=0)
if st.button("정답 확인"):
    if answer == 4:
        st.success("정답입니다!")
    else:
        st.warning("양변에서 3을 빼고, 2로 나누어 보세요.")
