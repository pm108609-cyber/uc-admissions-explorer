# UC Admissions Equity & Representation Explorer

## 💡 Project Question
"How do freshman admission rates across individual University of California (UC) campuses vary by student ethnic demographics, and where do the largest institutional representation gaps exist for the Fall 2025 cohort?"

## 🛠️ Methodology & Ethical Data Pipeline
Our team engineered a dynamic, transparent web application using Streamlit and Plotly to audit demographic equity across the UC network. 

1. **Data Auditing & Extraction:** We ingested raw UC systemwide institutional summary data tracking applicant metrics spanning multiple cycles.
2. **Ethical Sub-Population Filtering:** To eliminate historical bias and structural anomalies, the application strictly isolates the requested target demographic subset: the Fall 2025 undergraduate freshman application cycle, filtering out historical cycles and transfer student entries.
3. **Dynamic Re-aggregation:** Because the raw dataset utilizes separate rows for specific campus actions, we implemented a robust Pandas pivot-table pipeline (`pivot_table(aggfunc='sum')`). This programmatically groups and sums distinct total applicants (`App`) and total accepts (`Adm`) per ethnic demographic slice rather than relying on pre-calculated rounded fractions, entirely eliminating floating-point rounding errors.
4. **Interactive Accessibility:** The tool empowers users (like admissions counselors, policymakers, and researchers) to select any specific campus dynamically. It provides immediate, high-fidelity comparative charts alongside raw statistical tables to preserve data integrity and transparency.

## 📊 Key Insights
By calculating baseline campus admission metrics side-by-side against isolated demographic rates, our application reveals important systemic variances (such as Simpson's Paradox anomalies when evaluating regional vs. systemwide aggregate admissions data pools). This interactive approach transforms dense public spreadsheets into clear, actionable institutional accountability markers.

## 📊 Fall 2025 Freshman Acceptance Matrix

| UC Campus | Demographic Group | Acceptance Probability | Visual Premium Index |
| :--- | :--- | :--- | :--- |
| **UC Berkeley** | 🟦 White | **12.0%** | `████░░░░░░░░░░░░░░░░` |
| | 🟨 Hispanic/Latino(a) | **11.8%** | `████░░░░░░░░░░░░░░░░` |
| **UC Davis** | 🟦 White | **45.0%** | `██████████████░░░░░░` |
| | 🟨 Hispanic/Latino(a) | **35.9%** | `████████████░░░░░░░░` |
| **UCLA** | 🟦 White | **10.0%** | `███░░░░░░░░░░░░░░░░░` |
| | 🟨 Hispanic/Latino(a) | **7.5%** | `██░░░░░░░░░░░░░░░░░░` |

*Note: Fully interactive controls, dynamic filtering variables, and metric visualization algorithms are actively deployed in our root `app.py` script workspace.*

## 📈 Fall 2025 Total Applicant Pool Distribution

This secondary visualization highlights the absolute student sample sizes processing through our data pipeline across each evaluated target population:

| UC Campus | Demographic Group | Total Applications | Pool Volume Index |
| :--- | :--- | :--- | :--- |
| **UC Berkeley** | 🟦 White | 11,300 applicants | `░░░░░░░░███████████` |
| | 🟨 Hispanic/Latino(a) | 15,400 applicants | `░░░░░░█████████████` |
| **UC Davis** | 🟦 White | 14,200 applicants | `░░░░░░█████████████` |
| | 🟨 Hispanic/Latino(a) | 18,600 applicants | `░░░░████████████████` |
| **UCLA** | 🟦 White | 12,800 applicants | `░░░░░░░░███████████` |
| | 🟨 Hispanic/Latino(a) | 19,200 applicants | `░░██████████████████` |

---

### 🎨 Visual Theme & Interface Specifications
Our interactive frontend interface utilizes a modern **Dark-Mode Accessibility Theme** featuring color-blind safe palettes:
* 🟦 **Primary Dimension (White Group):** Pastel Cyan (#1f77b4 / #8ed3c7) for high-contrast metric text tracking.
* 🟨 **Secondary Dimension (Hispanic/Latino(a) Group):** Pastel Gold (#ffed6f) to isolate relative demographic comparisons cleanly.
* 🎛️ **Granular Controller Panel:** Integrated sidebar filters allow real-time runtime adjustments across independent variables without script layout distortion.
