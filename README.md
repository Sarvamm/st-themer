# ST Themer 🎨

**ST Themer** is a lightweight and interactive Streamlit app that allows you to visually customize your app's theme and save those themes as reusable `.toml` presets.

---

## ✨ Features

- 🎨 Live color customization:
  - Primary color
  - Background color
  - Secondary background color
  - Text color
- ⚡ Instant theme application using Streamlit's `.streamlit/config.toml`
- 💾 Save your custom themes to the `Saved_Themes/` directory
- 📁 Organized project layout with support for multiple pages and assets

---

## 🚀 How to Run

1. **Clone this repository**
   ```bash
   git clone https://github.com/your-username/st-themer.git
   cd st-themer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the app**
   ```bash
   streamlit run App.py
   ```

---

## 📂 Project Structure

```
theme-generator/
├── .github/
│   └── FUNDING.yml
├── .streamlit/
│   └── config.toml              # Active Streamlit theme
├── assets/
│   └── logo.png                 # App branding or UI icons
├── pages/
│   ├── About.py                 # Optional About/Info page
│   └── Main.py                  # Theme customization interface
├── App.py                       # Main entry point
├── LICENSE
├── README.md
└── requirements.txt             # Required Python packages
```

---

## 🛠️ How It Works

- The user selects color values using Streamlit’s `color_picker`.
- Pressing **Apply** updates `.streamlit/config.toml` instantly and reruns the app.
- Pressing **Save Preset** stores the selected colors in a TOML file at:
  ```
  Saved_Themes/<preset_name>/config.toml
  ```
  Example content:
  ```toml
  primaryColor = "#ff4b4b"
  backgroundColor = "#0e1117"
  secondaryBackgroundColor = "#262730"
  textColor = "#fafafa"
  ```

---


## 📜 License

Licensed under the Non-Profit Open Software License version 3.0

---

