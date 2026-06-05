import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página do Streamlit
st.set_page_config(page_title="Dashboard Agrícola", layout="wide")
st.title("🌱 Dashboard de Monitoramento e Irrigação")

# --- SIMULAÇÃO DE DADOS PARA TESTE IMEDIATO ---
datas = pd.date_range(end=pd.Timestamp.now(), periods=15, freq='D')
df = pd.DataFrame({
    'data_coleta': datas,
    'umidade': [35, 38, 28, 45, 52, 48, 33, 25, 42, 55, 60, 48, 39, 31, 29],
    'fosforo': [12] * 15,
    'potassio': [24] * 15,
    'ph': [6.2, 6.3, 6.1, 6.5, 6.4, 6.2, 6.0, 5.8, 6.2, 6.1, 6.3, 6.2, 6.4, 6.1, 6.0],
    'status_irrigacao': ['Desligado', 'Desligado', 'Ligado', 'Ligado', 'Desligado', 'Desligado', 'Desligado', 'Ligado', 'Ligado', 'Ligado', 'Desligado', 'Desligado', 'Desligado', 'Desligado', 'Ligado'],
    'temperatura': [28, 29, 31, 26, 24, 25, 29, 32, 27, 23, 22, 25, 28, 30, 31],
    'chuva_prevista': [0, 2, 0, 15, 25, 5, 0, 0, 8, 30, 12, 0, 0, 0, 0]
})

dados_atuais = df.iloc[-1]

# --- LÓGICA DE RECOMENDAÇÃO ---
def gerar_sugestao(umidade, temp, chuva):
    if umidade < 30 and chuva < 5:
        return "🚨 Crítico: Ligar irrigação imediatamente. Solo seco e sem previsão de chuva.", "error"
    elif umidade < 40 and temp > 30 and chuva < 10:
        return "⚠️ Alerta: Ligar irrigação em nível moderado. Alta evapotranspiração.", "warning"
    elif chuva > 20:
        return f"🛑 Desligar: Chuva forte prevista ({chuva:.1f}mm). Risco de encharcar o solo.", "success"
    else:
        return "✅ Normal: Umidade do solo adequada para as condições climáticas atuais.", "info"

sugestao_texto, tipo_alerta = gerar_sugestao(dados_atuais['umidade'], dados_atuais['temperatura'], dados_atuais['chuva_prevista'])

# --- LAYOUT DO DASHBOARD ---
col_status, col_Aviso = st.columns(2)
with col_status:
    st.metric(label="Status Atual do Sistema", value=dados_atuais['status_irrigacao'])
with col_Aviso:
    st.subheader("💡 Sugestão de Manejo")
    if tipo_alerta == "error": st.error(sugestao_texto)
    elif tipo_alerta == "warning": st.warning(sugestao_texto)
    elif tipo_alerta == "success": st.success(sugestao_texto)
    else: st.info(sugestao_texto)

st.markdown("---")
st.subheader("📊 Condições do Solo (Última Leitura)")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Umidade Atual", f"{dados_atuais['umidade']}%")
kpi2.metric("Fósforo (P)", f"{dados_atuais['fosforo']} mg/dm³")
kpi3.metric("Potássio (K)", f"{dados_atuais['potassio']} mg/dm³")
kpi4.metric("pH do Solo", f"{dados_atuais['ph']}")

st.markdown("---")
st.subheader("📈 Histórico de Monitoramento")
col_graf1, col_graf2 = st.columns(2)
with col_graf1:
    fig_umidade = px.line(df, x='data_coleta', y='umidade', title="Evolução da Umidade do Solo (%)", markers=True)
    st.plotly_chart(fig_umidade, use_container_width=True)
with col_graf2:
    fig_ph = px.line(df, x='data_coleta', y='ph', title="Histórico do pH do Solo", markers=True)
    st.plotly_chart(fig_ph, use_container_width=True)
