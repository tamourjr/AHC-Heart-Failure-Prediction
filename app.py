import streamlit as st
import figureupdatedds

st.title("Heart Disease Dashboard")


st.plotly_chart(figureupdatedds.hist_sex_disease())
st.plotly_chart(figureupdatedds.box_age_disease())
st.plotly_chart(figureupdatedds.scatter_age_maxhr())
st.plotly_chart(figureupdatedds.hist_chest_pain())
st.plotly_chart(figureupdatedds.violin_bp_by_disease())
st.plotly_chart(figureupdatedds.scatter_chol_age())
st.plotly_chart(figureupdatedds.treemap_gender_chestpain())
st.plotly_chart(figureupdatedds.hist_chestpain_gender())
st.plotly_chart(figureupdatedds.violin_maxhr_gender())
st.plotly_chart(figureupdatedds.bar_chestpain_gender())
st.plotly_chart(figureupdatedds.hist_st_slope())
st.plotly_chart(figureupdatedds.pie_chestpain())
