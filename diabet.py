import streamlit as st
import plotly.express as px
import pandas as pd
from datetime import datetime
import time

# Konfigurasi halaman
st.set_page_config(
    page_title="DiabetesCheck - SistemPakar",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS untuk styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    
    .risk-high {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        animation: pulse 2s infinite;
    }
    
    .risk-medium {
        background: linear-gradient(135deg, #ffa726, #ff9800);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    
    .risk-low {
        background: linear-gradient(135deg, #66bb6a, #4caf50);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    
    .info-box {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #36c5f0;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-weight: bold;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
    }
</style>
""", unsafe_allow_html=True)

def diagnose_diabetes(glucose, age, bmi, insulin):
    """Sistem pakar dengan aturan"""
    risk_score = 0
    risk_factors = []
    
    # Evaluasi Glucose
    if glucose >= 200:
        risk_score += 40
        risk_factors.append("Glucose sangat tinggi (≥200 mg/dL)")
    elif glucose >= 126:
        risk_score += 30
        risk_factors.append("Glucose tinggi (126-199 mg/dL)")
    elif glucose >= 100:
        risk_score += 15
        risk_factors.append("Glucose borderline (100-125 mg/dL)")
    
    # Evaluasi BMI
    if bmi >= 35:
        risk_score += 25
        risk_factors.append("BMI sangat tinggi (≥35)")
    elif bmi >= 30:
        risk_score += 20
        risk_factors.append("BMI tinggi (30-34.9)")
    elif bmi >= 25:
        risk_score += 10
        risk_factors.append("BMI berlebih (25-29.9)")
    
    # Evaluasi Usia
    if age >= 65:
        risk_score += 20
        risk_factors.append("Usia lanjut (≥65 tahun)")
    elif age >= 45:
        risk_score += 15
        risk_factors.append("Usia menengah (45-64 tahun)")
    elif age >= 35:
        risk_score += 10
        risk_factors.append("Usia dewasa (35-44 tahun)")
    
    # Evaluasi Insulin
    if insulin >= 200:
        risk_score += 20
        risk_factors.append("Insulin sangat tinggi (≥200 μIU/mL)")
    elif insulin >= 100:
        risk_score += 15
        risk_factors.append("Insulin tinggi (100-199 μIU/mL)")
    elif insulin >= 50:
        risk_score += 10
        risk_factors.append("Insulin borderline (50-99 μIU/mL)")
    
    # Menentukan tingkat risiko berdasarkan skor
    if risk_score >= 80:
        return "🚨 RISIKO SANGAT TINGGI", "Segera konsultasi dengan dokter!", risk_factors, "high"
    elif risk_score >= 60:
        return "⚠️ RISIKO TINGGI", "Disarankan pemeriksaan lebih lanjut", risk_factors, "high"
    elif risk_score >= 40:
        return "⚠️ RISIKO SEDANG", "Perhatikan gaya hidup dan pola makan", risk_factors, "medium"
    elif risk_score >= 20:
        return "ℹ️ RISIKO RENDAH-SEDANG", "Jaga pola hidup sehat", risk_factors, "medium"
    else:
        return "✅ RISIKO RENDAH", "Kondisi baik, pertahankan gaya hidup sehat", risk_factors, "low"

def show_recommendations(risk_level):
    """Menampilkan rekomendasi berdasarkan tingkat risiko"""
    st.markdown("### 💡 Rekomendasi")
    
    if risk_level == "high":
        st.error("""
        **Rekomendasi Segera:**
        - 🏥 Konsultasi dengan dokter endokrinologi
        - 🩸 Pemeriksaan HbA1c dan tes toleransi glucose
        - 📋 Evaluasi komplikasi diabetes (mata, ginjal, jantung)
        - 💊 Mungkin memerlukan pengobatan
        """)
    elif risk_level == "medium":
        st.warning("""
        **Rekomendasi Pencegahan:**
        - 🥗 Diet seimbang, kurangi karbohidrat sederhana
        - 🏃‍♂️ Olahraga teratur minimal 150 menit/minggu
        - ⚖️ Turunkan berat badan jika berlebih
        - 🩺 Pemeriksaan rutin setiap 6 bulan
        """)
    else:
        st.success("""
        **Rekomendasi Pemeliharaan:**
        - 🥗 Pertahankan pola makan sehat
        - 🏃‍♂️ Tetap aktif berolahraga
        - 📊 Monitoring berkala setahun sekali
        - 😊 Jaga kesehatan mental dan kelola stress
        """)

def main():
    # Header utama
    st.markdown("""
    <div class="main-header">
        <h1>🩺 Diabetes Check System</h1>
        <h3>Sistem Pakar Deteksi Risiko Diabetes</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar untuk informasi
    with st.sidebar:
        st.markdown("### 📋 Panduan Input")
        st.info("""
        **Glucose:** Kadar gula darah puasa (mg/dL)
        - Normal: < 100
        - Prediabetes: 100-125
        - Diabetes: ≥ 126
        
        **BMI:** Indeks Massa Tubuh
        - Normal: 18.5-24.9
        - Berlebih: 25-29.9
        - Obesitas: ≥ 30
        
        **Insulin:** Kadar insulin (μIU/mL)
        - Normal: 2.6-24.9
        - Tinggi: > 25
        
        **Usia:** Dalam tahun
        """)
    
    # Input Section
    st.markdown("## 📝 Input Data Pasien")
    
    col1, col2 = st.columns(2)
    
    with col1:
        glucose = st.number_input(
            "🍯 Glucose (mg/dL)", 
            min_value=0.0, 
            max_value=500.0, 
            step=0.1,
            help="Kadar gula darah puasa"
        )
        
        insulin = st.number_input(
            "💉 Insulin (μIU/mL)", 
            min_value=0.0, 
            max_value=900.0, 
            step=0.1,
            help="Kadar insulin dalam darah"
        )
    
    with col2:
        age = st.number_input(
            "🎂 Usia (tahun)", 
            min_value=0, 
            max_value=120, 
            step=1,
            help="Usia pasien dalam tahun"
        )
        
        bmi = st.number_input(
            "⚖️ BMI (kg/m²)", 
            min_value=0.0, 
            max_value=100.0, 
            step=0.1,
            help="Indeks Massa Tubuh"
        )
    
    # Tombol analisis
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔍 Analisis Risiko Diabetes", key="analyze"):
            if glucose > 0 and age > 0 and bmi > 0 and insulin > 0:
                # Progress bar untuk efek loading
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)
                
                st.markdown("---")
                
                # Hasil diagnosa
                diagnosis, recommendation, risk_factors, risk_level = diagnose_diabetes(glucose, age, bmi, insulin)
                
                # Tampilkan hasil dengan styling
                st.markdown("## 🩺 Hasil Analisis")
                
                if risk_level == "high":
                    st.markdown(f'<div class="risk-high"><h3>{diagnosis}</h3><p>{recommendation}</p></div>', 
                              unsafe_allow_html=True)
                elif risk_level == "medium":
                    st.markdown(f'<div class="risk-medium"><h3>{diagnosis}</h3><p>{recommendation}</p></div>', 
                              unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="risk-low"><h3>{diagnosis}</h3><p>{recommendation}</p></div>', 
                              unsafe_allow_html=True)
                
                # Faktor risiko
                if risk_factors:
                    st.markdown("## ⚠️ Faktor Risiko Teridentifikasi")
                    for factor in risk_factors:
                        st.markdown(f"- {factor}")
                
                # Rekomendasi
                show_recommendations(risk_level)
                
                # Grafik perbandingan dengan nilai normal
                st.markdown("## 📈 Perbandingan dengan Nilai Normal")
                
                data = {
                    'Parameter': ['Glucose', 'BMI', 'Insulin', 'Age'],
                    'Nilai Anda': [glucose, bmi, insulin, age],
                    'Batas Normal': [100, 25, 25, 0],
                    'Batas Tinggi': [126, 30, 100, 65]
                }
                
                df = pd.DataFrame(data)
                
                fig = px.bar(df, x='Parameter', y=['Nilai Anda', 'Batas Normal', 'Batas Tinggi'],
                           title="Perbandingan Parameter dengan Nilai Rujukan",
                           barmode='group',
                           color_discrete_map={
                               'Nilai Anda': '#667eea',
                               'Batas Normal': '#4caf50',
                               'Batas Tinggi': '#ff9800'
                           })
                
                fig.update_layout(
                    height=400,
                    xaxis_title="Parameter Kesehatan",
                    yaxis_title="Nilai",
                    legend_title="Kategori"
                )
                
                st.plotly_chart(fig, use_container_width=True)
                   
            else:
                st.error("⚠️ Mohon lengkapi semua data input!")

if __name__ == "__main__":
    main()