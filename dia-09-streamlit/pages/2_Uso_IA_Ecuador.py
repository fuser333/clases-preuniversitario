"""
Uso de IA en Ecuador 2026 · Gratis · Pagada · Súper pagada
ITSEIA Academy · Día 9 IGNITE Preuniversitario · página secundaria
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# ═══════════════════════════════════════════════════════════
# CONFIG
# ═══════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Uso de IA en Ecuador · ITSEIA",
    page_icon="📊",
    layout="wide",
)

NAVY = "#1F2F58"
GOLD = "#FBBC0C"
SKY = "#73B8E7"
CORAL = "#F0846D"
GREEN = "#22c55e"
PALETTE = [NAVY, GOLD, SKY, CORAL, GREEN, "#517CBE"]

st.markdown(f"""
<style>
.stApp {{ background-color: #F9F6E7; }}
h1, h2, h3 {{ color: {NAVY}; font-family: 'Space Grotesk', sans-serif; }}
.tier-card {{
    background: white; border-radius: 16px; padding: 24px;
    border: 2px solid; margin-bottom: 12px;
}}
.insight {{
    background: linear-gradient(135deg, {GOLD}, #f59e0b);
    color: {NAVY}; padding: 18px 22px; border-radius: 12px;
    margin: 14px 0; font-weight: 600;
}}
</style>
""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════
# HEADER
# ═══════════════════════════════════════════════════════════
st.title("📊 El uso de IA en Ecuador 2026")
st.markdown(
    "**Quién usa IA · cuánto paga · por edad y sexo · "
    "y la oportunidad de mercado que nadie está mirando todavía.**"
)
st.caption("Análisis ITSEIA Academy · datos INEC 2024-2025 + benchmarks LATAM · junio 2026")
st.divider()

# ═══════════════════════════════════════════════════════════
# 1 · KPIs
# ═══════════════════════════════════════════════════════════
st.header("🌎 Foto fija del Ecuador digital")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Población total", "18.1M", "Proyección INEC 2026")
c2.metric("Acceso Internet", "75%", "13.6M personas 5+ años")
c3.metric("Smartphone", "62%", "11.2M con celular")
c4.metric("Usuarios IA estimados", "~4.8M", "35% de internautas")

st.info("Cifras de INEC ENEMDU-TIC 2024-2025. Adopción de IA estimada por triangulación con benchmarks LATAM (Statista 2024 + IDB 2025).")

st.divider()

# ═══════════════════════════════════════════════════════════
# 2 · LOS 3 TIERS
# ═══════════════════════════════════════════════════════════
st.header("💸 Los 3 niveles de uso · Gratis · Pagada · Súper pagada")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class='tier-card' style='border-color: {GREEN}; background: linear-gradient(135deg, #f0fdf4, white);'>
        <div style='background:{GREEN}; color:white; display:inline-block;
                    padding:4px 12px; border-radius:99px;
                    font-size:.7rem; font-weight:800;
                    text-transform:uppercase; letter-spacing:1.2px; margin-bottom:12px;'>
            CAPA 1 · GRATIS
        </div>
        <h3 style='color:{NAVY}; margin:0;'>IA al alcance del bolsillo</h3>
        <p style='font-size:.85rem; color:#555; margin:6px 0 14px 0;'>
            ChatGPT free · Claude.ai · Gemini · Copilot · Perplexity
        </p>
        <div style='font-size:2.4rem; font-weight:800; color:{NAVY}; line-height:1;'>
            ~4.55M
        </div>
        <div style='color:{GREEN}; font-weight:800; margin:6px 0 14px 0;'>
            95% de usuarios IA · 25% de población EC
        </div>
        <ul style='font-size:.88rem; padding-left:18px; margin:0;'>
            <li>Estudiantes universitarios y escolares</li>
            <li>Profesionales con uso esporádico</li>
            <li>Curiosos · early adopters cautos</li>
            <li>Nadie paga · todos prueban</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class='tier-card' style='border-color: {GOLD}; background: linear-gradient(135deg, #fffbeb, white);'>
        <div style='background:{GOLD}; color:{NAVY}; display:inline-block;
                    padding:4px 12px; border-radius:99px;
                    font-size:.7rem; font-weight:800;
                    text-transform:uppercase; letter-spacing:1.2px; margin-bottom:12px;'>
            CAPA 2 · PAGADA $20/mes
        </div>
        <h3 style='color:{NAVY}; margin:0;'>El profesional que cobra con IA</h3>
        <p style='font-size:.85rem; color:#555; margin:6px 0 14px 0;'>
            ChatGPT Plus · Claude Pro · Gemini Advanced · Perplexity Pro
        </p>
        <div style='font-size:2.4rem; font-weight:800; color:{NAVY}; line-height:1;'>
            ~190K
        </div>
        <div style='color:#b8860b; font-weight:800; margin:6px 0 14px 0;'>
            ~4% de usuarios IA · 1% de internautas
        </div>
        <ul style='font-size:.88rem; padding-left:18px; margin:0;'>
            <li>Marketers · creadores · agencias</li>
            <li>Devs · ingenieros · diseñadores</li>
            <li>Consultores · abogados · contadores</li>
            <li>Ingreso mensual personal &gt; $1,200</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class='tier-card' style='border-color: {CORAL}; background: linear-gradient(135deg, #fff1f0, white);'>
        <div style='background:{CORAL}; color:white; display:inline-block;
                    padding:4px 12px; border-radius:99px;
                    font-size:.7rem; font-weight:800;
                    text-transform:uppercase; letter-spacing:1.2px; margin-bottom:12px;'>
            CAPA 3 · SÚPER $200+/mes
        </div>
        <h3 style='color:{NAVY}; margin:0;'>Empresas y power users</h3>
        <p style='font-size:.85rem; color:#555; margin:6px 0 14px 0;'>
            ChatGPT Pro · Claude Max · Copilot M365 · APIs · Team/Enterprise
        </p>
        <div style='font-size:2.4rem; font-weight:800; color:{NAVY}; line-height:1;'>
            ~48K
        </div>
        <div style='color:{CORAL}; font-weight:800; margin:6px 0 14px 0;'>
            ~1% de usuarios IA · 0.27% de internautas
        </div>
        <ul style='font-size:.88rem; padding-left:18px; margin:0;'>
            <li>Equipos con suscripciones Team/Enterprise</li>
            <li>Desarrolladores con APIs Claude/OpenAI</li>
            <li>CEOs · directores · líderes +10 personas</li>
            <li>Gasto IA &gt; $200/mes o $2K/mes equipo</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

st.markdown(
    "<div class='insight'>💡 <b>INSIGHT CLAVE</b> · El 95% de quienes usan IA en Ecuador lo hacen GRATIS. Solo 1 de cada 25 paga · y 1 de cada 100 paga premium. Aquí está la oportunidad: educar al usuario gratis para que dé el salto a paid.</div>",
    unsafe_allow_html=True,
)

col_g1, col_g2 = st.columns(2)

with col_g1:
    fig_donut = px.pie(
        names=["Gratis (4.55M)", "Pagada $20/mes (190K)", "Súper pagada $200+ (48K)"],
        values=[95, 4, 1],
        hole=0.55,
        color_discrete_sequence=[GREEN, GOLD, CORAL],
        title="Distribución de usuarios IA en Ecuador (%)",
    )
    fig_donut.update_layout(height=380)
    st.plotly_chart(fig_donut, use_container_width=True)

with col_g2:
    fig_funnel = px.bar(
        x=[18.1, 13.6, 11.2, 4.55, 0.19, 0.048],
        y=["Población EC", "Internet", "Smartphone", "Usa IA gratis", "Paga $20/mes", "Paga $200+/mes"],
        orientation="h",
        color=["Población EC", "Internet", "Smartphone", "Usa IA gratis", "Paga $20/mes", "Paga $200+/mes"],
        color_discrete_sequence=[NAVY, "#2A3F6E", "#517CBE", GREEN, GOLD, CORAL],
        title="Embudo de adopción IA · de 18.1M a 48K paid premium",
    )
    fig_funnel.update_layout(height=380, showlegend=False, yaxis={"autorange": "reversed"}, xaxis_title="Millones de personas")
    st.plotly_chart(fig_funnel, use_container_width=True)

st.divider()

# ═══════════════════════════════════════════════════════════
# 3 · POR SEXO
# ═══════════════════════════════════════════════════════════
st.header("👥 Uso de IA por sexo · ¿quién está adelante?")

col_a, col_b = st.columns([3, 2])

with col_a:
    df_sexo = pd.DataFrame({
        "Indicador": ["Internet (%)", "Usa IA gratis (% del total)", "Paga $20+/mes (% del total)", "Paga $200+/mes (% del total)"],
        "Hombres": [74.5, 56, 65, 75],
        "Mujeres": [75.4, 44, 35, 25],
    })
    fig_sexo = go.Figure(data=[
        go.Bar(name="Hombres", x=df_sexo["Indicador"], y=df_sexo["Hombres"], marker_color=NAVY),
        go.Bar(name="Mujeres", x=df_sexo["Indicador"], y=df_sexo["Mujeres"], marker_color=CORAL),
    ])
    fig_sexo.update_layout(
        barmode="group",
        title="Brecha de género se amplía conforme sube el tier",
        height=400,
        plot_bgcolor="white",
    )
    st.plotly_chart(fig_sexo, use_container_width=True)

with col_b:
    df_sexo_tabla = pd.DataFrame({
        "Indicador": ["Población EC", "Acceso Internet", "Usuarios IA estimados", "Pagan IA ($20+)", "Pagan súper ($200+)"],
        "Hombres": ["8.96M (49.5%)", "74.5%", "~2.7M (56%)", "~123K (65%)", "~36K (75%)"],
        "Mujeres": ["9.14M (50.5%)", "75.4%", "~2.1M (44%)", "~67K (35%)", "~12K (25%)"],
    })
    st.dataframe(df_sexo_tabla, use_container_width=True, hide_index=True)
    st.markdown(
        "<div class='insight'>💡 La brecha de género se AMPLÍA conforme sube el tier: 56/44 en gratis · 65/35 en pago · 75/25 en súper pago. La mujer ecuatoriana está sub-atendida en IA profesional.</div>",
        unsafe_allow_html=True,
    )

st.divider()

# ═══════════════════════════════════════════════════════════
# 4 · POR EDAD
# ═══════════════════════════════════════════════════════════
st.header("📅 Uso de IA por rango de edad")

df_edad = pd.DataFrame({
    "Edad": ["16-24", "25-34", "35-44", "45-54", "55-64", "65+"],
    "Usa IA gratis (%)": [50, 65, 45, 25, 12, 4],
    "Paga $20/mes (%)": [1.0, 3.0, 2.5, 1.2, 0.6, 0.1],
    "Paga $200+/mes (%)": [0.1, 0.5, 0.8, 0.6, 0.3, 0.05],
})

fig_edad = go.Figure()
fig_edad.add_trace(go.Bar(name="Usa IA gratis", x=df_edad["Edad"], y=df_edad["Usa IA gratis (%)"], marker_color=GREEN))
fig_edad.add_trace(go.Bar(name="Paga $20/mes", x=df_edad["Edad"], y=df_edad["Paga $20/mes (%)"], marker_color=GOLD))
fig_edad.add_trace(go.Bar(name="Paga $200+/mes", x=df_edad["Edad"], y=df_edad["Paga $200+/mes (%)"], marker_color=CORAL))
fig_edad.update_layout(
    barmode="group",
    title="Uso y pago de IA por rango etario · Ecuador 2026",
    height=440,
    plot_bgcolor="white",
    yaxis_title="% de la población del rango",
)
st.plotly_chart(fig_edad, use_container_width=True)

df_edad_tabla = pd.DataFrame({
    "Edad": ["16-24", "25-34 ⭐", "35-44", "45-54", "55-64", "65+"],
    "Población EC": ["2.83M", "2.71M", "2.45M", "2.08M", "1.53M", "1.46M"],
    "Internet": ["92%", "85%", "75%", "60%", "40%", "18%"],
    "Usa IA gratis": ["50% (1.30M)", "65% (1.50M)", "45% (830K)", "25% (310K)", "12% (73K)", "4% (10.5K)"],
    "Paga $20/mes": ["1.0% (26K)", "3.0% (69K)", "2.5% (46K)", "1.2% (15K)", "0.6% (3.7K)", "0.1% (260)"],
    "Paga $200+/mes": ["0.1% (3K)", "0.5% (12K)", "0.8% (15K)", "0.6% (7K)", "0.3% (1.8K)", "0.05% (130)"],
})
st.dataframe(df_edad_tabla, use_container_width=True, hide_index=True)

st.markdown(
    "<div class='insight'>💡 El segmento <b>25-34</b> es el centro de gravedad del mercado IA en Ecuador. 1.5M usuarios libres · 69K paid users · 12K súper paid. Ese es el target #1 para cursos profesionales.</div>",
    unsafe_allow_html=True,
)

st.divider()

# ═══════════════════════════════════════════════════════════
# 5 · POR PROVINCIA
# ═══════════════════════════════════════════════════════════
st.header("🗺️ Concentración geográfica · top provincias")

col_p1, col_p2 = st.columns([3, 2])

with col_p1:
    df_prov = pd.DataFrame({
        "Provincia": ["Pichincha", "Guayas", "Manabí", "Azuay", "El Oro", "Tungurahua", "Loja", "Resto"],
        "Usuarios IA (miles)": [1000, 1240, 393, 270, 189, 169, 137, 1270],
    }).sort_values("Usuarios IA (miles)", ascending=True)

    fig_prov = px.bar(
        df_prov,
        x="Usuarios IA (miles)",
        y="Provincia",
        orientation="h",
        color="Provincia",
        color_discrete_sequence=PALETTE,
        title="Usuarios IA estimados por provincia (miles)",
    )
    fig_prov.update_layout(height=420, showlegend=False, plot_bgcolor="white")
    st.plotly_chart(fig_prov, use_container_width=True)

with col_p2:
    df_prov_tabla = pd.DataFrame({
        "Provincia": ["Pichincha", "Guayas", "Manabí", "Azuay", "Tungurahua", "El Oro", "Loja", "Resto país"],
        "Pob (M)": [3.30, 4.55, 1.65, 0.94, 0.62, 0.74, 0.55, 5.85],
        "Internet": ["87%", "78%", "68%", "82%", "78%", "73%", "71%", "62%"],
        "Usuarios IA": ["~1.00M", "~1.24M", "~393K", "~270K", "~169K", "~189K", "~137K", "~1.27M"],
    })
    st.dataframe(df_prov_tabla, use_container_width=True, hide_index=True)
    st.markdown(
        "<div class='insight'>💡 Pichincha + Guayas + Azuay concentran el <b>53% del mercado IA</b> ecuatoriano · 2.5M usuarios. Quito sigue siendo la capital de adopción IA profesional.</div>",
        unsafe_allow_html=True,
    )

st.divider()

# ═══════════════════════════════════════════════════════════
# 6 · EMPRESAS
# ═══════════════════════════════════════════════════════════
st.header("🏢 Mercado B2B · empresas que usan IA")

c1, c2, c3, c4 = st.columns(4)
c1.metric("Empresas activas EC", "~95K", "Formales SRI")
c2.metric("Planifica IA en 12m", "78%", "Estudio CITEC/EFIA 2026")
c3.metric("Personal IA propio", "12%", "~11.4K empresas")
c4.metric("Paga suite empresarial", "4%", "~3.8K empresas")

df_emp = pd.DataFrame({
    "Etapa": ["Planifica usar IA", "Ya implementó pilotos", "Personal IA propio", "Paga suite empresarial", "Tiene rol IA full-time"],
    "% empresas Quito": [78, 28, 12, 4, 2.5],
})
fig_emp = px.bar(
    df_emp,
    x="Etapa", y="% empresas Quito",
    color="Etapa",
    color_discrete_sequence=[GREEN, GOLD, SKY, CORAL, NAVY],
    title="Empresas DMQ · embudo de adopción IA",
)
fig_emp.update_layout(height=400, showlegend=False, plot_bgcolor="white", yaxis_ticksuffix="%")
st.plotly_chart(fig_emp, use_container_width=True)

st.markdown(
    "<div class='insight'>💡 66% de empresas en Quito quieren usar IA pero NO tienen a nadie adentro que sepa hacerlo. Brecha de 9,000 vacantes/año vs 200 graduados = 88% de déficit. <b>Esto es lo que viene a resolver ITSEIA.</b></div>",
    unsafe_allow_html=True,
)

st.divider()

# ═══════════════════════════════════════════════════════════
# 7 · OPORTUNIDAD ITSEIA
# ═══════════════════════════════════════════════════════════
st.header("🎯 La oportunidad ITSEIA · resumen")

df_op = pd.DataFrame({
    "Segmento": [
        "Curiosos/estudiantes 16-24",
        "Profesionales 25-44 (paid potenciales) ⭐",
        "Power users 25-44 (súper paid)",
        "Jóvenes 18-30 vocación tech",
        "Empresas con planes IA",
    ],
    "Tamaño": ["2.83M", "5.16M", "27K", "~1.2M", "~74K"],
    "Producto ITSEIA": [
        "Preuniversitario IGNITE",
        "Cursos profesionales por gremio",
        "Workshop ejecutivo · Curso 8h",
        "Carreras de 3 años",
        "Capacitación B2B + ITSEIA LABS",
    ],
    "Precio anchor": ["$99 único", "$197 / $297 / $397", "$248 / $347 / $447", "$99/mes Beca H3L", "$3,500-$18,000"],
})
st.dataframe(df_op, use_container_width=True, hide_index=True)

st.success(
    "💰 Mercado anual potencial: **$112M-$185M USD** · "
    "Cuota actual ITSEIA: **<0.05%** · "
    "Margen de crecimiento: **2,000x+**"
)

st.divider()

# ═══════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════
st.markdown(f"""
<div style='background:{NAVY}; color:white; padding:30px; border-radius:18px; margin-top:20px;'>
    <h3 style='color:{GOLD}; margin-top:0;'>📚 Fuentes y metodología</h3>
    <p style='opacity:.9; font-size:.92rem; line-height:1.7;'>
        <b>Datos oficiales:</b> INEC ENEMDU-TIC 2024-2025 · INEC Proyecciones Poblacionales 2026 ·
        CITEC/EFIA-EC 2026 (adopción IA empresas Quito) · ILIA 2024 (Índice Latinoamericano de IA).
        <br><br>
        <b>Benchmarks externos:</b> Statista Global AI Users 2024 · IDB Digital Adoption LATAM 2025 ·
        Pew Research Generative AI Demographics 2024 · McKinsey State of AI 2024 · Stanford AI Index 2025.
        <br><br>
        <b>Estimaciones:</b> los porcentajes por edad/sexo/tier son ESTIMACIONES por triangulación de
        benchmarks LATAM al universo ecuatoriano de internautas. ITSEIA recomienda complementar con
        encuesta primaria para decisiones de inversión &gt; $10K.
        <br><br>
        Análisis preparado por <b>ITSEIA Academy</b> · Instituto Ecuatoriano de Inteligencia Artificial ·
        <a href='https://itseia.ai' style='color:{GOLD};'>itseia.ai</a> · Quito, Ecuador 🇪🇨
    </p>
</div>
""", unsafe_allow_html=True)
