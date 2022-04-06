# Machine Learning Notes

## References
[Open ML, Lecture 3:  Decision Trees & k Nearest Neighbors (KNN)](https://medium.com/open-machine-learning-course/open-machine-learning-course-topic-3-classification-decision-trees-and-k-nearest-neighbors-8613c6b6d2cd)


## Introduction


### Classical machine learning definition

From T. Mitchell's *Machine Learning* (1997).

A  machine is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at task T, as measured by P, improves with experience E.


Experience is available data:  a set of instances/clients/samples with a collection of features

Common tasks:  
1. classification (categorization based on features)
2. regression (predict a numerical value based on other features)
3. clustering (identifying distinct partitions in sample space whose features are alike)
4. anomaly detection (identify samples that are “greatly dissimilar” from others)



## Decision Trees

Determine a series of logical expressions used to group observations in categories.  May be view graphically as a tree. Results are more-easily interpretable by humans.


### Criteria for determining splits

#### Shannon’s entropy  
Measure of how unordered/chaotic/uncertain a system is.  

For a system with $N$ possible states each with probability $p_i$:

$$\displaystyle S = - \sum_{i=1}^{N}  p_i log_2 (p_i)$$


Reduction in entropy can be called Information Gain ($IG$) and is defined as:

$$\displaystyle IG(Q) = S_0 - \sum_{i=1}^n \left( \frac{N_i}{N} \right) S_i$$

where n is number of groups after split, $N_i$ is # of objects in group and $S_i$ is the entropy within the group.

Tradeoff in # of tree splits:  It’s possible to perfectly categorize training data with appropriately chosen groups but will almost certainly overfit any future test data.

Tree-building algorithms:  ID3 or C4.5  (no real explanation given)

#### Gini uncertainty/impurity  
OpenML lecture provides little description.

### Tree-building algorithm

* Greedy maximization
    * At, each step, choose variable/split poin that yields the most information gain/gini uncertainty, etc.  
    * Generally, split is selected in a place where target variable switches value.
* Repeat until total entropy is zero or below some pre-defined threshold

Popular algorithms: ID3, C4.5

Tradeoff in # of tree splits:  It’s possible to perfectly categorize training data with appropriately chosen groups but will almost certainly overfit any future test data.  An example of overfitting.

Exceptions where trees are built to max depth (such that each leaf has only one target class)
1. Random forest
2. Pruning (nodes which provide no great increase in quality are removed)

Tree-building algorithms:  ID3 or C4.5  (no real explanation given)



### Regression with Decision Trees

Choose features that divide data such that variance in each leaf is approximately equal

In `sklearn`:  `from sklearn.tree import DecisionTreeRegressor; reg_tree=DecisionTreeRegressor()`

Yields a piece-wise constant representation.

### Parameter tuning
GridSearchCV

### Evaluating the tree
Using tree, predict values of the heldout data with `tree.predict` and evaluate its performance via accuracy or another comparable metric.





## (k-)Nearest neighbors (kNN)

Predict target variable of a test point from those of the closest surrounding points.

Classification method.  Sometimes used for regression.

Assumptions
1.  Points nearby one another are likely to take the same variable
2.  There exists a sensible way to measure distance between two data points 
    * Hamming, Euclidean, cosine, Minkowski, etc. distances


"Lazy" algorithm:  Computations are only performed in the prediction step (for test points)

### Implementation
`sklearn.Neighbors.KNeighborsClassifier`.  Main parameters are `weights`, `metric`, and `algorithm`.


## Choosing model parameters and cross-validation

Generally, train model on one subset of the data and validate it on the remaining part

Schemes
1.  Hold-out
    * Set aside (or hold out) 20% - 40% for validation
    * Fit model on remaining data
2.  Cross validation
    * Split dataset into $K$ subsets
        * Common values are 5 or 10
        * Stratified cross-validation ensures same proportion of target variable in each fold
    * Perform $K$ hold-out-style analyses sequentially holding out each subset
    * Overall model quality is something like the average of the individual accuracies

`from sklearn.model_selection import train_test_split, StratifiedKFold`



