# Print the head of the avocados dataset. What columns are available?
print(avocados.head())
# For each avocado size group, calculate the total number sold, storing as nb_sold_by_size.
nb_sold_by_size = avocados.groupby('size')['nb_sold'].sum()
# Create a bar plot of the number of avocados sold by size.
nb_sold_by_size.plot(kind="bar")
# Show the plot.
plt.show()

# Get the total number of avocados sold on each date. The DataFrame has two rows for each date—one for organic, and one for conventional. Save this as nb_sold_by_date.
nb_sold_by_date = avocados.groupby('date')['nb_sold'].sum()
# Create a line plot of the number of avocados sold.
nb_sold_by_date.plot(kind='line')
# Show the plot.
plt.show()

# Create a scatter plot with nb_sold on the x-axis and avg_price on the y-axis. Title it "Number of avocados sold vs. average price".
avocados.plot(kind='scatter',x='nb_sold',y='avg_price',title='Number of avocados sold vs. average price')
# Show the plot.
plt.show()

# Subset avocados for the conventional type, and the average price column. Create a histogram.
avocados[avocados['type']=='conventional']['avg_price'].hist()
# Create a histogram of avg_price for organic type avocados.
avocados[avocados['type']=='organic']['avg_price'].hist()
# Add a legend to your plot, with the names "conventional" and "organic".
plt.legend(['conventional','organic'])
# Show your plot.
plt.show()

# Modify histogram transparency to 0.5 
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5)

# Modify histogram transparency to 0.5
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5)

# Modify bins to 20
avocados[avocados["type"] == "conventional"]["avg_price"].hist(alpha=0.5,bins=20)

# Modify bins to 20
avocados[avocados["type"] == "organic"]["avg_price"].hist(alpha=0.5,bins=20)

# Print a DataFrame that shows whether each value in avocados_2016 is missing or not.
print(avocados_2016.isna())
# Print a summary that shows whether any value in each column is missing or not.
print(avocados_2016.isna().any())
# Create a bar plot of the total number of missing values in each column.
avocados_2016.isna().sum().plot(kind='bar')
# Show plot
plt.show()

# Remove the rows of avocados_2016 that contain missing values and store the remaining rows in avocados_complete.
avocados_complete = avocados_2016.dropna()
# Verify that all missing values have been removed from avocados_complete. Calculate each column that has NAs and print.
print(avocados_complete.isna().any())

# A list has been created, cols_with_missing, containing the names of columns with missing values: "small_sold", "large_sold", and "xl_sold".
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
# Create a histogram of those columns.
avocados_2016[cols_with_missing].hist()
# Show the plot.
plt.show()

# Replace the missing values of avocados_2016 with 0s and store the result as avocados_filled.
cols_with_missing = ["small_sold", "large_sold", "xl_sold"]
avocados_2016[cols_with_missing].hist()
plt.show()
# Fill in missing values with 0
avocados_filled = avocados_2016.fillna(0)
# Create a histogram of the cols_with_missing columns of avocados_filled.
avocados_filled[cols_with_missing].hist()
# Show the plot
plt.show()

# Create a list of dictionaries with the new data called avocados_list.
avocados_list = [
    {"date": "2019-11-03", 'small_sold': 10376832, 'large_sold': 7835071},
    {"date": "2019-11-10", 'small_sold': 10717154, 'large_sold': 8561348},
]
# Convert the list into a DataFrame called avocados_2019.
avocados_2019 = pd.DataFrame(avocados_list)
# Print your new DataFrame.
print(avocados_2019)

# Create a dictionary of lists with the new data called avocados_dict.
avocados_dict = {
  "date": ["2019-11-17","2019-12-01"],
  "small_sold": [10859987,9291631],
  "large_sold": [7674135,6238096]
}
# Convert the dictionary to a DataFrame called avocados_2019.
avocados_2019 = pd.DataFrame(avocados_dict)
# Print the new DataFrame
print(avocados_2019)

# Read the CSV file "airline_bumping.csv" and store it as a DataFrame called airline_bumping.
airline_bumping = pd.read_csv('airline_bumping.csv')
# Print the first few rows of airline_bumping.
print(airline_bumping.head())
# For each airline, select nb_bumped and total_passengers and sum
airline_totals = airline_bumping.groupby('airline')[['nb_bumped','total_passengers']].sum()
# Create new col, bumps_per_10k: no. of bumps per 10k passengers for each airline
airline_totals["bumps_per_10k"] = airline_totals['nb_bumped'] / airline_totals['total_passengers'] * 10000
# Print airline_totals
print(airline_totals)

# Sort airline_totals by the values of bumps_per_10k from highest to lowest, storing as airline_totals_sorted.
airline_totals_sorted = airline_totals.sort_values('bumps_per_10k',ascending=False)
# Print your sorted DataFrame.
print(airline_totals_sorted)
# Save the sorted DataFrame as a CSV called "airline_totals_sorted.csv".
airline_totals_sorted.to_csv('airline_totals_sorted.csv')

