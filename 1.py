# create the list named temperatures
temperatures = [25.5, 28.1, 22.9, 30.4, 27.8, 24.3, 29.5]

# Add 31.0 to the end of the temperatures list
temperatures.append(37.0)

# Remove the third element (index 2) from the list
temp = temperatures.pop(3)
print(temp)

# calculate average temperatures
Average_temperature = sum(temperatures) / len(temperatures)

# Find the maximum and minimum temperature in the list
max_temperature = max(temperatures)
min_temperature = min(temperatures)

print(f"temp_list: {temperatures}")
print(f"max_temp: {max_temperature}")
print(f"min_temp: {min_temperature}")
print(f"Avg_temp: {Average_temperature:.2f}")

