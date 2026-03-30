from faker import Faker 
import pandas as pd 
import random
from datetime import datetime

fake = Faker()
data = []

for _ in range (10000):
    data.append({
        'shipment_id': fake.uuid4(),
        'customer_id': fake.uuid4(),
        'origin': fake.city(),
        'destination': fake.city(),
        'status': random.choice(['CREATED','IN_TRANSIT','DELIVERED']),
        'create_ts': datetime.now()
    })

print(data)
df = pd.DataFrame(data)
df.to_csv('shipments.csv', index = False)
print('Data genrated successfully')