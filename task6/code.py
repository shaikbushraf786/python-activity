def calculate_passenger_fare(distance, travel_class, passenger):
  class_rates = {"SL": 0.05, "3AC": 0.10, "2AC": 0.15, "1AC": 0.22}
  reservation_fees = {"SL": 2.00, "3AC": 4.00, "2AC": 5.00, "1AC": 6.00}

  rate = class_rates.get(travel_class, 0.05)
  res_fee = reservation_fees.get(travel_class, 2.00)

  base_fare = distance * rate
  discount = 0.0

  if passenger["age"] >= 60:
    discount = base_fare * 0.40
  elif passenger["age"] <= 5:
    discount = base_fare * 1.00

  discounted_fare = base_fare - discount
  total_ticket_fare = discounted_fare + res_fee

  return {
      "name": passenger["name"],
      "age": passenger["age"],
      "base_fare": round(base_fare, 2),
      "discount": round(discount, 2),
      "reservation_fee": res_fee,
      "total_fare": round(total_ticket_fare, 2),
  }


def process_reservation(distance, travel_class, passengers):
  itinerary = []
  total_group_cost = 0.0

  for p in passengers:
    ticket = calculate_passenger_fare(distance, travel_class, p)
    itinerary.append(ticket)
    total_group_cost += ticket["total_fare"]

  return itinerary, round(total_group_cost, 2)


if __name__ == "__main__":
  distance = 750
  travel_class = "3AC"
  passengers = [
      {"name": "Arthur Pendelton", "age": 35},
      {"name": "Margaret Pendelton", "age": 62},
      {"name": "Leo Pendelton", "age": 4},
  ]

  itinerary, total_cost = process_reservation(distance, travel_class, passengers)

  print(f"Travel Distance: {distance} KM | Class: {travel_class}")
  print("-" * 65)
  for t in itinerary:
    print(
        f"Passenger: {t['name']} (Age: {t['age']}) | Base: ${t['base_fare']}"
        f" | Disc: ${t['discount']} | Res Fee: ${t['reservation_fee']}"
        f" | Total: ${t['total_fare']}"
    )
  print("-" * 65)
  print(f"Total Group Reservation Cost: ${total_cost}")
