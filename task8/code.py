def analyze_manufacturing_profitability(batch_data, target_profit_pct):
  raw_material_cost = sum(
      item["quantity"] * item["unit_cost"]
      for item in batch_data["raw_materials"]
  )
  wastage_cost = raw_material_cost * batch_data["wastage_pct"]
  adjusted_material_cost = raw_material_cost + wastage_cost

  labor_cost = batch_data["labor_hours"] * batch_data["labor_rate_per_hour"]
  machine_cost = (
      batch_data["machine_hours"] * batch_data["machine_rate_per_hour"]
  )
  overhead_cost = batch_data["fixed_overhead"]

  total_production_cost = (
      adjusted_material_cost + labor_cost + machine_cost + overhead_cost
  )
  cost_per_unit = total_production_cost / batch_data["units_produced"]

  total_revenue = batch_data["units_produced"] * batch_data["selling_price_per_unit"]
  net_profit = total_revenue - total_production_cost
  profit_margin_pct = (net_profit / total_production_cost) * 100

  target_met = profit_margin_pct >= target_profit_pct

  return {
      "product_name": batch_data["product_name"],
      "units_produced": batch_data["units_produced"],
      "raw_material_cost": round(raw_material_cost, 2),
      "wastage_cost": round(wastage_cost, 2),
      "labor_cost": round(labor_cost, 2),
      "machine_cost": round(machine_cost, 2),
      "overhead_cost": round(overhead_cost, 2),
      "total_production_cost": round(total_production_cost, 2),
      "cost_per_unit": round(cost_per_unit, 2),
      "total_revenue": round(total_revenue, 2),
      "net_profit": round(net_profit, 2),
      "profit_margin_pct": round(profit_margin_pct, 2),
      "target_met": target_met,
  }


if __name__ == "__main__":
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
  report = analyze_manufacturing_profitability(batch, target_profit)

  print(f"Manufacturing Report: {report['product_name']}")
  print(f"Units Produced: {report['units_produced']}")
  print("-" * 50)
  print(f"Raw Material Cost: ${report['raw_material_cost']}")
  print(f"Wastage Allowance (5%): ${report['wastage_cost']}")
  print(f"Direct Labor Cost: ${report['labor_cost']}")
  print(f"Machine Operating Cost: ${report['machine_cost']}")
  print(f"Fixed Overheads: ${report['overhead_cost']}")
  print(f"Total Production Cost: ${report['total_production_cost']}")
  print(f"Cost Per Unit: ${report['cost_per_unit']}")
  print("-" * 50)
  print(f"Total Revenue: ${report['total_revenue']}")
  print(f"Net Profit: ${report['net_profit']}")
  print(f"Actual Profit Margin: {report['profit_margin_pct']}%")
  print(f"Target Profit Threshold: {target_profit}%")
  
  status = "YES (Target Achieved)" if report['target_met'] else "NO (Target Missed)"
  print(f"Meets Profit Target: {status}")
