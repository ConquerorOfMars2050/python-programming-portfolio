weight = 41.5

# Ground Shipping
if weight <= 2:
  print(weight * 1.50 + 20.00)
elif weight > 2 and weight <= 6:
  print(weight * 3 + 20.00)
elif weight > 6 and weight <= 10:
  print(weight * 4 + 20.00)
else:
  print(weight * 4.75 + 20.00)

# Ground Shipping Premium
premium_ground_shipping_cost = 125.00
print(premium_ground_shipping_cost)

# Drone Shipping
if weight <= 2:
  print(weight * 4.50)
elif weight > 2 and weight <= 6:
  print(weight * 9.00)
elif weight > 6 and weight <= 10:
  print(weight * 12.00)
else:
  print(weight * 14.25)
