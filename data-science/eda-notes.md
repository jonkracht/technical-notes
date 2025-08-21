# Exploratory data analysis

## Environment

For ease, generally performed within a Jupyter environment.

### Libraries
* pandas
* numpy
* matplotlib.pylab as plt (TODO: pyplot vs pylab?)
* seaborn

### Useful settings
* `plt.style.use('ggplot')` uses style sheet for plots
* `pd.set_option('max_columns', 200)` sets number of columns pandas prints to screen
* `%matplotlib inline` display plots inline (i.e. in notebook) rather than opening new window; newer environments like jupyter or modern IDE's do this by default but still a good idea to include for backward compatibility; alternatively, `%matplotlib notebook` allows interactivity (zooming, panning, data inspection) with the plot




## Load data

Import data of interest into a Pandas Dataframe.  Use command like `df = pd.read_csv(PATH/TO/DATA)`.  Other compatible file types include excel, html, json, pickle, sql and xml. 


## Data understanding

Dimensions of dataframe: df.shape
Print first few rows:  df.head()  (defaults to 5 rows unless argument is given)
Print last few rows:  df.tail()
Display column names:  df.columns
Display column dataypes: df.dtypes
Display some statistics of numerical columns:  df.describe()




## Data preparation

### Drop unwanted columns (maybe not of interest or redundant to another column)

#### Method 1
Obtain list of columns via `df.columns`
Copy list into:  `df = df[[COLUMN_LIST_HERE]].copy()` (`copy` ensures a new dataframe is created)
Comment out column names that are not of interest.

#### Method 2
`df.drop([LIST_OF_COLS_TO_DROP], axis=1)`




### Set column datatypes to match expectations

#### Date/time
df['COL'] = pd.to_datetime(df['COL'])

#### Integer
df['COL'] = pd.to_numeric(df['COL'])



### Rename columns
Standardize styling, remove spaces

Make all lowercase (for typing ease):  `df.columns = df.columns.str.lower()`

Rename:  `df.rename(columns={'old_col_name': 'new_col_name', ...})` 
(i.e. input a dictionary mapping old names to new)




### Missing values

#### Compute number of missing values in each column
`df.isna().sum()`
 



### Identify duplicated rows

#### Match on all columns
`df.loc[df.duplicated()]`


#### Match on subset of columns
`df.loc[df.duplicated(subset=['COL',...])]`

Examine possibly identical rows for reasons for duplication:
`df.query('COL' == COL_VAL)`

Remove identified duplicates:
`df = df.loc[~df.duplicated(subset=['COL', ...])].reset_index(drop=True).copy()`




## Feature understanding


### Univariate analysis

* Value counts (counts instances of each value in a column):  `df['COL'].value_counts()`
* Plot value count:  `ax = df['COL'].value_counts.head(10).plot(kind='bar', title = "TITLE")`
* Plot histogram:  `ax = df['COL'].plot(kind='hist', bins=20, title = "TITLE")`
* Kernel density estimation:  `kind=kde`


### Feature relationships

#### Scatter plot

##### Pandas built-in (calling matplotlib)
`df.plot(kind='scatter', x='COL1', y='COL2', title="TITLE")`

##### Seaborn
`sns.scatterplot(x='COL1', y='COL2', data=df)`

Include data from a third column as marker color:  `hue='COL3'`



#### Pair plot

Creates a grid of scatterplots displaying relations between feature pairs

`sns.pairplot(df, vars=['COL1', 'COL2', ...], hue = 'COL3')`

By default, only numerical columns are included

Some flags:
    * 'diag_kind'  Default is to plot histogram on main diagonal.  May also chose 'kde' for kernel density estimation.
    * 'plot_kws = {'alpha': 0.6, 's', 80, 'edgecolor': 'k'}'

Set figure supertitle:  `plt.suptitle('TITLE')`



#### PairGrid

Seaborn class that creates a "pairplot"-type image while letting the upper, lower and diagonal sections be defined independently


* Create instance of PairGrid:  `grid = sns.PairGrid(data = df, vars=[VAR_LIST])`
* Define upper/lower triangle of grid:  `grid = grid.map_upper(plt.scatter, color='darkred'`
* Define main diagonal:  `grid = grid.map_diag(plt.hist, bins=10, color='darkred', edgecolo='k')`

Other functions:  sns.kdeplot




#### Correlations

Shows correlations between various numeric features in the dataframe
`df[[LIST OF NUMERIC COLUMNS]].dropna().corr()`


Display visually by wrapping in seaborn heatmap:  `sns.heatmap(DF_CORR, annot=True)`






### Questions

Typical questions to keep in mind
* Who collected data?
* Do patterns in data conform to real world knowledge expectations?  If not, examine why.
* Any suspicious data points?
* Any patterns in missing values?



Pose questions to be answered by the dataset







## References
### Rob Mulla YT:  Exploratory Data Analysis with Pandas Python
https://www.youtube.com/watch?v=xi0vhXFPegw&list=WL&index=1279

