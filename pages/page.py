import streamlit as st
st.image("milk.webp")
# Title of the page
st.title("        Sales Analysis Project")
st.markdown("<h2 style='text-align: center; color: #4CAF50;'> Exploring the Dairy Goods Sales Dataset 🥛</h2>", unsafe_allow_html=True)

st.markdown("""
### Dataset: [Dairy Goods Sales Dataset (2019-2022)](https://www.kaggle.com/datasets/suraj520/dairy-goods-sales-dataset/data)  

As a **data analyst**, I recently explored this dataset from *Kaggle* and found it quite insightful.  

It provides a **detailed view** of **dairy farm sales performance and inventory management**. However, the currency is in INR, and since I live in Europe, I'll convert it to Euros for better relevance.  

---

### 🔍 Key Aspects Covered:  
✅ **Farm locations & land area**  
✅ **Cow populations & farm sizes** 🐄  
✅ **Sales numbers, stock levels & pricing** (1 INR ≈ 0.011 EUR) 💰  

---

### 🎯 The Goal  
Find **key insights**, spot **trends**, and make **data-driven recommendations** to help optimize **farm efficiency and revenue**.  

💡 **Let's break it down!** 📊🔍  
""")


import streamlit as st
import pandas as pd
import plotly.express as px
import calendar

# Load dataset
df = pd.read_csv('./data/dairy_dataset.csv')

# Ensure 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract Year and Month from the 'Date' column
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

# Group by Year and Month to sum the revenue
monthly_revenue = df.groupby(['Year', 'Month'])['Approx. Total Revenue(INR)'].sum().reset_index()

# Convert month numbers to month names for better readability
monthly_revenue['Month'] = monthly_revenue['Month'].apply(lambda x: calendar.month_abbr[x])

# Convert INR to EUR (approx. conversion rate)
conversion_rate = 0.011
monthly_revenue['Total Revenue (EUR)'] = monthly_revenue['Approx. Total Revenue(INR)'] * conversion_rate

# Plot the revenue trend in EUR
fig = px.line(monthly_revenue, x='Month', y='Total Revenue (EUR)', color='Year',
              title="📅 Monthly Revenue Trends Over the Years (in EUR)",
              labels={'Total Revenue (EUR)': 'Total Revenue (€)', 'Month': 'Month'},
              markers=True)

# Show the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
# 📌 Project Introduction
import streamlit as st
import pandas as pd
import plotly.express as px

st.markdown("# 🥛 Dairy Goods Sales Analysis (2019-2022)")

st.markdown("""
The Dairy Goods Sales Dataset provides a detailed view of **dairy farm operations, sales trends, and inventory management** from **2019 to 2022**.  
By analyzing this data, we aim to uncover **key insights**, identify trends, and make **data-driven recommendations** to improve farm efficiency and revenue.  
""")

# 💰 Total Revenue & Sales Quantity
st.markdown("## 📊 Total Revenue & Sales Quantity")

# Load dataset
df = pd.read_csv('./data/dairy_dataset.csv')

# Ensure 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Define conversion rate (INR to EUR)
INR_TO_EUR = 0.011  

# Convert revenue to EUR
total_revenue_eur = df['Approx. Total Revenue(INR)'].sum() * INR_TO_EUR
total_sales = df['Quantity Sold (liters/kg)'].sum()

# Display metrics in Euros (€)
col1, col2 = st.columns(2)
col1.metric(label="💰 Total Revenue", value=f"{total_revenue_eur:,.2f} EUR")
col2.metric(label="📦 Total Quantity Sold", value=f"{total_sales:,.2f} liters/kg")

st.markdown("""
- **💰 Total Revenue:** Total earnings generated from dairy product sales, displayed in **Euros (€)**.  
- **📦 Total Quantity Sold:** The total volume of dairy products sold, covering **both liquid milk and solid dairy goods** like cheese, yogurt, and butter.  
""")
import streamlit as st
import pandas as pd

# Exchange rate (INR to EUR)
INR_TO_EUR = 0.011  

# 💰 Product Price Overview
st.markdown("## 🏷️ Product Price Overview")

st.markdown("""
Before analyzing sales trends, let's first look at **product pricing**.  
Pricing is crucial for understanding **consumer purchasing behavior** and its impact on revenue.
""")

# 📊 Price Metrics (in EUR)
avg_price_eur = 54.79 * INR_TO_EUR
min_price_eur = 10.03 * INR_TO_EUR
max_price_eur = 99.99 * INR_TO_EUR

col1, col2, col3 = st.columns(3)
col1.metric(label="📊 Avg. Price per Unit", value=f"€{avg_price_eur:.2f}")
col2.metric(label="🔻 Lowest Price per Unit", value=f"€{min_price_eur:.2f}")
col3.metric(label="🔺 Highest Price per Unit", value=f"€{max_price_eur:.2f}")

st.markdown("""
## 📊 Farm Size vs. Revenue – Does a Bigger Farm Mean More Money?

One of the key questions in dairy farm operations is whether **larger farms generate more revenue**, or if smaller farms can be just as profitable.

This analysis compares **Total Land Area (acres)** with **Total Revenue (€)** using a **scatter plot**. Each dot represents a farm:

- **Larger dots** indicate farms with **higher revenue**.
- The **trendline** will help determine if **farm size impacts profitability**.
""")
import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('./data/dairy_dataset.csv')

# Convert revenue to EUR (assuming INR to EUR = 0.011)
INR_TO_EUR = 0.011  
df['Revenue (EUR)'] = df['Approx. Total Revenue(INR)'] * INR_TO_EUR


# Group by farm location and calculate total revenue + average farm size
farm_stats = df.groupby('Location').agg({
    'Total Land Area (acres)': 'mean',  # Average farm size
    'Revenue (EUR)': 'sum'  # Total revenue
}).reset_index()

# Scatter plot for farm size vs revenue
fig = px.scatter(
    farm_stats, 
    x='Total Land Area (acres)', 
    y='Revenue (EUR)', 
    title="📊 Farm Size vs. Revenue (€)",
    labels={'Total Land Area (acres)': 'Farm Size (acres)', 'Revenue (EUR)': 'Total Revenue (€)'},
    size='Revenue (EUR)',  # Bubble size based on revenue
    color='Revenue (EUR)',  # Color by revenue
    color_continuous_scale="magma",  # 🎨 High contrast color
    hover_data=['Location']  # Show farm name on hover
)

# Improve readability
fig.update_layout(
    plot_bgcolor="white",
    font=dict(size=14)
)

# Show in Streamlit
st.plotly_chart(fig, use_container_width=True, key="farm_size_vs_revenue")
import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('./data/dairy_dataset.csv')

# Convert revenue to EUR (assuming INR to EUR = 0.011)
INR_TO_EUR = 0.011  
df['Revenue (EUR)'] = df['Approx. Total Revenue(INR)'] * INR_TO_EUR



import streamlit as st
import pandas as pd


# Load dataset
df = pd.read_csv('./data/dairy_dataset.csv')

# Convert revenue to EUR (assuming INR to EUR = 0.011)
INR_TO_EUR = 0.011  
df['Revenue (EUR)'] = df['Approx. Total Revenue(INR)'] * INR_TO_EUR

import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('./data/dairy_dataset.csv')

# Ensure 'Date' column is in datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Define conversion rate (INR to EUR)
INR_TO_EUR = 0.011  

# Convert INR to EUR for total revenue
df['Total Revenue (EUR)'] = df['Approx. Total Revenue(INR)'] * INR_TO_EUR

# 🏷️ Revenue by Location
st.markdown("## 📍 Revenue by Location")

# Group by Location to sum revenue
location_revenue = df.groupby('Location')['Total Revenue (EUR)'].sum().reset_index()

# Create a bar chart for revenue by location
fig_location = px.bar(location_revenue, x='Location', y='Total Revenue (EUR)',
                      title="📍 Revenue by Location", labels={'Total Revenue (EUR)': 'Revenue (€)'},
                      color='Location')
st.plotly_chart(fig_location, use_container_width=True)
st.markdown("""
Chandigarh, Delhi, and Bihar stand out as the largest consumer markets for our dairy products, consistently driving significant revenue.  

These regions show high demand due to dense populations, strong dairy consumption habits, and well-established distribution channels.  

Urban areas like Chandigarh and Delhi contribute through retail and supermarket sales, while Bihar reflects strong demand in both urban and rural sectors.  
""")


import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('./data/dairy_dataset.csv')


overall_performance = df.groupby('Date')[['Approx. Total Revenue(INR)', 'Quantity Sold (liters/kg)']].sum
import streamlit as st
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv('./data/dairy_dataset.csv')

# Convert revenue to EUR (assuming INR to EUR = 0.011)
INR_TO_EUR = 0.011  
df['Revenue (EUR)'] = df['Approx. Total Revenue(INR)'] * INR_TO_EUR

# Group by farm location and calculate total revenue + average farm size
farm_stats = df.groupby('Location').agg({
    'Total Land Area (acres)': 'mean',  # Average farm size
    'Revenue (EUR)': 'sum'  # Total revenue
}).reset_index()

# Scatter plot for Farm Size vs Revenue
fig1 = px.scatter(
    farm_stats, 
    x='Total Land Area (acres)', 
    y='Revenue (EUR)', 
    title="📊 Farm Size vs. Revenue (€)",
    labels={'Total Land Area (acres)': 'Farm Size (acres)', 'Revenue (EUR)': 'Total Revenue (€)'},
    size='Revenue (EUR)',  # Bubble size based on revenue
    color='Revenue (EUR)',  # Color by revenue
    color_continuous_scale="magma",  # 🎨 High contrast color
    hover_data=['Location']  # Show farm name on hover
)

# Show first plot with a unique key
st.plotly_chart(fig1, use_container_width=True, key="farm_size_vs_revenue_1")

# 🐄 Revenue Per Cow – Does More Cows Mean More Money?
st.markdown("""
## 🐄 Revenue Per Cow – Does More Cows Mean More Money?

Does having **more cows** automatically mean **higher revenue**, or do some farms generate more revenue with **fewer cows**?  

This scatter plot helps us see:  
- **Bigger dots** = Farms generating **more revenue**  
- **Trendline** = Whether **more cows = more money**  
""")

# Grouping data to get revenue and number of cows per farm
farm_cow_stats = df.groupby('Location').agg({
    'Number of Cows': 'sum',  # Total cows per farm
    'Approx. Total Revenue(INR)': 'sum'  # Total revenue per farm
}).reset_index()

# Convert revenue to EUR
farm_cow_stats['Revenue (EUR)'] = farm_cow_stats['Approx. Total Revenue(INR)'] * INR_TO_EUR

# Scatter plot for Revenue Per Cow
fig2 = px.scatter(
    farm_cow_stats, 
    x='Number of Cows', 
    y='Revenue (EUR)', 
    title="🐄 Revenue Per Cow – Does More Cows Mean More Money?",
    labels={'Number of Cows': 'Total Cows', 'Revenue (EUR)': 'Total Revenue (€)'},
    size='Revenue (EUR)',  # Bubble size based on revenue
    color='Revenue (EUR)',  # Color based on revenue
    color_continuous_scale="viridis",  # High contrast colors
    hover_data=['Location']  # Show farm name on hover
)

# Show second plot with a unique key
st.plotly_chart(fig2, use_container_width=True, key="revenue_per_cow_1")


st.markdown("""
## 🏪 Online vs. Retail vs Wholesale – Where Do Dairy Sales Happen?  

Not all sales channels perform the same! Some may be **growing faster**, while others could be **more profitable**.  
- **Is retail still king?** 🏬  
- **Does online sales contribute more than expected?** 💻  
- **How important is wholesale?** 🚛  
""")

# Aggregate Revenue by Sales Channel
channel_revenue = df.groupby('Sales Channel')['Approx. Total Revenue(INR)'].sum().reset_index()

# Convert INR to EUR
channel_revenue['Total Revenue (€)'] = channel_revenue['Approx. Total Revenue(INR)'] * INR_TO_EUR

# Create Bar Chart
fig = px.bar(
    channel_revenue,
    x='Sales Channel',
    y='Total Revenue (€)',
    title="💰 Revenue by Sales Channel",
    text_auto='.2s',
    color='Total Revenue (€)',
    color_continuous_scale="tealrose"
)

# Improve readability
fig.update_layout(
    xaxis_title="Sales Channel",
    yaxis_title="Total Revenue (€)",
    plot_bgcolor="white",
    font=dict(size=14)
)

# Show in Streamlit
st.plotly_chart(fig, use_container_width=True, key="sales_channel_revenue")
import plotly.express as px

st.markdown("""
## 🧀🥛 Butter, Cheese, Milk – What Sells the Best?  

Some products might bring in **higher revenue** than others. This chart shows:  
- **Which dairy product is the biggest money-maker?** 💰  
- **Do some products underperform?** 📉  
- **Should farms focus on high-revenue products?**  
""")

# Aggregate Revenue by Product Name
product_revenue = df.groupby('Product Name')['Approx. Total Revenue(INR)'].sum().reset_index()

# Convert INR to EUR
product_revenue['Total Revenue (€)'] = product_revenue['Approx. Total Revenue(INR)'] * INR_TO_EUR

# Sort Top 5 Products
top_products = product_revenue.sort_values(by='Total Revenue (€)', ascending=False).head(5)

# Create Bar Chart
fig = px.bar(
    top_products,
    x='Product Name',
    y='Total Revenue (€)',
    title="💰 Top 5 Best-Selling Dairy Products",
    text_auto='.2s',
    color='Total Revenue (€)',
    color_continuous_scale="sunset"
)

# Improve readability
fig.update_layout(
    xaxis_title="Product Name",
    yaxis_title="Total Revenue (€)",
    plot_bgcolor="white",
    font=dict(size=14)
)


# Show in Streamlit
st.plotly_chart(fig, use_container_width=True, key="product_revenue")
st.markdown("""
### **Curd**
Curd is a fermented dairy product made from milk. It is created by adding bacterial cultures to warm milk, which helps it coagulate. Curd is typically eaten plain or used as a side dish in meals.

### **Lassi**
Lassi is a yogurt-based drink, popular in India. It is made by blending yogurt with water, and can be either sweet or salted. Lassi is often flavored with fruits, spices, or herbs and is served chilled.
""")

import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
df = pd.read_csv('./data/dairy_dataset.csv')

# Ensure 'Shelf Life (days)' is numeric
df['Shelf Life (days)'] = pd.to_numeric(df['Shelf Life (days)'], errors='coerce')

# Create a histogram
fig = px.histogram(df, x="Shelf Life (days)", nbins=30, title="📉 Shelf Life Distribution",
                   labels={"Shelf Life (days)": "Shelf Life (in days)"},
                   color_discrete_sequence=["#EF553B"])  # Using a strong red color for better contrast
st.markdown("## 🛑 Expiration Risk Analysis")
st.markdown("When discussing milk products, it's important to mention their expiration times, as some spoil much faster than others. Proper storage and handling play a key role in maintaining their quality and preventing waste. It's also crucial to know which products are the most profitable and how long they can be stored to optimize sales and reduce losses.")
# Show plot in Streamlit

st.markdown("### How long do our dairy products last?")
st.plotly_chart(fig, use_container_width=True, key="shelf_life")
# Identify products with the shortest shelf life
short_life_products = df[['Product Name', 'Brand', 'Shelf Life (days)', 'Approx. Total Revenue(INR)']]
short_life_products = short_life_products.groupby(['Product Name', 'Brand']).agg(
    {'Shelf Life (days)': 'min', 'Approx. Total Revenue(INR)': 'sum'}).reset_index()

# Sort by lowest shelf life
short_life_products = short_life_products.sort_values(by="Shelf Life (days)", ascending=True).head(10)

# Create a bar chart
fig = px.bar(short_life_products, x='Product Name', y='Shelf Life (days)',
             color='Approx. Total Revenue(INR)', 
             title="🚨 Top 10 Fastest Expiring Products",
             labels={"Shelf Life (days)": "Shelf Life (in days)", "Product Name": "Product"},
             color_continuous_scale="reds")  # Red scale to indicate risk

# Display in Streamlit
st.markdown("## ⏳ Top 10 Fastest Expiring Products")
st.markdown("These are the dairy products with the shortest shelf life. Quick sales strategies may be needed!")
st.plotly_chart(fig, use_container_width=True, key="short_life_products")
st.markdown("Curd is the best choice—it’s highly profitable and stays fresh for up to 5 days, while milk has a low profit margin and spoils within a day, making it much harder to manage.")



import plotly.express as px
import streamlit as st

# Conversion rate for INR to EUR
INR_TO_EUR = 0.011

# Group by Location and Sales Channel, summing up the revenue or quantity
channel_sales = df.groupby(['Location', 'Sales Channel'])['Approx. Total Revenue(INR)'].sum().reset_index()

# Convert the revenue from INR to EUR
channel_sales['Revenue (EUR)'] = channel_sales['Approx. Total Revenue(INR)'] * INR_TO_EUR

# Get top 3 farms by total revenue (EUR)
top_farms = df.groupby('Location')['Approx. Total Revenue(INR)'].sum().sort_values(ascending=False).head(3).index
top_farms_sales = channel_sales[channel_sales['Location'].isin(top_farms)]

# Filter data for each sales channel
online_sales = top_farms_sales[top_farms_sales['Sales Channel'] == 'Online']
retail_sales = top_farms_sales[top_farms_sales['Sales Channel'] == 'Retail']
wholesale_sales = top_farms_sales[top_farms_sales['Sales Channel'] == 'Wholesale']

# Create pie charts for each sales channel
col1, col2, col3 = st.columns(3)

# Pie chart for Online Sales in EUR
with col1:
    fig_online = px.pie(
        online_sales, 
        names='Location', 
        values='Revenue (EUR)', 
        color='Location',
        title="Online Sales Distribution",
        labels={'Location': 'Farm', 'Revenue (EUR)': 'Revenue (€)'},
        hole=0.3  # Donut chart style
    )
    st.plotly_chart(fig_online, use_container_width=True)

# Pie chart for Retail Sales in EUR
with col2:
    fig_retail = px.pie(
        retail_sales, 
        names='Location', 
        values='Revenue (EUR)', 
        color='Location',
        title="Retail Sales Distribution",
        labels={'Location': 'Farm', 'Revenue (EUR)': 'Revenue (€)'},
        hole=0.3  # Donut chart style
    )
    st.plotly_chart(fig_retail, use_container_width=True)

# Pie chart for Wholesale Sales in EUR
with col3:
    fig_wholesale = px.pie(
        wholesale_sales, 
        names='Location', 
        values='Revenue (EUR)', 
        color='Location',
        title="Wholesale Sales Distribution",
        labels={'Location': 'Farm', 'Revenue (EUR)': 'Revenue (€)'},
        hole=0.3  # Donut chart style
    )
    st.plotly_chart(fig_wholesale, use_container_width=True)
# Ensure 'Date' is in datetime format
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# Create 'Year-Month' column for grouping (convert Period to string)
df['Year-Month'] = df['Date'].dt.to_period('M').astype(str)  # Convert to string for compatibility

# Group data by 'Year-Month' and 'Sales Channel' to calculate total revenue
revenue_by_channel = df.groupby(['Year-Month', 'Sales Channel'])['Approx. Total Revenue(INR)'].sum().reset_index()

# Convert the total revenue to EUR using INR to EUR conversion rate
INR_TO_EUR = 0.011  # INR to EUR conversion rate
revenue_by_channel['Revenue (EUR)'] = revenue_by_channel['Approx. Total Revenue(INR)'] * INR_TO_EUR

# Create the line plot
fig = px.line(
    revenue_by_channel,
    x='Year-Month', 
    y='Revenue (EUR)',  # Show revenue in EUR
    color='Sales Channel',  # Separate lines for each sales channel
    title="📅 Online vs Retail vs Wholesale Sales Over Time (in EUR)",
    labels={'Revenue (EUR)': 'Total Revenue (€)', 'Year-Month': 'Time (Year-Month)'},
    markers=True  # Adding markers to make the lines more readable
)

# Show the chart in Streamlit
st.plotly_chart(fig, use_container_width=True)
import streamlit as st

st.markdown("""
#  Key Takeaways from the Data  

## 🚜 Best Farms & Livestock  
- The **largest farms with the most cows** perform the best in terms of profitability.  

## Main Consumers  
- **Delhi** and **Chhattisgarh** are the top consumer regions.To further boost sales, offering free online delivery or discounts on bulk purchases could attract more customers and enhance market reach.

## 🥛 Top 3 Products  
1. **Curd**  
2. **Butter**  
3. **Lassi**  
We need to explore better storage solutions for curd to extend its shelf life, maintain quality, and create more space for increased storage capacity.
*(Milk is not very profitable and difficult to store & maintain.)*  

##  Best Sales Channel  
- **Retail outperforms both online and offline sales.- There's **not a huge difference** between online and offline sales, indicating **potential for growth** in both channels**  

##  Best Month for Sales  
- **June** has the highest sales, aligning with public holidays in India.  


 

---

""")
