import random

import pandas as pd
import streamlit as st

st.title("③ 랜덤 추출과 기록")
st.info("이 페이지에서는 번호를 무작위로 뽑고 결과를 누적합니다. 추출을 반복하며 기록이 유지되는지 확인하고, 결과를 CSV 파일로 저장해 보세요.")
st.write("1부터 30까지의 번호 중에서 중복 없이 뽑습니다.")
st.subheader("1. 추출 조건")
count = st.slider("한 번에 뽑을 개수", 1, 10, 3)

if "simple_draws" not in st.session_state:
    st.session_state.simple_draws = []
if "simple_latest" not in st.session_state:
    st.session_state.simple_latest = []

if st.button("무작위로 뽑기"):
    result = random.sample(range(1, 31), count)
    st.session_state.simple_latest = result
    st.session_state.simple_draws.extend(result)
if st.button("기록 초기화"):
    st.session_state.simple_draws = []
    st.session_state.simple_latest = []

st.subheader("2. 추출 결과")
if st.session_state.simple_latest:
    st.write("이번에 뽑힌 번호:", st.session_state.simple_latest)
st.metric("지금까지 뽑은 개수", len(st.session_state.simple_draws))

st.subheader("3. 기록과 그래프")
if st.session_state.simple_draws:
    df = pd.DataFrame({"번호": st.session_state.simple_draws})
    st.dataframe(df, hide_index=True)
    st.bar_chart(df["번호"].value_counts().reindex(range(1, 31), fill_value=0).rename("추출 횟수"))
    st.download_button("기록 CSV 저장", df.to_csv(index=False).encode("utf-8-sig"), "draws.csv", "text/csv")
st.write("한 번의 추출에서는 중복되지 않지만, 다음 추출에서는 같은 번호가 다시 나올 수 있습니다.")
