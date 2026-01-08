import random

def sensor_data_stream():
    while True:
        yield round(random.uniform(20, 30), 2)


sensor = sensor_data_stream()

print("First 10 sensor readings:")
for i in range(10):
    print(next(sensor), "°C")
