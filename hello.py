from preswald import button, plotly, text, table
import pandas as pd
import plotly.express as px

text("# Welcome to Stock Closing Price Tracker")

# Load CSV data
df2 = pd.read_csv("data/prices.csv")
df2 = df2[df2['Date'] > '2023-01-01']

fig_prices = px.scatter(df2, x='Date', y='Close', color='Ticker', 
                        title='Stock Prices Over Time',
                        labels={'Close': 'Closing Price', 'Date': 'Date'})
fig_prices.update_layout(template='plotly_white',
                            xaxis=dict(rangeselector=dict(buttons=[
                            dict(count=1, label="1m", step="month", stepmode="backward"),
                            dict(count=6, label="6m", step="month", stepmode="backward"),
                            dict(count=1, label="YTD", step="year", stepmode="todate"),
                            dict(count=1, label="1y", step="year", stepmode="backward"),
                            dict(step="all")
                        ]),
                        rangeslider=dict(visible=True),
                        type="date"))
plotly(fig_prices)


avg_closing_price = df2.groupby('Ticker')['Close'].mean().reset_index()
avg_closing_price_sorted = avg_closing_price.sort_values('Close', ascending=False)
fig_bar = px.bar(avg_closing_price_sorted , x='Ticker', y='Close', 
                title='Average Closing Price by Ticker',
                labels={'Close': 'Average Closing Price', 'Ticker': 'Ticker'})
fig_bar.update_layout(template='plotly_white')
plotly(fig_bar)
text("The stock with highest closing cost is: " + avg_closing_price_sorted["Ticker"].iloc[0])