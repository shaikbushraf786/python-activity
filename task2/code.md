## Problem Statement

Design a Progressive Electricity Billing and Anomaly Detection System that calculates monthly electricity costs based on tiered consumption slabs, fixed base charges, progressive surcharges, and evaluates historical consumption across multiple months to flag unusual cost increases or consumption spikes.

**Tariff Slab Structure:**

* **Slab 1 (0 – 100 units):** $\$3.50$ per unit
* **Slab 2 (101 – 300 units):** $\$5.00$ per unit
* **Slab 3 (Above 300 units):** $\$7.00$ per unit
* **Fixed Charges:** $\$50.00$ per month
* **Surcharge:** $10\%$ on energy charges if total consumption exceeds $400$ units.

**Anomaly Detection Rule:**

* Flag any month where the total bill increases by more than $25.0\%$ compared to the immediately preceding month.

---

## Algorithm

1. **Initialize Tariff Parameters:** Set up slab limits, unit rates, fixed charges, and surcharge conditions.
2. **Calculate Monthly Bill:** For each month's total units consumed:
* Compute energy charges progressively across the slabs.
* Add the standard fixed charge.
* Apply a surcharge if units exceed the high-consumption threshold.


3. **Analyze Trends:** Iterate through the historical list of monthly bills.
* Compare each month's bill to the previous month.
* Calculate percentage increase. If it exceeds $25\%$, trigger an anomaly alert.


4. **Output Results:** Display the calculated bill for each month alongside any detected billing anomalies.

---

## Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Input Monthly Consumption Data]
    B --> C{For Each Month:\nCalculate Slab Energy Charges}
    C --> D[Add Fixed Charges]
    D --> E{Units > 400?}
    E -- Yes --> F[Add 10% Surcharge]
    E -- No --> G[Keep Base Total]
    F --> H[Store Monthly Bill]
    G --> H
    H --> I{More Months?}
    I -- Yes --> C
    I -- No --> J[Compare Consecutive Month Bills]
    J --> K{Percentage Increase > 25%?}
    K -- Yes --> L[Flag Unusual Increase Alert]
    K -- No --> M[Normal Variation]
    L --> N{More Comparisons?}
    M --> N
    N -- Yes --> K
    N -- No --> O[Display Bills and Alerts]
    O --> P[Stop]

```

---






```

---

## Sample Input

```python
consumption_data = {
    "January": 150,
    "February": 180,
    "March": 210,
    "April": 190,
    "May": 450,
    "June": 470,
}

```

---

## Sample Output

```text
Monthly Bills:
January: $475.0
February: $590.0
March: $705.0
April: $625.0
May: $1845.0
June: $1924.5

Anomaly Detection Alerts:
Unusual increase detected in May: Bill jumped by 195.2% compared to April

```
