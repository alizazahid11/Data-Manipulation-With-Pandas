# Look at temperatures.
print(temperatures)
# Set the index of temperatures to "city", assigning to temperatures_ind.
temperatures_ind = temperatures.set_index('city')
# Look at temperatures_ind. How is it different from temperatures?
print(temperatures_ind)
# Reset the index of temperatures_ind, keeping its contents.
print(temperatures_ind.reset_index())
# Reset the index of temperatures_ind, dropping its contents.
print(temperatures_ind.reset_index(drop=True))

# Create a list called cities that contains "Moscow" and "Saint Petersburg".
cities = ["Moscow", "Saint Petersburg"]
# Use [] subsetting to filter temperatures for rows where the city column takes a value in the cities list.
print(temperatures[temperatures['city'].isin(cities)])
# Use .loc[] subsetting to filter temperatures_ind for rows where the city is in the cities list.
print(temperatures_ind.loc[cities])

# Set the index of temperatures to the "country" and "city" columns, and assign this to temperatures_ind.
temperatures_ind = temperatures.set_index(['country','city'])
# Specify two country/city pairs to keep: "Brazil"/"Rio De Janeiro" and "Pakistan"/"Lahore", assigning to rows_to_keep.
rows_to_keep = [('Brazil','Rio De Janeiro'),('Pakistan','Lahore')]
# Print and subset temperatures_ind for rows_to_keep using .loc[].
print(temperatures_ind.loc[rows_to_keep])

# Sort temperatures_ind by the index values.
print(temperatures_ind.sort_index())
# Sort temperatures_ind by the index values at the "city" level.
print(temperatures_ind.sort_index(level='city'))
# Sort temperatures_ind by ascending country then descending city.
print(temperatures_ind.sort_index(level=['country','city'],ascending=[True,False]))

# Sort the index of temperatures_ind.
temperatures_srt = temperatures_ind.sort_index()
# Use slicing with .loc[] to get these subsets:
# from Pakistan to Russia.
print(temperatures_srt.loc['Pakistan':'Russia'])
# from Lahore to Moscow. (This will return nonsense.)
print(temperatures_srt.loc["Lahore":"Moscow"])
# from Pakistan, Lahore to Russia, Moscow.
print(temperatures_srt.loc[("Pakistan","Lahore"):("Russia","Moscow")])

# Use .loc[] slicing to subset rows from India, Hyderabad to Iraq, Baghdad.
pprint(temperatures_srt.loc[('India', 'Hyderabad'):('Iraq', 'Baghdad')])
# Use .loc[] slicing to subset columns from date to avg_temp_c.
print(temperatures_srt.loc[:,'date':'avg_temp_c'])
# Slice in both directions at once from Hyderabad to Baghdad, and date to avg_temp_c.
print(temperatures_srt.loc[('India','Hyderabad'):('Iraq','Baghdad'),'date','avg_temp_c'])

# Use Boolean conditions, not .isin() or .loc[], and the full date "yyyy-mm-dd", to subset temperatures for rows in 2010 and 2011 and print the results.
temperatures_bool = temperatures[(temperatures['date'] >= '2010-01-01') & (temperatures['date'] <= '2011-12-31')]
print(temperatures_bool)
# Set the index of temperatures to the date column and sort it.
temperatures_ind = temperatures.set_index('date').sort_index()
# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011.
print(temperatures_ind.loc['2010':'2011'])
# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011.
print(temperatures_ind.loc['2010-08':'2011-02'])

# Use .iloc[] on temperatures to take subsets.

# Get the 23rd row, 2nd column (index positions 22 and 1).
print(temperatures.iloc[22,1])
# Get the first 5 rows (index positions 0 to 5).
print(temperatures.iloc[0:5,:])
# Get all rows, columns 3 and 4 (index positions 2 to 4).
print(temperatures.iloc[:,2:4])
# Get the first 5 rows, columns 3 and 4.
print(temperatures.iloc[0:5,2:4])

# Add a year column to temperatures, from the year component of the date column.
temperatures['year']=temperatures['date'].dt.year
# Make a pivot table of the avg_temp_c column, with country and city as rows, and year as columns. Assign to temp_by_country_city_vs_year, and look at the result.
temp_by_country_city_vs_year = temperatures.pivot_table('avg_temp_c',index=['country','city'],columns='year')
print(temp_by_country_city_vs_year)

# Use .loc[] on temp_by_country_city_vs_year to take subsets.

# From Egypt to India.
temp_by_country_city_vs_year.loc['Egypt':'India']
# From Egypt, Cairo to India, Delhi.
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi')]
# From Egypt, Cairo to India, Delhi, and 2005 to 2010.
temp_by_country_city_vs_year.loc[('Egypt','Cairo'):('India','Delhi'),'2005':'2010']

# Calculate the mean temperature for each year, assigning to mean_temp_by_year.
mean_temp_by_year = temp_by_country_city_vs_year.mean()
# Filter mean_temp_by_year for the year that had the highest mean temperature.
print(mean_temp_by_year[mean_temp_by_year==mean_temp_by_year.max()])
# Calculate the mean temperature for each city (across columns), assigning to mean_temp_by_city.
mean_temp_by_city = temp_by_country_city_vs_year.mean(axis="columns")
# Filter mean_temp_by_city for the city that had the lowest mean temperature.
print(mean_temp_by_city[mean_temp_by_city==mean_temp_by_city.min()])