import pandas as pd
import plotly.express as px


df = pd.read_csv('heart.csv')
df['HeartDisease'] = df['HeartDisease'].map({0: 'No', 1: 'Yes'})
df['Sex'] = df['Sex'].map({'M': 'Male', 'F': 'Female'})
df.to_csv('heart_updated.csv', index=False)



def hist_sex_disease(df):
    fig = px.histogram(df, x='Sex', color='HeartDisease', barmode='group',
                       title='Heart Disease Distribution by Gender', text_auto=True)
    return fig



def box_age_disease():
    fig = px.box(df, x='HeartDisease', y='Age', color='HeartDisease',
                 title='Age Distribution by Heart Disease')
    return fig



def scatter_age_maxhr():
    fig = px.scatter(df, x='Age', y='MaxHR', color='HeartDisease', trendline='ols',
                     title='Age vs MaxHR with Heart Disease')
    return fig



def hist_chest_pain():
    fig = px.histogram(df, x='ChestPainType', color='HeartDisease', barmode='group',
                       title='Heart Disease Distribution by Chest Pain Type', text_auto=True)
    return fig



def violin_bp_by_disease():
    fig = px.violin(df, y='RestingBP', x='HeartDisease', box=True, points='all',
                    color='HeartDisease', title='Resting Blood Pressure by Heart Disease')
    return fig



def scatter_chol_age():
    fig = px.scatter(df, x='Cholesterol', y='Age', color='HeartDisease',
                     title='Cholesterol vs Age by Heart Disease',
                     color_discrete_map={
                         'Yes': '#FF6B6B',    # Coral Red
                         'No': '#4ECDC4'      # Aqua Mint
                     })
    return fig



def treemap_gender_chestpain():
    grouped = df.groupby(['Sex', 'ChestPainType']).size().reset_index(name='Count')
    fig = px.treemap(grouped, path=['Sex', 'ChestPainType'], values='Count',
                     title='Heart Disease Cases by Gender and Chest Pain Type',
                     color='Count', color_continuous_scale='Teal')
    return fig



def hist_chestpain_gender():
    fig = px.histogram(df, x='ChestPainType', color='HeartDisease',
                       facet_col='Sex', barmode='stack',
                       title='Heart Disease vs Chest Pain Type by Gender', text_auto=True)
    return fig


def violin_maxhr_gender():
    fig = px.violin(df, y='MaxHR', x='Sex', color='HeartDisease', box=True, points='all',
                    title='Heart Rate Distribution by Gender and Heart Disease',
                    color_discrete_map={'Yes': '#FF6B6B', 'No': '#4ECDC4'})
    return fig



def bar_chestpain_gender():
    fig = px.bar(df, x='ChestPainType', color='HeartDisease', barmode='group',
                 facet_col='Sex', title='Heart Disease by Chest Pain Type and Gender', 
                 color_discrete_map={'Yes': '#E74C3C', 'No': '#2ECC71'})
    return fig



def hist_st_slope():
    fig = px.histogram(df, x='ST_Slope', color='HeartDisease', barmode='group',
                       title='ST Slope Distribution by Heart Disease',
                       color_discrete_map={'Yes': '#E74C3C', 'No': '#2ECC71'}, text_auto=True)
    return fig



def pie_chestpain():
    fig = px.pie(df, names='ChestPainType', 
                 title='Distribution of Chest Pain Types',
                 hole=0.3, color_discrete_sequence=px.colors.sequential.RdBu)
    fig.update_traces(textinfo='percent+label')
    return fig
