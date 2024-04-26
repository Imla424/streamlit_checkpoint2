import pypickle
import streamlit as st
import pandas as pd
from sklearn.preprocessing import LabelEncoder

data=pypickle.load('model.pkl')

st.title('Bank account prediction')
uniqueid=st.number_input('The unique identifier for each interviwee?')
country=st.text_input('The country interviwee is in ?')
year= st.text_input('The year the survey was done in?')

location =st.radio('Select interviewee location: ', ('Rural','Urban'))
if location == 'Rural':
    location = st.text_input('Rural')
elif (location == 'Urban'):
    # take gender input in text
     location = st.text_input('Urban')

cellphone_access=st.radio('Does interviewee have access to cellphones?: ',('Yes', 'No'))
if cellphone_access =='Yes' :
    cellphone_access = st.text_input('Yes')
elif (cellphone_access == 'No'):
    cellphone_access = st.text_input('No')

household_size = st.number_input('Number of people living in one house')
age_of_respondent=st.number_input('How old is the respondent?')
gender_of_respondent=st.radio('Gender of interviewee : ',('Male', 'No'))
if gender_of_respondent == 'Male' :
    gender_of_respondent = st.text_input('Male')
elif (gender_of_respondent == 'Female'):
    gender_of_respondent = st.text_input('Female')

relationship_with_head=st.radio('Interviewee relationship with the head: ',('Head of household','spouse','child'))
if relationship_with_head == 'Head of household' :
    relationship_with_head=st.text_input('Head of household')
elif (relationship_with_head == 'spouse'):
    relationship_with_head =st.text_input('spouse')
elif (relationship_with_head == 'child'):
    relationship_with_spouse=st.text_input('child')

marital_status=st.radio('The marital status of the interviewee: ',('single','married','divorced'))
if marital_status == 'single' :
    marital_status=st.text_input('single')
elif (marital_status=='married'):
    marital_status=st.text_input('married')
elif (marital_status == 'divorced'):
    marital_status=st.text_input('divorced')

education_level=st.text_input('The interviewee education level')
job_type=st.text_input('The interviewee job type')

#encoder=['uniqueid', 'country','year','location','cellphone_access',
          #'household_size','age_of_respondent','gender_of_respondent','relationship_with_head','marital_status','education_level','job_type]

x=pd.DataFrame({

    'uniqueid': [uniqueid],
    'country': [country],
    'year': [year],
    'location': [location],
    'cellphone_access': [cellphone_access],
    'household_size': [household_size],
    'age_of_respondent': [age_of_respondent],
    'gender_of_respondent': [gender_of_respondent],
    'relationship_with_head': [relationship_with_head],
    'marital_status': [marital_status],
    'education_level': [education_level],
    'job_type': [job_type]

})

encoder= LabelEncoder()


#Label Encoder to convert categorical columns into numerical features passing in a lambda function
def object_to_int(dataframe_series):
    if dataframe_series.dtype=='object':
        dataframe_series = LabelEncoder().fit_transform(dataframe_series)
    return dataframe_series

df_merges = x.apply(lambda x: object_to_int(x))
df_merges.head()

if (st.button('Bank account prediction')):
    predict= data.predict(df_merges)
    if predict== 1:
        st.write('yes')
    else:
        st.write('No')