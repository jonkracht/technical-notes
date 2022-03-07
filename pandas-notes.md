From article [Exploratory Data Analysis with Pandas](https://medium.com/open-machine-learning-course/open-machine-learning-course-topic-1-exploratory-data-analysis-with-pandas-de57880f1a68)

---


Import pandas into Python:  `import pandas as pd`


Pandas data structure types
 * 1-dimensional:  series
 * 2-dimensional:  dataframe


## Creating dataframe from a file

* From csv:  `df = pd.read_csv([PATH/TO/CSV])`


## Modify a dataframe
* Change column variable type (ex. from integer to Boolean:  
`df[[COLUMN]] = df[COLUMN].astype([VARIABLE_TYPE])`

## Methods to provide info on a dataframe


|Description |Code  |
|--- | --- |
| Print first `N` rows of a dataframe (default is 5) | `df.head([N])`|
| Print last `N` rows of datafarme (default is 5)| `df.tail([N])` |
| Display summary of dataframe | `df.info`,  `df.describe` |
| Print dimensions of dataframe | `df.shape`  |
| Print column/feature names | `df.columns` |
|  |  |

Other methods:  index


## Dataframe manipulation
|Description |Code  |
|--- | --- |
| Sort dataframe by the values of one of more columns | `df.sort_values(by=[[COL1],[COL2],...], ascending=[[T/F],[T/F],...])`|
| Transpose dataframe (i.e. swap rows and columns) | `df.T` |
|  | `df.appy()` |
| Transform row/column |  `df.apply`, `df.map()`|
| Add column to `df`| `df.insert()` |
| Remove column(s) from `df`|  `df.drop([[COL1], [COL2],...], axis=1, inplace=True)`|
| Remove row | `df.drop([[ROW_IDX], [COL_IDX])` |

## Selection
|Desription|Code|
|---|---|
| Create sub-dataframe by a specific column's value| `df.groupby('[COL]')`|
| Select rows of dataframe that meet one or more criteria (==, <, >, etc.) | `df[df[[COL1]] == [VAL1] && df[[COL2]] > [VAL2] && ...]`|
| Select portion of dataframe using column names | `df.loc[[FIRST_ROW]:[LAST_ROW], [COL1], [COL2]]` |
| Select portion of datrame using column indices | `df.iloc[[FIRST_ROW]:[LAST_ROW], [COL1_IDX], [COL2_IDX]]`  |
| Get one value|  `d.loc[[ROW], [COL]]`|

## Computations
|Description |Code  |
|--- | --- |
| Compute mean of a numerical column | `df[[COL]].mean()`|
| Compute instances of values in column `[COL]`  | `df[[COL]].value_counts(normalize=[TRUE/FALSE])`  |
| Compute metrics of all or some subset of `df` |  `df.agg([np.mean, np.std, np.min, np.max, ...])`|

## Saving datafame
|Description |Code  |
|--- | --- |
| Save as csv | `df.to_csv('[FILENAME].csv')`|

