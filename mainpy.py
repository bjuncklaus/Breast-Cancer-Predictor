import pandas as pandas

file = open('datasource/bc.csv', 'r')

# This is the DataFrame that will be used to calculate the probabilities
df = pandas.DataFrame(pandas.read_csv(file, sep = '\,', engine='python'))

# Total amount of data
data_size = len(df)

# The percentage of samples to extract from the df DataFrame
sample_percentage = 0.5

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
    print('Total done:', ((i + 1) / len(samples)) * 100.0, '%')
    original_output = df.iloc[i][margin]
    print('Original output:', original_output)
    probability_characteristics = 1.0
    probability_ill_defined = 1.0
    probability_well_defined = 1.0
    for characteristic in characteristics:
        probability_ill_defined *= df.loc[df[margin] == ill_defined][characteristic].value_counts().to_dict()[samples[characteristic].iloc[i]]
        probability_well_defined *= df.loc[df[margin] == well_defined][characteristic].value_counts().to_dict()[samples[characteristic].iloc[i]]
        probability_characteristics *= df[characteristic].value_counts().to_dict()[samples[characteristic].iloc[i]]

    probability_ill_defined *= df.loc[df[margin] == ill_defined][margin].value_counts().to_dict()[ill_defined]
    probability_ill_defined /= data_size
    # print('Ill-defined probability:', (probability_ill_defined / probability_characteristics) * 100.0)

    probability_well_defined *= df.loc[df[margin] == well_defined][margin].value_counts().to_dict()[well_defined]
    probability_well_defined /= data_size
    # print('Well-defined probability:', (probability_well_defined / probability_characteristics) * 100.0)

    if (probability_ill_defined > probability_well_defined):
        # print('Predicted output:', ill_defined)
        if (original_output != ill_defined):
            accuracy -= 1
    elif (probability_ill_defined < probability_well_defined):
        # print('Predicted output:', well_defined)
        if (original_output != well_defined):
            accuracy -= 1
    else:
        print('Output:', "Can't determine")

    print('Total accuracy:', (accuracy / data_size) * 100.0, '%')