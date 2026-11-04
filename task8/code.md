## Problem Statement

Design a Manufacturing Cost and Profitability Analysis System that computes total production costs by integrating raw material expenses, direct labor charges, material wastage allowances, and machine operational overheads. The system then calculates unit selling prices, total revenues, net profit margins, and evaluates whether production meets or exceeds a specified target profit percentage.

**Cost & Profitability Rules:**

* **Material Cost:** Sum of raw material requirements multiplied by respective unit costs.
* **Wastage Allowance:** Added percentage surcharge (e.g., $5.0\%$ of material cost) accounting for production scrap/wastage.
* **Labor & Machine Cost:** Direct labor hours multiplied by hourly rates, plus machine operational hours multiplied by machine maintenance/power rates.
* **Total Production Cost:** Material Cost + Wastage + Labor Cost + Machine Cost + Overhead.
* **Target Profit:** Profitability target percentage (e.g., $\ge 20.0\%$ net profit margin on total production cost).

---

## Algorithm

1. **Initialize Production Parameters:** Set up unit costs for raw materials, wastage rates, labor rates, machine operational rates, and the target profit margin.
2. **Calculate Direct Costs:** Compute raw material expenses and apply the wastage percentage.
3. **Calculate Indirect Costs:** Compute total labor charges and machine operational overhead costs.
4. **Determine Total Production Cost:** Sum up material costs, wastage, labor charges, machine operational costs, and fixed overheads.
5. **Evaluate Profitability:**
* Calculate selling price and expected revenue based on units produced.
* Compute net profit and profit margin percentage.
* Compare profit margin against the target profit threshold.


6. **Output Results:** Display the cost breakdown sheet, total production cost, actual profit margin, and target achievement status.

---

## Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Input Production Batch Details & Target Profit %]
    B --> C[Calculate Raw Material Cost]
    C --> D[Apply Material Wastage Allowance %]
    D --> E[Calculate Labor Charges = Hours * Rate]
    E --> F[Calculate Machine Operating Cost = Hours * Rate]
    F --> G[Total Production Cost = Material + Wastage + Labor + Machine + Overhead]
    G --> H[Calculate Target Selling Price & Total Revenue]
    H --> I[Calculate Net Profit = Revenue - Total Cost]
    I --> J[Calculate Profit Margin % = Net Profit / Total Cost * 100]
    J --> K{Profit Margin >= Target Profit %?}
    K -- Yes --> L[Mark Status: Profit Target Met]
    K -- No --> M[Mark Status: Profit Target Not Met]
    L --> N[Store and Display Cost Breakdown & Profit Report]
    M --> N
    N --> O[Stop]

```



## Sample Input

```python
batch = {
    "product_name": "Industrial Electric Motor",
    "units_produced": 500,
    "raw_materials": [
        {"material": "Copper Wire (kg)", "quantity": 100, "unit_cost": 12.5},
        {"material": "Steel Housing (units)", "quantity": 500, "unit_cost": 15.0},
        {"material": "Bearings (units)", "quantity": 1000, "unit_cost": 3.0},
    ],
    "wastage_pct": 0.05,
    "labor_hours": 200,
    "labor_rate_per_hour": 25.0,
    "machine_hours": 150,
    "machine_rate_per_hour": 40.0,
    "fixed_overhead": 5000.0,
    "selling_price_per_unit": 65.0,
}
target_profit = 20.0

```

---

## Sample Output

```text
Manufacturing Report: Industrial Electric Motor
Units Produced: 500
--------------------------------------------------
Raw Material Cost: $11250.0
Wastage Allowance (5%): $562.5
Direct Labor Cost: $5000.0
Machine Operating Cost: $6000.0
Fixed Overheads: $5000.0
Total Production Cost: $27812.5
Cost Per Unit: $55.63
--------------------------------------------------
Total Revenue: $32500.0
Net Profit: $4687.5
Actual Profit Margin: 16.85%
Target Profit Threshold: 20.0%
Meets Profit Target: NO (Target Missed)

```
