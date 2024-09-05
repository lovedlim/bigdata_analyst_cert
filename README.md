# [퇴근후딴짓] 빅데이터 분석기사 실기 - 길벗 시나공 시리즈
 
[![Python](https://img.shields.io/badge/Python-3.10.12-blue)]()
[![Pandas](https://img.shields.io/badge/Pandas-2.0.3-orange)]()
[![Statsmodels](https://img.shields.io/badge/Statsmodels-0.14.1-green)]()
[![SciPy](https://img.shields.io/badge/SciPy-1.11.4-blue)]()
[![Scikit-learn](https://img.shields.io/badge/Scikit_learn-1.2.2-black)]()
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)

## 🌱 도서 링크
- [교보문고](), [yes24]()
<img src="https://github.com/user-attachments/assets/0beab88b-b463-4058-9c5c-c6a0284b1d37" width="40%" height="40%"/>


## 🌱 목차
- Intro. 시험 응시 전략, 시험 환경 소개, 코드 및 데이터 불러오기, 자주하는 질문 등
- PART1. 작업형1 (파이썬, 판다스, 연습문제)
- PART2. 작업형2 (이진분류, 다중분류, 회귀, 평가지표, 연습문제)
- PART3. 작업형3 (가설검정, 분산 분석, 카이제곱, 회귀, 로지스틱 회귀, 연습문제)
- PART4. 기출유형 (예시문제, 2회 ~ 8회까지)


## 🌱 예제코드 바로 실행하는 방법
- 노트북 선택(part/chapter) -> 구글 코랩에서 실행하기 -> Drive로 복사 -> 실행
  
![guide_colab](https://github.com/user-attachments/assets/840d2a4f-a725-4320-9c84-c76d37f910d7)

## 🌱 예제코드 전체 다운로드 방법
- "Code" 버튼 클릭 -> 풀다운 메뉴에서 "Download Zip"을 선택
- 입문자는 "예제코드 바로 실행하는 방법"을 추천합니다. 
<img width="819" alt="Screenshot 2024-08-21 at 11 58 59 AM" src="https://github.com/user-attachments/assets/4ade48e7-9071-4849-9ea1-5828de49e554">


## 🌱 실습 중 오류가 발생했을 때
- 제공된 최종 노트북 코드와 현재 코드를 비교하여 문제를 파악해보세요. 코드를 복사하여 붙여넣기 한 후 정상적으로 실행되는지 확인
- 문제가 지속될 경우, ChatGPT(https://chat.openai.com/), Claude(https://claude.ai) 를 활용


## 🌱 안내사항
- 아래와 같은 lightgbm 모델에서 학습시 발생하는 워닝은 무시해 주세요. (코랩 최신버전에서 워닝 발생, 시험환경 발생하지 않음)
```text
/usr/local/lib/python3.10/dist-packages/dask/dataframe/__init__.py:42: FutureWarning: 
Dask dataframe query planning is disabled because dask-expr is not installed.
You can install it with `pip install dask[dataframe]` or `conda install dask`.
This will raise in a future version.
  warnings.warn(msg, FutureWarning)
```

## 🌱 도서 활용 스터디
- 9회 운영(준비중): 2024년 0월 0일 ~ 2024년 11월 30일
- 디스코드 입장 링크: https://discord.gg/V8acvTnHhH
- 학습과 관련해 1:1 질의응답은 진행하지 않습니다. 미션을 수행하고, 멤버간 질의응답을 하는 공간입니다. 


## 레포지토리 구조
```text
.
├── README.md
├── part1
│   ├── ch1
│   │   └── ch1_python.ipynb
│   ├── ch2
│   │   └── ch2_pandas.ipynb
│   └── ch3
│       ├── ch3_ex_type1.ipynb
│       ├── delivery_time.csv
│       ├── school_data.csv
│       ├── school_data_science.csv
│       ├── school_data_social.csv
│       ├── type1_data1.csv
│       └── type1_data2.csv
├── part2
│   ├── ch2
│   │   ├── ch2_classification.ipynb
│   │   ├── test.csv
│   │   └── train.csv
│   ├── ch3
│   │   └── ch3_metrics.ipynb
│   ├── ch4
│   │   ├── ch4_regression.ipynb
│   │   ├── test.csv
│   │   └── train.csv
│   ├── ch5
│   │   ├── ch5_multi_class_classification.ipynb
│   │   ├── test.csv
│   │   └── train.csv
│   ├── ch6
│   │   ├── ch6_ex_classification.ipynb
│   │   ├── creditcard_test.csv
│   │   ├── creditcard_train.csv
│   │   ├── diabetes_test.csv
│   │   ├── diabetes_train.csv
│   │   ├── hr_test.csv
│   │   └── hr_train.csv
│   ├── ch7
│   │   ├── ch7_ex_multi_class_classification.ipynb
│   │   ├── drug_test.csv
│   │   ├── drug_train.csv
│   │   ├── glass_test.csv
│   │   ├── glass_train.csv
│   │   ├── score_test.csv
│   │   └── score_train.csv
│   └── ch8
│       ├── car_test.csv
│       ├── car_train.csv
│       ├── ch8_ex_regression.ipynb
│       ├── flight_test.csv
│       ├── flight_train.csv
│       ├── laptop_test.csv
│       └── laptop_train.csv
├── part3
│   ├── ch1
│   │   └── ch1_hypothesis_testing.ipynb
│   ├── ch2
│   │   ├── ch2_anova.ipynb
│   │   ├── fertilizer.csv
│   │   └── tree.csv
│   ├── ch3
│   │   └── ch3_chi_square.ipynb
│   ├── ch4
│   │   ├── ch4_linear_regression.ipynb
│   │   └── study.csv
│   ├── ch5
│   │   ├── ch5_logistic_regression.ipynb
│   │   └── health_survey.csv
│   └── ch6
│       ├── ch6_ex_type3.ipynb
│       ├── math.csv
│       └── tomato2.csv
└── part4
    ├── ch2
    │   ├── X_test.csv
    │   ├── X_train.csv
    │   ├── members.csv
    │   ├── p2_type1.ipynb
    │   ├── p2_type2.ipynb
    │   └── y_train.csv
    ├── ch3
    │   ├── members.csv
    │   ├── p3_type1.ipynb
    │   ├── p3_type2.ipynb
    │   ├── test.csv
    │   ├── train.csv
    │   └── year.csv
    ├── ch4
    │   ├── data4-1.csv
    │   ├── data4-2.csv
    │   ├── data4-3.csv
    │   ├── p4_type1.ipynb
    │   ├── p4_type2.ipynb
    │   ├── test.csv
    │   └── train.csv
    ├── ch5
    │   ├── data5-1.csv
    │   ├── data5-2.csv
    │   ├── data5-3.csv
    │   ├── p5_type1.ipynb
    │   ├── p5_type2.ipynb
    │   ├── test.csv
    │   └── train.csv
    ├── ch6
    │   ├── data6-1-1.csv
    │   ├── data6-1-2.csv
    │   ├── data6-1-3.csv
    │   ├── data6-3-2.csv
    │   ├── energy_test.csv
    │   ├── energy_train.csv
    │   ├── p6_type1.ipynb
    │   ├── p6_type2.ipynb
    │   └── p6_type3.ipynb
    ├── ch7
    │   ├── air_quality.csv
    │   ├── clam.csv
    │   ├── mart_test.csv
    │   ├── mart_train.csv
    │   ├── p7_type1.ipynb
    │   ├── p7_type2.ipynb
    │   ├── p7_type3.ipynb
    │   ├── stock_market.csv
    │   ├── student_assessment.csv
    │   └── system_cpu.csv
    └── ch8
        ├── chem.csv
        ├── churn.csv
        ├── churn_test.csv
        ├── churn_train.csv
        ├── customer_travel.csv
        ├── drinks.csv
        ├── p8_type1.ipynb
        ├── p8_type2.ipynb
        ├── p8_type3.ipynb
        ├── piq.csv
        └── tourist.csv
```

이 레포지토리에 실린 모든 내용의 저작권은 저자에게 있으며, 저자의 허락 없이 이 코드의 일부 또는 전부를 복제, 배포할 수 없습니다.
