import streamlit as st
import pandas as pd
st.header("📝 Job Application Tracker")
if 'jobs' not in st.session_state:
    st.session_state.jobs=[]
companyName=st.text_input(" company name  ")
role=st.text_input('Job Title')
status=st.radio('Application Status',['Applied','Interview','Offer','Rejected'])
interview_date = ""
if status=='Interview':
    interview_date=st.date_input("Interview Date")
notes=st.text_area("Additional Notes")
save=st.button('Add Entry')
if save:
   st.session_state.job.append({
       'companyName':companyName,
       'Role':role,
       'Status':status,
       'Interview Date':interview_date if status=='Interview' else "",
       'Notes':notes
   })
   st.success('✅ Job entry added Successfully')

if st.checkbox('show All Entries'):
    df=pd.DataFrame(st.session_state.jobs)
    st.dataframe(df)

    filter_status=st.selectbox('Filter By status',['All','Applied','Interview','Offer','Rejected'])
    if filter_status!='All':
        filter_df=df[df['Status']==filter_status]
        st.dataframe(filter_df)
    else:
        st.dataframe(df)
if st.button('Reset All Entries'):
    st.session_state.jobs=[]
    st.warning('🧹  All Entries have been cleared')
