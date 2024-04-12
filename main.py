# Pandas: Remove non-numeric rows in a DataFrame column

import pandas as pd

df = pd.DataFrame({
    'first_name': ['Alice', 'Bobby', 'Carl', 'Dan'],
    'salary': [175.1, 'b', 190.3, 'd'],
    'experience': [10, 15, 20, 25]
})

print(df)

print('-' * 50)

only_numeric = df[
    pd.to_numeric(df['salary'], errors='coerce').notnull()
]

print(only_numeric)