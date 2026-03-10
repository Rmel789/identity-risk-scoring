import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)
random.seed(42)

np.random.seed(42)
random.seed(42)

users = [f"user_{i:03d}" for i in range(1, 51)]
departments = ["IT", "Finance", "HR", "Engineering", "Sales", "Executive"]
locations = ["New York", "Chicago", "Remote", "London", "Unknown"]
resources = ["email", "vpn", "file_share", "admin_panel", "database", "hr_system", "payroll"]

def random_time(anomalous=False):
    if anomalous:
        hour = random.choice([0, 1, 2, 3, 22, 23])
    else:
        hour = random.randint(7, 19)
    minute = random.randint(0, 59)
    base = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 179))
    return base.replace(hour=hour, minute=minute)

records = []

for _ in range(2000):
    user = random.choice(users)
    anomalous = random.random() < 0.12
    dept = random.choice(departments)
    location = random.choice(["Unknown", "London"]) if anomalous else random.choice(locations[:3])
    resource = random.choice(["admin_panel", "database", "payroll"]) if anomalous else random.choice(resources)
    failed_logins = random.randint(3, 10) if anomalous else random.randint(0, 1)
    timestamp = random_time(anomalous)
    privilege_escalation = 1 if (anomalous and random.random() < 0.4) else 0
    mfa_bypass = 1 if (anomalous and random.random() < 0.3) else 0
    new_device = 1 if (anomalous and random.random() < 0.5) else random.randint(0, 1)
    records.append({
        "timestamp": timestamp,
        "user_id": user,
        "department": dept,
        "location": location,
        "resource_accessed": resource,
        "failed_logins": failed_logins,
        "privilege_escalation": privilege_escalation,
        "mfa_bypass": mfa_bypass,
        "new_device": new_device,
        "session_duration_min": random.randint(1, 30) if anomalous else random.randint(5, 120),
        "is_anomalous": int(anomalous)
    })

df = pd.DataFrame(records).sort_values("timestamp").reset_index(drop=True)
df.to_csv("data/identity_logs.csv", index=False)
print(f"Generated {len(df)} records")
print(f"Anomalous events: {df['is_anomalous'].sum()}")
print(f"Normal events: {(df['is_anomalous'] == 0).sum()}")