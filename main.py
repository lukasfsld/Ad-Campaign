import streamlit as st
from openai import OpenAI

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Veo Campaign Director Ultimate V5",
    page_icon="🎬",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #000000;
        color: white;
        border-radius: 8px;
        padding: 16px;
        font-weight: 700;
        font-size: 18px;
        border: none;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background-color: #333333;
        color: white;
    }
    h1, h2, h3 { font-family: 'Helvetica', sans-serif; }
    .stSelectbox, .stTextInput, .stTextArea { margin-bottom: 10px; }
    
    /* Boxen visuell etwas trennen */
    div.block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)


    else:
        api_key = st.text_input("OpenAI API Key", type="password")
    st.info("Optimiert für Google Veo & Midjourney v6.")

# --- HEADER ---
st.title("🎬 Veo Campaign Director Ultimate (V5)")
st.markdown("Profi-Tool für **High-End Werbekampagnen**. Volle Kontrolle über **Format (Aspect Ratio)**, Größe, Styling und Produkt.")
st.divider()

# --- 1. MODEL LOOK ---
st.subheader("1. Model Details")
col1, col2, col3, col4 = st.columns(4)

with col1:
    gender = st.selectbox("Geschlecht", ["Female Model", "Male Model", "Non-binary Model"])
    age = st.select_slider("Alter", options=["18-24", "25-34", "35-44", "45-55", "60+"], value="25-34")

with col2:
    ethnicity = st.text_input("Ethnie / Look", value="olive skin tone", placeholder="z.B. Scandinavian")
    hair_color = st.text_input("Haarfarbe", value="dark brown")

with col3:
    hair_texture = st.select_slider("Haarstruktur", options=["Straight (Glatt)", "Wavy (Wellig)", "Curly (Lockig)", "Coily (Afro)"], value="Wavy (Wellig)")
    hair_style = st.selectbox("Frisur-Stil", ["Loose & Open", "Sleek Ponytail", "Messy Bun", "Short Cut", "Bob Cut"])

with col4:
    eye_color = st.text_input("Augenfarbe", value="green")
    freckles = st.radio("Haut-Details", ["Klare Haut", "Sommersprossen"], horizontal=True)

# --- 2. KLEIDUNG & POSE ---
st.markdown("---")
st.subheader("2. Kleidung, Pose & Make-up")
c_outfit, c_pose = st.columns([1, 2])

with c_outfit:
    clothing = st.text_area("Was trägt das Model? (Outfit)", 
                            placeholder="z.B. Weißes Seidenkleid, Schwarzer Rollkragenpullover...",
                            height=100)
    makeup = st.select_slider("Make-up", options=["No Makeup", "Natural/Clean", "Soft Glam", "High Fashion"])


    # GRÖSSEN LOGIK
    if obj_type == "Kettenanhänger (Schmuck)":
  
