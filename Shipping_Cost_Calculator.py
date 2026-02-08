# Shipping Cost Calculator

try:
  ## Input package weight and shipping rate
  weight = float(input("Enter the package weight in kilograms: "))
  rate = float(input("Enter the shipping rate per kilogram: "))

  if weight < 0 or rate < 0:
    raise ValueError("Must be non-negative.");
  
  ## Calculate shipping cost
  shipping_cost = weight * rate
  
  ## Display the result
  print(f"Shipping Cost: {shipping_cost:.2f} USD")
  
except ValueError as e:
  print(f"Invalid Input: {e}")
