
### 🇩🇪 **Electricity Intensity in the German Economy (2010–2022)**

This Python script analyzes the **electricity intensity** of the German economy using time series input-output tables. Specifically, it measures the ratio of **electricity consumption (in monetary value)** to **gross output** (also in monetary value) across selected years: 2010, 2015, 2021, and 2022.

#### 🔍 **Purpose of the Code**

The code:

* Extracts electricity input to production (intermediate use)
* Computes total output value for each year
* Calculates the **intensity ratio** for electricity usage:

---

### 📐 **Mathematical Formula**

Let:

* $E_t$ = Total value of electricity input into production in year $t$ (in million euros)
* $X_t$ = Total domestic output (gross production) in year $t$ (in million euros)

Then, the **electricity intensity** in year $t$ is:

$$
I_t = \frac{E_t}{X_t}
$$

This ratio $I_t$ shows how much **electricity (in euros)** was consumed per **one euro of total production**.

---

### 📊 **Results of the Analysis**

| Year | Electricity Intensity $I_t$ | Interpretation                          |
| ---- | --------------------------- | --------------------------------------- |
| 2010 | 0.0133 (≈ 1.33%)            | High electricity use relative to output |
| 2015 | 0.0116 (≈ 1.16%)            | Efficiency improved slightly            |
| 2021 | 0.0124 (≈ 1.24%)            | Slight rebound in electricity usage     |
| 2022 | 0.0133 (≈ 1.33%)            | Back to 2010 levels                     |

**Interpretation:**
After a modest improvement in electricity efficiency from 2010 to 2015, electricity intensity rose again by 2022 — reaching the same level as in 2010. This pattern may reflect increased energy needs in certain sectors or structural shifts in production due to global or domestic shocks.

---

### 🌍 **Economic Interpretation & Outlook**

These numbers suggest that the **German economy's energy intensity** has not improved over the decade, raising questions about the pace of green transition, industrial restructuring, and energy efficiency.

The return to 2010 levels of electricity intensity by 2022 may hint at **energy-intensive recovery mechanisms**, potential **supply chain vulnerabilities**, or the early effects of the **Russia–Ukraine war**, which began in 2022 and had immediate implications for Europe’s energy market.

---

### 🔮 **Next Steps: Investigating the War's Impact (2024 IO Tables)**

As new input-output tables for **2024** become available, we will assess how the **Russia–Ukraine war** has structurally influenced Germany’s electricity usage and sectoral dependencies. This will offer insights into whether Germany is:

* Becoming more energy-resilient
* Accelerating or stalling in its transition to green technologies
* Redirecting production away from energy-intensive industries

---

### 🌐 **Comparative Analysis Ahead**

To place Germany in a global context, the next phase of this project will compare electricity intensity and technology shifts across:

* 🇪🇺 Other **European countries**
* 🇨🇳 **China**
* 🇺🇸 **United States**

This comparison will help us understand **where German industries are heading**, and whether they are maintaining competitiveness in a rapidly transforming global economy.



