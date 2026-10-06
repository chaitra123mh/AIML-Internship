import time
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "http://127.0.0.1:8000/predict"

data = {
    "features": {
        "Age": 30,
        "Gender": "F",
        "Fever": 1,
        "Cough": 1,
        "Fatigue": 0,
        "Breathlessness": 0,
        "Chest_Pain": 0,
        "Nausea": 1,
        "Headache": 1,
        "BMI": 22.0,
        "BP_Systolic": 120,
        "BP_Diastolic": 80,
        "SpO2": 98,
        "Glucose_mg_dL": 100,
        "HbA1c": 5.5
    }
}


def send_request():
    start = time.perf_counter()

    response = requests.post(
        URL,
        json=data,
        timeout=60
    )

    latency = time.perf_counter() - start

    return response.status_code, latency


print("=" * 60)
print("HealthBridge - 50 Concurrent Request Load Test")
print("=" * 60)

start_time = time.perf_counter()

results = []

with ThreadPoolExecutor(max_workers=50) as executor:
    futures = [
        executor.submit(send_request)
        for _ in range(50)
    ]

    for future in as_completed(futures):
        results.append(future.result())

total_time = time.perf_counter() - start_time

successful = [
    latency
    for status, latency in results
    if status == 200
]

failed = 50 - len(successful)

average_latency = (
    sum(successful) / len(successful)
    if successful
    else 0
)

max_latency = (
    max(successful)
    if successful
    else 0
)

throughput = len(successful) / total_time

print(f"Total requests       : 50")
print(f"Successful requests  : {len(successful)}")
print(f"Failed requests      : {failed}")
print(f"Total time           : {total_time:.2f} seconds")
print(f"Average latency      : {average_latency * 1000:.2f} ms")
print(f"Maximum latency      : {max_latency * 1000:.2f} ms")
print(f"Throughput           : {throughput:.2f} requests/second")
print("=" * 60)