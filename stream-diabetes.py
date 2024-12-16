import pickle
import os  # Pastikan modul os di-import
import streamlit as st

# Tentukan lokasi file model
model_file = 'diabetes_model.sav'

# Cek apakah file model ada di direktori aplikasi
if not os.path.exists(model_file):
    st.error(f"File {model_file} tidak ditemukan di direktori aplikasi!")
else:
    try:
        # Memuat model menggunakan pickle
        diabetes_model = pickle.load(open(model_file, 'rb'))
        st.success("Model berhasil dimuat!")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat memuat model: {str(e)}")

# Sisakan bagian kode untuk aplikasi di bawah ini
st.title('Prediksi Diabetes')
st.subheader('Masukkan Data untuk Memprediksi Diabetes')

# Form input data (contohnya)
Pregnancies = st.number_input('Angka Kehamilan', min_value=0, step=1, format="%d")
Glucose = st.number_input('Glukosa', min_value=0, step=1, format="%d")
BloodPressure = st.number_input('Tekanan Darah (mmHg)', min_value=0, step=1, format="%d")
Age = st.number_input('Usia (tahun)', min_value=0, step=1, format="%d")

# Tambahkan elemen lainnya sesuai kebutuhan aplikasi
# Misalnya tombol untuk memprediksi atau menampilkan hasil
if st.button('Test Prediksi Diabetes'):
    if 'diabetes_model' in locals():
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, Age]])
        if diab_prediction[0] == 1:
            st.success('Pasien terkena Diabetes')
        else:
            st.success('Pasien tidak terkena Diabetes')
    else:
        st.error("Model belum dimuat, silakan coba lagi.")

# Title of the web app
st.title('Prediksi Diabetes')

# Add a subtitle for better understanding
st.subheader('Masukkan Data untuk Memprediksi Diabetes')

# Four column layout with adjusted widths
col1, col2, col3, col4 = st.columns([2, 2, 2, 2])

with col1:
    Pregnancies = st.number_input('Angka Kehamilan', min_value=0, step=1, format="%d")
with col2:
    Glucose = st.number_input('Glukosa', min_value=0, step=1, format="%d")
with col3:
    BloodPressure = st.number_input('Tekanan Darah (mmHg)', min_value=0, step=1, format="%d")
with col4:
    Age = st.number_input('Usia (tahun)', min_value=0, step=1, format="%d") 

col5, col6, col7, col8 = st.columns([2, 2, 2, 2])

with col5:
    Insulin = st.number_input('Insulin serum (mu U/ml)', min_value=0, step=1, format="%d")
with col6:
    BMI = st.number_input('BMI', min_value=0.0, step=0.1, format="%.1f")
with col7:
    DiabetesPedigreeFunction = st.number_input('Indikator riwayat diabetes dalam keluarga', min_value=0.0, step=0.01, format="%.2f")
with col8:
    SkinThickness = st.number_input('Ketebalan lipatan kulit trisep (mm)', min_value=0, step=1, format="%d")

# Placeholder for the diagnosis result
diab_diagnosis = ''

# Create a button for prediction
if st.button('Test Prediksi Diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if diab_prediction[0] == 0:
        diab_diagnosis = 'Pasien tidak terkena Diabetes'
    else:
        diab_diagnosis = 'Pasien terkena Diabetes'
        
    # Display the diagnosis result
    st.success(diab_diagnosis)

# Add footer
st.write("---")
st.write("Aplikasi Prediksi Diabetes ini dibuat untuk membantu memprediksi kemungkinan diabetes berdasarkan data kesehatan yang dimasukkan.")
