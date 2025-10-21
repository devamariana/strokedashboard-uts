from flask import Flask, render_template
import plotly.express as px
import plotly.io as pio
from utils.preprocessing import clean_data

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Ambil data yang sudah dibersihkan
    df = clean_data()

    # List untuk menampung grafik
    charts = []

    # Grafik 1: Distribusi Jenis Kelamin (PIE)
    fig1 = px.pie(df, names='gender', title='Distribusi Jenis Kelamin')
    fig1.update_layout(
        margin=dict(t=50, b=50, l=50, r=50),
        legend=dict(orientation="h", y=-0.2, x=0.3),
        width=600, height=400
    )
    charts.append(pio.to_html(fig1, full_html=False))

    # Grafik 2: Distribusi Hipertensi
    fig2 = px.histogram(df, x='hypertension', title='Distribusi Hipertensi')
    charts.append(pio.to_html(fig2, full_html=False))

    # Grafik 3: Rata-rata Usia Berdasarkan Stroke
    fig3 = px.box(df, x='stroke', y='age', title='Rata-rata Usia Berdasarkan Stroke')
    charts.append(pio.to_html(fig3, full_html=False))

    # Grafik 4: Hubungan Usia dan BMI
    fig4 = px.scatter(df, x='age', y='bmi', color='stroke', title='Hubungan Usia dan BMI')
    charts.append(pio.to_html(fig4, full_html=False))

    # Grafik 5: Rata-rata Glukosa Berdasarkan Gender
    fig5 = px.bar(df, x='gender', y='avg_glucose_level', title='Rata-rata Glukosa Berdasarkan Gender')
    charts.append(pio.to_html(fig5, full_html=False))

    # Statistik deskriptif
    statistik_html = df.describe().to_html(classes='table table-striped', border=0)

    # Kirim ke template
    return render_template(
        'dashboard.html',
        charts=charts,
        total_data=len(df),
        total_atribut=len(df.columns),
        persentase_stroke=round(df['stroke'].mean() * 100, 2),
        statistik_html=statistik_html
    )

if __name__ == '__main__':
    app.run(debug=True)
