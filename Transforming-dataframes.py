# Print the head of the homelessness data
print(homelessness.head())
# Print information about homelessness
print(homelessness.info())

# Print the shape of homelessness
print(homelessness.shape)

# Print a description of homelessness
print(homelessness.describe())

# Import pandas using the alias pd
import pandas as pd

# Print the values of homelessness
print(homelessness.values)

# Print the column index of homelessness
print(homelessness.columns)

# Print the row index of homelessness
print(homelessness.index)

# Sort homelessness by the number of homeless individuals, from smallest to largest, and save this as homelessness_ind.
# Print the head of the sorted DataFrame.
# Sort homelessness by individuals
homelessness_ind = homelessness.sort_values('individuals')
# Print the top few rows
print(homelessness_ind.head())
# Sort homelessness by the number of homeless family_members in descending order, and save this as homelessness_fam.
# Print the head of the sorted DataFrame.
# Sort homelessness by descending family members
homelessness_fam = homelessness.sort_values('family_members',ascending=False)
# Print the top few rows
print(homelessness_fam.head())
# Sort homelessness first by region (ascending), and then by number of family members (descending). Save this as homelessness_reg_fam.
# Print the head of the sorted DataFrame.
# Sort homelessness by region, then descending family members
homelessness_reg_fam = homelessness.sort_values(['region','family_members'],ascending=[True,False])
# Print the top few rows
print(homelessness_reg_fam.head())

# Create a DataFrame called individuals that contains only the individuals column of homelessness.
# Select the individuals column
individuals = homelessness['individuals']
# Print the head of the result
print(individuals.head())

# Create a DataFrame called state_fam that contains only the state and family_members columns of homelessness, in that order.
# Select the state and family_members columns
state_fam = homelessness[["state","family_members"]]
# Print the head of the result
print(state_fam.head())

# Create a DataFrame called ind_state that contains the individuals and state columns of homelessness, in that order.
# Select only the individuals and state columns, in that order
ind_state = homelessness[["individuals","state"]]
# Print the head of the result
print(ind_state.head())

# Filter homelessness for cases where the number of individuals is greater than ten thousand, assigning to ind_gt_10k. View the printed result.
# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[(homelessness['individuals']>10000)]
print(ind_gt_10k)

# Filter homelessness for cases where the USA Census region is "Mountain", assigning to mountain_reg. View the printed result.
# Filter for rows where region is Mountain
mountain_reg = homelessness[(homelessness['region']=="Mountain")]
print(mountain_reg)


# Filter homelessness for cases where the number of family_members is less than one thousand and the region is "Pacific", assigning to fam_lt_1k_pac. View the printed result.
# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac = homelessness[(homelessness['family_members']<1000) & (homelessness['region']=='Pacific')]
print(fam_lt_1k_pac)

# Filter homelessness for cases where the USA census region is "South Atlantic" or it is "Mid-Atlantic", assigning to south_mid_atlantic. View the printed result.
# Subset for rows in South Atlantic or Mid-Atlantic regions
south_mid_atlantic = homelessness[(homelessness['region'].isin(['South Atlantic','Mid-Atlantic']))]
print(south_mid_atlantic)

# Filter homelessness for cases where the USA census state is in the list of Mojave states, canu, assigning to mojave_homelessness. View the printed result.
# The Mojave Desert states
canu = ["California", "Arizona", "Nevada", "Utah"]
# Filter for rows in the Mojave Desert states
mojave_homelessness = homelessness[(homelessness['state'].isin(canu))]
print(mojave_homelessness)

# Add a new column to homelessness, named total, containing the sum of the individuals and family_members columns.
# Add another column to homelessness, named p_individuals, containing the proportion of homeless people in each state who are individuals.
# Add total col as sum of individuals and family_members
homelessness['total']=homelessness['individuals']+   homelessness['family_members']
# Add p_individuals col as proportion of total that are individuals
homelessness['p_individuals']= homelessness['individuals'] / homelessness['total']
print(homelessness)

# Add a column to homelessness, indiv_per_10k, containing the number of homeless individuals per ten thousand people in each state.
# Subset rows where indiv_per_10k is higher than 20, assigning to high_homelessness.
# Sort high_homelessness by descending indiv_per_10k, assigning to high_homelessness_srt.
# Select only the state and indiv_per_10k columns of high_homelessness_srt and save as result. Look at the result.
# Create indiv_per_10k col as homeless individuals per 10k state pop
homelessness["indiv_per_10k"] = 10000 * homelessness['individuals'] / homelessness['state_pop']
# Subset rows for indiv_per_10k greater than 20
high_homelessness = homelessness[(homelessness['indiv_per_10k']>20)]
# Sort high_homelessness by descending indiv_per_10k
high_homelessness_srt = high_homelessness.sort_values('indiv_per_10k',ascending=False)
# From high_homelessness_srt, select the state and indiv_per_10k cols
result = high_homelessness_srt[['state','indiv_per_10k']]
print(result)

