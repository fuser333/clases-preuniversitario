"""
Dashboard Ventas Ecuador 2025 · ITSEIA Academy
Día 9 · IGNITE Preuniversitario · Streamlit demo

Ejecuta local con:
    streamlit run app_demo_dia_09.py

O súbelo a Streamlit Cloud para tener URL pública.
"""

from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

CSV_PATH = Path(__file__).parent / "ventas_ecuador_2025.csv"

# ═══════════════════════════════════════════════════════════
# CONFIGURACIÓN DE LA PÁGINA
# ═══════════════════════════════════════════════════════════
st.set_page_config(
    page_title="Dashboard Ventas Ecuador 2025 · ITSEIA",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Paleta de colores ITSEIA
NAVY = "#1F2F58"
GOLD = "#FBBC0C"
SKY = "#73B8E7"
CORAL = "#F0846D"
PALETTE = [NAVY, GOLD, SKY, CORAL, "#517CBE", "#2A3F6E"]

# CSS personalizado
st.markdown(
    f"""
    <style>
        .stApp {{ background-color: #F9F6E7; }}
        h1, h2, h3 {{ color: {NAVY}; font-family: 'Space Grotesk', sans-serif; }}
        .metric-container {{
            background: white; padding: 16px; border-radius: 12px;
            border-left: 5px solid {GOLD};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ═══════════════════════════════════════════════════════════
# SECCIÓN 1 · ENCABEZADO
# ═══════════════════════════════════════════════════════════
st.title("📊 Dashboard Ventas Ecuador 2025")
st.markdown(
    "**Análisis interactivo de ventas de productos tecnológicos por provincia · "
    "Preuniversitario IGNITE · ITSEIA Academy**"
)
st.divider()


# ═══════════════════════════════════════════════════════════
# SECCIÓN 2 · CARGA DEL CSV
# ═══════════════════════════════════════════════════════════
@st.cache_data
def cargar_datos():
    """Carga el CSV y normaliza columnas básicas."""
    df = pd.read_csv(CSV_PATH)
    # Aseguramos tipos
    df["unidades"] = df["unidades"].astype(int)
    df["precio_unitario"] = df["precio_unitario"].astype(float)
    df["ingresos_total"] = df["ingresos_total"].astype(float)
    return df


try:
    df = cargar_datos()
except FileNotFoundError:
    st.error(
        "⚠️ No encuentro el archivo `ventas_ecuador_2025.csv` en la misma carpeta de esta app.\n"
        "Súbelo y vuelve a ejecutar."
    )
    st.stop()

# ═══════════════════════════════════════════════════════════
# SECCIÓN 3 · SIDEBAR CON FILTROS
# ═══════════════════════════════════════════════════════════
st.sidebar.image("https://itseia.ai/logo.png", width=160)
st.sidebar.header("🎛️ Filtros")

provincias = sorted(df["provincia"].unique())
provincias_sel = st.sidebar.multiselect(
    "Provincia(s):",
    options=provincias,
    default=provincias,
    help="Selecciona una o más provincias",
)

productos = sorted(df["producto"].unique())
productos_sel = st.sidebar.multiselect(
    "Producto(s):",
    options=productos,
    default=productos,
)

precio_min = float(df["precio_unitario"].min())
precio_max = float(df["precio_unitario"].max())
rango_precio = st.sidebar.slider(
    "Rango de precio unitario (USD):",
    min_value=precio_min,
    max_value=precio_max,
    value=(precio_min, precio_max),
    step=10.0,
)

st.sidebar.divider()
st.sidebar.markdown("**📚 ITSEIA Academy**")
st.sidebar.markdown("Instituto Ecuatoriano de Inteligencia Artificial")
st.sidebar.markdown("🌐 [itseia.ai](https://itseia.ai)")
st.sidebar.markdown("📲 +593 99 748 9821")

# Aplicar filtros
df_f = df[
    (df["provincia"].isin(provincias_sel))
    & (df["producto"].isin(productos_sel))
    & (df["precio_unitario"].between(rango_precio[0], rango_precio[1]))
]

if df_f.empty:
    st.warning("No hay datos para los filtros seleccionados. Ajusta los filtros del sidebar.")
    st.stop()

# ═══════════════════════════════════════════════════════════
# SECCIÓN 4 · KPIs PRINCIPALES
# ═══════════════════════════════════════════════════════════
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="💰 Ingresos totales",
        value=f"${df_f['ingresos_total'].sum():,.0f}",
        delta=f"{len(df_f)} ventas",
    )

with col2:
    st.metric(
        label="📦 Unidades vendidas",
        value=f"{df_f['unidades'].sum():,.0f}",
    )

with col3:
    st.metric(
        label="🏷️ Precio promedio",
        value=f"${df_f['precio_unitario'].mean():.2f}",
    )

with col4:
    prov_top = df_f.groupby("provincia")["ingresos_total"].sum().idxmax()
    st.metric(
        label="🥇 Provincia top",
        value=prov_top,
    )

st.divider()

# ═══════════════════════════════════════════════════════════
# SECCIÓN 5 · GRÁFICOS INTERACTIVOS
# ═══════════════════════════════════════════════════════════
st.subheader("📈 Análisis visual")

col_g1, col_g2 = st.columns(2)

with col_g1:
    st.markdown("#### Ingresos por provincia")
    ingresos_prov = df_f.groupby("provincia", as_index=False)["ingresos_total"].sum()
    ingresos_prov = ingresos_prov.sort_values("ingresos_total", ascending=False)
    fig1 = px.bar(
        ingresos_prov,
        x="provincia",
        y="ingresos_total",
        color="provincia",
        color_discrete_sequence=PALETTE,
    )
    fig1.update_layout(
        plot_bgcolor="white",
        showlegend=False,
        height=380,
        title_font_color=NAVY,
    )
    st.plotly_chart(fig1, use_container_width=True)

with col_g2:
    st.markdown("#### Evolución mensual de ingresos")
    orden_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio",
                   "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    df_f["mes_lc"] = df_f["mes"].str.lower()
    ingresos_mes = (
        df_f.groupby("mes_lc", as_index=False)["ingresos_total"]
        .sum()
        .assign(orden=lambda d: d["mes_lc"].map({m: i for i, m in enumerate(orden_meses)}))
        .sort_values("orden")
    )
    fig2 = px.line(
        ingresos_mes,
        x="mes_lc",
        y="ingresos_total",
        markers=True,
        color_discrete_sequence=[GOLD],
    )
    fig2.update_layout(
        plot_bgcolor="white",
        height=380,
        xaxis_title="Mes",
        yaxis_title="Ingresos (USD)",
    )
    st.plotly_chart(fig2, use_container_width=True)

col_g3, col_g4 = st.columns(2)

with col_g3:
    st.markdown("#### Participación por producto")
    prod_share = df_f.groupby("producto", as_index=False)["ingresos_total"].sum()
    fig3 = px.pie(
        prod_share,
        values="ingresos_total",
        names="producto",
        hole=0.45,
        color_discrete_sequence=PALETTE,
    )
    fig3.update_layout(height=380)
    st.plotly_chart(fig3, use_container_width=True)

with col_g4:
    st.markdown("#### Precio vs Unidades (dispersión)")
    fig4 = px.scatter(
        df_f,
        x="precio_unitario",
        y="unidades",
        color="provincia",
        size="ingresos_total",
        hover_data=["producto", "mes"],
        color_discrete_sequence=PALETTE,
    )
    fig4.update_layout(plot_bgcolor="white", height=380)
    st.plotly_chart(fig4, use_container_width=True)

st.divider()

# ═══════════════════════════════════════════════════════════
# SECCIÓN 6 · TABLA Y DESCARGA
# ═══════════════════════════════════════════════════════════
st.subheader("📋 Datos filtrados")
st.dataframe(df_f.drop(columns=["mes_lc"], errors="ignore"), use_container_width=True, height=320)

csv_descarga = df_f.drop(columns=["mes_lc"], errors="ignore").to_csv(index=False).encode("utf-8")
st.download_button(
    label="⬇️ Descargar CSV filtrado",
    data=csv_descarga,
    file_name="ventas_ecuador_filtrado.csv",
    mime="text/csv",
)

# ═══════════════════════════════════════════════════════════
# FOOTER
# ═══════════════════════════════════════════════════════════
st.divider()
st.markdown(
    f"""
    <div style="text-align:center; color:{NAVY}; padding:18px;">
        <p>🚀 Construido en el <strong>Día 9 · Preuniversitario IGNITE de ITSEIA Academy</strong></p>
        <p>Instituto Ecuatoriano de Inteligencia Artificial · Quito, Ecuador 🇪🇨</p>
    </div>
    """,
    unsafe_allow_html=True,
)
