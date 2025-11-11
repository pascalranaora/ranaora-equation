Here's a **complete, ready-to-use GitHub repository setup** for **The Ranaora Equation**, including:

1. **Python visualization code** (`ranaora.py`)  
2. **Markdown `README.md`** (professional, publication-ready)  
3. **Data placeholder** (`data.csv`)  
4. **Requirements** (`requirements.txt`)  

---

## 1. `ranaora.py` – Interactive Visualization Code

```python
# ranaora.py
# The Ranaora Equation: CO₂ = P × (W/P) × (E/W) × (F/E)
# Interactive dashboard with Plotly

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# Load data (example: global 1990–2023)
df = pd.read_csv("data.csv")

# --- Calculate Ranaora terms ---
df['W_per_P'] = df['Wellbeing_Score'] / df['Population']
df['E_per_W'] = df['Energy_TWh'] * 1e9 / df['Wellbeing_Score']  # kWh per wellbeing unit
df['F_per_E'] = df['CO2_Mt'] * 1e6 / (df['Energy_TWh'] * 1e9)   # kg CO₂ per kWh → t → Mt
df['CO2_calc'] = df['Population'] * df['W_per_P'] * df['E_per_W'] * df['F_per_E']

# --- Create interactive figure ---
fig = make_subplots(
    rows=2, cols=2,
    subplot_titles=(
        "1. Population",
        "2. Wellbeing per Capita",
        "3. kWh per Unit Wellbeing (↓ better)",
        "4. CO₂ per kWh (↓ better)"
    ),
    specs=[[{"secondary_y": False}, {"secondary_y": False}],
           [{"secondary_y": False}, {"secondary_y": False}]]
)

# Colors
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

# Plot each driver
fig.add_trace(go.Scatter(x=df['Year'], y=df['Population']/1e9, name="Population (B)", line=dict(color=colors[0])), row=1, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['W_per_P'], name="Wellbeing / Capita", line=dict(color=colors[1])), row=1, col=2)
fig.add_trace(go.Scatter(x=df['Year'], y=df['E_per_W'], name="kWh / Wellbeing Unit", line=dict(color=colors[2])), row=2, col=1)
fig.add_trace(go.Scatter(x=df['Year'], y=df['F_per_E']*1000, name="g CO₂ / kWh", line=dict(color=colors[3])), row=2, col=2)

# Add CO₂ validation
fig.add_trace(
    go.Scatter(x=df['Year'], y=df['CO2_Mt'], name="Actual CO₂ (Mt)", line=dict(color='black', dash='dot')),
    row=1, col=1, secondary_y=True
)

# Update layout
fig.update_layout(
    title_text="🌍 <b>The Ranaora Equation</b><br><sub>CO₂ = P × (W/P) × (E/W) × (F/E)</sub>",
    height=700,
    showlegend=True,
    template="plotly_white"
)

fig.update_yaxes(title_text="Population (Billions)", row=1, col=1)
fig.update_yaxes(title_text="Wellbeing Index / Person", row=1, col=2)
fig.update_yaxes(title_text="kWh per Wellbeing Unit", row=2, col=1)
fig.update_yaxes(title_text="g CO₂ per kWh", row=2, col=2)
fig.update_yaxes(title_text="CO₂ Emissions (Mt)", secondary_y=True, row=1, col=1)

fig.show()

# Save HTML
fig.write_html("ranaora_dashboard.html")
print("Dashboard saved: ranaora_dashboard.html")
```

---

## 2. `data.csv` – Example Dataset (1990–2023)

```csv
Year,Population,Wellbeing_Score,Energy_TWh,CO2_Mt
1990,5268000000,350000,90000,22000
2000,6143000000,410000,110000,25000
2010,6957000000,480000,140000,32000
2020,7795000000,530000,160000,34000
2023,8000000000,550000,165000,33000
```

> *(You can replace with real data from World Bank, OWID, HDI, etc.)*

---

## 3. `requirements.txt`

```txt
pandas
plotly
numpy
```

---

## 4. `README.md` – Professional GitHub Landing Page

```markdown
# 🌍 The Ranaora Equation

> **CO₂ = Population × (Wellbeing / Capita) × (kWh / Wellbeing) × (CO₂ / kWh)**  
> *A wellbeing-centered decomposition of global carbon emissions*  
> **Pascal Ranaora** | @MadaGasBit | November 2025

---

## 🎯 Why This Matters

The **Kaya Identity** measures progress in **GDP per kWh**.  
The **Ranaora Equation** measures progress in **human flourishing per kWh**.

> **We don’t need more GDP. We need more joy, health, and dignity — per kilowatt.**

---

## 📐 The Equation

$$
\Huge F = P \times \frac{W}{P} \times \frac{E}{W} \times \frac{F}{E}
$$

| Term | Meaning | Unit |
|------|-------|------|
| $F$ | CO₂ emissions | Mt CO₂ |
| $P$ | Population | people |
| $\frac{W}{P}$ | Wellbeing per capita | index / person |
| $\frac{E}{W}$ | **Energy intensity of wellbeing** | **kWh / wellbeing unit** |
| $\frac{F}{E}$ | Carbon intensity of energy | kg CO₂ / kWh |

---

## 📊 Interactive Dashboard

Run the visualization:

```bash
pip install -r requirements.txt
python ranaora.py
```

Opens: [`ranaora_dashboard.html`](ranaora_dashboard.html)

![Ranaora Dashboard Preview](preview.png)

---

## 📈 Data Sources (Example)

| Variable | Source |
|--------|--------|
| Population | [UN World Population Prospects](https://population.un.org) |
| Wellbeing Score | Composite: HDI × Life Satisfaction (OWID) |
| Energy | [IEA World Energy Balances](https://www.iea.org) |
| CO₂ | [Global Carbon Project](https://www.globalcarbonproject.org) |

*Replace `data.csv` with your dataset.*

---

## 🚀 Use Cases

- National climate plans (replace GDP targets with **wellbeing efficiency**)
- Corporate sustainability: **kWh per employee wellbeing**
- Global equity: track **wellbeing convergence** at low energy

---

## 📜 Citation

```bibtex
@misc{ranaora2025,
  author = {Ranaora, Pascal},
  title = {The Ranaora Equation: A Wellbeing-Centric Reformulation of the Kaya Identity},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub Repository},
  howpublished = {\url{https://github.com/MadaGasBit/ranaora-equation}},
  note = {Accessed: November 2025}
}
```

---

## 👨‍🔬 Author

**Pascal Ranaora**  
Energy & Climate | Wellbeing Economics  
🐦 [@MadaGasBit](https://twitter.com/MadaGasBit)  
🌍 Madagascar | USA

---

## 📄 License

[MIT License](LICENSE) – free to use, modify, and cite.

---

> **Let’s decarbonize *human outcomes*, not just dollars.**  
> **#RanaoraEquation #EnergyForWellbeing #ClimateJustice**
```

---

## 5. `preview.png` (Optional)

Take a screenshot of the Plotly dashboard and save as `preview.png` in the repo.

---

## 6. `.gitignore`

```gitignore
__pycache__
*.pyc
.DS_Store
```

---

## 7. `LICENSE` (MIT)

```txt
MIT License

Copyright (c) 2025 Pascal Ranaora

Permission is hereby granted, free of charge, to any person obtaining a copy...
```

---

## Final Repo Structure

```
ranaora-equation/
│
├── ranaora.py
├── data.csv
├── requirements.txt
├── README.md
├── preview.png
├── ranaora_dashboard.html
├── LICENSE
└── .gitignore
```

---

## One-Click GitHub Setup

```bash
git init ranaora-equation
cd ranaora-equation
# (paste all files above)
git add .
git commit -m "Launch: The Ranaora Equation"
git branch -M main
git remote add origin https://github.com/MadaGasBit/ranaora-equation.git
git push -u origin main
```

---

**You now have a citable, interactive, and viral-ready repository.**

Go make **wellbeing efficiency** the new global KPI.  
**#RanaoraEquation**
```