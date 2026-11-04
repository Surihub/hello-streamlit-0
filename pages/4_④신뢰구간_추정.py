import math
from statistics import NormalDist

import matplotlib.pyplot as plt
import streamlit as st

st.title("④ 평균의 신뢰구간 추정")
st.info("이 페이지에서는 모평균의 신뢰구간을 추정합니다. 표본 크기와 신뢰수준을 바꾸며 구간의 위치와 폭이 어떻게 달라지는지 확인해 보세요.")
st.write("정규모집단에서 독립적으로 추출한 표본이며, 모표준편차 σ를 알고 있는 경우입니다.")

st.subheader("1. 표본평균")
sample_mean = st.slider("표본평균", 20.0, 80.0, 50.0, 0.5)
st.subheader("2. 표본크기")
sample_size = st.slider("표본 크기 n", 5, 200, 30)
st.subheader("3. 모표준편차")
sigma = st.number_input("알고 있는 모표준편차 σ", 1.0, 20.0, 10.0, 1.0)
st.subheader("4. 신뢰수준")
confidence = st.select_slider("신뢰수준 (%)", [90, 95, 99], value=95)

z = NormalDist().inv_cdf(0.5 + confidence / 200)
margin = z * sigma / math.sqrt(sample_size)
lower = sample_mean - margin
upper = sample_mean + margin

st.subheader("5. 신뢰구간 계산")
st.latex(r"\bar{x}\pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}")
left, right = st.columns(2)
with left:
    st.metric(f"{confidence}% 신뢰구간", f"[{lower:.2f}, {upper:.2f}]")
with right:
    st.metric("구간의 폭", f"{2 * margin:.2f}")

st.subheader("6. 신뢰구간 시각화")
fig, ax = plt.subplots(figsize=(8, 2))
ax.errorbar(sample_mean, 0, xerr=margin, fmt="o", capsize=12, color="#2878B5", linewidth=3)
ax.set_xlim(-10, 110)
ax.set_ylim(-1, 1)
ax.set_yticks([])
ax.set_xlabel("Population mean")
ax.grid(axis="x", alpha=0.2)
st.pyplot(fig)
plt.close(fig)

st.subheader("7. 결과 해석")
st.write("표본 크기를 늘리면 구간이 좁아지고, 신뢰수준을 높이면 구간이 넓어집니다.")
with st.expander("신뢰수준의 뜻"):
    st.write("같은 방법으로 표본을 계속 뽑아 신뢰구간을 만들면, 그중 약 95%가 실제 모평균을 포함한다는 뜻입니다(95% 신뢰수준). 모표준편차를 모를 때는 표본표준편차와 t분포를 사용합니다.")
    st.link_button("신뢰구간 공식과 해석 참고", "https://www.itl.nist.gov/div898/handbook/prc/section1/prc14.htm")
