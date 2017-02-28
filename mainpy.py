import pandas as pandas
import random
import numpy as np

file = open('datasource/bc.csv', 'r')

# This is the DataFrame that will be used to calculate the probabilities
df = pandas.DataFrame(pandas.read_csv(file, sep = '\,', engine='python'))

# Total amount of data
data_size = len(df)

# The percentage of samples to extract from the df DataFrame
sample_percentage = 0.3

# The extracted samples. Note that samples is also a DataFrame
samples = df.sample(n = sample_percentage * data_size)

# Dropping the samples from the df DataFrame
df = df.drop(samples.index)

# Header of the outcome classes
margin = 'Margin'

# Outcome classes
well_defined = 'Well-defined'
ill_defined = 'Ill-defined'

# Header of the Characteristics
breast_density = 'BreastDensity'
location = 'Location'
age = 'Age'
bc = 'BC'
mass = 'Mass'
ad = 'AD'
metastasis = 'Metastasis'
mc = 'MC'
size = 'Size'
shape = 'Shape'
fiber_tissue_development = 'FibrTissueDev'
lymph_nodes = 'LymphNodes'
skin_retract = 'SkinRetract'
nipple_discharge = 'NippleDischarge'
spiculation = 'Spiculation'

characteristics = [breast_density, location, age, bc, mass, ad, metastasis, mc, size, shape, fiber_tissue_development, lymph_nodes, skin_retract, nipple_discharge, spiculation]

# dict = df.loc[df[margin] == ill_defined][breast_density].value_counts().to_dict()

# print(df.loc[df[margin] == ill_defined][breast_density].value_counts().to_dict()[samples[breast_density].iloc[0]] / data_size)
# print(df.loc[df[margin] == ill_defined][margin].value_counts().to_dict()[ill_defined] / data_size)

# print(samples[breast_density].iloc[0])
# for a in df.loc[df[margin] == ill_defined][breast_density].value_counts().to_dict():
#     print(a)
# samples[breast_density].iloc[0]

probability_c = 0
for i in range(len(samples)):
    print('Sample:', df.iloc[i])
    working_probability_ill = 1
    working_probability_well = 1
    for characteristic in characteristics:
        working_probability_ill *= df.loc[df[margin] == ill_defined][characteristic].value_counts().to_dict()[samples[characteristic].iloc[i]] / data_size
        working_probability_well *= df.loc[df[margin] == well_defined][characteristic].value_counts().to_dict()[samples[characteristic].iloc[i]] / data_size

    probability_c = working_probability_ill
    working_probability_ill *= df.loc[df[margin] == ill_defined][margin].value_counts().to_dict()[ill_defined] / data_size
    print('Ill-defined probability:', (working_probability_ill / probability_c) * 100)

    probability_c = working_probability_well
    working_probability_well *= df.loc[df[margin] == well_defined][margin].value_counts().to_dict()[well_defined] / data_size
    print('Well-defined probability:', (working_probability_well / probability_c) * 100)

# for a in samples[breast_density]:
#     print(a)

# print(df.loc[df[margin] == well_defined]['BreastDensity'].value_counts())
# print(df.loc[df[margin] == ill_defined]['BreastDensity'].value_counts())
