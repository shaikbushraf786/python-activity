def calculate_income_tax(taxable_income):
  tax = 0.0
  if taxable_income > 70000:
    tax += (70000 - 30000) * 0.10
    tax += (taxable_income - 70000) * 0.20
  elif taxable_income > 30000:
    tax += (taxable_income - 30000) * 0.10
  return tax


def process_payroll(employee):
  gross_salary = (
      employee["basic_pay"]
      + employee["hra"]
      + employee["transport"]
      + employee["overtime_pay"]
      + employee["incentives"]
  )

  pf = employee["basic_pay"] * 0.12
  prof_tax = 200.0

  taxable_income = gross_salary - pf
  income_tax = calculate_income_tax(taxable_income)

  total_deductions = pf + prof_tax + income_tax
  net_salary = gross_salary - total_deductions

  return {
      "emp_id": employee["emp_id"],
      "name": employee["name"],
      "gross_salary": round(gross_salary, 2),
      "pf": round(pf, 2),
      "prof_tax": round(prof_tax, 2),
      "income_tax": round(income_tax, 2),
      "total_deductions": round(total_deductions, 2),
      "net_salary": round(net_salary, 2),
  }


if __name__ == "__main__":
  employees = [
      {
          "emp_id": "E201",
          "name": "Sarah Connor",
          "basic_pay": 45000,
          "hra": 15000,
          "transport": 5000,
          "overtime_pay": 3000,
          "incentives": 5000,
      },
      {
          "emp_id": "E202",
          "name": "John Reese",
          "basic_pay": 60000,
          "hra": 20000,
          "transport": 6000,
          "overtime_pay": 4000,
          "incentives": 10000,
      },
      {
          "emp_id": "E203",
          "name": "Miles Dyson",
          "basic_pay": 30000,
          "hra": 10000,
          "transport": 3000,
          "overtime_pay": 1000,
          "incentives": 2000,
      },
  ]

  for emp in employees:
    statement = process_payroll(emp)
    print(f"Employee ID: {statement['emp_id']} ({statement['name']})")
    print(f"Gross Salary: ${statement['gross_salary']}")
    print(
        f"Deductions -> PF: ${statement['pf']}, Prof Tax:"
        f" ${statement['prof_tax']}, Income Tax: ${statement['income_tax']}"
    )
    print(f"Total Deductions: ${statement['total_deductions']}")
    print(f"Net Take-Home Salary: ${statement['net_salary']}")
    print("-" * 50)
