import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Read data
ASL_Lex = pd.read_csv('ASL.Lex2.0.clean.csv')
SB = pd.read_csv('All Countries - clean.csv')
languages = ['ASL', 'HKG - Hong Kong', 'ID1 - Jakarta, Indonesia',\
             'ID2 - Yogyakarta, Indonesia', 'JPN - Japan', 'LKA - Sri Lanka',\
             'VN1 - Ho Chi Minh City, Vietnam']
languages_abbr = ['ASL','HKG', 'ID1', 'ID2', 'JPN', 'LKA', 'VN1']

# For handshape, there are 91 possible values for SB.
# Other values are discarded from the data set.
SB = SB[SB.get('Handshape') <= 91]
combined_df = ASL_Lex.append(SB)

# Create a summary table
summary = pd.DataFrame({'Handshape': np.arange(1,101)})
for language in languages:
    summary = pd.merge(summary,
                       combined_df[combined_df.get('Language') == language]\
                       .groupby('Handshape').count().get('Gloss')\
                       /combined_df.groupby('Language').count()\
                       .get('Gloss')[language],\
                       on='Handshape', how='left')
summary = summary.set_index('Handshape')\
          .set_axis(languages_abbr, axis=1)

'''
print(summary)

# Export to CSV
# THE FOLLOWING LINE MAY OVERWRITE A FILE.
#summary.to_csv('frequency_result.csv')

# Plot a heatmap
plt.imshow(summary, cmap='Blues', interpolation='nearest', aspect='auto')
plt.show()

# Plot a scatter
for lang in languages_abbr:
    plt.scatter(range(1, 101), np.array(summary.get(lang)), label=lang, s=18)
plt.legend()
plt.show()
'''

# Replace all NaN with zero
summary = summary.fillna(0)

# Calculate overall frequency of each handshape
averages = summary.mean(axis=1).sort_values(ascending=False)
averages.plot(kind='bar')
plt.xticks(fontsize=8)
plt.show()
