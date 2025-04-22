import streamlit as st
import figures  

st.title("Heart Disease Dashboard")


st.plotly_chart(figures.hist_sex_disease())
st.plotly_chart(figures.box_age_disease())
st.plotly_chart(figures.scatter_age_maxhr())
st.plotly_chart(figures.hist_chest_pain())
st.plotly_chart(figures.violin_bp_by_disease())
st.plotly_chart(figures.scatter_chol_age())
st.plotly_chart(figures.treemap_gender_chestpain())
st.plotly_chart(figures.hist_chestpain_gender())
st.plotly_chart(figures.violin_maxhr_gender())
st.plotly_chart(figures.bar_chestpain_gender())
st.plotly_chart(figures.hist_st_slope())
st.plotly_chart(figures.pie_chestpain())
