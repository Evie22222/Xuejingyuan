import pandas as pd
import matplotlib.pyplot as plt

file_path = './dataset_temperature.csv'
data = pd.read_csv(file_path)

data['time'] = pd.to_datetime(data['time'])

print(data.head())

plt.figure(figsize=(10, 5))
plt.plot(data['time'], data['temperature'], marker='o', linestyle='-')
plt.title('Temperature over Time')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()