def evaluate_plans(user_usage, max_budget, plans):
  eligible_plans = []

  for plan in plans:
    excess_voice = max(0, user_usage["voice_mins"] - plan["voice_limit"])
    excess_data = max(0, user_usage["data_gb"] - plan["data_limit"])
    excess_sms = max(0, user_usage["sms_count"] - plan["sms_limit"])

    excess_charge = (
        (excess_voice * 0.50) + (excess_data * 10.00) + (excess_sms * 0.10)
    )
    total_cost = plan["base_price"] + excess_charge

    plan_evaluation = {
        "plan_name": plan["plan_name"],
        "base_price": plan["base_price"],
        "excess_charge": round(excess_charge, 2),
        "total_cost": round(total_cost, 2),
        "is_eligible": total_cost <= max_budget,
    }
    eligible_plans.append(plan_evaluation)

  valid_candidates = [p for p in eligible_plans if p["is_eligible"]]
  best_plan = (
      min(valid_candidates, key=lambda x: x["total_cost"])
      if valid_candidates
      else None
  )

  return eligible_plans, best_plan


if __name__ == "__main__":
  user_usage = {"voice_mins": 450, "data_gb": 12, "sms_count": 100}
  max_budget = 60.0

  plans = [
      {
          "plan_name": "Basic Saver",
          "base_price": 30.0,
          "voice_limit": 300,
          "data_limit": 5,
          "sms_limit": 50,
      },
      {
          "plan_name": "Standard Plus",
          "base_price": 45.0,
          "voice_limit": 500,
          "data_limit": 10,
          "sms_limit": 200,
      },
      {
          "plan_name": "Unlimited Ultra",
          "base_price": 70.0,
          "voice_limit": 1000,
          "data_limit": 30,
          "sms_limit": 500,
      },
  ]

  evaluations, best_plan = evaluate_plans(user_usage, max_budget, plans)

  print("Plan Evaluation Summary:")
  for eval_item in evaluations:
    status = "Eligible" if eval_item["is_eligible"] else "Ineligible / Over Budget"
    print(
        f"Plan: {eval_item['plan_name']} | Base: ${eval_item['base_price']}"
        f" | Excess: ${eval_item['excess_charge']} | Total:"
        f" ${eval_item['total_cost']} | Status: {status}"
    )

  print("-" * 60)
  if best_plan:
    print(
        f"Most Economical Eligible Plan: {best_plan['plan_name']} at"
        f" ${best_plan['total_cost']}"
    )
  else:
    print("No plans fit the budget and usage requirements.")
