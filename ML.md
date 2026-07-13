# Machine Learning Formulas — Complete Reference

---

## 0. Bias, Variance, Overfitting & Underfitting

**Bias** — error from wrong assumptions in the model (model too simple to capture pattern).
```
Bias[f̂(x)] = E[f̂(x)] − f(x)
```

**Variance** — error from sensitivity to fluctuations in the training set.
```
Var[f̂(x)] = E[ (f̂(x) − E[f̂(x)])^2 ]
```

**Bias–Variance Decomposition (Expected Test Error):**
```
E[(y − f̂(x))^2] = Bias[f̂(x)]^2 + Var[f̂(x)] + σ²
```
where σ² = irreducible noise.

**Trade-off:** Increasing model complexity → Bias ↓, Variance ↑ (and vice versa). Optimal model minimizes total error = Bias² + Variance.

**Underfitting:** High bias, low variance. Model too simple → poor performance on both train & test data.

**Overfitting:** Low bias, high variance. Model too complex → fits noise → great on train, poor on test data.

---

## 1. Linear Regression

**Algebraic form (single variable):**
```
y = β0 + β1·x + ε
```

**Vector / matrix form:**
```
y = Xβ + ε
```

**Closed-form solution (Normal Equation):**
```
β̂ = (XᵀX)⁻¹ Xᵀy
```

**Cost function (MSE / Loss):**
```
J(β) = (1/2m) Σᵢ (ŷᵢ − yᵢ)²
```

**Gradient Descent update rule:**
```
βⱼ := βⱼ − α · (1/m) Σᵢ (ŷᵢ − yᵢ)·xᵢⱼ
```
(α = learning rate, m = number of samples)

**In vector form:**
```
β := β − α·(1/m)·Xᵀ(Xβ − y)
```

**Performance / Error Metrics:**
```
MAE  = (1/m) Σ |yᵢ − ŷᵢ|
MSE  = (1/m) Σ (yᵢ − ŷᵢ)²
RMSE = √MSE
R²   = 1 − (SS_res / SS_tot) = 1 − Σ(yᵢ−ŷᵢ)² / Σ(yᵢ−ȳ)²
Adjusted R² = 1 − [(1−R²)(n−1)/(n−k−1)]
```

---

## 2. Multiple Linear Regression

**Algebraic form:**
```
y = β0 + β1x1 + β2x2 + ... + βnxn + ε
```

**Matrix form (same as linear regression, X now has n features):**
```
y = Xβ + ε,  X ∈ ℝ^(m×(n+1))
```

**Normal Equation:**
```
β̂ = (XᵀX)⁻¹ Xᵀy
```

**Gradient Descent (vectorized):**
```
β := β − α·(1/m)·Xᵀ(Xβ − y)
```

**Cost Function (with L2 / Ridge regularization):**
```
J(β) = (1/2m)[ Σ(ŷᵢ−yᵢ)² + λ Σ βⱼ² ]
```

**Ridge update rule:**
```
βⱼ := βⱼ − α[(1/m)Σ(ŷᵢ−yᵢ)xᵢⱼ + (λ/m)βⱼ]
```

**Lasso (L1) Cost:**
```
J(β) = (1/2m) Σ(ŷᵢ−yᵢ)² + λ Σ|βⱼ|
```

**Metrics:** same as Linear Regression (MAE, MSE, RMSE, R², Adjusted R²) + **VIF** for multicollinearity:
```
VIFⱼ = 1 / (1 − Rⱼ²)
```

---

## 3. Logistic Regression

**Algebraic (linear combination):**
```
z = β0 + β1x1 + ... + βnxn = βᵀx
```

**Sigmoid / Logistic function:**
```
ŷ = σ(z) = 1 / (1 + e^(−z))
```

**Vectorized hypothesis:**
```
ŷ = σ(Xβ)
```

**Odds & Log-odds (logit):**
```
odds = p/(1−p)
logit(p) = ln( p / (1−p) ) = βᵀx
```

**Cost Function (Binary Cross-Entropy / Log Loss):**
```
J(β) = −(1/m) Σ [ yᵢ ln(ŷᵢ) + (1−yᵢ) ln(1−ŷᵢ) ]
```

**Gradient Descent update:**
```
βⱼ := βⱼ − α·(1/m) Σ (ŷᵢ − yᵢ)·xᵢⱼ
```

**Vectorized:**
```
β := β − α·(1/m)·Xᵀ(σ(Xβ) − y)
```

**Performance Metrics:**
```
Confusion Matrix: TP, TN, FP, FN

Accuracy    = (TP+TN)/(TP+TN+FP+FN)
Precision   = TP/(TP+FP)
Recall/TPR  = TP/(TP+FN)
Specificity = TN/(TN+FP)
F1-Score    = 2·(Precision·Recall)/(Precision+Recall)
AUC-ROC     = area under (TPR vs FPR) curve
FPR         = FP/(FP+TN)
```

---

## 4. Support Vector Machine (SVM)

**Linear SVM — Hyperplane (algebra):**
```
wᵀx + b = 0
```

**Decision rule:**
```
ŷ = sign(wᵀx + b)
```

**Margin (geometric, angle-based interpretation):**
```
margin = 2 / ‖w‖
```
Distance of a point from hyperplane:
```
d = (wᵀx + b) / ‖w‖
```

**Primal Optimization Problem (Hard Margin):**
```
minimize:  (1/2)‖w‖²
subject to: yᵢ(wᵀxᵢ + b) ≥ 1  ∀i
```

**Soft Margin (with slack ξᵢ):**
```
minimize:  (1/2)‖w‖² + C·Σξᵢ
subject to: yᵢ(wᵀxᵢ + b) ≥ 1 − ξᵢ,  ξᵢ ≥ 0
```

**Hinge Loss (Cost Function):**
```
J(w) = C·Σ max(0, 1 − yᵢ(wᵀxᵢ+b)) + (1/2)‖w‖²
```

**Gradient Descent update (sub-gradient):**
```
If yᵢ(wᵀxᵢ+b) ≥ 1:   w := w − α·w
Else:                 w := w − α·(w − C·yᵢxᵢ)
```

**Dual form (Lagrangian):**
```
max Σαᵢ − (1/2)ΣΣ αᵢαⱼyᵢyⱼ(xᵢᵀxⱼ)
subject to: 0 ≤ αᵢ ≤ C,  Σαᵢyᵢ = 0
```

**Kernel Trick — replace xᵢᵀxⱼ with K(xᵢ,xⱼ):**

Linear Kernel:
```
K(xᵢ,xⱼ) = xᵢᵀxⱼ
```

Polynomial Kernel:
```
K(xᵢ,xⱼ) = (xᵢᵀxⱼ + c)^d
```

Gaussian / RBF Kernel:
```
K(xᵢ,xⱼ) = exp( −‖xᵢ−xⱼ‖² / (2σ²) )   OR   exp(−γ‖xᵢ−xⱼ‖²)
```

**Performance Metrics:** Accuracy, Precision, Recall, F1, ROC-AUC (same as Logistic Regression above).

---

## 5. Decision Trees

**Entropy (measure of impurity):**
```
H(S) = −Σ pᵢ log₂(pᵢ)
```

**Information Gain (split criterion):**
```
IG(S,A) = H(S) − Σ ( |Sᵥ|/|S| )·H(Sᵥ)
```

**Gini Impurity:**
```
Gini(S) = 1 − Σ pᵢ²
```

**Gini Gain:**
```
ΔGini = Gini(S) − Σ (|Sᵥ|/|S|)·Gini(Sᵥ)
```

**Variance Reduction (for regression trees):**
```
Var(S) = (1/N) Σ (yᵢ − ȳ)²
```

**Gain Ratio (C4.5, corrects bias toward many-valued attributes):**
```
GainRatio(S,A) = IG(S,A) / SplitInfo(S,A)
SplitInfo(S,A) = −Σ (|Sᵥ|/|S|) log₂(|Sᵥ|/|S|)
```

**Performance Metrics:** Accuracy, Precision, Recall, F1 (classification); MSE, RMSE, R² (regression trees).

---

## 6. Naive Bayes

**Bayes' Theorem (algebra):**
```
P(y|x) = [ P(x|y)·P(y) ] / P(x)
```

**Naive Bayes assumption (conditional independence):**
```
P(x1,x2,...,xn | y) = Π P(xᵢ|y)
```

**Classification rule (MAP estimate):**
```
ŷ = argmax_y [ P(y) · Π P(xᵢ|y) ]
```

**Log form (avoids underflow):**
```
ŷ = argmax_y [ ln P(y) + Σ ln P(xᵢ|y) ]
```

**Gaussian Naive Bayes (continuous features):**
```
P(xᵢ|y) = 1/√(2πσ_y²) · exp( −(xᵢ−μ_y)² / (2σ_y²) )
```

**Laplace Smoothing (for categorical data):**
```
P(xᵢ|y) = (count(xᵢ,y) + 1) / (count(y) + k)
```
(k = number of feature categories)

**Performance Metrics:** Accuracy, Precision, Recall, F1, Confusion Matrix (same formulas as Logistic Regression section).

---

## 7. K-Nearest Neighbors (KNN)

**Distance Metrics:**

Euclidean:
```
d(x,x') = √( Σ (xᵢ−x'ᵢ)² )
```

Manhattan:
```
d(x,x') = Σ |xᵢ−x'ᵢ|
```

Minkowski (generalized):
```
d(x,x') = ( Σ |xᵢ−x'ᵢ|^p )^(1/p)
```

Cosine Similarity / angle-based distance:
```
cos(θ) = (x·x') / (‖x‖‖x'‖)
d_cosine = 1 − cos(θ)
```

**Classification rule:**
```
ŷ = mode{ yᵢ : xᵢ ∈ N_k(x) }
```

**Regression rule:**
```
ŷ = (1/k) Σ yᵢ,  xᵢ ∈ N_k(x)
```

**Weighted KNN:**
```
ŷ = Σ wᵢyᵢ / Σwᵢ,   wᵢ = 1/d(x,xᵢ)²
```

**Performance Metrics:** Accuracy, Precision, Recall, F1 (classification); MAE, MSE, RMSE (regression).

---

## 8. Linear Discriminant Analysis (LDA)

**Class Mean:**
```
μ_k = (1/N_k) Σ xᵢ  (for class k)
```

**Within-Class Scatter Matrix:**
```
S_W = Σ_k Σ_(xᵢ∈k) (xᵢ−μ_k)(xᵢ−μ_k)ᵀ
```

**Between-Class Scatter Matrix:**
```
S_B = Σ_k N_k (μ_k−μ)(μ_k−μ)ᵀ
```
(μ = overall mean)

**Objective (Fisher's criterion) — maximize class separation (angle/projection based):**
```
J(w) = (wᵀS_B w) / (wᵀS_W w)
```

**Optimal projection vector (solved via generalized eigenvalue problem):**
```
S_W⁻¹S_B w = λw
```

**Discriminant function (linear boundary):**
```
δ_k(x) = xᵀΣ⁻¹μ_k − (1/2)μ_kᵀΣ⁻¹μ_k + ln(π_k)
```

**Classification rule:**
```
ŷ = argmax_k δ_k(x)
```

**Performance Metrics:** Accuracy, Precision, Recall, F1, confusion matrix.

---

## 9. Multi-Layer Feedforward Networks & Perceptron

**Perceptron — Algebraic:**
```
z = Σ wᵢxᵢ + b = wᵀx + b
ŷ = f(z),  f = step function: f(z) = 1 if z≥0 else 0
```

**Perceptron Learning Rule (weight update):**
```
wᵢ := wᵢ + α(y − ŷ)xᵢ
b  := b + α(y − ŷ)
```

**Multi-Layer Feedforward Network — forward pass (layer l):**
```
z^(l) = W^(l)·a^(l−1) + b^(l)
a^(l) = g(z^(l))
```

**Common activation functions:**
```
Sigmoid:  g(z) = 1/(1+e^(−z))
Tanh:     g(z) = (e^z − e^(−z))/(e^z + e^(−z))
ReLU:     g(z) = max(0,z)
Softmax:  g(z)ᵢ = e^(zᵢ) / Σⱼe^(zⱼ)
```

**Loss functions:**
```
MSE (regression):      J = (1/2m)Σ(ŷᵢ−yᵢ)²
Cross-Entropy (class): J = −(1/m)Σ[yᵢln(ŷᵢ)+(1−yᵢ)ln(1−ŷᵢ)]
```

**Backpropagation (gradient descent through layers):**
```
δ^(L) = ∇_a J ⊙ g'(z^(L))          (output layer error)
δ^(l) = (W^(l+1))ᵀδ^(l+1) ⊙ g'(z^(l))   (hidden layer error)

∂J/∂W^(l) = δ^(l)·(a^(l−1))ᵀ
∂J/∂b^(l) = δ^(l)

W^(l) := W^(l) − α·∂J/∂W^(l)
b^(l) := b^(l) − α·∂J/∂b^(l)
```

**Performance Metrics:** Accuracy, Precision, Recall, F1, ROC-AUC (classification); MSE, RMSE, MAE, R² (regression).

---

## 10. Cross Validation Methods

**Hold-Out:**
```
Data → Train set + Test set (e.g., 70/30 or 80/20 split)
```

**K-Fold Cross Validation:**
```
Split data into k folds
For i = 1 to k:
    Train on (k−1) folds, test on fold i
CV Error = (1/k) Σᵢ Errorᵢ
```

**Leave-One-Out CV (LOOCV):** special case k = n
```
CV Error = (1/n) Σᵢ Error(xᵢ)
```

**Stratified K-Fold:** same as K-Fold, but class proportions preserved in each fold.

**Bias-Variance of CV:**
```
LOOCV → low bias, high variance
K-Fold (k=5 or 10) → balanced bias-variance
```

**Metric aggregation:**
```
Mean CV Score = (1/k) Σ scoreᵢ
Std CV Score = √[ (1/k)Σ(scoreᵢ − mean)² ]
```

---

## 11. K-Means & K-Medoids

**K-Means Objective (minimize within-cluster sum of squares — WCSS):**
```
J = Σₖ Σ_(xᵢ∈Cₖ) ‖xᵢ − μₖ‖²
```

**Centroid update:**
```
μₖ = (1/|Cₖ|) Σ_(xᵢ∈Cₖ) xᵢ
```

**Assignment step:**
```
Cₖ = { xᵢ : ‖xᵢ−μₖ‖² ≤ ‖xᵢ−μⱼ‖² ∀j }
```

**Algorithm (iterative, converges like gradient descent):**
```
1. Initialize k centroids randomly
2. Repeat until convergence:
   a. Assign each point to nearest centroid
   b. Recompute centroids as mean of assigned points
```

**K-Medoids Objective (uses actual data points as centers, minimizes absolute distance):**
```
J = Σₖ Σ_(xᵢ∈Cₖ) d(xᵢ, mₖ)
```
where mₖ = medoid (actual data point minimizing total dissimilarity within cluster)

**Metrics for clustering quality:**
```
Silhouette Score: s(i) = (b(i)−a(i)) / max(a(i),b(i))
   a(i) = avg distance to points in own cluster
   b(i) = avg distance to points in nearest other cluster

Inertia (WCSS) = Σₖ Σ_(xᵢ∈Cₖ) ‖xᵢ−μₖ‖²

Davies-Bouldin Index = (1/k)Σₖ max_(j≠k) [(σₖ+σⱼ)/d(μₖ,μⱼ)]
```

---

## 12. Hierarchical Clustering (Top-Down & Bottom-Up)

**Bottom-Up / Agglomerative (start with n clusters, merge iteratively):**
```
1. Each point = its own cluster
2. Repeat until one cluster remains:
   a. Merge two closest clusters based on linkage distance
   b. Update distance matrix
```

**Top-Down / Divisive (start with 1 cluster, split iteratively):**
```
1. All points = one cluster
2. Repeat until each point is its own cluster:
   a. Split cluster into two using a chosen criterion (e.g., max distance / k-means with k=2)
```

**Cluster distance (generic):**
```
d(Cᵢ,Cⱼ) = linkage function of pairwise point distances
```

**Dendrogram cut:** choose threshold distance to determine final number of clusters.

---

## 13. Linkage Methods (Single & Complete/Multiple Linkage)

**Single Linkage (minimum distance, nearest neighbor):**
```
d(Cᵢ,Cⱼ) = min_(x∈Cᵢ, y∈Cⱼ) d(x,y)
```

**Complete Linkage (maximum distance, farthest neighbor):**
```
d(Cᵢ,Cⱼ) = max_(x∈Cᵢ, y∈Cⱼ) d(x,y)
```

**Average Linkage:**
```
d(Cᵢ,Cⱼ) = (1/|Cᵢ||Cⱼ|) Σ_(x∈Cᵢ) Σ_(y∈Cⱼ) d(x,y)
```

**Centroid Linkage:**
```
d(Cᵢ,Cⱼ) = ‖μᵢ − μⱼ‖²
```

**Ward's Linkage (minimizes total within-cluster variance increase):**
```
d(Cᵢ,Cⱼ) = [ (|Cᵢ||Cⱼ|) / (|Cᵢ|+|Cⱼ|) ] · ‖μᵢ − μⱼ‖²
```

---

## 14. Dimensionality Reduction (General)

**Goal:** Project data X ∈ ℝ^(n×d) → Z ∈ ℝ^(n×k), k < d, minimizing information loss.

**Variance retained:**
```
Explained Variance Ratio = λᵢ / Σλⱼ
```

**Reconstruction Error:**
```
Error = ‖X − X̂‖²,   X̂ = reconstruction from reduced dimensions
```

**Common methods:** PCA (linear, variance-based), LDA (supervised, class-separation based), t-SNE / UMAP (nonlinear, manifold-based), Autoencoders (neural network based).

---

## 15. Principal Component Analysis (PCA)

**Step 1 — Standardize data:**
```
xᵢⱼ' = (xᵢⱼ − μⱼ) / σⱼ
```

**Step 2 — Covariance Matrix:**
```
Σ = (1/n) XᵀX   (X mean-centered)
```

**Step 3 — Eigen decomposition (find principal axes):**
```
Σv = λv
```
(λ = eigenvalue = variance explained by component; v = eigenvector = principal direction)

**Step 4 — Sort eigenvalues descending, select top k eigenvectors → projection matrix W:**
```
W = [v1, v2, ..., vk]
```

**Step 5 — Project data:**
```
Z = XW
```

**Angle/geometric interpretation:** principal components are orthogonal directions (angle = 90° between components) that maximize variance:
```
maximize: wᵀΣw   subject to  ‖w‖ = 1
```
(solved via Lagrangian → Σw = λw, same as eigen equation above)

**Total variance explained by k components:**
```
Explained Variance = ( Σᵢ₌₁ᵏ λᵢ ) / ( Σⱼ₌₁ᵈ λⱼ )
```

**Reconstruction:**
```
X̂ = ZWᵀ
Reconstruction Error = ‖X − X̂‖²
```

---

*End of reference document.*
