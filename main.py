import pandas as pandas
import numpy as np

file = open('datasource/bc.csv', 'r')

# This is the DataFrame that will be used to calculate the probabilities
df = pandas.DataFrame(pandas.read_csv(file, sep = '\,', engine='python'))

# Total amount of data
data_size = len(df)

# The percentage of samples to extract from the df DataFrame
sample_percentage = 0.2

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

# Overall accuracy
accuracy = data_size

# Naïve Bayes calculation
for i in range(len(samples)):
    original_output = df.iloc[i][margin]
    # print('Original output class:', original_output
    print()
    print('########################################################################################')
    current_sample = df.iloc[i]
    print(current_sample)
    print()
    probability_characteristics = 1.0
    probability_ill_defined = 1.0
    probability_well_defined = 1.0
    for characteristic in characteristics:
        probability_ill_defined *= df.loc[df[margin] == ill_defined][characteristic].value_counts().to_dict()[samples[characteristic].iloc[i]]
        probability_well_defined *= df.loc[df[margin] == well_defined][characteristic].value_counts().to_dict()[samples[characteristic].iloc[i]]
        probability_characteristics *= df[characteristic].value_counts().to_dict()[samples[characteristic].iloc[i]]

    probability_ill_defined *= df.loc[df[margin] == ill_defined][margin].value_counts().to_dict()[ill_defined]
    probability_ill_defined /= data_size

    probability_well_defined *= df.loc[df[margin] == well_defined][margin].value_counts().to_dict()[well_defined]
    probability_well_defined /= data_size

    print('Probabilities:', 'Well-defined =', probability_well_defined / 100.0, '%', '|', 'Ill-defined =', probability_ill_defined / 100.0, '%')
    if (probability_ill_defined > probability_well_defined):
        print('Predicted output class:', ill_defined)
        if (original_output != ill_defined):
            accuracy -= 1
    elif (probability_ill_defined < probability_well_defined):
        print('Predicted output class:', well_defined)
        if (original_output != well_defined):
            accuracy -= 1
    else:
        print('Output:', "Can't determine")

    total_accuracy = (accuracy / data_size) * 100.0
    print('Total accuracy:', total_accuracy, '%')
    print('Total done:', ((i + 1) / len(samples)) * 100.0, '%')
    print('########################################################################################')

pre_calculated_accuracy = (1.0 - (sample_percentage / 2)) * 100.0
print('Pre-calculated accuracy prediction:', pre_calculated_accuracy, '%', '|', 'Error:', np.abs(pre_calculated_accuracy - total_accuracy), '%')
