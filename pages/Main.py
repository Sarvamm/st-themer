import streamlit as st
import time
from datetime import datetime, time as dt_time
import toml
import json

data = toml.load(".streamlit/config.toml")
pr, bg, sb, tx = (
    data["theme"]["primaryColor"],
    data["theme"]["backgroundColor"],
    data["theme"]["secondaryBackgroundColor"],
    data["theme"]["textColor"],
)

if "theme_dict" not in st.session_state:
    st.session_state['theme_dict'] = json.load(open('themes.json', "r"))


st.header("Theme Customization")
st.markdown("Customize the theme colors of your Streamlit app.")
c1, c2, c3, c4 = st.columns([1, 1, 1, 1])

con1 = c1.container(border=True)
pr = con1.color_picker("Primary", pr)
con1.markdown(f"The current color is {pr}")

con2 = c2.container(border=True)
bg = con2.color_picker("Background", bg)
con2.markdown(f"The current color is {bg}")

con3 = c3.container(border=True)
sb = con3.color_picker("Secondary bg", sb)
con3.markdown(f"The current color is {sb}")

con4 = c4.container(border=True)
tx = con4.color_picker("Text", tx)
con4.markdown(f"The current color is {tx}")


k1, k2, k3, k4 = st.columns([1, 1, 1, 1])

def apply(pr, bg, sb, tx) -> None:
    data["theme"]["primaryColor"] = pr
    data["theme"]["backgroundColor"] = bg
    data["theme"]["secondaryBackgroundColor"] = sb
    data["theme"]["textColor"] = tx
    with open(".streamlit/config.toml", "w") as f:
        toml.dump(data, f)
    st.rerun()
    return None
        
        
if k1.button("Apply", key='main_page'):
    apply(pr, bg, sb, tx)
    


@st.dialog("Download")
def download_preset() -> None:
    try:
        if st.download_button("Download Config", open(".streamlit/config.toml", "r"), file_name="config.toml"):
            st.success("Downloaded")
    except Exception as e:
        st.error(str(e))

    return None


@st.dialog("Save Preset")
def save_preset() -> None:

    preset_name : str = st.text_input("Enter preset name")
    try:
        if st.button("save", key='save_preset_dialog'):
            st.session_state["theme_dict"][preset_name]  =  {
                    "primaryColor" : pr,
                    "backgroundColor" : bg,
                    "secondaryBackgroundColor" : sb,
                    "textColor" : tx
            }           
            
            st.success("Theme saved successfully!")
    except Exception as e:
        st.error(str(e))
    return None

@st.dialog("Load Preset")
def load_preset() -> None:
    theme_list = list(st.session_state["theme_dict"].keys())
    chosen = st.selectbox("Select a theme you want to apply", theme_list)
    
    if st.button('Apply', key='load_preset_dialog'):
        apply(
            pr=st.session_state["theme_dict"][chosen]['primaryColor'],
            bg=st.session_state["theme_dict"][chosen]['backgroundColor'],
            sb=st.session_state["theme_dict"][chosen]['secondaryBackgroundColor'],
            tx=st.session_state["theme_dict"][chosen]['textColor']
        )
        
    
    

if k2.button("Save preset"):
    save_preset()
    
if k3.button("Load preset"):
    load_preset()
    
if k4.button("Download preset"):
    download_preset()

st.divider()


def main():
    # Main content based on selection
    st.subheader("Here's how streamlit widgets will look like:")
    input_widgets()
    basic_widgets()
    status_elements()


def basic_widgets():
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("Regular Button"):
            st.write("Button clicked!")

    with col3:
        if st.button("Disabled Button", disabled=True):
            st.write("This won't show")

    with col2:
        if st.button("Button with Custom Color", type="primary"):
            st.write("Primary button clicked!")

    # Checkbox
    checkbox_state = st.checkbox("Show extra content", value=False)
    if checkbox_state:
        st.write("This content appears when checkbox is selected!")


def input_widgets():
    col1, col2 = st.columns(2)

    with col1:
        # Text inputs
        text_input = st.text_input("Text Input", "Default text")
        st.write("You entered:", text_input)

        password = st.text_input("Password Input", type="password")
        if password:
            st.write("Password entered (not shown for security)")

        text_area = st.text_area("Text Area (multi-line)", "Default\nMulti-line\nText")
        st.write("Text area content has", len(text_area.split()), "words")

    with col2:
        # Numeric inputs
        number = st.number_input("Number Input", min_value=0, max_value=100, value=50)
        st.write("Selected number:", number)

        slider_val = st.slider("Slider", min_value=0, max_value=100, value=50)
        st.write("Slider value:", slider_val)

        range_val = st.slider(
            "Range Slider", min_value=0, max_value=100, value=(25, 75)
        )
        st.write("Range selected:", range_val)

    # Selection widgets

    col1, col2, col3 = st.columns(3)

    with col1:
        option = st.selectbox("Select Box", ["Option 1", "Option 2", "Option 3"])
        st.write("Selected option:", option)

    with col2:
        multi_option = st.multiselect(
            "Multi-Select",
            ["Option A", "Option B", "Option C", "Option D"],
            ["Option A", "Option C"],
        )
        st.write("Selected options:", multi_option)

    with col3:
        radio_option = st.radio("Radio Button", ["Cat", "Dog", "Fish"])
        st.write("Selected animal:", radio_option)

    # Date and time inputs

    col1, col2, col3 = st.columns(3)

    with col1:
        date = st.date_input("Date Input", datetime.now())
        st.write("Selected date:", date)

    with col2:
        time_val = st.time_input("Time Input", dt_time(12, 0))
        st.write("Selected time:", time_val)

    with col3:
        color = st.color_picker("Color Picker", "#00BFFF")
        st.write("Selected color:", color)
        st.markdown(
            f"<div style='background-color:{color};width:100%;height:30px;'></div>",
            unsafe_allow_html=True,
        )


def status_elements():
    progress_bar = st.progress(0)

    if st.button("Run Progress Bar"):
        for percent_complete in range(101):
            time.sleep(0.01)
            progress_bar.progress(percent_complete)
        st.success("Progress complete!")


if __name__ == "__main__":
    main()
