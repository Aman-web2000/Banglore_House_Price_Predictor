import streamlit as st 
import pandas as pd
import pickle 

pickle_in=open(r"A:\DS ML\Regression\Benguluru House price prediction\HousePrice.pkl",'rb')

reg=pickle.load(pickle_in)

def regressor(l):
    return reg.predict(l)[0]

def main():

    html_title="""
    <div style=" background-color:black;">
    <h1 style="text-align: center; color:white;">House Price Predictor 🏘️</h1
    </div>
    """
    st.markdown(html_title,unsafe_allow_html=True)

    st.subheader('Area Type')
    area_type=st.selectbox("",['Built-up  Area','Super built-up  Area','Plot  Area','Carpet  Area'])

    st.subheader('Number Of Rooms')
    rooms=st.slider('',min_value=3,max_value=50,step=2)

    st.subheader('Availability')
    avail=st.radio("",['Ready To Move','Not Ready'])

    st.subheader('Location')
    location=st.selectbox("",[ 'Rajaji Nagar', 'Electronic City','Malleswaram','Chandapura',"Indira Nagar",'Others'])

    st.subheader('Size(Sq. feet)')
    size=st.number_input('',min_value=200,max_value=3000,step=50)
    
    input_df=pd.DataFrame(data=[[area_type,avail,location,size,rooms]],columns=['area_type','availability','location','total_sqft','Total_rooms'])

    if st.button('Predict'):
        
        ans=regressor(input_df)
        ans=str(round(ans,2))
        
        html_ans="""
        <div>
        <h1 style="text-align: center; color:green;"> ₹ {ans} Lakhs</h1>
        </div>
        """.format(ans=ans)

        st.markdown(html_ans,unsafe_allow_html=True)



if __name__=="__main__":
    main()