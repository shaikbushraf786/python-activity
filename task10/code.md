## Problem Statement

Design a Campus Event Financial Planning System that computes total event expenditure across multiple categories (venue, equipment, catering, transport, and certificates), factors in fixed sponsorship revenues, determines participant contribution requirements, evaluates funding shortfalls, and calculates the minimum registration count needed to achieve financial break-even.

**Financial Rules:**

* **Total Cost:** $\text{Venue Cost} + \text{Equipment Cost} + \text{Catering Cost} + \text{Transport Cost} + \text{Certificate Cost}$
* **Net Funding Needed:** $\text{Total Cost} - \text{Total Sponsorships}$
* **Break-Even Registration Count:** $\lceil \text{Net Funding Needed} / \text{Per-Participant Fee} \rceil$

---

## Algorithm

1. **Initialize:** Define fixed expenses (venue, equipment, transport), variable expenses per participant (catering, certificates), sponsorship funds, and proposed registration fee per participant.
2. **Calculate Total Fixed Costs:** Sum venue rental, equipment rentals, and transportation expenses.
3. **Calculate Variable Cost per Participant:** Sum per-head catering and certificate printing expenses.
4. **Evaluate Breakeven Point:**
* Determine net cost after subtracting sponsorships.
* Calculate minimum registration count by dividing net cost by the per-participant registration fee (rounded up to the nearest whole integer).


5. **Output Results:** Display cost breakdown, sponsorship details, net deficit/surplus, and the break-even registration threshold.

---

## Flowchart

```mermaid
flowchart TD
    A[Start] --> B[Input Fixed Costs, Variable Costs per Head, Sponsorships, & Reg Fee]
    B --> C[Total Fixed Cost = Venue + Equipment + Transport]
    C --> D[Variable Cost Per Head = Catering + Certificates]
    D --> E[Input Expected Participant Count]
    E --> F[Total Event Cost = Fixed Cost + (Variable Cost Per Head * Participants)]
    F --> G[Net Deficit = Total Cost - Sponsorships]
    G --> H[Break-Even Count = Ceiling(Net Deficit / Registration Fee)]
    H --> I[Store & Display Financial Summary & Break-Even Analysis]
    I --> J[Stop]

```

---

## Python Source Code

```python
import math


def calculate_event_finances(
    fixed_costs, variable_costs, sponsorships, expected_participants, reg_fee
):
  total_fixed = (
      fixed_costs["venue"]
      + fixed_costs["equipment"]
      + fixed_costs["transport"]
  )
  variable_per_head = (
      variable_costs["catering"] + variable_costs["certificates"]
  )

  total_variable = variable_per_head * expected_participants
  total_cost = total_fixed + total_variable

  net_funding_needed = total_cost - sponsorships

  if reg_fee > 0:
    breakeven_count = math.ceil(net_funding_needed / reg_fee)
  else:
    breakeven_count = float("inf")

  expected_revenue = expected_participants * reg_fee
  expected_shortfall = max(0.0, net_funding_needed - expected_revenue)

  return {
      "total_fixed_cost": round(total_fixed, 2),
      "variable_cost_per_head": round(variable_per_head, 2),
      "total_event_cost": round(total_cost, 2),
      "total_sponsorships": round(sponsorships, 2),
      "net_funding_needed": round(net_funding_needed, 2),
      "breakeven_registration_count": max(0, breakeven_count),
      "expected_revenue": round(expected_revenue, 2),
      "expected_shortfall": round(expected_shortfall, 2),
  }


if __name__ == "__main__":
  fixed_costs = {"venue": 1500.0, "equipment": 800.0, "transport": 500.0}

  variable_costs = {"catering": 25.0, "certificates": 5.0}

  sponsorships = 2000.0
  expected_participants = 120
  registration_fee = 35.0

  finances = calculate_event_finances(
      fixed_costs,
      variable_costs,
      sponsorships,
      expected_participants,
      registration_fee,
  )

  print("=== CAMPUS EVENT FINANCIAL REPORT ===")
  print(f"Total Fixed Costs: ${finances['total_fixed_cost']}")
  print(f"Variable Cost Per Participant: ${finances['variable_cost_per_head']}")
  print(f"Total Projected Cost ({expected_participants} participants): ${finances['total_event_cost']}")
  print(f"Total Sponsorships: ${finances['total_sponsorships']}")
  print(f"Net Funding Deficit: ${finances['net_funding_needed']}")
  print("-" * 45)
  print(f"Minimum Registrations Needed to Break Even: {finances['breakeven_registration_count']}")
  print(f"Projected Revenue from {expected_participants} Attendees: ${finances['expected_revenue']}")
  print(f"Projected Shortfall / Surplus: ${finances['expected_shortfall']}")

```
