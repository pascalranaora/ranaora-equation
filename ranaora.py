# ranaora.py
# The Ranaora Equation: CO₂ = P × (W/P) × (E/W) × (F/E)
# Interactive Plotly dashboard – works out-of-the-box

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# -------------------------------------------------
# 1. Load data (replace with real sources later)
# -------------------------------------------------
df = pd.read_csv("data.csv")

# -------------------------------------------------
# 2. Compute Ranaora terms
# -------------------------------------------------
df["W_per_P"] = df["Wellbeing_Score"] / df["Population"]
df["E_per_W"] = df["Energy_TWh"] * 1e9 / df["Wellbeing_Score"]          # kWh per wellbeing unit
df["F_per_E"] = df["CO2_Mt"] * 1e6 / (df["Energy_TWh"] * 1e9)          # kg CO₂ / kWh
df["CO2_calc"] = (
    df["Population"] * df["W_per_P"] * df["E_per_W"] * df["F_per_E"]
)

# -------------------------------------------------
# 3. Build the 2×2 subplot grid
# -------------------------------------------------
fig = make_subplots(
    rows=2,
    cols=2,
    subplot_titles=(
        "1. Population",
        "2. Wellbeing per Capita",
        "3. kWh per Unit Wellbeing (↓ better)",
        "4. CO₂ per kWh (↓ better)",
    ),
    # IMPORTANT: enable secondary_y on the Population panel
    specs=[
        [{"secondary_y": True}, {"secondary_y": False}],
        [{"secondary_y": False}, {"secondary_y": False}],
    ],
)

# -------------------------------------------------
# 4. Colors
# -------------------------------------------------
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728"]

# -------------------------------------------------
# 5. Add traces
# -------------------------------------------------
# Row 1, Col 1 – Population + CO₂ validation (secondary axis)
fig.add_trace(
    go.Scatter(x=df["Year"], y=df["Population"] / 1e9,
               name="Population (B)", line=dict(color=colors[0])),
    row=1, col=1
)
fig.add_trace(
    go.Scatter(x=df["Year"], y=df["CO2_Mt"],
               name="Actual CO₂ (Mt)", line=dict(color="black", dash="dot")),
    row=1, col=1, secondary_y=True
)

# Row 1, Col 2 – Wellbeing per capita
fig.add_trace(
    go.Scatter(x=df["Year"], y=df["W_per_P"],
               name="Wellbeing / Capita", line=dict(color=colors[1])),
    row=1, col=2
)

# Row 2, Col 1 – kWh per wellbeing unit
fig.add_trace(
    go.Scatter(x=df["Year"], y=df["E_per_W"],
               name="kWh / Wellbeing Unit", line=dict(color=colors[2])),
    row=2, col=1
)

# Row 2, Col 2 – g CO₂ per kWh
fig.add_trace(
    go.Scatter(x=df["Year"], y=df["F_per_E"] * 1000,
               name="g CO₂ / kWh", line=dict(color=colors[3])),
    row=2, col=2
)

# -------------------------------------------------
# 6. Layout & axis titles
# -------------------------------------------------
fig.update_layout(
    title_text="🌍 <b>The Ranaora Equation</b><br>"
               "<sub>CO₂ = P × (W/P) × (E/W) × (F/E)</sub>",
    height=720,
    template="plotly_white",
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
)

# Y-axis titles
fig.update_yaxes(title_text="Population (Billions)", row=1, col=1)
fig.update_yaxes(title_text="CO₂ Emissions (Mt)", secondary_y=True, row=1, col=1)

fig.update_yaxes(title_text="Wellbeing Index / Person", row=1, col=2)
fig.update_yaxes(title_text="kWh per Wellbeing Unit", row=2, col=1)
fig.update_yaxes(title_text="g CO₂ per kWh", row=2, col=2)

# -------------------------------------------------
# 7. Show & export
# -------------------------------------------------
fig.show()
fig.write_html("ranaora_dashboard.html")
print("Dashboard saved → ranaora_dashboard.html")