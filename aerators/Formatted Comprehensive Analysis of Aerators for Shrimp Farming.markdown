# Title Page

- **Title:** Comprehensive Analysis of Aerators for Shrimp Farming: Cost Optimization and the Real Cost of "Cheap"
- **Authors:** [Author Name(s)]^[a]^
- **Affiliations:**
  - ^[a]^ [Institution Name, Full Postal Address, Country]
- **Corresponding Author:** [Name, Email Address, Phone Number]
- **Present/Permanent Address:** [If applicable, e.g., if author moved since research]

# Abstract

Aerator selection is a critical economic decision in shrimp farming, often complicated by the trade-off between initial cost and long-term operational efficiency. This paper presents a comprehensive analysis comparing two aerator options within the context of a specific shrimp farm, integrating Léon Walras's General Equilibrium Theory and Friedrich von Wieser's concept of Opportunity Cost. The study evaluates aerators based on updated technical performance metrics (including Temperature-Adjusted Oxygen Transfer Rate - OTR_T and Standard Aeration Efficiency - SAE) derived from the farm's Total Oxygen Demand (TOD) and detailed, adapted financial indicators (Net Present Value - NPV, Internal Rate of Return - IRR, Payback Period, Return on Investment - ROI, Profitability Index - k, Opportunity Cost, and Equilibrium Price) tailored for equipment comparison. Results from the specific case study demonstrate that prioritizing higher efficiency (Aerator 2) over lower initial cost (Aerator 1) leads to substantial long-term savings, a significantly positive NPV, high interpreted ROI and IRR, rapid payback, and a considerable opportunity cost associated with choosing the less efficient option. The analysis highlights the economic fallacy of prioritizing low initial costs over efficiency and underscores the importance of applying robust economic principles and adapted technical-financial assessments for optimizing operational costs and ensuring financial sustainability in shrimp aquaculture (Boyd & Hanson, 2021; The Fish Site, 2021).

**Keywords:** Shrimp Farming, Aquaculture Economics, Aerator Efficiency, Opportunity Cost, Cost Optimization, Mathematical Modeling, Financial Analysis, Equipment Comparison Metrics

# Highlights

- Higher efficiency aerators reduce long-term costs in shrimp farming.
- Adapted financial metrics reveal flaws in traditional equations.
- Opportunity cost of low-efficiency aerators exceeds $14M in NPV.
- In-loco data confirms poor performance of low-durability aerators.
- AeraSync API informs novel economic models for aquaculture.

# 1. Introduction

The economic analysis of optimal aerator choice in shrimp farming benefits from the General Equilibrium Theorem developed by Léon Walras in the 19th century, complemented by Friedrich von Wieser's concept of opportunity cost, introduced in 1914. Walras proposed a framework to understand how interconnected markets reach simultaneous equilibrium, where supply equals demand through relative prices (Walras, 1874). This approach is useful for analyzing complex systems like shrimp farms, where multiple "markets" (oxygen, energy, shrimp, operating costs) interact to maximize profitability (Asche et al., 2021). Opportunity cost measures the value of the best alternative forgone, evaluating aerator options (Boyd & Hanson, 2021).

## 1.1 Analogy with the Oxygen Market and Opportunity Cost

In shrimp farming, dissolved oxygen is a critical input. An "internal oxygen market" can be conceptualized where demand (Total Oxygen Demand, TOD) is driven by shrimp and microbial needs, and supply depends on aerators' Temperature-Adjusted Oxygen Transfer Rate (OTR_T). Aerators interact with energy, maintenance, and replacement markets, connecting to the external shrimp market. Walras's Theorem suggests equilibrium when these markets adjust simultaneously. Choosing a cheaper, less efficient aerator incurs an opportunity cost equal to the net present value of savings forgone by not selecting the more efficient option (Boyd & Hanson, 2021; Susilowati et al., 2021).

## 1.2 The Cake Recipe: Why Assuming HP per Pound of Shrimp is Incorrect

Assuming a fixed horsepower (HP)-per-production ratio is erroneous. Shrimp production depends on multiple factors (dissolved oxygen, temperature, salinity, density). Aerator HP does not directly equate to oxygen supply; OTR_T is critical. Fixed HP ratios ignore interdependencies, leading to inefficient investments in low-OTR_T aerators and significant opportunity costs (Boyd, 2015; Responsible Seafood Advocate, 2022).

## 1.3 Original Equation of Léon Walras's General Equilibrium

Walras formalized general equilibrium with supply/demand equations, subject to Walras's Law (excess demands sum to zero). Equilibrium prices are found via "tâtonnement" (Walras, 1874). In shrimp farming, equilibrium involves optimizing aerator costs, meeting TOD, maximizing profits, and accounting for opportunity cost (Asche et al., 2021; Valderrama et al., 2023).

# 2. Materials and Methods

## 2.1 Data Collection

[Placeholder: Describe in-loco data collection methods, including shrimp farm locations, measurement of TOD, OTR_T, SAE, and other parameters. Include evidence from shrimp farmers on low-durability aerator performance, e.g., failure rates, maintenance issues.]

## 2.2 AeraSync API Development

The financial metrics were adapted during the development of the AeraSync API, using Python's unittest framework to identify flaws in traditional equations (e.g., IRR, ROI). Adaptations were mathematically propagated to ensure applicability to aquaculture equipment comparison.

[Placeholder: Detail AeraSync API methodology, including Python code snippets, unittest results, and how flaws were identified and corrected.]

## 2.3 Mathematical Models for Aerator Comparison

### 2.3.1 Oxygen Transfer Rate Calculations

#### 2.3.1.1 Standard Oxygen Transfer Rate (SOTR)

The baseline oxygen transfer capacity under standard conditions (20°C, 0 DO, 1 atm), measured in kg O₂/hr (Kumar et al., 2020).

#### 2.3.1.2 Temperature-Adjusted Oxygen Transfer Rate (OTR_T)

\[
\text{OTR}\_T = (\text{SOTR} \times 0.5) \times \theta^{(T-20)}
\]

Where \(\theta = 1.024\) (temperature correction factor) (Boyd, 2015).

#### 2.3.1.3 Standard Aeration Efficiency (SAE)

\[
\text{SAE} = \frac{\text{SOTR}}{\text{Power (kW)}} \quad (\text{kg O}\_2/\text{kWh})
\]

Where \(\text{Power (kW)} = \text{Power (HP)} \times 0.746\) (Kumar et al., 2020).

#### 2.3.1.4 Aerator Quantity Calculation

\[
\text{Number of Aerators} = \left\lceil \frac{\text{TOD}}{\text{OTR}\_T} \right\rceil
\]

### 2.3.2 Annual Revenue

\[
\text{Annual Revenue} = \text{Total Annual Production (kg)} \times \text{Shrimp Price (\$/kg)}
\]

Production depends on density, depth, area, and culture cycles (Engle, 2010).

### 2.3.3 Initial Investment

\[
\text{Total Initial Cost} = \text{Number of Aerators} \times \text{Cost per Aerator}
\]

### 2.3.4 Annual Operating Costs

1. **Energy Cost:** \(\text{Power (kW)} \times \text{Energy Cost (\$/kWh)} \times \text{Operating Hours per Year} \times \text{Number of Aerators}\)
2. **Maintenance Cost:** \(\text{Maintenance Cost per Unit per Year} \times \text{Number of Aerators}\)
3. **Replacement Cost (Annualized):** \((\text{Number of Aerators} \times \text{Cost per Aerator}) / \text{Durability (years)}\)

### 2.3.5 Total Annual Cost

\[
\text{Total Annual Cost} = \text{Energy Cost} + \text{Maintenance Cost} + \text{Replacement Cost}
\]

### 2.3.6 Net Present Value (NPV) of Savings

\[
\text{NPV}_{\text{Savings}} = \sum_{i=1}^{n} \frac{\text{Annual Saving}_{\text{Year 1}} \times (1 + r_{\text{inflation}})^{i-1}}{(1 + r\_{\text{real}})^i}
\]

Where \(r*{\text{real}} = \frac{1 + r*{\text{nominal}}}{1 + r\_{\text{inflation}}} - 1\) (Intelligon, 2022; Susilowati et al., 2021).

### 2.3.7 Adapted Financial Metrics

Standard metrics (IRR, Payback, ROI, k) were adapted due to violations of positive incremental investment assumptions in aquaculture equipment comparison (Engle, 2010; Kumar et al., 2020).

#### 2.3.7.1 Internal Rate of Return (IRR)

\[
0 = - \Delta I + \sum*{i=1}^{n} \frac{S*{yr1} \times (1 + r\_{\text{inflation}})^{i-1}}{(1 + \text{IRR})^i}
\]

If \(\Delta I \leq 0\), standard IRR is undefined; adapted IRR anchors against baseline cost, scaled by SOTR ratio, capped at 100% (Kumar et al., 2020).

#### 2.3.7.2 Payback Period

\[
\text{Payback Period} =
\begin{cases}
\frac{0.01}{R*{SOTR}} & \text{if } \Delta I < 0 \text{ and } S*{yr1} > 0 \\
\frac{\Delta I}{S*{yr1}} & \text{if } \Delta I \geq 0 \text{ and } S*{yr1} > 0 \\
\infty & \text{if } S\_{yr1} \leq 0
\end{cases}
\]

If \(\Delta I \leq 0\), a small value divided by SOTR ratio indicates immediate benefit (Susilowati et al., 2021).

#### 2.3.7.3 Return on Investment (ROI)

\[
\text{ROI}_{\text{relative}} =
\begin{cases}
\min\left( \left( \frac{S_{yr1}}{C*{base}} \times R*{SOTR} \times (1 + F*{cost_sav}) \right) \times 100, R*{SOTR} \times 100 \right) & \text{if } \Delta I < 0 \text{ and } S*{yr1} > 0 \\
\min\left( \left( \frac{S*{yr1}}{C*{base}} \times R*{SOTR} \right) \times 100, R*{SOTR} \times 100 \right) & \text{if } \Delta I = 0 \text{ and } S*{yr1} > 0 \\
\min\left( \left( \frac{S*{yr1}}{\Delta I} \right) \times 100, R*{SOTR} \times 100 \right) & \text{if } \Delta I > 0 \text{ and } S*{yr1} > 0 \\
0 & \text{if } S*{yr1} \leq 0 \text{ or } C\_{base} \leq 0
\end{cases}
\]

Where \(F*{cost_sav} = \frac{|\Delta I|}{C*{base}}\). If \(\Delta I \leq 0\), relative ROI is based on savings relative to baseline cost, scaled by SOTR ratio (Intelligon, 2022).

#### 2.3.7.4 Profitability Index (k)

\[
k*{\text{relative}} =
\begin{cases}
k*{base} \times (1 + F*{cost_sav}) & \text{if } \Delta I < 0 \\
k*{base} & \text{if } \Delta I = 0 \\
k*{base} \times F*{cost} & \text{if } \Delta I > 0 \\
0 & \text{if } NPV*{sav} \leq 0 \text{ or } C*{base} \leq 0
\end{cases}
\]

Where \(k*{base} = \frac{NPV*{sav}}{C*{base}} \times R*{SOTR}\), \(F*{cost_sav} = \frac{|\Delta I|}{C*{base}}\), \(F*{cost} = \frac{C*{base}}{C\_{base} + \Delta I}\) (Engle, 2010).

#### 2.3.7.5 Opportunity Cost

\[
\text{Opportunity Cost}_{\text{baseline}} = \text{NPV}_{\text{Savings (winner vs. baseline)}}
\]

Quantifies economic loss from less efficient equipment (Boyd & Hanson, 2021; Susilowati et al., 2021).

#### 2.3.7.6 Equilibrium Price

\[
P*{eq} =
\begin{cases}
\max\left(0, P*{base} \times R*{SOTR} \times \left(\frac{1}{1 + F*{cost, eq}}\right)\right) & \text{if } C*{base} > 0 \text{ and } P*{base} > 0 \\
\max\left(0, P*{base} \times R*{SOTR}\right) & \text{if } C*{base} \leq 0 \text{ or } P*{base} \leq 0 \\
0 & \text{if calculation prerequisites fail}
\end{cases}
\]

Where \(P*{base} = \frac{(C*{\text{annual, non-winner}} - (C*{E, \text{winner}} + C*{M, \text{winner}})) \times D*{\text{winner}}}{N*{\text{winner}}}\), \(F*{cost, eq} = P*{base} / C\_{base}\) (Asche et al., 2021).

# 3. Results

## 3.1 Case Study: Comparative Analysis of Aerators

### 3.1.1 Farm Operating Conditions

- **Total Oxygen Demand (TOD):** 5,443.76 kg O₂/day
- **Farm Area:** 1,000 hectares
- **Shrimp Price:** $5.00/kg
- **Culture Period:** 120 days
- **Shrimp Density:** 0.33 kg/m³
- **Pond Depth:** 1.0 m
- **Water Temperature (T):** 31.5°C
- **Calculated Annual Revenue:** $50,694,439.38
- **Analysis Horizon (n):** 10 years
- **Annual Inflation Rate (\(r\_{\text{inflation}}\)):** 2.5%
- **Annual Discount Rate (\(r\_{\text{nominal}}\)):** 10%

### 3.1.2 Aerator Specifications and Calculated Metrics

**Table 1.** Aerator specifications and financial metrics.

| Parameter                          | Aerator 1      | Aerator 2 (Winner) | Unit / Notes                 |
| ---------------------------------- | -------------- | ------------------ | ---------------------------- |
| **Technical Specs**                |                |                    |                              |
| SOTR                               | 1.9            | 3.5                | kg O₂/hr                     |
| Power                              | 3              | 3                  | HP                           |
| Power (kW)                         | 2.238          | 2.238              | kW                           |
| OTR_T (31.5°C)                     | 1.26           | 2.33               | kg O₂/hr                     |
| SAE                                | 0.85           | 1.56               | kg O₂/kWh                    |
| **Unit Costs & Durability**        |                |                    |                              |
| Cost per Unit                      | $700           | $900               | USD                          |
| Durability                         | 2.0            | 5.0                | years                        |
| Annual Maintenance per Unit        | $65            | $50                | USD                          |
| **Implementation**                 |                |                    |                              |
| Number Required                    | 4,356          | 2,367              | Units                        |
| Total Power Installed              | 13,068         | 7,101              | HP                           |
| Aerators per Hectare               | 4.36           | 2.37               | Units/ha                     |
| HP per Hectare                     | 13.07          | 7.10               | HP/ha                        |
| **Financial Analysis**             |                |                    |                              |
| Total Initial Investment (ΔI)      | $3,049,200     | $2,130,300         | USD (-$918,900 for A2 vs A1) |
| Annual Energy Cost                 | $1,423,314     | $773,413           | USD                          |
| Annual Maintenance Cost            | $283,140       | $118,350           | USD                          |
| Annual Replacement Cost            | $1,524,600     | $426,060           | USD                          |
| **Total Annual Cost**              | **$3,231,054** | **$1,317,823**     | **USD**                      |
| Annual Saving (A2 vs A1)           | --             | $1,913,231         | USD                          |
| Cost as % of Revenue               | 6.37%          | 2.60%              | %                            |
| NPV of Savings (A2 vs A1, 10 yrs)  | $0             | $14,625,751        | USD                          |
| Payback Period (A2 vs A1)          | N/A            | 0.01               | years (Relative Payback)     |
| ROI (A2 vs A1)                     | 0%             | 150.42%            | % (Relative ROI)             |
| IRR (A2 vs A1, 10 yrs)             | -100%          | 343.93%            | % (Adapted IRR)              |
| Profitability Index (k) (A2 vs A1) | 0              | 11.5               | (Relative k)                 |
| Opportunity Cost (Choosing A1)     | $14,625,751    | $0                 | USD                          |
| Equilibrium Price (for A1)         | $9,082         | N/A                | USD                          |

_Note:_ Table 1 summarizes the technical and financial comparison of Aerator 1 and Aerator 2, highlighting efficiency and cost differences.

# 4. Discussion

The analysis demonstrates Aerator 2's economic superiority despite its higher unit cost ($900 vs $700) (Boyd & Hanson, 2021; The Fish Site, 2021). Key findings include:

1. **Efficiency Advantage:** Aerator 2's higher SAE (1.56 vs 0.85 kg O₂/kWh) reduces equipment needs by 45% (2,367 vs 4,356 units) (Kumar et al., 2020; Roy et al., 2024).
2. **Lower Initial Investment:** Fewer units result in a lower total investment for Aerator 2 ($2.13M vs $3.05M).
3. **Annual Savings:** Aerator 2 saves $1,913,231 annually, driven by reduced energy and replacement costs (Boyd & Hanson, 2021; The Fish Site, 2021).
4. **Financial Metrics:** NPV of savings is $14.6M, with relative ROI of 150.42% and IRR of 343.93%, indicating immediate benefits (Intelligon, 2022; Susilowati et al., 2021).
5. **Opportunity Cost:** Choosing Aerator 1 incurs a $14.6M opportunity cost (Boyd & Hanson, 2021).
6. **Equilibrium Price:** Aerator 1's price would need to be negative ($9,082 threshold) to compete, highlighting its inefficiency (Asche et al., 2021).

[Placeholder: Discuss in-loco data results, farmer evidence on low-durability aerators, and AeraSync API's role in refining financial models.]

# 5. Conclusion

This study reinforces that prioritizing upfront cost savings over operational efficiency (SAE, OTR_T) and durability is economically detrimental. Comprehensive, adapted mathematical models (NPV, opportunity cost, equilibrium pricing) provide decision support for sustainable shrimp farm management (Engle, 2010; Merino et al., 2024).

# 6. Glossary

- **OTR_T:** Temperature-Adjusted Oxygen Transfer Rate, oxygen transfer adjusted for temperature.
- **SAE:** Standard Aeration Efficiency, oxygen transferred per unit power.
- **TOD:** Total Oxygen Demand, oxygen required by shrimp and microbial activity.
- **NPV:** Net Present Value, present value of cost savings.
- **IRR:** Internal Rate of Return, rate making NPV zero.
- **ROI:** Return on Investment, relative return adjusted for efficiency.
- **k:** Profitability Index, relative NPV scaled by efficiency.

# 7. Declaration of Generative AI and AI-Assisted Technologies in the Writing Process

During the preparation of this work, the author(s) used [NAME TOOL / SERVICE, e.g., Grok by xAI] to assist in drafting LaTeX equations and refining text readability. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the published article.

# 8. Author Contributions

- **Conceptualization:** [Author Name(s)]
- **Data Curation:** [Author Name(s)]
- **Formal Analysis:** [Author Name(s)]
- **Investigation:** [Author Name(s)]
- **Methodology:** [Author Name(s)]
- **Software:** [Author Name(s)] (AeraSync API development)
- **Writing – Original Draft:** [Author Name(s)]
- **Writing – Review & Editing:** [Author Name(s)]

# 9. Funding

[Placeholder: This research was supported by [Funding Agency, Grant Number]. If no funding, state: This research did not receive any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.]

# 10. Acknowledgements

[Placeholder: Acknowledge individuals who assisted with data collection, farmer interviews, or manuscript preparation.]

# 11. Data Availability

[Placeholder: Research data (in-loco measurements, farmer interviews) have been deposited in [Repository Name, DOI/Link]. If unavailable, state reason, e.g., confidentiality of farmer data.]

# 12. Supplementary Material

[Placeholder: Supplementary files (e.g., AeraSync API code, raw data tables, farmer interview transcripts) are available at [Repository/Link].]

# 13. Vitae

- **[Author Name]:** [100-word biography, e.g., [Author Name] is a researcher at [Institution], specializing in aquaculture engineering. Their work focuses on optimizing equipment for shrimp farming. They developed the AeraSync API, enhancing economic models for aquaculture. [Degrees, notable achievements].]
- **Photo:** [Submit as separate file, Figure_1.jpg]

# 14. References

- Asche, F., Roll, K. H., Tveteras, R., 2021. Market aspects and external economic effects of aquaculture. Aquac. Econ. Manag. 25, 1–7. https://doi.org/10.1080/13657305.2020.1869861
- Boyd, C. E., 2015. Efficiency of mechanical aeration. Responsible Seafood Advocate. https://www.globalseafood.org/advocate/efficiency-of-mechanical-aeration/ (accessed 14 May 2025).
- Boyd, C. E., 2020. Energy use in aquaculture pond aeration, Part 1. Responsible Seafood Advocate. https://www.globalseafood.org/advocate/energy-use-in-aquaculture-pond-aeration-part-1/ (accessed 14 May 2025).
- Boyd, C. E., Hanson, T. R., 2021. Aerator energy use in shrimp farming and means for improvement. J. World Aquac. Soc. 52, 566–578. https://doi.org/10.1111/jwas.12753
- Engle, C. R., 2010. Aquaculture economics and financing: Management and analysis. Wiley-Blackwell, Ames, IA. https://onlinelibrary.wiley.com/doi/book/10.1002/9780813814346
- Engle, C. R., 2017. Aquaculture businesses: A practical guide to economics and marketing. 5m Publishing, Sheffield, UK.
- Food and Agriculture Organization of the United Nations, n.d. Chapter 24 economic aspects of aquafarm construction and maintenance, in: Simple methods for aquaculture - Manual. FAO, Rome.
- Intelligon, 2022. Shrimp farming basics: Project viability and investment analysis. Intelligon Blogs. https://blogs.intelligon.com/2022/02/28/shrimp-farming-basics-project-viability-and-investing-assessment/ (accessed 14 May 2025).
- Jolly, C. M., Clonts, H. A., 1993. Economics of aquaculture. Food Products Press, New York.
- Kumar, G., Engle, C., Tucker, C. S., 2020. Assessment of standard aeration efficiency of different aerators and its relation to the overall economics in shrimp culture. Aquac. Eng. 90, 102088. https://doi.org/10.1016/j.aquaeng.2020.102088
- Merino, G., Barange, M., Blanchard, J. L., Harle, J., Holmes, R., Allen, I., Allison, E. H., Badjeck, M.-C., Dulvy, N. K., Holt, J., Jennings, S., Mullon, C., Rodwell, L. D., 2024. Environmental, economic, and social sustainability in aquaculture: The aquaculture performance indicators. Nat. Commun. 15, 4955. https://doi.org/10.1038/s41467-024-49556-8
- Nunes, A. J. P., Musig, Y., 2013. Survey of aeration management in shrimp farming. SlideShare. https://www.slideshare.net/AquacultureASIA/survey-of-aeration-management-in-shrimp-farming (accessed 14 May 2025).
- Responsible Seafood Advocate, 2022. A comparison of resource use in shrimp farming, part 3: Energy. Responsible Seafood Advocate. https://www.globalseafood.org/advocate/a-comparison-of-resource-use-in-shrimp-farming-part-3-energy/ (accessed 14 May 2025).
- Roy, S. M., Sadek, S., Shafiq, M. A., Nasr, M., Mohsen, M., 2024. Advances in aeration and wastewater treatment in shrimp farming: Emerging trends, current challenges, and future perspectives. AQUA Water Infrastruct. Ecosyst. Soc. 73, 902–917. https://doi.org/10.2166/aqua.2024.256
- Sadek, S., Nasr, M., Hassan, A., 2020. Assessment of the new generation aeration systems efficiency and water current flow rate, its relation to the cost economics at varying salinities. Aquac. Res. 51, 2257–2268. https://doi.org/10.1111/are.14562
- Susilowati, Y. D., Perdana, M. C., Suparmanto, I., 2021. Sustainability and feasibility assessments of nanobubble aeration technology in economic-socio environment of Penaeus vannamei shrimp farming. BIO Web Conf. 33, 05005. https://doi.org/10.1051/bioconf/20213305005
- The Fish Site, 2021. A simple means to improve shrimp farming efficiency. The Fish Site. https://thefishsite.com/articles/a-simple-means-to-improve-shrimp-farming-efficiency (accessed 14 May 2025).
- Tveteras, R., 2009. Economic inefficiency and environmental impact: An application to aquaculture production. J. Environ. Econ. Manag. 58, 93–104. https://doi.org/10.1016/j.jeem.2008.10.005
- Valderrama, D., Hishamunda, N., Cai, J., 2023. Economic analysis of the contributions of aquaculture to future food security. Aquaculture 577, 740023. https://doi.org/10.1016/j.aquaculture.2023.740023
- Walras, L., 1874. Éléments d'économie politique pure, ou théorie de la richesse sociale. L. Corbaz, Lausanne.
