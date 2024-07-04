# Print the head of the sales DataFrame
print(sales.head())

# Print the info about the sales DataFrame
print(sales.info())

# Print the mean of weekly_sales
print(sales['weekly_sales'].mean())

# Print the median of weekly_sales
print(sales['weekly_sales'].median())

# Print the maximum of the date column
print(sales['date'].max())

# Print the minimum of the date column
print(sales['date'].min())

# Use the custom iqr function defined for you along with .agg() to print the IQR of the temperature_c column of sales
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)
# Print IQR of the temperature_c column
print(sales['temperature_c'].agg(iqr))

# Update the column selection to use the custom iqr function with .agg() to print the IQR of temperature_c, fuel_price_usd_per_l, and unemployment, in that order.
# A custom IQR function
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg(iqr))


# Update the aggregation functions called by .agg(): include iqr and np.median in that order.
# Import NumPy and create custom IQR function
import numpy as np
def iqr(column):
    return column.quantile(0.75) - column.quantile(0.25)

# Update to print IQR and median of temperature_c, fuel_price_usd_per_l, & unemployment
print(sales[["temperature_c", "fuel_price_usd_per_l", "unemployment"]].agg([iqr,np.median]))

# Sort the rows of sales_1_1 by the date column in ascending order.
sales_1_1 = sales_1_1.sort_values('date',ascending=True)
# Get the cumulative sum of weekly_sales and add it as a new column of sales_1_1 called cum_weekly_sales.
sales_1_1['cum_weekly_sales'] = sales_1_1['weekly_sales'].cumsum()
# Get the cumulative maximum of weekly_sales, and add it as a column called cum_max_sales.
sales_1_1['cum_max_sales']=sales_1_1['weekly_sales'].cummax()
# Print the date, weekly_sales, cum_weekly_sales, and cum_max_sales columns.
print(sales_1_1[["date", "weekly_sales", "cum_weekly_sales", "cum_max_sales"]])

# Remove rows of sales with duplicate pairs of store and type and save as store_types and print the head.
store_types = sales.drop_duplicates(subset=['store','type'])
print(store_types.head())
# Remove rows of sales with duplicate pairs of store and department and save as store_depts and print the head.
store_depts = sales.drop_duplicates(subset=['store','department'])
print(store_depts.head())
# Subset the rows that are holiday weeks using the is_holiday column, and drop the duplicate dates, saving as holiday_dates.
holiday_dates = sales[sales['is_holiday']==True].drop_duplicates(subset='date')
# Select the date column of holiday_dates, and print.
print(holiday_dates['date'])

# Count the number of stores of each store type in store_types.
store_counts = store_types['type'].value_counts()
print(store_counts)
# Count the proportion of stores of each store type in store_types.
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)
# Count the number of different departments in store_depts, sorting the counts in descending order.
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)
# Count the proportion of different departments in store_depts, sorting the proportions in descending order.
dept_props_sorted = store_depts.value_counts(sort=True, normalize=True)
print(dept_props_sorted)

# Calculate the total weekly_sales over the whole dataset.
sales_all = sales["weekly_sales"].sum()
# Subset for type "A" stores, and calculate their total weekly sales.
sales_A = sales[sales["type"] == "A"]["weekly_sales"].sum()
# Do the same for type "B" and type "C" stores.
sales_B = sales[sales["type"] == "B"]["weekly_sales"].sum()
sales_C = sales[sales["type"] == "C"]["weekly_sales"].sum()
# Combine the A/B/C results into a list, and divide by sales_all to get the proportion of sales by type.
sales_propn_by_type = [sales_A, sales_B, sales_C] / sales_all
print(sales_propn_by_type)

# Group sales by "type", take the sum of "weekly_sales", and store as sales_by_type.
sales_by_type = sales.groupby("type")["weekly_sales"].sum()
# Calculate the proportion of sales at each store type by dividing by the sum of sales_by_type. Assign to sales_propn_by_type
sales_propn_by_type =  sales_by_type/ sum(sales_by_type)
print(sales_propn_by_type)

# Group sales by "type" and "is_holiday", take the sum of weekly_sales, and store as sales_by_type_is_holiday.
sales_by_type_is_holiday = sales.groupby(['type','is_holiday'])['weekly_sales'].sum()
print(sales_by_type_is_holiday)

# Import numpy with the alias np.
import numpy as np
# Get the min, max, mean, and median of weekly_sales for each store type using .groupby() and .agg(). Store this as sales_stats. Make sure to use numpy functions!
sales_stats = sales.groupby('type')['weekly_sales'].agg([np.min,np.max,np.mean,np.median])
print(sales_stats)
# Get the min, max, mean, and median of unemployment and fuel_price_usd_per_l for each store type. Store this as unemp_fuel_stats.
unemp_fuel_stats = sales.groupby('type').agg({'unemployment':[np.min,np.max,np.mean,np.median] ,'fuel_price_usd_per_l':[np.min,np.max,np.mean,np.median]})
print(unemp_fuel_stats)

# Get the mean weekly_sales by type using .pivot_table() and store as mean_sales_by_type
mean_sales_by_type = sales.pivot_table(values="weekly_sales", index='type')
print(mean_sales_by_type)

# Get the mean and median (using NumPy functions) of weekly_sales by type using .pivot_table() and store as mean_med_sales_by_type.
# Import NumPy as np
import numpy as np

# Pivot for mean and median weekly_sales for each store type
mean_med_sales_by_type = sales.pivot_table(values='weekly_sales',index='type',aggfunc=[np.mean,np.median])
print(mean_med_sales_by_type)


# Get the mean of weekly_sales by type and is_holiday using .pivot_table() and store as mean_sales_by_type_holiday
mean_sales_by_type_holiday = sales.pivot_table(values='weekly_sales',index='type',columns='is_holiday')
print(mean_sales_by_type_holiday)

# Print the mean weekly_sales by department and type, filling in any missing values with 0.
print(sales.pivot_table(values='weekly_sales',index='department',columns='type',fill_value=0))

# Print the mean weekly_sales by department and type, filling in any missing values with 0 and summing all rows and columns
print(sales.pivot_table(values="weekly_sales", index="department", columns="type", fill_value=0,margins=True))

