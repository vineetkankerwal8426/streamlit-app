import streamlit as st
import pandas as pd
from vega_datasets import data
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(
    page_title="STOCKS VIEW", page_icon="chart_with_upwards_trend", layout="centered"
)
@st.cache_data
def chart(data):
    global hover,tooltips,main_chart
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    main_chart = (
        alt.Chart(data ,title=options)
        .mark_line()
        .encode(
            x=alt.X("date", title="DATE"),
            y=alt.Y("price", title="PRICE"),
            color="symbol",
        )
    )
    points = main_chart.transform_filter(hover).mark_circle(size=30)
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="yearmonthdate(date)",
            y="price",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date", title="Date"),
                alt.Tooltip("price", title="USD "),
            ],
        )
        .add_selection(hover)
    )

    return (main_chart +points+ tooltips).interactive()





st.title(":red[STOCK VIEW]")
df = pd.DataFrame(data.stocks())
options = st.selectbox(':green[SELECT STOCK]',['WELCOME','MSFT','AMZN','IBM','AAPL','GOOG','COMPAIR ALL','HIGHEST PRICE PERCENTAGE'])
if options=='WELCOME':
    st.snow()
    st.header("WELCOME TO :red[STOCK VIEW]")
    st.subheader('FOR ANY SUGGESTION REGARDING THIS APP IMPROVEMENT, PLEASE CONTACT:')
    st.write('GMAIL: codevkankerwal@gmail.com')
    st.write("LINKEDIN: [vineetkankerwal](https://www.linkedin.com/in/vineet-kankerwal-11145b260)")
    if st.button('PRESS IF YOU LIKE MY WORK'):
        st.subheader(":red[❤❤]THANKS FOR YOUR SUPPORT")
        code = '''#include <iostream>
int main()
{
       std::cout<<"THANK YOU SO MUCH";
       return 0;
}'''
        st.code(code,language = 'c++')
        st.balloons()
    st.write('MADE BY VK KANKERWAL')
elif options =="COMPAIR ALL":
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.metric(label='GOOG',value='$560.19' ,delta=457.82)
    with col2:
        st.metric(label='AAPL',value='$223.02' ,delta=197.08)
    with col3:
        st.metric(label='IBM',value='$125.55' ,delta=25.03)
    with col4:
        st.metric(label='AMZN',value='$128.82' ,delta=59.95)
    with col5:
        st.metric(label='MSFT',value='$ 28.8',delta= -11.08)
    st.altair_chart(chart(df),use_container_width = True)
elif options=='MSFT':
    st.metric(label='MSFT',value='$ 28.8',delta= -11.08)
    st.altair_chart(chart(df[df.symbol=='MSFT']),use_container_width =True)
elif options=='AMZN':
    st.metric(label='AMZN',value='$128.82' ,delta=59.95)
    st.altair_chart(chart(df[df.symbol=='AMZN']),use_container_width=True)
elif options=='IBM':
    st.metric(label='IBM',value='$125.55' ,delta=25.03)
    st.altair_chart(chart(df[df.symbol=='IBM']),use_container_width=True) 
elif options=='AAPL':
    st.metric(label='AAPL',value='$223.02' ,delta=197.08)
    st.altair_chart(chart(df[df.symbol=='AAPL']),use_container_width=True)
elif options=='GOOG':
    st.metric(label='GOOG',value='$560.19' ,delta=457.82)
    st.altair_chart(chart(df[df.symbol=='GOOG']),use_container_width=True)
elif options == 'HIGHEST PRICE PERCENTAGE':
    l1 = df.sort_values(['price',],ascending=False).groupby('symbol').head(1)['price'].values.tolist()
    l2 = df.sort_values(['price',],ascending=False).groupby('symbol').head(1)['symbol'].values.tolist()
    fig = plt.pie(l1,labels=l2,autopct="%1.1f%%")
    st.pyplot(fig)
else:
    st.snow()
    st.balloons()
