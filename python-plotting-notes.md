# Plotting in Python

## References
* [mlcourse.ai, Topic 2.  Visual Data Analysis](https://mlcourse.ai/book/topic02/topic02_visual_data_analysis.html)

## Initialization



Matplotlib:  `import matplotlib.pyplot as plt`

seaborn:  `import seaborn as sns`

Set plot style:  `sns.set()`


## Univariate analysis

Analyze features independently

Histograms/density plots:  may provide insight into underlying distribution (type, skewness, etc.)
* pandas hist method:  `df[[COL1],...].hist()`
* pandas plot method of type 'density':  `df[[COL1],...].plot(kind='density', subplots=True)`
* seaborn distribution plot:  sns.displot(

## Multivariate analysis


