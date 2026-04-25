soil_moisture_data = [23, 25, 19, 30, 28, 21, 24, 26, 22, 27]

average = sum(soil_moisture_data) / len(soil_moisture_data)
maximum = max(soil_moisture_data)
minimum = min(soil_moisture_data)

if average < 22:
    status = "Low moisture - possible instability risk"
elif 22 <= average <= 27:
    status = "Moderate moisture - stable conditions"
else:
    status = "High moisture - potential landslide risk"

print("SOIL STABILITY ANALYSIS")
print(f"Average: {average:.2f}%")
print(f"Max: {maximum}%")
print(f"Min: {minimum}%")
print(f"Status: {status}")
