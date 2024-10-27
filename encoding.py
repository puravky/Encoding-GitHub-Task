import pandas as pd
import numpy as np

data = {
    'Size': ['Small', 'Medium', 'Large', 'Small', 'Large', 'Medium'],
    'Color': ['Red', 'Blue', 'Green', 'Blue', 'Green', 'Red']
}

df = pd.DataFrame(data)

# Ordinal Encoding
def ordinal_encode(column, categories):
    category_map = {category: idx for idx, category in enumerate(categories)}
    encoded_column = column.map(category_map)
    return encoded_column

size_categories = ['Small', 'Medium', 'Large'] 
df['Size_ordinal_encoded'] = ordinal_encode(df['Size'], size_categories)

print("After Ordinal Encoding on Size wala Column:")
print(df)

# One-Hot Encoding 
def one_hot_encode(column):
    unique_values = column.unique()
    one_hot_df = pd.DataFrame()
    for value in unique_values:
        one_hot_df[f'{column.name}_{value}'] = np.where(column == value, 1, 0)
    return one_hot_df

one_hot_color = one_hot_encode(df['Color'])
df = pd.concat([df, one_hot_color], axis=1)

print("After One-Hot Encoding on Color wala Column:")
print(df)
