# Probability Distributions Cheatsheet

> **Notation guide:** PMF = Probability Mass Function · PDF = Probability Density Function · CDF = Cumulative Distribution Function · MGF = Moment Generating Function · Γ = Gamma function · B(α,β) = Beta function · Φ = Standard Normal CDF · C(n,k) = Binomial coefficient

---

## Part 1 — Discrete Distributions

A discrete distribution assigns probability to a **countable** set of values. P(X = k) is given by the **PMF**.

---

### 1. Bernoulli — `Ber(p)`

| Property | Formula |
|---|---|
| **Parameters** | p ∈ (0,1): probability of success |
| **Support** | k ∈ {0, 1} |
| **PMF** | P(X=k) = p^k · (1−p)^(1−k) |
| **E[X]** | p |
| **Var(X)** | p(1−p) |
| **MGF** | 1−p + p·e^t |
| **Skewness** | (1−2p) / √(p(1−p)) |
| **Kurtosis (excess)** | (1−6p(1−p)) / (p(1−p)) |

**Key properties:**
- The simplest binary outcome distribution (success/failure, 0/1)
- Building block: sum of n iid Bernoullis → Binomial(n, p)
- Maximum variance at p = 0.5

**Common uses:** Single coin flip, pass/fail a test, any one-off binary event

---

### 2. Binomial — `Bin(n, p)`

| Property | Formula |
|---|---|
| **Parameters** | n ∈ ℕ: number of trials; p ∈ (0,1): success probability |
| **Support** | k ∈ {0, 1, …, n} |
| **PMF** | P(X=k) = C(n,k) · p^k · (1−p)^(n−k) |
| **E[X]** | np |
| **Var(X)** | np(1−p) |
| **MGF** | (1−p + p·e^t)^n |
| **Skewness** | (1−2p) / √(np(1−p)) |
| **Kurtosis (excess)** | (1−6p(1−p)) / (np(1−p)) |

**Key properties:**
- Sum of n independent Ber(p) random variables
- Symmetric when p = 0.5
- By CLT → N(np, np(1−p)) for large n
- By Poisson limit: if n → ∞ and np → λ, then Bin(n,p) → Poi(λ)
- Bin(1, p) = Ber(p)

**Common uses:** Number of heads in n flips, defective items in a batch, A/B testing conversions, survey yes/no responses

---

### 3. Geometric — `Geo(p)`

| Property | Formula |
|---|---|
| **Parameters** | p ∈ (0,1): probability of success on each trial |
| **Support** | k ∈ {1, 2, 3, …} (number of trials until first success) |
| **PMF** | P(X=k) = (1−p)^(k−1) · p |
| **E[X]** | 1/p |
| **Var(X)** | (1−p) / p² |
| **MGF** | p·e^t / (1 − (1−p)·e^t),   t < −ln(1−p) |
| **Median** | ⌈ −1/log₂(1−p) ⌉ |

**Key properties:**
- **Memoryless**: P(X > m+n | X > m) = P(X > n)
- The **only discrete memoryless distribution**
- Geo(p) is a special case of NB(1, p)
- Skewness = (2−p)/√(1−p)

**Common uses:** Trials until first success, coin flips until first head, waiting for first defect, reliability analysis

---

### 4. Negative Binomial — `NB(r, p)`

| Property | Formula |
|---|---|
| **Parameters** | r ∈ ℕ: number of successes; p ∈ (0,1) |
| **Support** | k ∈ {r, r+1, r+2, …} (total trials to get r successes) |
| **PMF** | P(X=k) = C(k−1, r−1) · p^r · (1−p)^(k−r) |
| **E[X]** | r/p |
| **Var(X)** | r(1−p) / p² |
| **MGF** | (p·e^t / (1−(1−p)·e^t))^r |

**Key properties:**
- Generalizes Geometric: NB(1, p) = Geo(p)
- Sum of r independent Geo(p) random variables
- Var(X) > E[X] → **overdispersed** (useful for count data)
- Alternative parameterization by number of failures is also common

**Common uses:** Trials until r-th success, overdispersed count data, insurance claim modeling, RNA-seq read counts

---

### 5. Poisson — `Poi(λ)`

| Property | Formula |
|---|---|
| **Parameters** | λ > 0: average event rate (mean number of events) |
| **Support** | k ∈ {0, 1, 2, …} |
| **PMF** | P(X=k) = e^(−λ) · λ^k / k! |
| **E[X]** | λ |
| **Var(X)** | λ |
| **MGF** | exp(λ(e^t − 1)) |
| **Skewness** | 1/√λ |
| **Kurtosis (excess)** | 1/λ |

**Key properties:**
- **Equidispersed**: E[X] = Var(X) = λ — a key diagnostic
- Sum of independent Poissons is Poisson: Poi(λ₁) + Poi(λ₂) = Poi(λ₁+λ₂)
- Limit of Bin(n, p) as n → ∞, np → λ
- Approximates Normal for large λ
- Poisson process: events occur independently at constant rate λ

**Common uses:** Events per unit time/area, calls per hour, mutations per genome, accidents, typos, radioactive decay events

---

### 6. Hypergeometric — `HG(N, K, n)`

| Property | Formula |
|---|---|
| **Parameters** | N: population size; K: number of successes in population; n: number of draws |
| **Support** | k ∈ { max(0, n+K−N), …, min(n, K) } |
| **PMF** | P(X=k) = C(K,k)·C(N−K, n−k) / C(N, n) |
| **E[X]** | nK/N |
| **Var(X)** | n·(K/N)·(1−K/N)·(N−n)/(N−1) |
| **MGF** | No simple closed form |

**Key properties:**
- Models **sampling without replacement** from a finite population
- The factor (N−n)/(N−1) is the **finite population correction** — reduces variance vs Binomial
- As N → ∞ with K/N → p: HG → Bin(n, p)
- Var(X) < Var(Bin(n, K/N)) always — without-replacement sampling is less variable

**Common uses:** Drawing cards from a deck, quality control batch testing, ecological capture-recapture, Fisher's exact test

---

### 7. Discrete Uniform — `DU(a, b)`

| Property | Formula |
|---|---|
| **Parameters** | a, b ∈ ℤ with a ≤ b; n = b−a+1 values |
| **Support** | k ∈ {a, a+1, …, b} |
| **PMF** | P(X=k) = 1/n |
| **E[X]** | (a+b)/2 |
| **Var(X)** | (n²−1)/12 |
| **MGF** | e^(at)·(1−e^(nt)) / n(1−e^t) |
| **Skewness** | 0 |
| **Kurtosis (excess)** | −6(n²+1) / 5(n²−1) |

**Key properties:**
- **Maximum entropy** distribution on a finite set — the "most random" discrete distribution
- Perfectly symmetric; skewness = 0
- Basis for pseudo-random number generators and the inverse CDF method

**Common uses:** Rolling a fair die, random selection, lottery draws, cryptographic key generation, Monte Carlo simulation

---

### 8. Zipf (Zeta) — `Zipf(s)`

| Property | Formula |
|---|---|
| **Parameters** | s > 1: exponent; ζ(s) = Riemann zeta function |
| **Support** | k ∈ {1, 2, 3, …} |
| **PMF** | P(X=k) = 1 / (k^s · ζ(s)) |
| **E[X]** | ζ(s−1)/ζ(s),   if s > 2; else undefined |
| **Var(X)** | Finite only if s > 3 |
| **MGF** | No simple closed form |

**Key properties:**
- **Heavy-tailed power law**: probability decays as 1/k^s
- Empirically, s ≈ 1 in many real-world phenomena ("Zipf's Law")
- Mean and variance can be infinite depending on s
- Related to Pareto distribution in the continuous case

**Common uses:** Word frequency in language, city population rankings, website traffic, income/wealth distributions, file size distributions

---

## Part 2 — Continuous Distributions

A continuous distribution assigns probability over intervals. P(X = x) = 0 for any single point; probability is given by integrating the **PDF**.

---

### 1. Uniform — `U(a, b)`

| Property | Formula |
|---|---|
| **Parameters** | a < b ∈ ℝ |
| **Support** | x ∈ [a, b] |
| **PDF** | f(x) = 1/(b−a) |
| **CDF** | F(x) = (x−a)/(b−a) |
| **E[X]** | (a+b)/2 |
| **Var(X)** | (b−a)²/12 |
| **MGF** | (e^(tb) − e^(ta)) / t(b−a) |
| **Skewness** | 0 |
| **Kurtosis (excess)** | −6/5 |

**Key properties:**
- **Maximum entropy** on [a, b]
- Foundation for the **inverse CDF (probability integral transform)** method: if U ~ U(0,1), then F⁻¹(U) has CDF F
- Symmetric; all moments exist and are finite

**Common uses:** Random number generation, Monte Carlo simulation, rounding/quantization error, uninformative priors

---

### 2. Normal (Gaussian) — `N(μ, σ²)`

| Property | Formula |
|---|---|
| **Parameters** | μ ∈ ℝ: mean; σ² > 0: variance |
| **Support** | x ∈ (−∞, +∞) |
| **PDF** | f(x) = exp(−(x−μ)²/2σ²) / (σ√(2π)) |
| **CDF** | F(x) = Φ((x−μ)/σ) |
| **E[X]** | μ |
| **Var(X)** | σ² |
| **MGF** | exp(μt + σ²t²/2) |
| **Skewness** | 0 |
| **Kurtosis (excess)** | 0 |

**Key properties:**
- Bell-shaped, symmetric about μ; mean = median = mode
- **68–95–99.7 rule**: P(|X−μ| < kσ) ≈ 68%, 95%, 99.7% for k = 1,2,3
- **Central Limit Theorem**: sum of iid r.v.s → Normal (the universal attractor)
- **Stable distribution**: sum of Normals is Normal
- Completely characterised by its first two moments
- Standard Normal: Z ~ N(0,1); (X−μ)/σ = Z

**Common uses:** Heights, weights, test scores, measurement errors, financial returns (approximate), CLT approximations throughout statistics

---

### 3. Exponential — `Exp(λ)`

| Property | Formula |
|---|---|
| **Parameters** | λ > 0: rate parameter (mean = 1/λ) |
| **Support** | x ∈ [0, +∞) |
| **PDF** | f(x) = λ·e^(−λx) |
| **CDF** | F(x) = 1 − e^(−λx) |
| **E[X]** | 1/λ |
| **Var(X)** | 1/λ² |
| **MGF** | λ/(λ−t),   t < λ |
| **Skewness** | 2 |
| **Kurtosis (excess)** | 6 |
| **Hazard rate** | λ (constant) |

**Key properties:**
- **Memoryless**: P(X > s+t | X > s) = P(X > t)
- The **only continuous memoryless distribution**
- Special case of Gamma: Exp(λ) = Γ(1, λ)
- Inter-arrival time of a Poisson(λ) process

**Common uses:** Time between Poisson events, component lifetimes, queueing service times, radioactive decay, survival analysis

---

### 4. Gamma — `Γ(α, β)`

| Property | Formula |
|---|---|
| **Parameters** | α > 0: shape; β > 0: rate (scale θ = 1/β also used) |
| **Support** | x ∈ (0, +∞) |
| **PDF** | f(x) = β^α · x^(α−1) · e^(−βx) / Γ(α) |
| **CDF** | γ(α, βx) / Γ(α)  (lower incomplete gamma) |
| **E[X]** | α/β |
| **Var(X)** | α/β² |
| **MGF** | (β/(β−t))^α,   t < β |
| **Skewness** | 2/√α |
| **Kurtosis (excess)** | 6/α |

**Key properties:**
- Sum of α independent Exp(β) random variables
- Exp(λ) = Γ(1, λ); Chi-squared: χ²(k) = Γ(k/2, 1/2)
- **Conjugate prior** for Poisson rate λ (Bayesian inference)
- Right-skewed; approaches Normal as α → ∞
- Erlang distribution: Γ(k, λ) with k ∈ ℕ

**Common uses:** Waiting time for α-th Poisson event, rainfall/claim amounts, Bayesian priors, survival/reliability analysis, queueing theory

---

### 5. Beta — `Beta(α, β)`

| Property | Formula |
|---|---|
| **Parameters** | α, β > 0: shape parameters |
| **Support** | x ∈ [0, 1] |
| **PDF** | f(x) = x^(α−1)·(1−x)^(β−1) / B(α,β) |
| **CDF** | I_x(α, β)  (regularized incomplete beta function) |
| **E[X]** | α/(α+β) |
| **Var(X)** | αβ / ((α+β)²(α+β+1)) |
| **MGF** | No simple closed form (series via hypergeometric function) |
| **Mode** | (α−1)/(α+β−2),   α,β > 1 |
| **Skewness** | 2(β−α)√(α+β+1) / ((α+β+2)√(αβ)) |

**Key properties:**
- Lives on [0,1] — natural for probabilities and proportions
- **Conjugate prior** for the Binomial parameter p
- Highly flexible shape: uniform (α=β=1), J-shaped, U-shaped, bell-shaped
- U(0,1) = Beta(1,1)
- k-th order statistic of n U(0,1) r.v.s ~ Beta(k, n−k+1)

**Common uses:** Bayesian inference for proportions, A/B testing, project time estimation (PERT), modeling rates and percentages

---

### 6. Chi-Squared — `χ²(k)`

| Property | Formula |
|---|---|
| **Parameters** | k ∈ ℕ: degrees of freedom |
| **Support** | x ∈ [0, +∞) |
| **PDF** | f(x) = x^(k/2−1)·e^(−x/2) / (2^(k/2)·Γ(k/2)) |
| **CDF** | γ(k/2, x/2) / Γ(k/2) |
| **E[X]** | k |
| **Var(X)** | 2k |
| **MGF** | (1−2t)^(−k/2),   t < 1/2 |
| **Skewness** | √(8/k) |
| **Kurtosis (excess)** | 12/k |

**Key properties:**
- If Z₁, …, Zₖ ~ N(0,1) iid, then Z₁²+…+Zₖ² ~ χ²(k)
- Special case of Gamma: χ²(k) = Γ(k/2, 1/2)
- χ²(1) = Z² where Z ~ N(0,1)
- Sum: χ²(k₁) + χ²(k₂) = χ²(k₁+k₂)
- Approaches N(k, 2k) for large k

**Common uses:** Goodness-of-fit tests, tests of independence (contingency tables), distribution of sample variance S², confidence intervals for σ²

---

### 7. Student's t — `t(ν)`

| Property | Formula |
|---|---|
| **Parameters** | ν > 0: degrees of freedom |
| **Support** | x ∈ (−∞, +∞) |
| **PDF** | Γ((ν+1)/2) · (1+x²/ν)^(−(ν+1)/2) / (√(νπ)·Γ(ν/2)) |
| **CDF** | Via regularized incomplete beta function |
| **E[X]** | 0,   ν > 1; else undefined |
| **Var(X)** | ν/(ν−2),   ν > 2; else undefined |
| **MGF** | Does not exist |
| **Kurtosis (excess)** | 6/(ν−4),   ν > 4 |

**Key properties:**
- **Heavier tails** than Normal; robust to outliers
- t(ν) → N(0,1) as ν → ∞
- t(1) = Cauchy distribution (no mean or variance)
- t²(ν) = F(1, ν)
- Used when σ² is unknown and estimated from data

**Common uses:** One- and two-sample t-tests, confidence intervals for μ with unknown σ, regression coefficient significance tests, robust/heavy-tailed modeling

---

### 8. F-Distribution — `F(d₁, d₂)`

| Property | Formula |
|---|---|
| **Parameters** | d₁, d₂ > 0: numerator and denominator degrees of freedom |
| **Support** | x ∈ [0, +∞) |
| **PDF** | √( (d₁x)^d₁ · d₂^d₂ / (d₁x+d₂)^(d₁+d₂) ) / (x · B(d₁/2, d₂/2)) |
| **CDF** | Regularized incomplete beta function |
| **E[X]** | d₂/(d₂−2),   d₂ > 2 |
| **Var(X)** | 2d₂²(d₁+d₂−2) / (d₁(d₂−2)²(d₂−4)),   d₂ > 4 |
| **MGF** | Does not exist |
| **Skewness** | (2d₁+d₂−2)·√(8(d₂−4)) / ((d₂−6)·√(d₁(d₁+d₂−2))),   d₂ > 6 |

**Key properties:**
- Ratio of two independent chi-squareds divided by their df: F = (χ²(d₁)/d₁) / (χ²(d₂)/d₂)
- 1/F(d₁,d₂) = F(d₂,d₁)   (reciprocal relationship)
- t²(ν) = F(1, ν)
- Right-skewed; approaches Normal for large d₁, d₂

**Common uses:** ANOVA (comparing group means via variance ratio), regression overall F-test, comparing two sample variances, model selection

---

### 9. Weibull — `W(k, λ)`

| Property | Formula |
|---|---|
| **Parameters** | k > 0: shape; λ > 0: scale |
| **Support** | x ∈ [0, +∞) |
| **PDF** | (k/λ)·(x/λ)^(k−1)·exp(−(x/λ)^k) |
| **CDF** | 1 − exp(−(x/λ)^k) |
| **E[X]** | λ · Γ(1 + 1/k) |
| **Var(X)** | λ² · [ Γ(1+2/k) − (Γ(1+1/k))² ] |
| **MGF** | No simple closed form (series exists) |
| **Hazard rate** | h(x) = (k/λ)·(x/λ)^(k−1) |

**Key properties:**
- Flexible hazard rate: **decreasing** (k<1, infant mortality), **constant** (k=1, random failures), **increasing** (k>1, wear-out)
- k=1: Weibull = Exp(1/λ)
- k=2: Rayleigh distribution
- k≈3.5: approximates Normal
- Most widely used distribution in reliability engineering

**Common uses:** Component lifetime/failure analysis, wind speed modeling, extreme value theory, material fatigue, survival analysis

---

### 10. Log-Normal — `LogN(μ, σ²)`

| Property | Formula |
|---|---|
| **Parameters** | μ ∈ ℝ, σ² > 0 (parameters of the underlying Normal, on log scale) |
| **Support** | x ∈ (0, +∞) |
| **PDF** | exp(−(ln x−μ)²/2σ²) / (xσ√(2π)) |
| **CDF** | Φ((ln x − μ)/σ) |
| **E[X]** | exp(μ + σ²/2) |
| **Var(X)** | (e^σ² − 1)·exp(2μ+σ²) |
| **MGF** | Does not exist (characteristic function used) |
| **Median** | e^μ |
| **Mode** | e^(μ−σ²) |

**Key properties:**
- If X ~ LogN(μ, σ²), then ln(X) ~ N(μ, σ²)
- **Right-skewed**, non-negative: mean > median > mode
- Multiplicative CLT: product of many positive iid r.v.s → Log-Normal (as additive CLT → Normal)
- Skewness = (e^σ² + 2)·√(e^σ² − 1)

**Common uses:** Stock prices and asset returns, biological measurements (cell sizes, survival times), latency / response times, income and city size distributions, concentrations of pollutants

---

### 11. Cauchy — `Cauchy(x₀, γ)`

| Property | Formula |
|---|---|
| **Parameters** | x₀ ∈ ℝ: location; γ > 0: scale |
| **Support** | x ∈ (−∞, +∞) |
| **PDF** | 1 / (πγ[1 + ((x−x₀)/γ)²]) |
| **CDF** | 1/2 + arctan((x−x₀)/γ)/π |
| **E[X]** | **Undefined** (integral diverges) |
| **Var(X)** | **Undefined** |
| **MGF** | **Does not exist** |
| **Median** | x₀ |
| **Mode** | x₀ |

**Key properties:**
- Ratio of two independent N(0,1) r.v.s: Z₁/Z₂ ~ Cauchy(0,1)
- Student's t with ν=1: t(1) = Cauchy(0,1)
- **Stable distribution**: sum of Cauchys is Cauchy (but LLN and CLT fail!)
- No moments of order ≥ 1 exist — the canonical "pathological" example
- Sample mean of Cauchy r.v.s is also Cauchy (doesn't converge)

**Common uses:** Physics (resonance/Breit-Wigner line shapes), ratio distributions in signal processing, stress-testing statistical estimators, theoretical counterexample in probability

---

## Part 3 — Key Relationships & Insights

### Family Tree: How Distributions Relate

```
Bernoulli(p)
    │
    ├─── [sum of n] ──────────────────────── Binomial(n, p)
    │                                              │
    │                                    [n→∞, np→λ] ──── Poisson(λ)
    │                                              │
    │                                    [n→∞, CLT] ──── Normal(np, np(1-p))
    │
    └─── [trials until 1st success] ────── Geometric(p)
              │
              └─── [sum of r] ────────── Negative Binomial(r, p)

Normal(0,1)
    │
    ├─── [Z²] ──────────────────────────── Chi-Squared(1)
    │         [sum of k Z²'s] ──────────── Chi-Squared(k) = Gamma(k/2, 1/2)
    │
    ├─── [Z₁/√(χ²(ν)/ν)] ──────────────── Student's t(ν)
    │         t(ν)² ─────────────────────── F(1, ν)
    │         t(1)  ─────────────────────── Cauchy(0, 1)
    │         t → N(0,1) as ν → ∞
    │
    └─── [exp(μ + σZ)] ─────────────────── Log-Normal(μ, σ²)

Gamma(α, β)
    │
    ├─── α=1 ─────────────────────────── Exponential(β)   [memoryless]
    ├─── α=k/2, β=1/2 ───────────────── Chi-Squared(k)
    ├─── α∈ℕ ────────────────────────── Erlang(α, β)
    └─── [sum of α Exp(β)] ───────────── Gamma(α, β)

F(d₁, d₂) = [χ²(d₁)/d₁] / [χ²(d₂)/d₂]
           = 1 / F(d₂, d₁)   [reciprocal symmetry]

HyperGeometric(N, K, n) → Binomial(n, K/N)   as N → ∞
Binomial(n, p)           → Poisson(λ)          as n→∞, np→λ
Poisson(λ)               → Normal(λ, λ)        as λ → ∞
Weibull(1, λ)            = Exponential(1/λ)
Beta(1, 1)               = Uniform(0, 1)
```

---

### The Memoryless Property

Only **two** distributions are memoryless:

| Type | Distribution | Property |
|---|---|---|
| Discrete | Geometric(p) | P(X > m+n \| X > m) = P(X > n) |
| Continuous | Exponential(λ) | P(X > s+t \| X > s) = P(X > t) |

Interpretation: "Having waited this long tells you nothing about how much longer you'll wait." This makes them the natural models for failure times without aging.

---

### Conjugate Prior Pairs (Bayesian Inference)

A conjugate prior means the posterior is in the same family as the prior — closed-form updating.

| Likelihood | Conjugate Prior | Posterior |
|---|---|---|
| Binomial(n, p) | Beta(α, β) | Beta(α + successes, β + failures) |
| Poisson(λ) | Gamma(α, β) | Gamma(α + Σxᵢ, β + n) |
| Normal(μ, σ²) — unknown μ | Normal(μ₀, τ²) | Normal (updated mean) |
| Normal(μ, σ²) — unknown σ² | Inverse-Gamma | Inverse-Gamma |
| Geometric(p) | Beta(α, β) | Beta(α + n, β + Σxᵢ − n) |

---

### Distributions with Undefined Moments

| Distribution | Mean | Variance | When |
|---|---|---|---|
| Cauchy | Undefined | Undefined | Always |
| Student's t(ν) | Undefined | Undefined | ν ≤ 1 (mean), ν ≤ 2 (var) |
| Pareto / Zipf | Undefined | Undefined | Depends on exponent s |
| Log-Normal | Exists | Exists | Always (but MGF doesn't) |
| F(d₁, d₂) | Undefined | Undefined | d₂ ≤ 2 (mean), d₂ ≤ 4 (var) |

**Key insight:** Heavy-tailed distributions (power-law tails) are the usual culprits. The Law of Large Numbers and CLT may fail for these.

---

### Maximum Entropy Distributions

Given a constraint, the maximum entropy distribution is the "most uncertain" / "least informative" one consistent with that constraint.

| Constraint | Max Entropy Distribution |
|---|---|
| Finite support {a, …, b} | Discrete Uniform |
| Continuous support [a, b] | Uniform(a, b) |
| Mean μ fixed, support [0, ∞) | Exponential(1/μ) |
| Mean μ and variance σ² fixed, support ℝ | Normal(μ, σ²) |
| Mean μ fixed, support ℕ | Geometric |

**Key insight:** Normal and Exponential are not just convenient — they are the most "spread out" distributions consistent with their constraints. This is why they appear so often in nature.

---

### Hazard Rate (Failure Rate) Comparison

The hazard rate h(x) = f(x)/(1−F(x)) describes the instantaneous failure risk given survival to time x.

| Distribution | Hazard Rate | Shape | Interpretation |
|---|---|---|---|
| Exponential | λ (constant) | Flat | Random/memoryless failures |
| Weibull (k < 1) | Decreasing | ↓ | Infant mortality |
| Weibull (k = 1) | Constant | Flat | = Exponential |
| Weibull (k > 1) | Increasing | ↑ | Wear-out / aging |
| Normal | Increasing | ↑ | Wear-out |
| Log-Normal | Non-monotone | ↑ then ↓ | Complex failure modes |

---

### Limiting / Approximation Results

| Exact Distribution | Approximation | Condition |
|---|---|---|
| Binomial(n, p) | Poisson(np) | n large, p small, np moderate |
| Binomial(n, p) | Normal(np, np(1−p)) | n large (CLT) |
| Poisson(λ) | Normal(λ, λ) | λ large |
| HyperGeometric(N, K, n) | Binomial(n, K/N) | N much larger than n |
| Student's t(ν) | Normal(0, 1) | ν large (> ~30) |
| Chi-Squared(k) | Normal(k, 2k) | k large |
| Gamma(α, β) | Normal(α/β, α/β²) | α large |

---

### Variance vs Mean: Dispersion Patterns

| Distribution | Relationship | Name |
|---|---|---|
| Poisson(λ) | Var = Mean = λ | Equidispersed |
| Binomial(n, p) | Var = Mean·(1−p) < Mean | Underdispersed |
| Negative Binomial | Var > Mean | Overdispersed |
| Normal | Independent (set freely) | — |

**Practical use:** If count data has Var >> Mean, Poisson is a poor fit → use Negative Binomial. If Var << Mean, look for truncation or clustering effects.

---

### Quick "Which Distribution?" Decision Guide

**Is the outcome discrete or continuous?**

**Discrete:**
- Binary outcome (0 or 1)? → **Bernoulli**
- Count of successes in n trials? → **Binomial**
- Trials until first success? → **Geometric**
- Trials until r-th success? → **Negative Binomial**
- Count of rare events per unit? → **Poisson**
- Sampling without replacement? → **Hypergeometric**
- All outcomes equally likely? → **Discrete Uniform**
- Count data with power-law rank? → **Zipf**

**Continuous:**
- All values in [a,b] equally likely? → **Uniform**
- Symmetric, bell-shaped, CLT context? → **Normal**
- Time until next event (memoryless)? → **Exponential**
- Sum of waiting times, right-skewed? → **Gamma**
- Proportion or probability value in [0,1]? → **Beta**
- Non-negative, right-skewed, multiplicative? → **Log-Normal**
- Failure/reliability with varying hazard? → **Weibull**
- Small-sample inference, unknown σ? → **Student's t**
- Ratio of variances, ANOVA? → **F-distribution**
- Pathological/heavy-tailed stress test? → **Cauchy**

---

*End of cheatsheet. All formulas use standard parameterizations; alternative parameterizations exist (e.g., Gamma by scale θ=1/β, Exponential by mean μ=1/λ).*
