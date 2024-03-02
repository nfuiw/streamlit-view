import streamlit as st
import pandas as pd
import numpy as np

st.title('안녕, 스트림릿!')
st.write('이것은 내 첫 번째 스트림릿 앱입니다.')

views = [100, 20, 40]
views

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

st.write(df)

if st.button("click button"):
  st.write("Data Loading..")
  # 데이터 로딩 함수는 여기에!

checkbox_btn = st.checkbox('Checktbox Button')
	
if checkbox_btn:
  st.write('Great!')

checkbox_btn2 = st.checkbox('Checktbox Button2', value=True)
	
if checkbox_btn2:
  st.write('Button2')


selected_item = st.radio("Radio Part", ("A", "B", "C"))
	
if selected_item == "A":
  st.write("A!!")
elif selected_item == "B":
  st.write("B!")
elif selected_item == "C":
  st.write("C!")

option = st.selectbox('Please select in selectbox!',
                       ('kyle', 'seongyun', 'zzsza'))
	
st.write('You selected:', option)


multi_select = st.multiselect('Please select somethings in multi selectbox!',
                                ['A', 'B', 'C', 'D'])
	
st.write('You selected:', multi_select)

values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)

st.text_input('텓ㄱ스트') #텍스트 데이터
st.text_input('비밀번호', 123, type="password") #텍스트 데이터를 암호로 사용
st.number_input('복숭아 개수', 100) #숫자 데이터를 입력하고 싶은 경우
st.text_area('이름', 'ㅁㄴㅇㄹㅁㄴㅇㄹㅁㄴㅇㄴㅁㅇㄹㅁㄴㅇㄹㅁㄴㅇㄹㅁㄴㅇㄹㅁㄴㅇㄹㅁㄴ어ㅜ라ㅓㅇㄴ무ㅏㅓ롸ㅓㄴ오라ㅓ모나ㅓ오라먼와') #여러 줄의 텍스트 데이터를 입력하고 싶은 경우
st.date_input('날짜') #날짜
st.time_input('시간')# 시간


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
              'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
	
@st.cache
def load_data(nrows):
  data = pd.read_csv(DATA_URL, nrows=nrows)
  lowercase = lambda x: str(x).lower()
  data.rename(lowercase, axis='columns', inplace=True)
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  return data
	
data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")
	
if st.checkbox('Show raw data'):
  st.subheader('Raw data')
  st.write(data)
	
st.subheader('Number of pickups by hour')
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)
	
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
	
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)