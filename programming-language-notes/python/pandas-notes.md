# Notes on pandas


References:
* [Open ML Course, Topic 1:  Exploratory Data Analysis with Pandas](https://medium.com/open-machine-learning-course/open-machine-learning-course-topic-1-exploratory-data-analysis-with-pandas-de57880f1a68)  [(YouTube version)](https://www.youtube.com/watch?v=fwWCw_cE5aI&list=WL&index=137)
* [pandas documentation:  10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html#object-creation)
* [pandas Cookbook (examples of common pandas code)](https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook)

---
## Initialization

Import pandas into Python:  `import pandas as pd`


Pandas data structure types:
 * 1-dimensional:  series
 * 2-dimensional:  dataframe (akin to a set of series; columns/features may be of mixed datatypes (string, int, etc.))





## Creating pandas data structures


Create manually:  
* Series:  `pd.Series([LIST])`
* Dataframe (dictionary whose keys are column names and values are dataframe values: `pd.DataFrame([Dictionary or Numpy_Array], index=[COLUMN_NAMES])`

Load from file:
* From csv:  `df = pd.read_csv([PATH/TO/CSV])`
* From excel:  `df = pd.read_excel('[FILENAME]')`

Merging:
|Description |Code  |
|--- | --- |
| Concatenate smaller dataframes | `df=pd.concat([SUB_DF1], [SUB_DF2], ...)`|
| Join (SQL-style merges)| `df=pd.merge([SUB_DF1], [SUB_DF2], on=[KEY_VAL])` |



## Summary methods


| Description                           | Code                                                               |
| ---                                   | ---                                                                |
| Get column variable type              | `df.dtypes`                                                        |
| Display column/feature names          | `df.columns`                                                       |
| Print first `N` rows (default is 5)   | `df.head([N])`                                                     |
| Print last `N` rows (default is 5)    | `df.tail([N])`                                                     |
| Display summary of the dataframe      | `df.info`,  `df.describe`                                          |
| Display dimensions                    | `df.shape`                                                         |
| Get row names                         | `df.index`                                                         |
| Get unique values in a column         | `df[[COL]].nunique()`                                              |
| Show frequency counts of two features | `pd.crosstab(df['[COL_1]'], df['[COL_2]'], values=[], aggfunc=[])` |






## Dataframe manipulation
|Description |Code  |
|--- | --- |
| Manually set value(s) by label | `df.at[[ROW], [COL]] = [VALUE]` |
| Manually set value(s) by position | `df.iat[[ROW_IDX], [COL_IDX]] = [VALUE]`|
| Change column variable type (ex. from integer to Boolean) |  `df[[COLUMN]] = df[COLUMN].astype([VARIABLE_TYPE])` |
| Sort dataframe by the values of one of more columns | `df.sort_values(by=[[COL1],[COL2],...], ascending=[[T/F],[T/F],...])`|
| Transpose dataframe (i.e. swap rows and columns) | `df.T` |
| Various mathematical functions |`df.add()`, `df.sub()`, `df.div()`, `df.mul()` |
| Apply function `FUNCT` to elements of column `COL` | `df[[COL]].apply([FUNCT])` |
| Apply "simple" (i.e. lambda-able) function to elements of column `COL` | `df[[COL]].apply([LAMBDA_FUNCTION] )`|
| Transform row/column using key/value pairs of a dictionary|  `df[[COL]].map([DICT])`|
| Add a column| `df.insert(['[NEW_COL]'])` |
| Remove column(s) |  `df.drop([[COL1], [COL2],...], axis=1, inplace=True)`|
| Remove row | `df.drop([[ROW_IDX], [COL_IDX])` |
| Make a numpy array representation of the dataframe (all values must be of the same type) | `df.to_numpy()` |


## Missing values
| Description | Code |
|---|---|
| Drop any rows with missing values | `df.dropna(how="any")`|
| Fill missing values with `[VAL]`| `df.fillna(value=[VAL])` |
| Return a Boolean mask indicating if value is `na` | `pd.isna(df)`|

## Selection
|Desription|Code|
|---|---|
| Select a single column (yields a series) | `df[[COL]]`|
| Select portion of dataframe using column names | `df.loc[[FIRST_ROW]:[LAST_ROW], [COL1], [COL2]]` |
| Select portion of datrame using row, column indices | `df.iloc[[FIRST_ROW]:[LAST_ROW], [COL1_IDX], [COL2_IDX]]`  |
| Get value at specified row, column|  `d.loc[[ROW], [COL]]`|
| Create sub-dataframes whose members have identical feature(s) value | `df.groupby(['[COL1]', '[COL2]', ...])`|
| Create a series whose elements are `[COL2]` values only where `[COL1] == [VAL]` | `df.loc[df[[COL1]] == [VAL], [COL2]]` |
| Select rows of dataframe that meet one or more criteria (==, <, >, etc.) | `df[df[[COL1]] == [VAL1] && df[[COL2]] > [VAL2] && ...]`|
| Select rows whose feature value is one of a desired set | `df[df[[COL].isin([VALUE_LIST])]]`|

Obtain complement set to a logical operation with `~`

## Computations

In general, operations exclude missing values.

|Description |Code  |
|--- | --- |
| Compute mean of a numerical column | `df['[COL]'].mean()`|
| Compute numerical mean of all rows | `df.mean(1)`|
| Compute instances of values in column `[COL]`  | `df['[COL]'].value_counts(normalize=[TRUE/FALSE])`  |
| Compute metrics of all or some subset |  `df.agg([np.mean, np.std, np.min, np.max, ...])`|



## Saving/exporting
|Description |Code  |
|--- | --- |
| Save as csv | `df.to_csv('[FILENAME].csv')`|
| Save to Excel file| `df.to_excel('[FILENAME].xlsx', sheet_name='[SHEET_NAME]')|


## [Miscellaneous](Miscellaneous)
|Description |Code  |pandas histogram sort bins by number
|--- | --- |
| Set number of decimal places displayed in output | `df.to_csv('pd.set('display.precision', [N_DEC_POINTS])')`|
| Set backend for rendering images | `%config InlineBackend.figure_format = 'svg' (or 'png', etc)`|


##sdfa Other methods
* `query`
* `pivot_table`
* `melt`
