# OpenFlow

OpenFlow is a Python library which lets you handle data flows into your application. It uses pandas.DataFrame as its primary tool.

You can find a basic introduction to OpenFlow [here](https://blog.lapw.at/serverless-data-fetching-stack-openfaas-openflow/).

## Usage

```python
pip install openflow
```

## Example

To use OpenFlow, you need to define a `fetch()` function. This function will fetch the data from the source of your choice. In this example, the source will be this [CSV file](https://raw.githubusercontent.com/fivethirtyeight/data/master/bechdel/movies.csv) containing a list of movies.

> The `fetch()` function has to return a **pandas.Dataframe** instance.

```python
from datetime import date

import pandas as pd
from openflow import DataSource

url = 'https://raw.githubusercontent.com/fivethirtyeight/data/master/bechdel/movies.csv'
fetch = lambda _: pd.read_csv(url)

movies_datasource = DataSource(fetch)
print(movies_datasource.get_dataframe())
#       year       imdb     ...     period code decade code
# 0     2013  tt1711425     ...             1.0         1.0
# 1     2012  tt1343727     ...             1.0         1.0
# ...    ...        ...     ...             ...         ...
# 1792  1971  tt0067992     ...             NaN         NaN
# 1793  1970  tt0065466     ...             NaN         NaN

movies_datasource.add_output('percentage_of_max_budget', lambda df: df['budget'] / df['budget'].max())
movies_datasource.add_output('age', lambda df: date.today().year - df['year'])

# you can reuse previously defined outputs
movies_datasource.add_output('cat_age', lambda df: (df['age'] / 7).astype(int))

# we force the computation because `get_dataframe()` was already called once before
print(movies_datasource.get_dataframe(force_computation=True))

#       year       imdb     ...     percentage_of_max_budget  age  cat_age
# 0     2013  tt1711425     ...                     0.030588    5        0
# 1     2012  tt1343727     ...                     0.105882    6        0
# ...    ...        ...     ...                          ...  ...      ...
# 1792  1971  tt0067992     ...                     0.007059   47        6
# 1793  1970  tt0065466     ...                     0.002353   48        6
```

> Three new outputs have been added to the original DataSource.
