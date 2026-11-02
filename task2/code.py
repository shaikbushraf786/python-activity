def calculate_bill(units):
  fixed_charge = 50.0
  energy_charge = 0.0

  if units <= 100:
    energy_charge = units * 3.5
  elif units <= 300:
    energy_charge = (100 * 3.5) + ((units - 100) * 5.0)
  else:
    energy_charge = (100 * 3.5) + (200 * 5.0) + ((units - 300) * 7.0)

  surcharge = 0.0
  if units > 400:
    surcharge = energy_charge * 0.10

  total_bill = fixed_charge + energy_charge + surcharge
  return round(total_bill, 2)


def analyze_consumption(monthly_data):
  bills = {}
  for month, units in monthly_data.items():
    bills[month] = calculate_bill(units)

  alerts = []
  months = list(bills.keys())
  for i in range(1, len(months)):
    prev_month = months[i - 1]
    curr_month = months[i]
    prev_bill = bills[prev_month]
    curr_bill = bills[curr_month]

    if prev_bill > 0:
      increase_pct = ((curr_bill - prev_bill) / prev_bill) * 100
      if increase_pct > 25.0:
        alerts.append(
            f"Unusual increase detected in {curr_month}: Bill jumped by"
            f" {increase_pct:.1f}% compared to {prev_month}"
        )

  return bills, alerts


if __name__ == "__main__":
  consumption_data = {
      "January": 150,
      "February": 180,
      "March": 210,
      "April": 190,
      "May": 450,
      "June": 470,
  }

  bills, alerts = analyze_consumption(consumption_data)

  print("Monthly Bills:")
  for month, bill in bills.items():
    print(f"{month}: ${bill}")

  print("\nAnomaly Detection Alerts:")
  for alert in alerts:
    print(alert)
