import streamlit as st
from openai import OpenAI

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Veo Campaign Director Ultimate",
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
    .stSelectbox, .stTextInput { margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: API KEY ---
with st.sidebar:
    st.header("🔑 Settings")
    if "OPENAI_API_KEY" in st.secrets:
        st.success("API Key aktiv (Secrets) ✅")
        api_key = st.secrets["OPENAI_API_KEY"]
    else:
        api_key = st.text_input("OpenAI API Key", type="password")

# --- HEADER ---
st.title("🎬 Veo Campaign Director Ultimate")
st.markdown("Der Profi-Generator für **High-End Werbekampagnen**. Kontrolliere Haut, Licht, Produkt und jetzt auch die **Pose**.")
st.divider()

# --- 1. MODEL LOOK ---
st.subheader("1. Model & Styling")
col1, col2, col3, col4 = st.columns(4)

with col1:
    gender = st.selectbox("Geschlecht", ["Female Model", "Male Model", "Non-binary Model"])
    age = st.select_slider("Alter", options=["18-24", "25-34", "35-44", "45-55", "60+"], value="25-34")

with col2:
    ethnicity = st.text_input("Ethnie / Look", value="olive skin tone", placeholder="z.B. Scandinavian")
    hair_color = st.text_input("Haarfarbe", value="dark brown")

with col3:
    hair_style = st.selectbox("Frisur", ["Loose & Natural", "Sleek Ponytail", "Wet Look", "Messy Bun", "Short Buzz Cut"])
    eye_color = st.text_input("Augenfarbe", value="green")

with col4:
    freckles = st.radio("Haut-Details", ["Klare Haut", "Sommersprossen"], horizontal=True)
    makeup = st.select_slider("Make-up", options=["No Makeup", "Natural/Clean", "Soft Glam", "High Fashion"])

# --- 2. POSE & STIMMUNG (NEU!) ---
st.markdown("---")
st.subheader("2. Pose, Blick & Vibe")
p1, p2, p3, p4 = st.columns(4)

with p1:
    # NEU: Pose Auswahl
    pose = st.selectbox("Körperhaltung (Pose)", 
                        ["Standing Upright (Power Pose)", "Relaxed Leaning", "Walking towards Camera", 
                         "Sitting Elegantly", "Over the Shoulder", "Dynamic Action/Motion"])

with p2:
    # NEU: Blickrichtung
    gaze = st.selectbox("Blickrichtung", 
                        ["Straight into Camera (Direct Eye Contact)", "Looking away (Dreamy)", 
                         "Looking down (Thoughtful)", "Looking up (Hopeful)"])

with p3:
    expression = st.selectbox("Gesichtsausdruck", 
                              ["Neutral & Cool", "Confident Smile", "Laughing/Authentic", "Fierce/Intense", "Seductive"])

with p4:
    wind = st.select_slider("Dynamik (Wind)", options=["Static", "Soft Breeze", "Strong Wind"], value="Soft Breeze")

# --- 3. TECHNIK & SETTING ---
st.markdown("---")
st.subheader("3. Technik, Haut & Licht")
t1, t2, t3, t4 = st.columns(4)

with t1:
    skin_finish = st.selectbox("Haut-Finish", ["Natural Matte", "Dewy & Glowy", "Sweaty/Athletic", "Glass Skin"])

with t2:
    lighting = st.selectbox("Licht-Setzung", ["Soft Beauty Light", "Golden Hour (Sun)", "Rembrandt (Moody)", "Cinematic Contrast", "Neon"])

with t3:
    framing = st.selectbox("Ausschnitt", ["Extreme Close-Up (Face)", "Portrait (Head & Shoulders)", "Medium Shot (Waist Up)", "Full Body"])

with t4:
    lens = st.selectbox("Objektiv", ["85mm (Portrait)", "100mm Macro (Details)", "35mm (Lifestyle)", "24mm (Wide/Fashion)"])

# --- 4. KAMPAGNE & PRODUKT ---
st.markdown("---")
st.subheader("4. Die Kampagne (Produkt)")
c1, c2 = st.columns([1, 1])

with c1:
    product = st.text_input("Produkt / Thema", placeholder="z.B. Luxus Handtasche, Anti-Aging Serum")
    wear_product = st.checkbox("Model trägt/hält das Produkt sichtbar?", value=False)

with c2:
    bg = st.selectbox("Hintergrund", 
                      ["Clean White Studio", "Dark Luxury Background", "Warm Beige Tone", 
                       "Blurred City Street", "Nature/Forest", "Blue Sky", "Abstract Gradient"])

# --- GPT GENERATION ---
def generate_prompt():
    if not api_key:
        st.error("⚠️ API Key fehlt!")
        return None

    client = OpenAI(api_key=api_key)

    # Produkt-Logik
    if wear_product:
        prod_instr = f"The model is WEARING/HOLDING the product '{product}' visibly. It is the focal point."
    else:
        prod_instr = f"Campaign for '{product}', but model is NOT wearing it visibly. Focus on the VIBE of the brand."

    system_prompt = """
    You are a Senior Art Director for High-End Commercial AI Generation.
    Write a single, highly detailed prompt for Veo/Midjourney.
    
    CRITICAL REQUIREMENTS:
    1. SKIN: "subsurface scattering, micropore texture, visible pores, vellus hair". NO plastic skin.
    2. POSE: Strictly follow the defined pose and gaze.
    3. CAMERA: Include technical camera specs provided.
    """

    user_prompt = f"""
    Create a luxury ad prompt:
    
    MODEL: {gender}, {age}, {ethnicity}.
    STYLE: {hair_color} hair ({hair_style}, {wind}), {eye_color} eyes.
    SKIN/MAKEUP: {freckles}, {skin_finish} finish, {makeup} makeup.
    
    POSE & ACTION:
    - Pose: {pose}
    - Gaze: {gaze}
    - Expression: {expression}
    
    CONTEXT: {prod_instr}
    SETTING: {bg} background. Lighting: {lighting}.
    
    TECHNICAL: {framing}, shot on {lens} lens. High fidelity, raw photo style.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error: {e}")
        return None

# --- OUTPUT ---
if st.button("AD-CAMPAIGN STARTEN 🚀"):
    if not product:
        st.warning("Bitte gib ein Produkt ein!")
    else:
        with st.spinner("Writing Director's Treatment..."):
            res = generate_prompt()
            if res:
                st.success("Prompt Generiert!")
                st.code(res, language="text")
                st.caption("Ready for Veo / Midjourney / Flux")
