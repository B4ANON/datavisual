import streamlit as st
import plotly_express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd


#iferror
#st.set_option('depreaction.showfileUploaderEncoding', False)

#title
st.title("UNIVERSAL DATA VISUALIZATION")

#sidebar
st.sidebar.subheader("visual settings")

#file upload
uploaded_file = st.sidebar.file_uploader(label="upload your csv or excel file .*MAX 200 MB*",type=['csv','xlsx'])


global df
if uploaded_file is not None:
    print(uploaded_file)
    print("completed")
    try:
        df = pd.read_csv(uploaded_file)
    except Exception as e:
        print(e)
        df = pd.read_excel(uploaded_file)

global numeric_columns
try:
    st.write(df)
    numeric_columns = list(df.select_dtypes(['float','int']).columns)
except Exception as e:
    print(e)
    st.write("please uplaod file to application")


    #select widget
chart_select = st.sidebar.selectbox(label="select chart type",options=['Scatterplots','Bar_plot','Pie_plot', 'Lineplots'])



if chart_select == 'Scatterplots':
    st.sidebar.subheader("Scatterplot settings")
    try:
        x_values = st.sidebar.selectbox('x axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('y axis', options=numeric_columns)
        plot = px.scatter(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(plot)
    except Exception as e:
        print(e)




if chart_select == 'Lineplots':
    st.sidebar.subheader("Lineplots settings")
    try:
        x_values = st.sidebar.selectbox('x axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('y axis', options=numeric_columns)
        li = px.line(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(li)
    except Exception as e:
        print(e)

if chart_select == 'Bar_plot':
    st.sidebar.subheader("Bar_plot settings")
    try:
        x_values = st.sidebar.selectbox('x axis', options=numeric_columns)
        y_values = st.sidebar.selectbox('y axis', options=numeric_columns)
        ba = px.bar(data_frame=df, x=x_values, y=y_values)
        st.plotly_chart(ba)
    except Exception as e:
        print(e)

if chart_select == 'Pie_plot':
    st.sidebar.subheader("Pie_plot settings")
    try:
        
    
        pc = px.pie(data_frame=df, values='population',names='country')
        st.plotly_chart(pc)
    except Exception as e:
        print(e)













