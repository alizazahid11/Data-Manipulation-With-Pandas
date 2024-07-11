# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()
print(schools.columns)

# Start coding here...
# Add as many cells as you like...
score=0.8*800
max_score=schools.loc[schools['average_math']>score]
best_math_schools=max_score[['school_name','average_math']].sort_values('average_math',ascending=False)
print(best_math_schools)


# Calculate total SAT score by summing up math, reading, and writing scores
schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools=schools[['school_name','total_SAT']].sort_values('total_SAT',ascending=False).head(10)


borough=schools.groupby('borough')
num_schools=borough.size()
average_SAT=borough['total_SAT'].mean()
std_SAT=borough['total_SAT'].std()
# Create largest_std_dev DataFrame
largest_std_dev = pd.DataFrame({
    'borough': num_schools.index,
    'num_schools': num_schools.values,
    'average_SAT': average_SAT,
    'std_SAT': std_SAT
}).round(2)
# Identify borough with largest std_SAT
largest_std_dev = largest_std_dev.loc[largest_std_dev['std_SAT'].idxmax()].to_frame().T

# Display the result
print(largest_std_dev)