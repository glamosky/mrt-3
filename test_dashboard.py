import streamlit as st
import os

st.title("MRT-3 Dashboard Test")

# Check current directory
st.write("Current working directory:", os.getcwd())

# List files in current directory
st.write("Files in current directory:")
for file in os.listdir('.'):
    st.write(f"- {file}")

# Check if data directory exists
if os.path.exists('data'):
    st.write("✅ Data directory exists")
    st.write("Files in data directory:")
    for file in os.listdir('data'):
        st.write(f"- {file}")
else:
    st.write("❌ Data directory not found")

# Try to import required packages
try:
    import pandas as pd
    st.write("✅ pandas imported successfully")
except ImportError as e:
    st.write(f"❌ pandas import failed: {e}")

try:
    import plotly.express as px
    st.write("✅ plotly imported successfully")
except ImportError as e:
    st.write(f"❌ plotly import failed: {e}")

try:
    import numpy as np
    st.write("✅ numpy imported successfully")
except ImportError as e:
    st.write(f"❌ numpy import failed: {e}")
