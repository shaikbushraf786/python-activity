def generate_invoice(cart_items):
  tax_rates = {
      "Electronics": 0.18,
      "Groceries": 0.05,
      "Clothing": 0.12,
      "General": 0.10,
  }

  itemized_bills = []
  gross_total = 0.0

  for item in cart_items:
    rate = tax_rates.get(item["category"], 0.10)
    base_cost = item["unit_price"] * item["quantity"]
    tax_amount = base_cost * rate
    total_price = base_cost + tax_amount

    gross_total += total_price
    itemized_bills.append({
        "product_name": item["product_name"],
        "category": item["category"],
        "quantity": item["quantity"],
        "unit_price": item["unit_price"],
        "tax_amount": round(tax_amount, 2),
        "total_price": round(total_price, 2),
    })

  discount_pct = 0.0
  if gross_total >= 500:
    discount_pct = 0.10
  elif gross_total >= 200:
    discount_pct = 0.05

  raw_discount = gross_total * discount_pct
  capped_discount = min(raw_discount, 100.00)
  net_payable = gross_total - capped_discount

  return {
      "itemized_bills": itemized_bills,
      "gross_total": round(gross_total, 2),
      "discount_pct": discount_pct * 100,
      "discount_applied": round(capped_discount, 2),
      "net_payable": round(net_payable, 2),
  }


if __name__ == "__main__":
  cart = [
      {
          "product_name": "Wireless Mouse",
          "category": "Electronics",
          "quantity": 2,
          "unit_price": 25.0,
      },
      {
          "product_name": "Organic Coffee",
          "category": "Groceries",
          "quantity": 3,
          "unit_price": 15.0,
      },
      {
          "product_name": "Winter Jacket",
          "category": "Clothing",
          "quantity": 1,
          "unit_price": 120.0,
      },
      {
          "product_name": "Bluetooth Speaker",
          "category": "Electronics",
          "quantity": 1,
          "unit_price": 80.0,
      },
  ]

  invoice = generate_invoice(cart)

  print("=== RETAIL INVOICE ===")
  for item in invoice["itemized_bills"]:
    print(
        f"Item: {item['product_name']} ({item['category']}) | Qty:"
        f" {item['quantity']} | Unit: ${item['unit_price']} | Tax:"
        f" ${item['tax_amount']} | Total: ${item['total_price']}"
    )

  print("-" * 50)
  print(f"Gross Total: ${invoice['gross_total']}")
  print(
      f"Discount Tier Applied: {invoice['discount_pct']}% (Capped at Max"
      f" Limit)"
  )
  print(f"Discount Amount: -${invoice['discount_applied']}")
  print(f"Net Payable Amount: ${invoice['net_payable']}")
