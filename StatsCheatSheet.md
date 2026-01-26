# Descriptive Statistics Cheat Sheet (Sample vs Population)

## Measures of Central Tendency

| Concept | Population Notation | Sample Notation | Description |
|--------|--------------------|-----------------|-------------|
| Mean   | μ                  | x̄               | Average value |
| Median | —                  | —               | Middle value |
| Mode   | —                  | —               | Most frequent value |

---

## Measures of Variability (Spread)

| Concept              | Population | Sample | Description |
|----------------------|------------|--------|-------------|
| Variance             | σ²         | s²     | Average squared deviation from mean |
| Standard Deviation  | σ          | s      | Square root of variance |
| Range                | max − min  | max − min | Difference between largest and smallest |
| Interquartile Range | Q3 − Q1     | Q3 − Q1 | Spread of middle 50% |

---

## Formulas

### Mean
- Population:  
  μ = (Σ Xi) / N  

- Sample:  
  x̄ = (Σ xi) / n  

---

### Variance
- Population:  
  σ² = Σ (Xi − μ)² / N  

- Sample (unbiased estimator):  
  s² = Σ (xi − x̄)² / (n − 1)  

---

### Standard Deviation
- Population:  
  σ = √σ²  

- Sample:  
  s = √s²  

---

## Notation Summary

| Symbol | Meaning |
|--------|---------|
| N      | Population size |
| n      | Sample size |
| Xi     | Population data value |
| xi     | Sample data value |
| μ      | Population mean |
| x̄      | Sample mean |
| σ      | Population standard deviation |
| s      | Sample standard deviation |


# Random Variables Cheat Sheet

## Types of Random Variables

### Discrete Random Variable
- Takes countable values (0, 1, 2, …)
- Examples: number of heads, dice roll
- Uses: Probability Mass Function (PMF)

### Continuous Random Variable
- Takes any value in an interval
- Examples: height, time, weight
- Uses: Probability Density Function (PDF)

---

## Expected Value (Mean)

### Discrete:
E(X) = Σ x · P(X = x)

### Continuous:
E(X) = ∫ x f(x) dx

Interpretation: long-run average value

---

## Variance and Standard Deviation

### Variance:
Var(X) = E[(X − μ)²]  
or  
Var(X) = E(X²) − [E(X)]²  

### Standard Deviation:
SD(X) = √Var(X)

---

## Common Notation

| Symbol | Meaning |
|--------|---------|
| X      | Random variable |
| x      | A specific value of X |
| P(X=x) | Probability X equals x |
| f(x)   | PDF (continuous case) |
| μ or E(X) | Mean / expected value |
| σ²     | Variance |
| σ      | Standard deviation |

---

## Laws of Expectation

- Linearity:  
  E(aX + b) = aE(X) + b  

- For sums:  
  E(X + Y) = E(X) + E(Y)

---

## Distributions (Examples)

| Distribution | Mean | Variance |
|--------------|------|----------|
| Bernoulli(p) | p | p(1−p) |
| Binomial(n,p) | np | np(1−p) |
| Poisson(λ) | λ | λ |
| Uniform(a,b) | (a+b)/2 | (b−a)² / 12 |
| Normal(μ,σ²) | μ | σ² |


# Confidence Intervals & Hypothesis Testing Cheat Sheet

## Key Ideas

- Parameter: true (unknown) population value (μ, p, σ²)
- Statistic: sample estimate (x̄, p̂, s²)
- Confidence Interval (CI): range of plausible values for a parameter
- Hypothesis Test: procedure to test a claim about a parameter using sample data

---

## Confidence Intervals (General Form)

Estimate ± (Critical Value) × (Standard Error)

---

## Common Confidence Intervals

### 1. Mean (σ known, Normal or large n → Z interval)

CI:  
x̄ ± z* (σ / √n)

---

### 2. Mean (σ unknown → t interval)

CI:  
x̄ ± t* (s / √n)

- df = n − 1  
- Use t-distribution

---

### 3. Population Proportion

CI:  
p̂ ± z* √[ p̂(1 − p̂) / n ]

Conditions:
- np̂ ≥ 10 and n(1 − p̂) ≥ 10

---

### 4. Difference of Means (Independent samples)

CI:  
(x̄₁ − x̄₂) ± t* √( s₁²/n₁ + s₂²/n₂ )

---

### 5. Difference of Proportions

CI:  
(p̂₁ − p̂₂) ± z* √( p̂₁(1−p̂₁)/n₁ + p̂₂(1−p̂₂)/n₂ )

---

## Common Critical Values

| Confidence Level | z* |
|------------------|----|
| 90%              | 1.645 |
| 95%              | 1.96 |
| 99%              | 2.576 |

---

## Hypothesis Testing Framework

### Step 1: State Hypotheses
- Null hypothesis: H₀ (status quo, equality)
- Alternative hypothesis: Hₐ (what you want to show)

Examples:
- H₀: μ = μ₀  
- Hₐ: μ ≠ μ₀ (two-sided)  
- Hₐ: μ > μ₀ (right-tailed)  
- Hₐ: μ < μ₀ (left-tailed)

---

### Step 2: Choose Significance Level

- α = 0.10, 0.05, or 0.01 (common)
- Probability of Type I error (rejecting true H₀)

---

### Step 3: Test Statistic

#### Mean (σ known → Z test):
z = (x̄ − μ₀) / (σ / √n)

#### Mean (σ unknown → t test):
t = (x̄ − μ₀) / (s / √n)  
df = n − 1

#### Proportion:
z = (p̂ − p₀) / √[ p₀(1 − p₀) / n ]

---

### Step 4: P-value or Critical Value

- P-value = probability (under H₀) of observing a result as extreme as the sample
- Decision rules:
  - If p-value ≤ α → Reject H₀  
  - If p-value > α → Fail to reject H₀  

---

### Step 5: Conclusion (in context)

State whether there is sufficient evidence to support Hₐ.

---

## Errors & Power

### Type I Error
- Reject H₀ when H₀ is true  
- Probability = α  

### Type II Error
- Fail to reject H₀ when H₀ is false  
- Probability = β  

### Power
- Power = 1 − β  
- Probability of correctly rejecting false H₀  

---

## One-Sample Tests Summary

| Parameter | Test | Statistic |
|----------|------|-----------|
| Mean (σ known) | Z-test | z |
| Mean (σ unknown) | t-test | t |
| Proportion | Z-test | z |

---

## Connection Between CI and Tests

- A two-sided test at level α ↔ CI with confidence (1 − α)
- If μ₀ is inside the CI → Fail to reject H₀  
- If μ₀ is outside the CI → Reject H₀  

---

## Assumptions Checklist

- Random sample or random assignment  
- Independence  
- Normal population OR large sample (CLT)  
- For proportions: success–failure condition met  

# Inferential Statistics Cheat Sheet

## What is Inferential Statistics?

Inferential statistics uses **sample data** to make conclusions or predictions about a **population**.

Main goals:
- Estimate population parameters
- Test hypotheses about populations
- Quantify uncertainty

---

## Key Terms & Notation

| Term | Meaning |
|------|--------|
| Parameter | True population value (μ, p, σ²) |
| Statistic | Sample estimate (x̄, p̂, s²) |
| Sampling distribution | Distribution of a statistic over many samples |
| Standard error (SE) | SD of a sampling distribution |
| Bias | Systematic error in estimation |
| Consistent estimator | Converges to true parameter as n → ∞ |

---

## Sampling Distributions

### Sample Mean
- Mean: E(x̄) = μ  
- Variance: Var(x̄) = σ² / n  
- SD (SE): σ / √n  

### Sample Proportion
- Mean: E(p̂) = p  
- SD (SE): √[ p(1 − p) / n ]

### Central Limit Theorem (CLT)
For large n, the sampling distribution of x̄ is approximately **Normal**:
x̄ ~ N(μ, σ² / n)

Conditions:
- Random sample  
- Independent observations  
- Large n (≈ 30+) or normal population  

---

## Point Estimation

| Parameter | Estimator |
|-----------|-----------|
| μ | x̄ |
| p | p̂ |
| σ² | s² |

Properties of good estimators:
- Unbiased
- Low variance
- Consistent

---

## Confidence Intervals (General)

Estimate ± (Critical Value) × (Standard Error)

---

## Common Confidence Intervals

### Mean (σ known → Z interval)
x̄ ± z* (σ / √n)

---

### Mean (σ unknown → t interval)
x̄ ± t* (s / √n)  
df = n − 1

---

### Proportion
p̂ ± z* √[ p̂(1 − p̂) / n ]

Conditions:
- np̂ ≥ 10 and n(1 − p̂) ≥ 10

---

### Difference of Means (Independent samples)
(x̄₁ − x̄₂) ± t* √( s₁²/n₁ + s₂²/n₂ )

---

### Difference of Proportions
(p̂₁ − p̂₂) ± z* √( p̂₁(1−p̂₁)/n₁ + p̂₂(1−p̂₂)/n₂ )

---

## Hypothesis Testing Framework

### Step 1: Hypotheses
- H₀: parameter = hypothesized value  
- Hₐ: parameter ≠, >, or < hypothesized value  

---

### Step 2: Significance Level
- α = P(Type I Error)  
- Common: 0.10, 0.05, 0.01  

---

### Step 3: Test Statistics

#### Mean (σ known):
z = (x̄ − μ₀) / (σ / √n)

#### Mean (σ unknown):
t = (x̄ − μ₀) / (s / √n)  
df = n − 1  

#### Proportion:
z = (p̂ − p₀) / √[ p₀(1 − p₀) / n ]

---

### Step 4: Decision Rule
- If p-value ≤ α → Reject H₀  
- If p-value > α → Fail to reject H₀  

---

### Step 5: Conclusion
State result **in context** of the problem.

---

## Errors & Power

### Type I Error
Reject true H₀  
Probability = α  

### Type II Error
Fail to reject false H₀  
Probability = β  

### Power
Power = 1 − β  
Probability of correctly rejecting false H₀  

---

## Common Tests Summary

| Parameter | Test | Distribution |
|----------|------|--------------|
| Mean (σ known) | Z-test | Normal |
| Mean (σ unknown) | t-test | t |
| Proportion | Z-test | Normal |
| Two means | Two-sample t | t |
| Two proportions | Two-proportion z | Normal |
| Variance | Chi-square | χ² |

---

## Connection: CI ↔ Hypothesis Tests

Two-sided test at level α ↔ (1 − α) CI  

- If hypothesized value is **inside CI** → Fail to reject H₀  
- If hypothesized value is **outside CI** → Reject H₀  

---

## Assumptions Checklist

- Random sampling or random assignment  
- Independence  
- Normal population or large n (CLT)  
- For proportions: success–failure condition  

---

## Common Critical Values (Z)

| Confidence | z* |
|------------|----|
| 90% | 1.645 |
| 95% | 1.96 |
| 99% | 2.576 |
