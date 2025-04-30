import streamlit as st
from streamlit_extras.buy_me_a_coffee import button

version: str = "0.0.3"
logo: str = "./assets/logo.png"
coffee_username: str = "astrayn"

#Page setup
HomePage = st.Page(
    page="pages/Main.py",
    icon="🎨",
    title = "Streamlit Themer",
    default = True
)

AboutPage = st.Page(
    page="pages/About.py",
    icon="👤",    
    title = "About"
)

# Navigation Bar
pg = st.navigation([HomePage, AboutPage])


st.logo(logo, size='large')
with st.sidebar:
    st.markdown(14*"<br>", unsafe_allow_html=True)
    st.caption("Support me by clicking on this button 👇")
    button(username=coffee_username, floating=False, width=221)
    st.caption(version)



pg.run()