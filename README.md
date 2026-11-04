# 수학 앱 만들기

Streamlit 기본 기능을 수학 예시로 실습하는 앱입니다.

- 기본 출력: 글, 수식, 메시지, 이미지와 영상
- 여러 가지 입력: 숫자, 슬라이더, 선택, 버튼과 조건문
- 자료와 그래프: 평균·중앙값 변화, 표, 그래프, CSV 불러오기
- 랜덤 추출과 기록: 번호 추출, 세션 내 기록 유지, CSV 저장
- 신뢰구간 추정: 표본 크기와 신뢰수준에 따른 구간 변화

## 실행

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

uv를 사용한다면 `uv sync` 후 `uv run streamlit run streamlit_app.py`로 실행할 수 있습니다.

Streamlit Community Cloud의 실행 파일은 `streamlit_app.py`로 지정합니다.

신뢰구간 예시는 정규모집단에서 모표준편차를 아는 경우를 다룹니다. 기록은 현재 사용자 세션에 유지되며, 영구 보관하려면 CSV로 저장합니다.
