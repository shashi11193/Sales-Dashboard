import pandas as pd
import numpy as np
import plotly.express as px
import sqlite3

# Generate the sales data
dates = pd.date_range(start='2020-01-01', end='2020-12-31', freq='D')
sales = np.random.randint(100, 1000, size=len(dates))
sales_data = pd.DataFrame({'Date': dates, 'Sales': sales})
sales_data['7-Day MA'] = sales_data['Sales'].rolling(window=7).mean()

# Plotting the sales data
fig = px.line(sales_data, x='Date', y=['Sales', '7-Day MA'], title='Sales Performance 2020')
fig.show()

# Save data to SQLite database
conn = sqlite3.connect('sales_data.db')
sales_data.to_sql('sales', conn, if_exists='replace', index=False)
conn.close()
