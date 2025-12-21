import streamlit as st
from openai import OpenAI

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Nano Banana Campaign Director (V10)",
    page_icon="🍌",
    layout="wide"
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stButton>button {
        width: 100%;
        background-color: #FFD700; /* Banana Yellow */
        color: black;
        border-radius: 8px;
        padding: 16px;
        font-weight: 800;
        font-size: 18px;
        border: none;
        margin-top: 20px;
    }
    .stButton>button:hover {
        background-color: #E5C100;
        color: black;
    }
    h1, h2, h3 { font-family: 'Helvetica', sans-serif; }
    .stSelectbox, .stTextInput, .stTextArea { margin-bottom: 10px; }
    
    div.block-container { padding-top: 2rem; }
    /* Checkbox Styles */
    div[data-testid="stCheckbox"] label span {
        font-weight: 600;
    }
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
    
    st.info("Optimiert für **Nano Banana** (Gemini 2.5 Image / Veo).")
    st.markdown("---")
    st.caption("V10: 360° Orbit, Profi-Licht & Shot-Focus.")

# --- HEADER ---
st.title("🍌 Nano Banana Campaign Director (V10)")
st.markdown("Das ultimative Tool: **360° Kamera-Fahrten**, **Licht-Architektur** und **Fokus-Steuerung**.")
st.divider()

# --- 1. MODEL LOOK & REALISMUS ---
st.subheader("1. Model & Realismus")
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
    freckles = st.radio("Haut-Basis", ["Klare Haut", "Sommersprossen"], horizontal=True)
    
    # REALISMUS FEATURES
    use_vellus = st.checkbox("Vellus Hair (Flaum)", value=True, help="Fügt ultra-realistische Härchen auf der Haut hinzu.")
    use_imperfections = st.checkbox("Natural Imperfections", value=False, help="Asymmetrie und kleine Makel.")

# --- 2. KLEIDUNG & POSE ---
st.markdown("---")
st.subheader("2. Kleidung, Pose & Moments")
c_outfit, c_pose = st.columns([1, 2])

with c_outfit:
    clothing = st.text_area("Was trägt das Model? (Outfit)", 
                            placeholder="z.B. Weißes Seidenkleid, Schwarzer Rollkragenpullover...",
                            height=100)
    makeup = st.select_slider("Make-up", options=["No Makeup", "Natural/Clean", "Soft Glam", "High Fashion"])

with c_pose:
    use_candid = st.checkbox("📸 Candid Moment (Ungestellt)?", value=False)
    
    p1, p2, p3 = st.columns(3)
    
    if use_candid:
        with p1:
            candid_moment = st.selectbox("Moment", ["Caught off guard", "Laughing mid-sentence", "Fixing Hair", "Looking past camera"])
            pose = f"Candid Shot: {candid_moment}"
            gaze = "Natural / Ungestellt"
            expression = "Authentic"
    else:
        with p1:
            pose = st.selectbox("Körperhaltung", 
                                ["Standing Upright (Power Pose)", "Relaxed Leaning", "Walking towards Camera", 
                                 "Sitting Elegantly", "Dynamic Action", "Over the Shoulder"])
        with p2:
            gaze = st.selectbox("Blickrichtung", 
                                ["Straight into Camera", "Looking away (Dreamy)", "Looking down", "Looking up"])
        with p3:
            expression = st.selectbox("Gesichtsausdruck", 
                                      ["Neutral & Cool", "Confident Smile", "Laughing", "Fierce/Intense", "Seductive"])
    
    wind = "Natural movement" if use_candid else st.select_slider("Haar-Dynamik", options=["Static", "Soft Breeze", "Strong Wind"], value="Soft Breeze")


# --- 3. TECHNIK, LICHT & KAMERA (NEU: 360 ORBIT & LIGHTING) ---
st.markdown("---")
st.subheader("3. Kamera, Licht & Atmosphäre")
t1, t2, t3, t4 = st.columns(4)

with t1:
    # NEU: 360 ORBIT
    cam_move = st.selectbox("Kamera-Bewegung (Video)", 
                            ["360° Orbit (Circle around Model)", "Static Tripod", "Slow Zoom In", "Handheld", "Drone Orbit (Landscape)"])
    
    # NEU: SHOT FOCUS
    shot_focus = st.selectbox("Shot Focus (Wer ist der Star?)",
                              ["Balanced (Model + Product)", "Model Hero (Face Focus)", "Product Hero (Blurry Model)", "Detail Shot (Hands/Product Only)"])

with t2:
    # NEU: LICHT ARCHITEKT
    lighting = st.selectbox("Licht-Setup (Profi)", 
                            ["Butterfly Lighting (Beauty)", "Split Lighting (Dramatic Side)", "Rim Light / Backlight (Halo Effect)", 
                             "Rembrandt (Classic)", "Golden Hour (Sun)", "Softbox Studio (Clean)", "Neon / Cyberpunk"])

with t3:
    film_look = st.selectbox("Film Look", 
                             ["Standard Commercial", "Kodak Portra 400", "Teal & Orange", "Black & White", "Pastel/Dreamy", "Moody/Dark"])
    framing = st.selectbox("Ausschnitt", ["Extreme Close-Up", "Portrait", "Medium Shot", "Full Body"])

with t4:
    lens = st.selectbox("Objektiv", ["85mm (Portrait)", "100mm Macro", "35mm (Lifestyle)", "24mm (Wide)"])
    
    use_aperture = st.checkbox("Manuelle Blende?", value=False)
    aperture = st.selectbox("Blende", ["f/1.2 (Bokeh)", "f/1.8 (Soft)", "f/8.0 (Sharp)"]) if use_aperture else None

# --- 4. FORMAT & PRODUKT ---
st.markdown("---")
st.subheader("4. Format, Produkt & Referenz")
k1, k2 = st.columns([1, 1])

with k1:
    product = st.text_input("Produkt / Thema", placeholder="z.B. Goldene Halskette")
    
    st.markdown("---")
    use_size = st.checkbox("Spezifische Größe (cm)?", value=False)
    if use_size:
        obj_type = st.radio("Objekt Art", ["Kettenanhänger", "Objekt"], horizontal=True)
        obj_size = st.slider(f"Größe (cm)", 0.5, 5.0, 2.5, 0.1)
    else:
        obj_type, obj_size = None, None
    
    st.markdown("---")
    wear_product = st.checkbox("Referenz-Bild hochladen?", value=False, help="Prompt für Bild-Upload optimieren.")

with k2:
    st.markdown("**Bildformat:**")
    aspect_ratio = st.selectbox("Format", ["Querformat (16:9)", "Hochformat (9:16)", "Quadrat (1:1)", "Cinematic (21:9)"])

    st.markdown("**Hintergrund:**")
    weather = st.selectbox("Wetter", ["Clear/Sunny", "Cloudy", "Rainy/Wet", "Foggy", "Snowing"])
    
    bg_mode = st.radio("Hintergrund", ["Szenisch", "Einfarbig"], horizontal=True, label_visibility="collapsed")
    if bg_mode == "Szenisch":
        bg_sel = st.selectbox("Szenario", ["Clean White Studio", "Dark Luxury", "Warm Beige", "City Street", "Nature", "Blue Sky", "Abstract"])
        final_bg = f"{bg_sel} background"
    else:
        col = st.color_picker("Farbe", "#FF0044")
        final_bg = f"Solid background hex {col}"

# --- PROMPT GENERATION ---
def generate_prompt():
    if not api_key:
        st.error("⚠️ API Key fehlt!")
        return None
    client = OpenAI(api_key=api_key)

    # FORMAT
    if "16:9" in aspect_ratio: ar_text = "Aspect Ratio: 16:9"
    elif "9:16" in aspect_ratio: ar_text = "Aspect Ratio: 9:16 (Vertical)"
    elif "21:9" in aspect_ratio: ar_text = "Aspect Ratio: 21:9"
    else: ar_text = "Aspect Ratio: 1:1"

    # KAMERA BEWEGUNG LOGIK (360 ORBIT)
    if "360° Orbit" in cam_move:
        move_instr = "CAMERA MOVEMENT: Smooth continuous 360-degree orbital camera movement circling the central subject, keeping the model perfectly centered while revealing the outfit and product from all angles."
    else:
        move_instr = f"CAMERA MOVEMENT: {cam_move}."

    # GRÖSSE
    size_instr = ""
    if use_size and obj_size:
        size_instr = f"SCALE: Object exactly {obj_size}cm in size."

    # PRODUKT & FOKUS
    if wear_product:
        prod_instr = (f"CRITICAL: User provides REFERENCE IMAGE for '{product}'. "
                      f"Prompt: 'Use reference image for exact item blending.' Focus: '{product}'. {size_instr}")
        ref_reminder = "✅ WICHTIG: Referenzbild hochladen!"
    else:
        prod_instr = f"Campaign for '{product}'. Focus on vibe. {size_instr}"
        ref_reminder = ""

    # SHOT FOCUS LOGIK
    if shot_focus == "Model Hero (Face Focus)":
        focus_instr = "FOCUS: Sharp focus on the model's face and expression. Background and product slightly secondary."
    elif shot_focus == "Product Hero (Blurry Model)":
        focus_instr = f"FOCUS: Extreme focus on the '{product}'. The model's face should be slightly out of focus (bokeh) to highlight the item."
    elif shot_focus == "Detail Shot (Hands/Product Only)":
        focus_instr = f"FOCUS: Macro detail shot of '{product}'. Crop in tight, faces might be cut off."
    else:
        focus_instr = "FOCUS: Perfectly balanced focus between model and product."

    outfit_instr = f"OUTFIT: {clothing}." if clothing else "OUTFIT: High-fashion minimal."

    # REALISMUS
    skin_details = freckles
    if use_vellus: skin_details += ", visible vellus hair (peach fuzz) on cheeks"
    if use_imperfections: skin_details += ", natural asymmetry, micro-imperfections"

    tech_specs = f"{framing}, {lens}, {lighting}"
    if use_aperture and aperture: tech_specs += f", {aperture}"

    system_prompt = """
    You are an expert Prompt Engineer for Nano Banana (Gemini 2.5 Image).
    Write a single, comprehensive prompt triggering HYPER-REALISM.
    Include specific camera movements (especially 360 orbit if requested) and lighting setups.
    """

    user_prompt = f"""
    Write a Nano Banana prompt:
    
    SUBJECT: {gender}, {age}, {ethnicity}.
    LOOK: {hair_texture}, {hair_color}, {hair_style}, {wind}. {eye_color} eyes.
    SKIN: {skin_details}. (Subsurface scattering).
    
    POSE: {pose}. GAZE: {gaze}.
    
    CONTEXT: {prod_instr}
    FOCUS PRIORITY: {focus_instr}
    
    SCENE: {final_bg}. ATMOSPHERE: {weather}. COLOR: {film_look}.
    TECH: {tech_specs}.
    
    {move_instr}
    
    FORMAT: {ar_text}.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": system_prompt}, {"role": "user", "content": user_prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content, ref_reminder
    except Exception as e:
        st.error(f"Error: {e}")
        return None, None

# --- OUTPUT ---
if st.button("NANO BANANA PROMPT GENERIEREN 🍌"):
    if not product:
        st.warning("Bitte Produkt eingeben!")
    else:
        with st.spinner("Rendere Prompt..."):
            res, reminder = generate_prompt()
            if res:
                st.success("Prompt fertig!")
                if reminder: st.info(reminder)
                st.code(res, language="text")
