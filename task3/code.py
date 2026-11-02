def process_patient_bill(patient):
  subtotal = (
      patient["consultation"]
      + patient["diagnostics"]
      + patient["treatment"]
      + (patient["room_rate"] * patient["days_stayed"])
  )

  classification = "General"
  insurance_covered = 0.0
  discount = 0.0

  if patient["is_insured"]:
    classification = "Insured"
    insurance_covered = subtotal * 0.80
    remaining_balance = subtotal - insurance_covered
  else:
    remaining_balance = subtotal

  if patient["age"] >= 60 and not patient["is_insured"]:
    classification = "Senior Citizen"
    discount = remaining_balance * 0.15
    remaining_balance -= discount
  elif patient["annual_income"] < 250000 and not patient["is_insured"]:
    classification = "Subsidized / Charity"
    discount = remaining_balance * 0.25
    remaining_balance -= discount

  final_payable = round(remaining_balance, 2)
  insurance_covered = round(insurance_covered, 2)
  discount = round(discount, 2)
  total_bill = round(subtotal, 2)

  return {
      "patient_id": patient["patient_id"],
      "name": patient["name"],
      "classification": classification,
      "total_charges": total_bill,
      "insurance_covered": insurance_covered,
      "discount_applied": discount,
      "net_payable": final_payable,
  }


if __name__ == "__main__":
  patients = [
      {
          "patient_id": "P501",
          "name": "Robert Smith",
          "age": 65,
          "is_insured": False,
          "annual_income": 400000,
          "consultation": 1500,
          "diagnostics": 3500,
          "treatment": 10000,
          "room_rate": 2000,
          "days_stayed": 4,
      },
      {
          "patient_id": "P502",
          "name": "Emily Davis",
          "age": 28,
          "is_insured": True,
          "annual_income": 600000,
          "consultation": 2000,
          "diagnostics": 5000,
          "treatment": 25000,
          "room_rate": 3000,
          "days_stayed": 3,
      },
      {
          "patient_id": "P503",
          "name": "Michael Brown",
          "age": 42,
          "is_insured": False,
          "annual_income": 180000,
          "consultation": 1000,
          "diagnostics": 2000,
          "treatment": 8000,
          "room_rate": 1500,
          "days_stayed": 2,
      },
  ]

  for p in patients:
    result = process_patient_bill(p)
    print(f"Patient ID: {result['patient_id']} ({result['name']})")
    print(f"Classification: {result['classification']}")
    print(f"Total Charges: ${result['total_charges']}")
    print(f"Insurance Covered: ${result['insurance_covered']}")
    print(f"Discount Applied: ${result['discount_applied']}")
    print(f"Net Payable: ${result['net_payable']}")
    print("-" * 40)
