# create the list named temperatures
temperatures = [25.5, 28.1, 22.9, 30.4, 27.8, 24.3, 29.5]

# Add 31.0 to the end of the temperatures list
temperatures.append(37.0)

# Remove the third element (index 2) from the list
temp = temperatures.pop(3)
print(temp)

# Find the maximum and minimum temperature in the list
max_temperature = max(temperatures)
min_temperature = min(temperatures)

print(max_temperature)
print(min_temperature)