import streamlit as st
import requests
import pandas as pd
import plotly.express as px

code_to_region = {
    'COL_5000110001OD': '전국',
    'COL_5000810001OD': '서울',
    'COL_5001610001OD': '경기',
    'COL_5012410001OD': '인천',
    'COL_5002510001OD': '부산',
    'COL_5016510001OD': '대전',
    'COL_5015910001OD': '광주',
    'COL_5015010001OD': '대구',
    'COL_5017110001OD': '울산',
    'COL_5003310001OD': '세종',
    'COL_5017710001OD': '강원',
    'COL_5018510001OD': '충북',
    'COL_5019410001OD': '충남',
    'COL_5020710001OD': '전북',
    'COL_5021610001OD': '전남',
    'COL_5022310001OD': '경북',
    'COL_5023710001OD': '경남',
    'COL_5025010001OD': '제주',
}
region_to_code = {v: k for k, v in code_to_region.items()}

@st.cache_data(ttl=86400)  # 24시간 = 86400초
def get_data(type_):
    cookies = {
        'JSESSIONID': '74F8B68DE1315C7A835C390AB9D41BD6',
        'SCOUTER': 'x33ame6oedu1dq',
        'WMONID': 'jLz3irTAxfh',
        '_harry_fid': 'hh828125739',
        'XTVID': 'A250516165553082398',
        'xloc': '3072X1728',
        '_harry_lang': 'ko',
        '_ga': 'GA1.1.1247597096.1747382153',
        '_ga_0WH3G11899': 'GS2.1.s1747382153$o1$g0$t1747382160$j0$l0$h0',
        '_ga_FZ1729SWDK': 'GS2.1.s1747385351$o2$g1$t1747385374$j0$l0$h0',
    }

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'ko,en;q=0.9,en-US;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://www.reb.or.kr',
        'Referer': 'https://www.reb.or.kr/r-one/portal/stat/easyStatPage/A_2024_00045.do',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="136", "Microsoft Edge";v="136", "Not.A/Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    if type_ == '매매':
        data = 'firParam=&deviceType=&statblId=T244183132827305&statId=S234820263&statTitle=(%EC%A3%BC)+%EB%A7%A4%EB%A7%A4%EA%B0%80%EA%B2%A9%EC%A7%80%EC%88%98&wrttimeMinYear=2012&wrttimeMaxYear=2025&wrttimeMinQt=01&wrttimeMaxQt=53&chartType=&chartStockType=&chart23Type=2D&chartLegend=&alarmSetSeq=&usrTblSeq=&hisCycleNo=&tabMapVal=NONE&infId=&topCateId=700000&optDivVal=13&dtacycleCd=WK&wrttimeType=B' + \
            '&wrttimeStartYear=2012&wrttimeStartQt=01&wrttimeEndYear=9999&wrttimeEndQt=99' + \
            '&wrttimeLastestVal=10&wrttimeOrder=A&uiChgVal=&dmPointVal=&chartCategories=%EC%84%A0%ED%83%9D&chartCategoriesMore=%EC%84%A0%ED%83%9D&chartCls=%EC%84%A0%ED%83%9D&mapCategories=&mapItms=&tabGrpKeyword=&tabItmKeyword=&tabClsKeyword=&viewLocOpt=V&optST=H&optSC=L&optSI=H&tabDvsKeyword=&alarmSetStatblNm=&alarmSetStatblEndDt=&usrTblStatblNm=&usrTblStatblExp=&callTag=F&returnObjName=callPopExpn&tabTreeClsExpnOptCbo=13&expnGrpKeyword=&expnClsKeyword=&expnItmKeyword=&callSheet=IB8&hasClsAllChk=Y&hasItmAllChk=Y&hasGrpAllChk=Y&chkItms=10001&chkClss=50001%2C50008%2C50016%2C50124%2C50025%2C50150%2C50159%2C50165%2C50171%2C50033%2C50177%2C50185%2C50194%2C50207%2C50216%2C50223%2C50237%2C50250&dtadvsVal=OD'
    elif type_ == '전세':
        data = 'firParam=&deviceType=&statblId=T247713133046872&statId=S234820263&statTitle=(%EC%A3%BC)+%EC%A0%84%EC%84%B8%EA%B0%80%EA%B2%A9%EC%A7%80%EC%88%98&wrttimeMinYear=2012&wrttimeMaxYear=2025&wrttimeMinQt=01&wrttimeMaxQt=53&chartType=&chartStockType=HISTORY&chart23Type=2D&chartLegend=&alarmSetSeq=&usrTblSeq=&hisCycleNo=&tabMapVal=NONE&infId=&topCateId=700000&optDivVal=13&dtacycleCd=WK&wrttimeType=B' + \
            '&wrttimeStartYear=2012&wrttimeStartQt=01&wrttimeEndYear=9999&wrttimeEndQt=99' + \
            '&wrttimeLastestVal=10&wrttimeOrder=A&uiChgVal=&dmPointVal=&chartCategories=%EC%84%A0%ED%83%9D&chartCategoriesMore=%EC%84%A0%ED%83%9D&chartCls=%EC%84%A0%ED%83%9D&mapCategories=&mapItms=&tabGrpKeyword=&tabItmKeyword=&tabClsKeyword=&viewLocOpt=V&optST=H&optSC=L&optSI=H&tabDvsKeyword=&alarmSetStatblNm=&alarmSetStatblEndDt=&usrTblStatblNm=&usrTblStatblExp=&callTag=F&returnObjName=&tabTreeClsExpnOptCbo=13&expnGrpKeyword=&expnClsKeyword=&expnItmKeyword=&callSheet=IB8&hasClsAllChk=Y&hasItmAllChk=Y&hasGrpAllChk=Y&chkItms=10001&chkClss=50001%2C50008%2C50016%2C50124%2C50025%2C50150%2C50159%2C50165%2C50171%2C50033%2C50177%2C50185%2C50194%2C50207%2C50216%2C50223%2C50237%2C50250&dtadvsVal=OD'
    else:
        st.error("잘못된 유형입니다. '매매' 또는 '전세'를 선택하세요.")
        return None

    response = requests.post(
        'https://www.reb.or.kr/r-one/portal/stat/sttsDataPreviewList.do',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    json_data = response.json()
    data_list = json_data.get('DATA', [])

    df = pd.DataFrame(data_list)
    df['wrttimeId'] = pd.to_datetime(df['wrttimeId'])
    df.rename(columns=code_to_region | {'wrttimeId': '자료시점'}, inplace=True)

    for col in df.columns:
        if col != '자료시점':
            df[col] = pd.to_numeric(df[col], errors='coerce')

    df = df.sort_values('자료시점').set_index('자료시점')

    return df


def main():
    st.markdown('<h4>📈 주간아파트동향 (한국부동산원)</h4>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        type_option = st.selectbox('📊 거래유형', ['매매', '전세'])
    with col2:
        region_option = st.selectbox('🏢 지역선택', list(region_to_code.keys()))
    with st.spinner('데이터 불러오는 중...'):
        df = get_data(type_option)

    if df is not None:
        region_col = region_option

        if region_col in df.columns:
            latest_value = df[region_col].iloc[-1]
            previous_value = df[region_col].iloc[-2]
            change_pct = (latest_value - previous_value) / previous_value * 100 if previous_value != 0 else 0
            if change_pct > 0:
                change_color = "red"
                sign = "+"
            elif change_pct < 0:
                change_color = "blue"
                sign = ""
            else:
                change_color = "black"
                sign = ""
            latest_date_str = df.index[-1].strftime('%y.%m.%d')
            title_text = (
                f"{region_option} {type_option}가격지수 {latest_value:.2f}, "
                f"<span style='color:{change_color};'>{sign}{change_pct:.2f}%</span>, {latest_date_str}"
            )

            fig = px.line(
                df,
                x=df.index,
                y=region_col,
                labels={'x': '', region_col: ''}, 
                title=title_text
            )
            fig.update_layout(
                height=400,
                title=dict(text=title_text, font=dict(size=18)),
                xaxis_title='',
                yaxis=dict(
                    title='',          
                    title_standoff=0,  
                    automargin=True    
                ),
                margin=dict(l=0, r=0, t=60, b=40),
                hovermode='x unified'
            )
            fig.add_hline(
                y=latest_value,
                line_color="red",
                line_width=0.5,
                #line_dash="line",
                annotation_text='',
                annotation_position="top left",
                annotation_font_color="red"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.error(f"'{region_option}' 데이터가 존재하지 않습니다.")

    st.caption("ⓒ 2025.1.30. 유행살이. All rights reserved.")
    reduce_top_margin = """
        <style>
        header {visibility: hidden;}
        .block-container {
            padding-top: 2rem !important;
        }
        </style>
    """
    st.markdown(reduce_top_margin, unsafe_allow_html=True)
    hide_streamlit_ui = """
        <style>
        #MainMenu {visibility: hidden;}        /* 오른쪽 상단 메뉴 */
        footer {visibility: hidden;}           /* 오른쪽 하단 워터마크 */
        header {visibility: hidden;}           /* 페이지 상단 헤더 */
        .stDeployButton {visibility: hidden;}  /* 배포 버튼 */
        .st-emotion-cache-zq5wmm {visibility: hidden;} /* 오른쪽 아래 로고 */
        </style>
    """
    st.markdown(hide_streamlit_ui, unsafe_allow_html=True)




if __name__ == "__main__":
    main()