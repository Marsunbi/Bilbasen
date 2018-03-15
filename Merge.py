import pandas as pd

df1 = pd.read_csv('C:/Users/Martin Birkemose/PycharmProjects/Bilbasen/bilbasen2_clean.csv', sep='\t', index_col=0)
df2 = pd.read_csv('C:/Users/Martin Birkemose/PycharmProjects/Bilbasen/bilbasen3_clean.csv', sep='\t', index_col=0)
df3 = pd.read_csv('C:/Users/Martin Birkemose/PycharmProjects/Bilbasen/bilbasen4_clean.csv', sep='\t', index_col=0)

dataframes = [df1, df2, df3]
final_df = pd.concat(dataframes)

final_df.to_csv('final_dataset.csv', sep='\t')
print(final_df.info())