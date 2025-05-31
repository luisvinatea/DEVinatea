# Analysis of Aerators for Shrimp Farming: Cost Optimization and the Real Cost of "Cheap"

**Author:** Luis Paulo Vinatea Barberena  
**Affiliation:** BarberNode  
**Correspondence:** luisvinatea@icloud.com, +55 48 99221-9675  
**Address:** Servidao das Caranhas, 22, Barra da Lagoa, Florianopolis, SC, Brazil, 88061635  
**Date:** 2025-05-02

---

## Abstract

Aerator selection is a critical economic decision in shrimp farming,
often complicated by the trade-off between initial cost and long-term
operational efficiency. This paper presents an analysis comparing two
aerator options within the context of a specific shrimp farm,
integrating Léon Walras\'s General Equilibrium Theory and Friedrich von
Wieser\'s concept of Opportunity Cost. The study evaluates aerators
based on updated technical performance metrics (including
Temperature-Adjusted Oxygen Transfer Rate - $OTR_T$ and Standard
Aeration Efficiency - $SAE$) derived from the farm's Total Oxygen
Demand ($TOD$) and detailed, adapted financial indicators (Net Present
Value - $NPV$, Internal Rate of Return - $IRR$, Payback Period,
Return on Investment - $ROI$, Profitability Index - $k$, Opportunity
Cost, and Equilibrium Price) tailored for equipment comparison. Results
from the specific case study demonstrate that prioritizing higher
efficiency (Aerator 2) over lower initial unitary cost (Aerator 1) leads
to substantial long-term savings, a significantly positive $NPV$, high
interpreted $ROI$ and $IRR$, rapid payback, and a considerable
opportunity cost associated with choosing the less efficient option. The
analysis underscores the importance of applying robust economic
principles and adapted technical-financial assessments for optimizing
operational costs and ensuring financial sustainability in shrimp
aquaculture (Boyd & Hanson, 2021; The Fish Site, 2021).

**Keywords:** Shrimp Farming, Aquaculture Economics, Aerator Efficiency, Opportunity Cost, Cost Optimization, Mathematical Modeling, Financial Analysis, Equipment Comparison Metrics

## Highlights

- Higher efficiency aerators reduce long-term costs in shrimp farming.
- Adapted financial metrics reveal flaws in traditional equations.
- Opportunity cost of low-efficiency aerators exceeds $14M in
    $NPV$.
- In-loco data confirms poor performance of low-durability aerators.

## 1. Introduction

The economic analysis of optimal aerator choice in shrimp farming
benefits from the General Equilibrium Theorem developed by Léon Walras
in the 19th century, complemented by Friedrich von Wieser\'s concept of
opportunity cost, introduced in 1914. Walras proposed a framework to
understand how interconnected markets reach simultaneous equilibrium,
where supply equals demand through relative prices (Walras, 1874). This
approach is useful for analyzing complex systems like shrimp farms,
where multiple \"markets\" (oxygen, energy, shrimp, operating costs)
interact to maximize profitability (Asche et al., 2021). Opportunity
cost measures the value of the best alternative forgone, evaluating
aerator options (Boyd & Hanson, 2021).

### 1.1 Analogy with the Oxygen Market and Opportunity Cost

In shrimp farming, dissolved oxygen is a critical input. An "internal
oxygen market" can be conceptualized where demand (Total Oxygen Demand,
$TOD$) is driven by shrimp and microbial needs, and supply depends on
aerators' Temperature-Adjusted Oxygen Transfer Rate ($OTR_T$).
Aerators interact with energy, maintenance, and replacement markets,
connecting to the external shrimp market. Walras\'s Theorem suggests
equilibrium when these markets adjust simultaneously. Choosing a
cheaper, less efficient aerator incurs an opportunity cost equal to the
net present value of savings forgone by not selecting the more efficient
option (Boyd & Hanson, 2021; Susilowati et al., 2021).

### 1.2 The Cake Recipe: Why Assuming $HP$ per Pound of Shrimp is Incorrect

Assuming a fixed horsepower ($HP$)-per-production ratio is erroneous.
Shrimp production depends on multiple factors (dissolved oxygen,
temperature, salinity, density). Aerator $HP$ does not directly equate
to oxygen supply; $OTR_T$ is critical. Fixed $HP$ ratios ignore
interdependencies, leading to inefficient investments in low-$OTR_T$
aerators and significant opportunity costs (Boyd, 2015; Responsible
Seafood Advocate, 2022).

### 1.3 Original Equation of Léon Walras\'s General Equilibrium

Walras formalized general equilibrium with supply/demand equations,
subject to Walras\'s Law (excess demands sum to zero). Equilibrium
prices are found via \"tâtonnement\" (Walras, 1874). In shrimp farming,
equilibrium involves optimizing aerator costs, meeting $TOD$,
maximizing profits, and accounting for opportunity cost (Asche et al.,
2021; Valderrama et al., 2023).

### 1.3 Context Overview

This paper analyzes several aerators in a specific shrimp farm context,
integrating updated technical performance metrics and adapted financial
indicators. The study evaluates aerators based on Standard Oxygen
Transfer Rate ($SOTR$), to fulfill a 1000 hectares Shrimp Farm for a
given Total Oxygen Demand ($TOD$), and derives financial indicators
tailored for equipment comparison. Results demonstrate that prioritizing
higher efficiency leads to substantial long-term savings, a
significantly positive $NPV$, high interpreted $ROI$ and $IRR$,
rapid payback, and a considerable opportunity cost associated with
choosing the less efficient option.

### 1.4 Aerator Market in Ecuador

The Ecuadorian aerator market is characterized by a wide range of
options, from low-cost, low-efficiency models to high-performance,
high-cost alternatives. The choice of aerator significantly impacts
operational costs and shrimp yield. The market is influenced by factors
such as energy prices, shrimp prices, and technological advancements in
aeration systems. Understanding the trade-offs between initial
investment and long-term operational efficiency is crucial for shrimp
farmers aiming to optimize their production systems (Boyd & Hanson,
2021; The Fish Site, 2021).

By analysing aerator imports from Ecuador\'s customs database, in the
period of 2021 to 2024, we can gain insights on market trends, pricing
strategies, and the competitive landscape of aerator suppliers in the
region.

After performing data manipulation techniques, we can observe the
following patterns:

![Figure 1: Aerator Imports Analysis (2021-2024)](../plots/aerator_imports_2021_2024.png)

_Figure 1. Dashboard showing aerator imports (2021-2024) across multiple dimensions including countries of origin, importers, and product descriptions._

The dashboard on aerator imports (2021-2024) reveals some insights
across multiple dimensions. China dominates as the top country of origin
with $15.5M ($FOB$), followed by Taiwan at $4.1M, while generic
brands lead at $17.9M ($CIF$), far ahead of Wangfa at $3.2M. In
terms of importers, Area Andina S.A. handles the highest volume at 647K
units, with Crustáceos y Peces de Sudamerica as the second-largest at
137K units. Product descriptions show aerators of 12-16 pallet units
leading at 548K kg (net weight), indicating a focus on bulk shipments.
Ningbo is the top embarkation city with 398K units (ad valorem), and
Agencia Maritima Global moves 708K units (freight value), highlighting
their logistical prominence. Consignee directions peak with La Puntilla
(Satellite) at 211K units (insured value), and the generic model
category tops brokered models at 154K units, reflecting market
preferences for cost savings.

![Figure 2: Aerator Price Distribution (2021-2024)](../plots/aerator_fob_price.png)

_Figure 2. Distribution of FOB unit prices for different aerator brands, showing pricing landscape from budget to premium segments._

The aerator prices chart (2021-2024) shows a highly skewed distribution
of FOB unit prices, with a mean of $812.96, indicating that most
brands have prices below this value, but a long tail extends to
$1200+. Acquaeco has the highest average unit price at $1258.27,
followed by Walker at $1108.55, suggesting they cater to a premium
segment. In contrast, Zuma offers the lowest average at $500.80,
followed by WangFa at $546.36, positioning them as budget options.
Other brands like Hongteng ($673.33), and Aerex ($802.14) cluster
closer to the mean, while Wenling ($961.32) and Annex ($1021.79)
sit between the mid-range and high-end, reflecting a diverse pricing
landscape in the aerator market.

## 2. Case Study: Comparing Different Aerator Options for an Ecuadorian Shrimp Farm

### 2.1 Case Study Overview and Parameters

This case study examines an intensive shrimp farm in Ecuador with 1,000
hectares of production area. The farm operates at a tropical water
temperature of 31.5°C, which significantly affects oxygen transfer
efficiency through the established temperature correction factor
($\theta = 1.024$). The farm's Total Oxygen Demand ($TOD$) is
calculated at 5.47 $\text{kg O}_2/hr/hectare$, resulting in a
substantial total requirement of 5,470 $\text{kg O}_2/hr$ across
the entire operation.

For this analysis, we compare seven different paddlewheel aerator models (Aerator 0 through Aerator 6), all operating at the standard power rating of 3 $HP$ (2.238 $kW$). These aerators exhibit varying performance characteristics:

**Table 2: Case Study Parameters**

<div class="table-responsive">
<table class="compact-table">
<caption><strong>Table 2.</strong> Case study parameters for the financial and technical analysis.</caption>
<thead>
<tr>
<th class="medium-col">Parameter</th>
<th class="medium-col">Value</th>
</tr>
</thead>
<tbody>
<tr><td>Production scale</td><td>1,000 hectares</td></tr>
<tr><td>Operating temperature</td><td>31.5°C</td></tr>
<tr><td>Energy cost</td><td>$0.05/kWh</td></tr>
<tr><td>Daily aeration</td><td>8 hours</td></tr>
<tr><td>Shrimp density</td><td>0.33 kg/m³</td></tr>
<tr><td>Culture period</td><td>120 days</td></tr>
<tr><td>Shrimp market price</td><td>$5.00/kg</td></tr>
<tr><td>Annual discount rate</td><td>10%</td></tr>
<tr><td>Annual inflation rate</td><td>3%</td></tr>
<tr><td>Analysis timeframe</td><td>10 years</td></tr>
</tbody>
</table>
</div>

### 2.2 Aerator Investment Options

The aerators under consideration present a classic economic dilemma: less expensive models with lower efficiency versus higher-priced models with superior oxygen transfer rates. While Aerator 0 has the lowest initial cost ($500), it does not offer the lowest operational cost. Aerator 1, despite being more expensive ($600), delivers lower $SOTR$ ($1.0 \text{kg O}_2/hr \text{ vs. } 1.2 \text{kg O}_2/hr$). The most efficient option, Aerator 6, transfers 6.0 $\text{kg O}_2/hr$ but costs $1,500 per unit.

The economic challenge is compounded by differences in durability (ranging from 2.0 to 6.0 years) and maintenance costs (from $20 to $90 per unit annually). This creates complex trade-offs between initial investment and long-term operational expenses. The total number of aerators required varies dramatically between options due to their different oxygen transfer capacities, directly impacting both initial investment and ongoing operational costs.

**Table 1: Aerator Specifications and Costs**

<div class="table-responsive">
<table class="compact-table">
<caption><strong>Table 1.</strong> Aerator specifications and costs including SOTR in kg O₂/hr, purchase price in USD, annual maintenance costs, and expected durability in years.</caption>
<thead>
<tr>
<th class="narrow-col">Model</th>
<th class="narrow-col">SOTR (kg O₂/hr)</th>
<th class="narrow-col">Purchase Price</th>
<th class="narrow-col">Maintenance Cost/year</th>
<th class="narrow-col">Durability (years)</th>
</tr>
</thead>
<tbody>
<tr><td>Aerator 0</td><td>1.2</td><td>$500</td><td>$85</td><td>2.0</td></tr>
<tr><td>Aerator 1</td><td>1.0</td><td>$600</td><td>$70</td><td>2.5</td></tr>
<tr><td>Aerator 2</td><td>1.5</td><td>$700</td><td>$90</td><td>2.0</td></tr>
<tr><td>Aerator 3</td><td>2.0</td><td>$800</td><td>$40</td><td>3.0</td></tr>
<tr><td>Aerator 4</td><td>3.0</td><td>$900</td><td>$50</td><td>6.0</td></tr>
<tr><td>Aerator 5</td><td>4.5</td><td>$1,200</td><td>$20</td><td>3.5</td></tr>
<tr><td>Aerator 6</td><td>6.0</td><td>$1,500</td><td>$30</td><td>4.0</td></tr>
</tbody>
</table>
</div>

### 2.3 Parameters Used

##### 2.3.1 Standard Oxygen Transfer Rate ($SOTR$)

The baseline oxygen transfer capacity under standard conditions (20°C, 0
DO, 1 atm), measured in $\text{kg O}_2/hr$ (Kumar et al., 2020).

##### 2.3.2 Temperature-Adjusted Oxygen Transfer Rate ($OTR_T$)

$$\text{OTR}_T = (\text{SOTR} \times 0.5) \times \theta^{(T-20)}$$

Where $\theta = 1.024$ (temperature correction factor) (Boyd, 2015).

##### 2.3.3 Standard Aeration Efficiency ($SAE$)

$$\text{SAE} = \frac{\text{SOTR}}{\text{Power (kW)}} (\text{kg } \text{O}_2/\text{kWh})$$

Where $\text{Power (kW)} = \text{Power (HP)} \times 0.746$ (Kumar
et al., 2020).

![Figure 3: Aerator Performance Metrics](aerators_relative-efficiency-profitability_financials_files/aerators_relative-efficiency-profitability_financials_4_0.png)

_Figure 3. Comparison of aerator performance metrics including Standard Oxygen Transfer Rate (SOTR) and Standard Aeration Efficiency (SAE)._

##### 2.3.4 Aerator Quantity Calculation

$$\text{Number of Aerators} = \left\lceil \frac{\text{TOD}}{\text{OTR}_T} \right\rceil$$

![Figure 4: Aerator Quantity Requirements](aerators_relative-efficiency-profitability_financials_files/aerators_relative-efficiency-profitability_financials_6_0.png)

_Figure 4. Number of aerators required for each model to meet the farm's Total Oxygen Demand (TOD)._

### 2.3.5 Annual Revenue

$$\text{Total Initial Cost} = \text{Number of Aerators} \times \text{Cost per Aerator}$$

Production depends on density, depth, area, and culture cycles (Engle,
2010).

### 2.3.6 Initial Investment

$$\text{Total Initial Cost} = \text{Number of Aerators} \times \text{Cost per Aerator}$$

### 2.3.7 Annual Operating Costs

1.  **Energy Cost:** $\text{Power (kW)} \times \text{Energy Cost USD/kWh} \times \text{Operating Hours per Year} \times \text{Number of Aerators}$
2.  **Maintenance Cost:** $\text{Maintenance Cost per Unit per Year} \times \text{Number of Aerators}$
3.  **Replacement Cost (Annualized):** $(\text{Number of Aerators} \times \text{Cost per Aerator}) / \text{Durability (years)}$

![Figure 5: Annual Operating Cost Analysis](aerators_relative-efficiency-profitability_financials_files/aerators_relative-efficiency-profitability_financials_8_0.png)

_Figure 5. Breakdown of annual operating costs including energy, maintenance, and replacement costs for each aerator model._

### 2.4 Financial Indicators

#### 2.4.1 Net Present Value (NPV) of Savings

$$\text{NPV}_{\text{Savings}} = \sum_{i=1}^{n} \frac{\text{Annual Saving}_{\text{Year 1}} \times (1 + r_{\text{inflation}})^{i-1}}{(1 + r_{real})^i}$$

Where $r_{real} = \frac{1 + r_{nominal}}{1 + r_{inflation}} - 1$
(Intelligon, 2022; Susilowati et al., 2021).

### 2.4.2 Adapted Financial Metrics

#### 2.4.2.1 Internal Rate of Return (IRR)

$$0 = - \Delta I + \sum_{i=1}^{n} \frac{S_{yr1} \times (1 + r_{\text{inflation}})^{i-1}}{(1 + \text{IRR})^i}$$

If $\Delta I \leq 0$, standard IRR is undefined; adapted IRR anchors
against baseline cost, scaled by SOTR ratio, capped at 100% (Kumar et
al., 2020).

![Figure 6: Internal Rate of Return Analysis](aerators_relative-efficiency-profitability_financials_files/aerators_relative-efficiency-profitability_financials_10_0.png)

_Figure 6. Internal Rate of Return (IRR) comparison showing financial attractiveness of each aerator option._

### 2.4.2.1 Payback Period

$$
\text{Payback Period} = \begin{cases}
\frac{0.01}{R_{\text{SOTR}}} & \text{if } \Delta I < 0 \text{ and } S_{\text{yr1}} > 0 \\
\frac{\Delta I}{S_{\text{yr1}}} & \text{if } \Delta I \geq 0 \text{ and } S_{\text{yr1}} > 0 \\
\infty & \text{if } S_{\text{yr1}} \leq 0
\end{cases}
$$

Where:

- $R_{SOTR} = \frac{S_{yr1}}{C_{base}} \times R_{SOTR}$
- $C_{base}$ is the baseline cost (Engle, 2010)

### 2.4.2.2 Relative Return on Investment (ROI)

$$
\text{ROI}_{\text{relative}} = \begin{cases}
\min\left( \left( \frac{S_{\text{yr1}}}{C_{\text{base}}} \times R_{\text{SOTR}} \times (1 + F_{\text{cost\_sav}}) \right) \times 100, R_{\text{SOTR}} \times 100 \right) & \text{if } \Delta I < 0 \\
\min\left( \left( \frac{S_{\text{yr1}}}{C_{\text{base}}} \times R_{\text{SOTR}} \right) \times 100, R_{\text{SOTR}} \times 100 \right) & \text{if } \Delta I = 0 \\
\min\left( \left( \frac{S_{\text{yr1}}}{\Delta I} \right) \times 100, R_{\text{SOTR}} \times 100 \right) & \text{if } \Delta I > 0 \\
0 & \text{if } S_{\text{yr1}} \leq 0
\end{cases}
$$

**Note**: Conditions are: $S_{\text{yr1}} > 0$ and $C_{\text{base}} > 0$

Where:

- $F_{cost\_sav} = \frac{|\Delta I|}{C_{base}}$
- If $\Delta I \leq 0$, relative ROI is based on savings relative to baseline cost, scaled by SOTR ratio (Intelligon, 2022)

### 2.4.2.3 Profitability Index ($k$)

$$
k_{\text{relative}} = \begin{cases}
k_{\text{base}} \times (1 + F_{\text{cost\_sav}}) & \text{if } \Delta I < 0 \\
k_{\text{base}} & \text{if } \Delta I = 0 \\
k_{\text{base}} \times F_{\text{cost}} & \text{if } \Delta I > 0 \\
0 & \text{if } \text{NPV}_{\text{sav}} \leq 0
\end{cases}
$$

**Note**: Condition is $C_{\text{base}} > 0$

Where:

- $k_{base} = \frac{NPV_{sav}}{C_{base}} \times R_{SOTR}$
- $F_{cost, eq} = \frac{|\Delta I|}{C_{base}}$
- $F_{cost} = \frac{C_{base}}{C_{base} + \Delta I}$ (Engle, 2010)

![Figure 7: Profitability Index Comparison](aerators_relative-efficiency-profitability_financials_files/aerators_relative-efficiency-profitability_financials_12_0.png)

_Figure 7. Profitability Index (k) showing the relative profitability of different aerator investments._

### 2.4.2.4 Equilibrium Price ($P_{eq}$)

$$
P_{\text{eq}} = \begin{cases}
\max\left(0, P_{\text{base}} \times R_{\text{SOTR}} \times \left(\frac{1}{1 + F_{\text{cost, eq}}}\right)\right) & \text{if } C_{\text{base}} > 0 \\
\max\left(0, P_{\text{base}} \times R_{\text{SOTR}}\right) & \text{if } C_{\text{base}} \leq 0 \\
0 & \text{otherwise}
\end{cases}
$$

**Note**: Condition is $P_{\text{base}} > 0$

Where:

- $P_{base} = \frac{(C_{\text{annual, non-winner}} - (C_{E, \text{winner}} + C_{M, \text{winner}})) \times D_{\text{winner}}}{N_{\text{winner}}}$
- $F_{cost, eq} = \frac{P_{base}}{C_{base}}$ (Asche et al., 2021)

![Figure 8: Equilibrium Price Analysis](aerators_relative-efficiency-profitability_financials_files/aerators_relative-efficiency-profitability_financials_14_0.png)

_Figure 8. Market equilibrium analysis showing theoretical prices based on Walras's General Equilibrium Theory._

### 2.4.2.5 Opportunity Cost

$$\text{Opportunity Cost}_{\text{baseline}} = \text{NPV}_{\text{Savings (winner vs. baseline)}}$$

Quantifies economic loss from less efficient equipment (Boyd & Hanson,
2021; Susilowati et al., 2021).

## 3. Results

### 3.1 Aerator Performance Summary

**Table 3: Aerator Performance and Cost Efficiency Metrics**

<div class="table-responsive">
<table class="compact-table">
<caption><strong>Table 3.</strong> Aerator performance and cost efficiency metrics. SOTR in kg O₂/hr, Annual Production in kg O₂/year, Cost Efficiency in USD/kg O₂, Cost per SOTR in USD/unit.</caption>
<thead>
<tr>
<th class="narrow-col">Aerator</th>
<th class="narrow-col">SOTR</th>
<th class="narrow-col">Price</th>
<th class="medium-col">Annual Production</th>
<th class="narrow-col">Cost Efficiency</th>
<th class="narrow-col">Cost per SOTR</th>
<th class="narrow-col">SOTR per Dollar</th>
</tr>
</thead>
<tbody>
<tr><td>Aerator 0</td><td>1.2</td><td>$500</td><td>2,301</td><td>$0.142</td><td>$417</td><td>0.0024</td></tr>
<tr><td>Aerator 1</td><td>1.0</td><td>$600</td><td>1,918</td><td>$0.170</td><td>$600</td><td>0.0017</td></tr>
<tr><td>Aerator 2</td><td>1.5</td><td>$700</td><td>2,877</td><td>$0.114</td><td>$467</td><td>0.0021</td></tr>
<tr><td>Aerator 3</td><td>2.0</td><td>$800</td><td>3,836</td><td>$0.085</td><td>$400</td><td>0.0025</td></tr>
<tr><td>Aerator 4</td><td>3.0</td><td>$900</td><td>5,753</td><td>$0.057</td><td>$300</td><td>0.0033</td></tr>
<tr><td>Aerator 5</td><td>4.5</td><td>$1,200</td><td>8,630</td><td>$0.038</td><td>$267</td><td>0.0037</td></tr>
<tr><td>Aerator 6</td><td>6.0</td><td>$1,500</td><td>11,507</td><td>$0.028</td><td>$250</td><td>0.0040</td></tr>
</tbody>
</table>
</div>

### 3.2 Farm-Scale Financial Analysis

**Farm Parameters:** 1,000 hectares, $TOD$: 5,470 $\text{kg O}_2/hr$, Annual Revenue: $16.6M, Analysis Period: 10 years

<div class="table-responsive">
<table class="compact-table">
<caption><strong>Table 4.</strong> Farm-scale investment and operating cost analysis. Investment and costs in millions USD ($M), Revenue % as percentage of total revenue ($16.6M), NPV Opportunity Cost in millions USD.</caption>
<thead>
<tr>
<th class="narrow-col">Aerator</th>
<th class="narrow-col">Quantity</th>
<th class="narrow-col">Units/Ha</th>
<th class="narrow-col">Investment</th>
<th class="narrow-col">Energy</th>
<th class="narrow-col">Maintenance</th>
<th class="narrow-col">Replace.</th>
<th class="narrow-col">Total</th>
<th class="narrow-col">Revenue %</th>
<th class="narrow-col">NPV Opp. Cost</th>
</tr>
</thead>
<tbody>
<tr><td>Aerator 0</td><td>6,941</td><td>6.94</td><td>$3.47</td><td>$2.27</td><td>$0.59</td><td>$1.74</td><td>$4.59</td><td>27.7%</td><td>$28.6</td></tr>
<tr><td>Aerator 1</td><td>8,329</td><td>8.33</td><td>$5.00</td><td>$2.72</td><td>$0.58</td><td>$2.00</td><td>$5.30</td><td>32.0%</td><td>$34.3</td></tr>
<tr><td>Aerator 2</td><td>5,553</td><td>5.55</td><td>$3.89</td><td>$1.81</td><td>$0.50</td><td>$1.94</td><td>$4.26</td><td>25.7%</td><td>$25.9</td></tr>
<tr><td>Aerator 3</td><td>4,165</td><td>4.17</td><td>$3.33</td><td>$1.36</td><td>$0.17</td><td>$1.11</td><td>$2.64</td><td>15.9%</td><td>$13.0</td></tr>
<tr><td>Aerator 4</td><td>2,777</td><td>2.78</td><td>$2.50</td><td>$0.91</td><td>$0.14</td><td>$0.42</td><td>$1.46</td><td>8.8%</td><td>$3.6</td></tr>
<tr><td>Aerator 5</td><td>1,851</td><td>1.85</td><td>$2.22</td><td>$0.60</td><td>$0.04</td><td>$0.63</td><td>$1.28</td><td>7.7%</td><td>$2.1</td></tr>
<tr><td>Aerator 6</td><td>1,389</td><td>1.39</td><td>$2.08</td><td>$0.45</td><td>$0.04</td><td>$0.52</td><td>$1.02</td><td>6.1%</td><td>$0.0</td></tr>
</tbody>
</table>
</div>

### 3.3 Financial Metrics Analysis

<div class="table-responsive">
<table class="compact-table">
<caption><strong>Table 5.</strong> Financial performance metrics. IRR and ROI in percentage, Payback in years, SAE in kg O₂/kWh, OTRT in kg O₂/hr, Total HP in horsepower, HP/Ha as HP per hectare.</caption>
<thead>
<tr>
<th class="narrow-col">Aerator</th>
<th class="narrow-col">IRR %</th>
<th class="narrow-col">ROI %</th>
<th class="narrow-col">Payback Yrs</th>
<th class="narrow-col">Prof. Index</th>
<th class="narrow-col">SAE</th>
<th class="narrow-col">OTRT</th>
<th class="narrow-col">Total HP</th>
<th class="narrow-col">HP/Ha</th>
</tr>
</thead>
<tbody>
<tr><td>Aerator 0</td><td>51.58</td><td>20.00</td><td>1.94</td><td>2.38</td><td>0.72</td><td>0.79</td><td>20,823</td><td>20.82</td></tr>
<tr><td>Aerator 1</td><td>24.52</td><td>16.67</td><td>4.08</td><td>1.45</td><td>0.60</td><td>0.66</td><td>24,987</td><td>24.99</td></tr>
<tr><td>Aerator 2</td><td>44.93</td><td>25.00</td><td>2.23</td><td>2.30</td><td>0.90</td><td>0.99</td><td>16,659</td><td>16.66</td></tr>
<tr><td>Aerator 3</td><td>43.29</td><td>33.33</td><td>2.31</td><td>1.91</td><td>1.20</td><td>1.31</td><td>12,495</td><td>12.49</td></tr>
<tr><td>Aerator 4</td><td>53.64</td><td>21.96</td><td>1.86</td><td>1.25</td><td>1.80</td><td>1.97</td><td>8,331</td><td>8.33</td></tr>
<tr><td>Aerator 5</td><td>141.64</td><td>19.19</td><td>0.71</td><td>1.35</td><td>2.70</td><td>2.96</td><td>5,553</td><td>5.55</td></tr>
<tr><td>Aerator 6</td><td>205.76</td><td>100.00</td><td>0.49</td><td>8.23</td><td>3.59</td><td>3.94</td><td>4,167</td><td>4.17</td></tr>
</tbody>
</table>
</div>

### 3.4 Equilibrium Price Analysis

**Market Equilibrium:** Theoretical prices based on Walras's General Equilibrium Theory (relative to Aerator 6 as winner)

<div class="table-responsive">
<table class="compact-table">
<caption><strong>Table 6.</strong> Market equilibrium analysis based on Walras's General Equilibrium Theory with Aerator 6 as reference winner. Prices in USD, Durability in years, Maintenance cost in USD per unit annually.</caption>
<thead>
<tr>
<th class="narrow-col">Aerator</th>
<th class="narrow-col">Actual Price</th>
<th class="narrow-col">Equilibrium Price</th>
<th class="narrow-col">Price Diff.</th>
<th class="medium-col">Market Status</th>
<th class="narrow-col">Durability Yrs</th>
<th class="narrow-col">Maintenance</th>
<th class="medium-col">Rating</th>
</tr>
</thead>
<tbody>
<tr><td>Aerator 0</td><td>$500</td><td>$2,347</td><td>$1,847</td><td>Underpriced</td><td>2.0</td><td>$85</td><td>Fair</td></tr>
<tr><td>Aerator 1</td><td>$600</td><td>$2,292</td><td>$1,692</td><td>Underpriced</td><td>2.5</td><td>$70</td><td>Poor</td></tr>
<tr><td>Aerator 2</td><td>$700</td><td>$2,695</td><td>$1,995</td><td>Underpriced</td><td>2.0</td><td>$90</td><td>Fair</td></tr>
<tr><td>Aerator 3</td><td>$800</td><td>$2,051</td><td>$1,251</td><td>Underpriced</td><td>3.0</td><td>$40</td><td>Good</td></tr>
<tr><td>Aerator 4</td><td>$900</td><td>$1,391</td><td>$491</td><td>Underpriced</td><td>6.0</td><td>$50</td><td>Excellent</td></tr>
<tr><td>Aerator 5</td><td>$1,200</td><td>$1,685</td><td>$485</td><td>Underpriced</td><td>3.5</td><td>$20</td><td>Excellent</td></tr>
<tr><td>Aerator 6</td><td>$1,500</td><td>$1,500</td><td>$0</td><td>Winner (Ref.)</td><td>4.0</td><td>$30</td><td>Excellent</td></tr>
</tbody>
</table>
</div>

### 3.5 Marginal Analysis

<div class="table-responsive">
<table class="compact-table">
<caption><strong>Table 7.</strong> Marginal returns and upgrade path analysis. Investment in USD, SOTR Gain in kg O₂/hr, Production Gain in kg O₂/year, SOTR per Dollar dimensionless, Production per Dollar in kg O₂/year/USD, Cumulative in kg O₂.</caption>
<thead>
<tr>
<th class="medium-col">Upgrade Path</th>
<th class="narrow-col">Add. Investment</th>
<th class="narrow-col">SOTR Gain</th>
<th class="narrow-col">Production Gain</th>
<th class="narrow-col">Count Change</th>
<th class="narrow-col">SOTR per Dollar</th>
<th class="narrow-col">Prod. per Dollar</th>
<th class="narrow-col">Slope</th>
<th class="narrow-col">Cumulative</th>
</tr>
</thead>
<tbody>
<tr><td>Aerator 0 → 1</td><td>$100</td><td>-0.2</td><td>-384</td><td>1,388</td><td>-0.0020</td><td>-3.8</td><td>-0.0020</td><td>-10</td></tr>
<tr><td>Aerator 1 → 2</td><td>$100</td><td>0.5</td><td>959</td><td>-2,776</td><td>0.0050</td><td>9.6</td><td>0.0050</td><td>-5</td></tr>
<tr><td>Aerator 2 → 3</td><td>$100</td><td>0.5</td><td>959</td><td>-1,388</td><td>0.0050</td><td>9.6</td><td>0.0050</td><td>50</td></tr>
<tr><td>Aerator 3 → 4</td><td>$100</td><td>1.0</td><td>1,918</td><td>-1,388</td><td>0.0100</td><td>19.2</td><td>0.0100</td><td>180</td></tr>
<tr><td>Aerator 4 → 5</td><td>$300</td><td>1.5</td><td>2,877</td><td>-926</td><td>0.0050</td><td>9.6</td><td>0.0050</td><td>945</td></tr>
<tr><td>Aerator 5 → 6</td><td>$300</td><td>1.5</td><td>2,877</td><td>-462</td><td>0.0050</td><td>9.6</td><td>0.0050</td><td>2,160</td></tr>
</tbody>
</table>
</div>
