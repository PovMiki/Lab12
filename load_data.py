# Zadanie 2
import random
import pandas as pd
from datetime import datetime, timedelta
from sqlalchemy import create_engine

rows = []
start = datetime(2026, 5, 1)
for _ in range(2000):
    rows.append({
        "event_time": start + timedelta(minutes=random.randint(0, 60 * 24 * 30)),
        "user_id": f"u{random.randint(1, 50):03d}",
        "category": random.choice(["books", "electronics", "clothes", "food", "toys"]),
        "amount": round(random.uniform(5, 300), 2),
        "status": random.choice(["paid", "paid", "paid", "pending", "cancelled"]),
    })

df = pd.DataFrame(rows)
engine = create_engine("postgresql+psycopg2://bi:bi@localhost:5433/ntpd")
df.to_sql("transactions", engine, if_exists="replace", index=False)
print("wiersze", len(df))
