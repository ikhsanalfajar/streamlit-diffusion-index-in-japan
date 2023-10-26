import pickle
import streamlit as st

model = pickle.load(open('estimasi_diffusion_index_in_japan.sav', 'rb'))

st.title('Diffusion index in Japan')

year = st.number_input('Input Tahun')
month = st.number_input('Input Bulan')
day = st.number_input('Input Hari')
HouseholdTrend = st.number_input('Input Tren Rumah Tangga')
HouseholdTrend_Retail = st.number_input('Input Ritel Tren Rumah Tangga')
HouseholdTrend_FoodService = st.number_input(
    'Input Layanan Makanan Tren Rumah Tangga')
HouseholdTrend_Services = st.number_input('Input Layanan Tren Rumah Tanggan')
HouseholdTrend_Housing = st.number_input('Input Perumahan Tren Rumah Tangga')
CorporateTrend = st.number_input('Input Tren Korporasi')
CorporateTrend_Manufacturing = st.number_input(
    'Input Tren Korporasi Manufaktur')
CorporateTrend_NonManufacturing = st.number_input(
    'Input Tren Korporasi Non-Manufaktur')
Employment = st.number_input('Input Pekerjaan')

predict = ''

if st.button('Estimasi Diffusion'):
    predict = model.predict(
        [[year, month, day, HouseholdTrend, HouseholdTrend_Retail, HouseholdTrend_FoodService, HouseholdTrend_Services,
          HouseholdTrend_Housing, CorporateTrend, CorporateTrend_Manufacturing, CorporateTrend_NonManufacturing, Employment]]
    )
    st.write('Estimasi : ', predict)
