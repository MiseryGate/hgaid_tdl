import streamlit as st
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor,ExtraTreesRegressor
from sklearn.model_selection import validation_curve, LeaveOneOut, train_test_split, cross_val_score
from sklearn.model_selection import cross_validate, KFold, cross_val_score, RandomizedSearchCV, GridSearchCV
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder 
from matplotlib import pyplot
import pickle
import math

#Baca Data
#data = pd.read_csv("./fkrtl_reguler.csv")
#loaded_model = pickle.load(open('./model.pkl', 'rb'))


LOGO_IMAGE = "./health-katon-white.png"
#Disable Warning
st.set_option('deprecation.showPyplotGlobalUse', False)
#Set Size
sns.set(rc={'figure.figsize':(8,8)})
#Coloring
colors_1 = ['#66b3ff','#99ff99']
colors_2 = ['#66b3ff','#99ff99']
colors_3 = ['#79ff4d','#4d94ff']
colors_4 = ['#ff0000','#ff1aff']
st.markdown(
    f"""
    <div style="text-align: center;">
    <img class="logo-img" src="data:png;base64,{base64.b64encode(open(LOGO_IMAGE, 'rb').read()).decode()}">
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown("<h1 style='text-align: center; color: #FFFFFF; font-family:sans-serif'>Health Guard : Analysis and Identification</h1>", unsafe_allow_html=True)
menu = st.sidebar.selectbox("Select Menu", ("Dashboard", "Prediksi","Kluster"))
st.sidebar.image("./logo.png", width=70)
if menu == "Dashboard":
    st.write("Menu Dashboard")
    st.markdown("""<a style='display: block; text-align: center; font-size:40px; ' href="https://drive.google.com/drive/folders/1dq9QgqbUWlpIgCNIwSYT9Q-yOHHuoO25">Tautan GDrive</a>""", unsafe_allow_html=True)
    st.markdown("""<a style='display: block; text-align: center; font-size:40px; ' href="https://bit.ly/DashboardAnakAyam">Tautan Dashboard</a>""", unsafe_allow_html=True)

      # CSS to inject contained in a string
    hide_table_row_index = """
                    <style>
                    .css-1q8dd3e.edgvbvh1 {display:none}
                    </style>
                    """

        # Inject CSS with Markdown
    st.markdown(hide_table_row_index, unsafe_allow_html=True)
if menu == "Prediksi":
    st.write("Menu Prediksi")
    #st.write(data.head(2))