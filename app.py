import streamlit as st

st.set_page_config(
    page_title="🩺 건강 MBTI",
    page_icon="🩺",
    layout="centered"
)


if "page" not in st.session_state:
    st.session_state.page = -1

if "name" not in st.session_state:
    st.session_state.name = ""

if "scores" not in st.session_state:
    st.session_state.scores = {
        "M":0,
        "D":0,
        "I":0,
        "S":0
    }

if "disease_scores" not in st.session_state:
    st.session_state.disease_scores = {
        "거북목 증후군":0,
        "허리디스크":0,
        "손목터널증후군":0,
        "근막통증증후군":0,
        "척추측만증":0,

        "위염":0,
        "역류성 식도염":0,
        "과민성 대장증후군":0,
        "변비":0,
        "기능성 소화불량":0,

        "감기":0,
        "알레르기 비염":0,
        "천식":0,
        "결막염":0,
        "편도염":0,

        "불면증":0,
        "스트레스 증후군":0,
        "번아웃":0,
        "불안장애":0,
        "긴장성 두통":0
    }

# 질문
questions = [

# ===== 근골격계 =====

{
    "text":"하루 4시간 이상 앉아서 공부하거나 일한다.",
    "type":"M",
    "disease":"거북목 증후군"
},
{
    "text":"목이나 어깨가 자주 뻐근하다.",
    "type":"M",
    "disease":"근막통증증후군"
},
{
    "text":"가방을 항상 한쪽 어깨로만 메는 편이다.",
    "type":"M",
    "disease":"척추측만증"
},
{
    "text":"스마트폰을 오래 사용한다.",
    "type":"M",
    "disease":"거북목 증후군"
},
{
    "text":"손목이나 손가락이 저린 적이 있다.",
    "type":"M",
    "disease":"손목터널증후군"
},
{
    "text":"평소 스트레칭을 자주 한다.",
    "type":"M",
    "disease":"근막통증증후군",
    "reverse":True
},
{
    "text":"일주일에 운동을 3회 이상 한다.",
    "type":"M",
    "disease":"허리디스크",
    "reverse":True
},

# ===== 소화기 =====

{
    "text":"아침을 자주 거른다.",
    "type":"D",
    "disease":"위염"
},
{
    "text":"음식을 빨리 먹는다.",
    "type":"D",
    "disease":"기능성 소화불량"
},
{
    "text":"긴장하거나 스트레스를 받으면 배가 아픈 경우가 있다.",
    "type":"D",
    "disease":"과민성 대장증후군"
},
{
    "text":"야식을 자주 먹는다.",
    "type":"D",
    "disease":"역류성 식도염"
},
{
    "text":"카페인 음료(커피·에너지음료)를 자주 마신다.",
    "type":"D",
    "disease":"위염"
},
{
    "text":"식사 시간이 매일 일정하지 않다.",
    "type":"D",
    "disease":"기능성 소화불량",
    "reverse":True
},
{
    "text":"골고루 먹는 편이다.",
    "type":"D",
    "disease":"변비",
    "reverse":True
},

# ===== 면역 =====

{
    "text":"감기에 자주 걸린다.",
    "type":"I",
    "disease":"감기"
},
{
    "text":"목이 아파도 휴식을 충분히 취하지 않는다.",
    "type":"I",
    "disease":"편도염"
},
{
    "text":"침구류를 자주 세탁하지 않는다.",
    "type":"I",
    "disease":"알레르기 비염"
},
{
    "text":"미세먼지가 심한 날에도 야외 활동을 자주 한다.",
    "type":"I",
    "disease":"천식"
},
{
    "text":"콘택트렌즈를 권장 시간보다 오래 착용한다.",
    "type":"I",
    "disease":"결막염"
},
{
    "text":"7시간 이상 잔다.",
    "type":"I",
    "disease":"감기",
    "reverse":True
},
{
    "text":"물을 하루 1L 이상 마시는 편이다.",
    "type":"I",
    "disease":"편도염",
    "reverse":True
},
# ===== 스트레스 =====

{
    "text":"사소한 일에도 스트레스를 많이 받는다.",
    "type":"S",
    "disease":"스트레스 증후군"
},
{
    "text":"잠들기 직전까지 스마트폰을 사용하는 편이다.",
    "type":"S",
    "disease":"불면증"
},
{
    "text":"자고 일어나도 피곤하다.",
    "type":"S",
    "disease":"번아웃"
},
{
    "text":"스마트폰을 하루 5시간 이상 사용한다.",
    "type":"S",
    "disease":"긴장성 두통"
},
{
    "text":"집중력이 쉽게 떨어진다.",
    "type":"S",
    "disease":"불안장애"
},
{
    "text":"스트레스 해소 방법이 있다.",
    "type":"S",
    "disease":"스트레스 증후군",
    "reverse":True
},
{
    "text":"스트레스를 빨리 회복하는 편이다.",
    "type":"S",
    "disease":"번아웃",
    "reverse":True
}

]

options = [
    "항상 그렇다",
    "가끔 그렇다",
    "거의 아니다"
]

point = {
    "항상 그렇다":2,
    "가끔 그렇다":1,
    "거의 아니다":0
}

# 첫 화면

st.title("🩺 건강 MBTI (제출용!!!)")
st.write("생활습관으로 알아보는 건강 유형 검사")

if st.session_state.page == -1:

    st.session_state.name = st.text_input("이름을 입력하세요.")
    if st.button("검사 시작"):

        if st.session_state.name.strip() != "":
            st.session_state.page = 0
            st.rerun()

# 질문 화면

elif st.session_state.page < len(questions):

    current = st.session_state.page

    st.progress((current + 1) / len(questions))

    st.subheader(f"질문 {current + 1} / {len(questions)}")

    q = questions[current]

    answer = st.radio(
        q["text"],
        options,
        key=f"q{current}"
    )

    if st.button("다음 ▶"):

        score = point[answer]

        # 역문항 처리
        if q.get("reverse", False):
            score = 2 - score

        # 영역 점수
        st.session_state.scores[q["type"]] += score

        # 질환 점수
        st.session_state.disease_scores[q["disease"]] += score

        st.session_state.page += 1
        st.rerun()

# 결과 화면

else:

    scores = st.session_state.scores

    st.header(f"{st.session_state.name}님의 검사 결과")

    #st.write(f"근골격계(Muscle) : {scores['M']}점")
    #st.write(f"소화기(Digest) : {scores['D']}점")
    #st.write(f"면역력(Immunity) : {scores['I']}점")
    #st.write(f"스트레스(Stress) : {scores['S']}점")

    health_order = sorted(
    scores.items(),
    key=lambda x: x[1],
    reverse=True
)

    code = "".join([x[0] for x in health_order])

    name = {
        "M":"근골격계(Muscle)",
        "D":"소화기(Digest)",
        "I":"면역력(Immunity)",
        "S":"스트레스(Stress)"
    }

    type_name = {
        "M": "자세관리형",
        "D": "식습관관리형",
        "I": "면역관리형",
        "S": "스트레스관리형"
    }

    main = health_order[0][0]

    st.subheader(f"{st.session_state.name}님의 건강 MBTI - {type_name[main]}")
    
    st.success(code)

    st.write(
        "관리 우선순위 : " +
        " → ".join(name[x[0]] for x in health_order)
    )

        # TOP 3 위험 질환

    ranking = sorted(
        st.session_state.disease_scores.items(),
        key=lambda x: x[1],
        reverse=True
    )

    # TOP 3 위험 질환

    st.subheader("※ 위험도가 높은 질환 TOP 3")

    for i in range(3):
        st.write(
            f"{i+1}. {ranking[i][0]} ({ranking[i][1]}점)"
        )

    disease_info = {

        "거북목 증후군":(
            "목을 앞으로 빼는 자세로 인해 발생하는 자세 질환",
            "바른 자세 유지, 스트레칭하기"
        ),

        "허리디스크":(
            "허리 디스크가 돌출되어 통증이 생기는 질환",
            "무거운 물건 들기 줄이고 코어운동"
        ),

        "손목터널증후군":(
            "손목 신경이 눌려 저림이 발생하는 질환",
            "손목 스트레칭, 장시간 사용 줄이기"
        ),

        "근막통증증후군":(
            "근육과 근막에 통증이 발생하는 질환",
            "스트레칭과 마사지"
        ),

        "척추측만증":(
            "척추가 옆으로 휘는 질환",
            "바른 자세 유지"
        ),

        "위염":(
            "위 점막에 염증이 생기는 질환",
            "규칙적인 식사"
        ),

        "역류성 식도염":(
            "위산이 식도로 역류하는 질환",
            "야식 줄이기"
        ),

        "과민성 대장증후군":(
            "스트레스와 장 운동 이상으로 발생",
            "스트레스 관리"
        ),

        "변비":(
            "배변이 원활하지 않은 상태",
            "물과 식이섬유 섭취"
        ),

        "기능성 소화불량":(
            "원인 없이 소화가 잘되지 않는 질환",
            "천천히 식사하기"
        ),
        "감기":(
            "면역력이 떨어질 때 쉽게 발생하는 바이러스성 질환",
            "충분한 수면과 손 씻기"
        ),

        "알레르기 비염":(
            "알레르기 반응으로 코 점막에 염증이 생기는 질환",
            "실내 청결 유지"
        ),

        "결막염":(
            "눈에 염증이 생기는 질환",
            "눈을 자주 만지지 않기"
        ),

        "편도염":(
            "편도에 염증이 생기는 질환",
            "충분한 휴식"
        ),

        "천식":(
            "면역 기능이 떨어진 상태",
            "균형 잡힌 식사와 운동"
        ),

        "불면증":(
            "잠들기 어렵거나 자주 깨는 질환",
            "취침 전 스마트폰 사용 줄이기"
        ),

        "스트레스 증후군":(
            "기분이 지속적으로 가라앉는 상태",
            "규칙적인 생활과 상담"
        ),

        "불안장애":(
            "지속적인 불안과 긴장이 나타나는 질환",
            "심호흡과 스트레스 관리"
        ),

        "번아웃":(
            "지속적인 피로와 무기력 상태",
            "충분한 휴식"
        ),

        "긴장성 두통":(
            "스트레스로 인해 발생하는 두통",
            "휴식과 스트레칭"
        )
    }

    top = ranking[0][0]

    st.subheader("대표 위험 질환")

    st.error(top)

    st.write(disease_info[top][0])

    st.write("**예방법**")
    st.success(disease_info[top][1])

    if st.button("🔄 다시 검사하기"):
        st.session_state.page = -1
        st.session_state.name = ""
        st.session_state.scores = {
            "M":0,
            "D":0,
            "I":0,
            "S":0
        }

        st.session_state.disease_scores = {
            "거북목 증후군":0,
            "허리디스크":0,
            "손목터널증후군":0,
            "근막통증증후군":0,
            "척추측만증":0,
            "위염":0,
            "역류성 식도염":0,
            "과민성 대장증후군":0,
            "변비":0,
            "기능성 소화불량":0,
            "감기":0,
            "알레르기 비염":0,
            "결막염":0,
            "편도염":0,
            "천식":0,
            "불면증":0,
            "스트레스 증후군":0,
            "불안장애":0,
            "번아웃":0,
            "긴장성 두통":0
        }

        st.rerun()

    st.divider()
    st.write("""
    ★ 본 프로그램은 생활습관을 기반으로 위험도를 예측한 결과이므로 실제 건강 상태와 다를 수 있습니다.
    
    정확한 진단은 반드시 병원을 방문하여 전문의의 진료를 받으시기 바랍니다.
    """)