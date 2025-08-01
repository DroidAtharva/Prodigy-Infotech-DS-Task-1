import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_38144.csv', skiprows=4)
df_head = df.head(5)


plt.bar(df_head['Country Name'], df_head['2024'])
plt.xlabel('Country Name')
plt.ylabel('Population in 2024')
plt.title('Population of First 5 Countries (2024)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

