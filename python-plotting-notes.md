# Plotting in Python

## References
* [mlcourse.ai, Topic 2.  Visual Data Analysis](https://mlcourse.ai/book/topic02/topic02_visual_data_analysis.html)
* [seaborn tutorial](https://seaborn.pydata.org/tutorial/distributions.html)

## Initialization


### Matplotlib:  
`import matplotlib.pyplot as plt`

### seaborn:  
`import seaborn as sns`

Set plot style:  `sns.set()`


## Univariate

Examine the characteristics of each feature/variable/column independently

### Quantitative features

#### Histograms/density plots  
Either discrete or continuous representations of value distributions.  May provide insight into underlying distribution(s) (type, skewness, etc.).
* pandas hist method:  `df[[COL1],...].hist()`
* pandas plot method with kind set to 'density':  `df[[COL1],...].plot(kind='density', subplots=True)`
* seaborn distribution plot (identical to `histplot`):  `sns.displot(data=[DATA_FRAME], x=[COL_OF_INTEREST])`
    * flags: binwidth, bins (either number of or a list of bin breaks), discrete, stat="density", probability (normalize histogram)
    * kind = "kde"; flags:  bw_adjust= [Value] controls how wide a bin the density plots averages over; hue, multiple="stack", cut flag specifies how far curve should be computer outside range of data 
    * Histogram + kde density:  `sns.displot(data=[df], x='[COL1]', kde=True)`

* Subplot of histograms:  `df[features].plot(kind="density", subplots=True, layout=(1, 2), sharex=False, figsize=(10, 4))`


#### Boxplot
Shows median, interquartile range and outliers

* `sns.boxplot(data=[df], x='[COL1]')`


#### Violin plot

* `sns.violinplot()`





### Categorical and binary features

(Binary variables are a special case of categorical where there are only two values.)  
Ordinal:  similar to categorical but with an order


#### Bar plot

"Histogram" for categorical variables.

* seaborn's countplot:  `sns.countplot(data=[df], x='[COL1]', ...)`




## Multivariate analysis
Examine relationships between two or more features/variables/columns

### Quantitative/quantative


#### Correlation matrix

* `corr_matrix = df.[[QUANT_COLS]].corr(); sns.heatmap(corr_matrix)`
* Flags for `corr()`:  method="Pearson","", ...
* Use a mask to only show lower triangle
    * mask = np.zeros_like(corr, dtype=np.bool); mask[np.triu_indices_from(mask)] = True
    * sns.heatmap(corr, mask=mask, vmax=1, center=0, annot=True, fmt=".1f", square=True, linewidths=0.5, cbar_kws={"shrink": 0.5});

#### Scatter plot
Cartesian (2D) representation
* `plt.scatter(df[[COL1]], df[[COL2]])`
* Include variable histograms:  `sns.countplot(data=[df], x='[COL1]', y='[COL2]', kind="scatter")`
* Density version:  `sns.jointplot(data=[df], x='[COL1]', y='[COL2]', kind='kde', color='g')`
* Matrix of scatterplots:  `sns.pairplot(data=df[[QUANT_COLS]])`
    * Helpful to use 'png' backend for speedier rendering (`%config InlineBackend.figure_format = 'png' or 'svg' or 'retina'`)


### Quantitative/categorical

#### Scatter plot colored by categorical variable

`sns.lmplot(data=[df], x=[QUANT_COL_1], y=[QUANT_COL_2], hue=[CAT_COL], fit_reg=False)`

#### Boxplots
* `sns.boxplot(data=[df], x=[CAT_COL], y=[QUANT_COL])`
* `sns.catplot(data=[df], x=[CAT_COL_1], y=[QUANT_COL], col=[CAT_COL_2])`




### Categorical/categorical

#### Countplot
`sns.countplot(data=[df], x=[CAT_COL_1], hue=['CAT_COL2'])`





#### Histograms/density plots  

sns.displot  

hue (create histograms where df is partitioned by a specific column value)
element = "step", multiple="stack", "dodge"; common_norm=False normalizes each subset by itself

Create a subplot of histograms:  `sns.displot([df], x='[COL1]', row/col=['COL2'])`

#### Scatter plot


 



### Whole data set visualization


#### t-SNE (t-distributed stochastic neighbor embedding)
Compute a projection onto a lower-dimensional plane

* Required libraries:
    * `from sklearn.manifold import TSNE`
    * `from sklearn.preprocessing import StandardScaler`
* Wrangle features
    * Convert yes/no to 1/0
* Normalize:  `scaler = StandardScaler(); df_scaled = scaler.fit_transform([df])`
* Compute t-SNE representation:  `tsne = TSNE(random_state=[INTEGER]); tsne_rep = tsne.fit_transform(df_scaled)`
* Plot:  `plt.scatter(tsne_rep[:, 0], tsne_rep[:, 1], c=df[[CAT_COL]])`




### Miscellaneous
* Save file with `plt.savefig('[FILENAME]', dpi=[DPI])`
* Default plot settings:  `plt.rcParams["image.cmap"] = "viridis"`
