import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Streamlit app title
st.title("Climate-Based HAAY AWG System Simulation")

# Interactive temperature and humidity sliders for user input
temperature = st.slider("Adjust Temperature (°C)", min_value=-10, max_value=50, value=25)
humidity = st.slider("Adjust Humidity (%)", min_value=0, max_value=100, value=50)

# Determine activated system based on temperature and humidity values with more detailed conditions
if temperature > 35 and humidity < 30:
    system_status = "Activated: Advanced Desiccant System with High Solar Power"
    system_info = ("This system extracts moisture using an advanced desiccant process with optimized solar power "
                   "to handle extremely high temperatures and low humidity.")
elif 30 < temperature <= 35 and 20 <= humidity < 50:
    system_status = "Activated: Hybrid Desiccant and Cooling System"
    system_info = ("Combines desiccant and active cooling to maintain efficiency in high temperatures and moderate humidity.")
elif 25 <= temperature <= 35 and 50 <= humidity <= 80:
    system_status = "Activated: Full Cooling System, High Fan Speed, Renewable Energy"
    system_info = ("A full cooling system is engaged with high fan speed for efficient water condensation in warm, humid conditions.")
elif 20 <= temperature < 30 and 30 <= humidity < 60:
    system_status = "Activated: Standard Cooling Plates, Optimal Fan Speed"
    system_info = ("Standard cooling plates operate at optimal fan speed to provide efficient water extraction under moderate conditions.")
elif 10 <= temperature < 25 and 20 <= humidity < 40:
    system_status = "Activated: Energy-Saving Cooling Mode"
    system_info = ("An energy-saving mode activates with moderate cooling and reduced fan speed for balanced energy usage.")
elif 5 <= temperature < 20 and 10 <= humidity < 30:
    system_status = "Activated: Pre-Heating and Low-Power Desiccant System"
    system_info = ("Pre-heating technology prevents frost, and a low-power desiccant system helps maintain water extraction in cooler, drier air.")
elif temperature < 10 and humidity >= 30:
    system_status = "Activated: Pre-Heating with Moderate Cooling Plates"
    system_info = ("Pre-heating is combined with moderate cooling plates to prevent frost and ensure functionality in cold, moist air.")
elif temperature < 0 and humidity < 20:
    system_status = "Activated: Extreme Pre-Heating and High-Efficiency Desiccant System"
    system_info = ("An extreme pre-heating system is engaged, along with a high-efficiency desiccant process, for very cold and dry climates.")
else:
    # Expanded fallback to minimize standby
    system_status = "Activated: General Climate Adaptation Mode"
    system_info = ("This general mode adapts dynamically to various conditions, ensuring basic water extraction at suboptimal settings.")

# Display the current activated system and its function
st.subheader("System Status:")
st.write(system_status)
st.write(f"**What this setting does:** {system_info}")






