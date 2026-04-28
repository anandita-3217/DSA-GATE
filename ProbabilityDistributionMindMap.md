# Probability Distributions Cheatsheet

---

## Discrete Distributions

<table>
<thead>
<tr style="background-color:#1e2740">
<th style="color:#a5b4fc;padding:8px 10px;white-space:nowrap">Distribution</th>
<th style="color:#a5b4fc;padding:8px 10px;white-space:nowrap">Notation</th>
<th style="color:#a5b4fc;padding:8px 10px;white-space:nowrap">Support</th>
<th style="color:#a5b4fc;padding:8px 10px;white-space:nowrap">PMF — P(X = k)</th>
<th style="color:#a5b4fc;padding:8px 10px;white-space:nowrap">E[X]</th>
<th style="color:#a5b4fc;padding:8px 10px;white-space:nowrap">Var(X)</th>
<th style="color:#a5b4fc;padding:8px 10px;white-space:nowrap">MGF M(t)</th>
<th style="color:#a5b4fc;padding:8px 10px;white-space:nowrap">Skewness</th>
<th style="color:#a5b4fc;padding:8px 10px;white-space:nowrap">Key Property</th>
<th style="color:#a5b4fc;padding:8px 10px;white-space:nowrap">Common Uses</th>
</tr>
</thead>
<tbody>
<tr style="background-color:#1e1a3a">
<td style="border-left:4px solid #7c6fe0;padding:8px 10px;font-weight:bold;color:#a78bfa;white-space:nowrap"><strong>Bernoulli</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>Ber(p)</code><br><small>p ∈ (0,1)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">{0, 1}</td>
<td style="padding:8px 10px;color:#e2e8f0">p<sup>k</sup> (1−p)<sup>1−k</sup></td>
<td style="padding:8px 10px;color:#e2e8f0">p</td>
<td style="padding:8px 10px;color:#e2e8f0">p(1−p)</td>
<td style="padding:8px 10px;color:#e2e8f0">1−p + pe<sup>t</sup></td>
<td style="padding:8px 10px;color:#e2e8f0">(1−2p)/√(p(1−p))</td>
<td style="padding:8px 10px;color:#e2e8f0">Simplest binary outcome; building block of Binomial</td>
<td style="padding:8px 10px;color:#e2e8f0">Coin flip, pass/fail, any single binary event</td>
</tr>
<tr style="background-color:#0f2a1f">
<td style="border-left:4px solid #10b981;padding:8px 10px;font-weight:bold;color:#34d399;white-space:nowrap"><strong>Binomial</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>Bin(n, p)</code><br><small>n ∈ ℕ, p ∈ (0,1)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">{0, 1, …, n}</td>
<td style="padding:8px 10px;color:#e2e8f0">C(n,k) p<sup>k</sup> (1−p)<sup>n−k</sup></td>
<td style="padding:8px 10px;color:#e2e8f0">np</td>
<td style="padding:8px 10px;color:#e2e8f0">np(1−p)</td>
<td style="padding:8px 10px;color:#e2e8f0">(1−p+pe<sup>t</sup>)<sup>n</sup></td>
<td style="padding:8px 10px;color:#e2e8f0">(1−2p)/√(np(1−p))</td>
<td style="padding:8px 10px;color:#e2e8f0">Sum of n iid Ber(p); → Poi(λ) as n→∞, np→λ; → Normal by CLT</td>
<td style="padding:8px 10px;color:#e2e8f0">Defective items, A/B testing, survey responses</td>
</tr>
<tr style="background-color:#2a1500">
<td style="border-left:4px solid #f97316;padding:8px 10px;font-weight:bold;color:#fb923c;white-space:nowrap"><strong>Geometric</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>Geo(p)</code><br><small>p ∈ (0,1)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">{1, 2, 3, …}</td>
<td style="padding:8px 10px;color:#e2e8f0">(1−p)<sup>k−1</sup> p</td>
<td style="padding:8px 10px;color:#e2e8f0">1/p</td>
<td style="padding:8px 10px;color:#e2e8f0">(1−p)/p²</td>
<td style="padding:8px 10px;color:#e2e8f0">pe<sup>t</sup>/(1−(1−p)e<sup>t</sup>)</td>
<td style="padding:8px 10px;color:#e2e8f0">(2−p)/√(1−p)</td>
<td style="padding:8px 10px;color:#e2e8f0">Only discrete memoryless distribution; NB(1,p)</td>
<td style="padding:8px 10px;color:#e2e8f0">Trials until first success, first defect</td>
</tr>
<tr style="background-color:#2a0f1e">
<td style="border-left:4px solid #ec4899;padding:8px 10px;font-weight:bold;color:#f472b6;white-space:nowrap"><strong>Neg. Binomial</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>NB(r, p)</code><br><small>r ∈ ℕ, p ∈ (0,1)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">{r, r+1, …}</td>
<td style="padding:8px 10px;color:#e2e8f0">C(k−1,r−1) p<sup>r</sup> (1−p)<sup>k−r</sup></td>
<td style="padding:8px 10px;color:#e2e8f0">r/p</td>
<td style="padding:8px 10px;color:#e2e8f0">r(1−p)/p²</td>
<td style="padding:8px 10px;color:#e2e8f0">(pe<sup>t</sup>/(1−(1−p)e<sup>t</sup>))<sup>r</sup></td>
<td style="padding:8px 10px;color:#e2e8f0">(2−p)/√(r(1−p))</td>
<td style="padding:8px 10px;color:#e2e8f0">Generalises Geo (r=1); overdispersed (Var &gt; E)</td>
<td style="padding:8px 10px;color:#e2e8f0">Overdispersed count data, RNA-seq, insurance</td>
</tr>
<tr style="background-color:#0a1f35">
<td style="border-left:4px solid #3b82f6;padding:8px 10px;font-weight:bold;color:#60a5fa;white-space:nowrap"><strong>Poisson</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>Poi(λ)</code><br><small>λ &gt; 0</small></td>
<td style="padding:8px 10px;color:#e2e8f0">{0, 1, 2, …}</td>
<td style="padding:8px 10px;color:#e2e8f0">e<sup>−λ</sup> λ<sup>k</sup> / k!</td>
<td style="padding:8px 10px;color:#e2e8f0">λ</td>
<td style="padding:8px 10px;color:#e2e8f0">λ</td>
<td style="padding:8px 10px;color:#e2e8f0">exp(λ(e<sup>t</sup>−1))</td>
<td style="padding:8px 10px;color:#e2e8f0">1/√λ</td>
<td style="padding:8px 10px;color:#e2e8f0">E[X]=Var(X)=λ (equidispersed); sums are Poisson</td>
<td style="padding:8px 10px;color:#e2e8f0">Events per unit time, calls/hour, mutations</td>
</tr>
<tr style="background-color:#1f1a00">
<td style="border-left:4px solid #eab308;padding:8px 10px;font-weight:bold;color:#facc15;white-space:nowrap"><strong>Hypergeometric</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>HG(N,K,n)</code><br><small>N: pop; K: successes; n: draws</small></td>
<td style="padding:8px 10px;color:#e2e8f0">{max(0,n+K−N),…,min(n,K)}</td>
<td style="padding:8px 10px;color:#e2e8f0">C(K,k) C(N−K,n−k) / C(N,n)</td>
<td style="padding:8px 10px;color:#e2e8f0">nK/N</td>
<td style="padding:8px 10px;color:#e2e8f0">n(K/N)(1−K/N)(N−n)/(N−1)</td>
<td style="padding:8px 10px;color:#e2e8f0">No closed form</td>
<td style="padding:8px 10px;color:#e2e8f0">—</td>
<td style="padding:8px 10px;color:#e2e8f0">Sampling without replacement; → Bin as N→∞</td>
<td style="padding:8px 10px;color:#e2e8f0">Quality control, Fisher's exact test, ecology</td>
</tr>
<tr style="background-color:#0f2010">
<td style="border-left:4px solid #22c55e;padding:8px 10px;font-weight:bold;color:#4ade80;white-space:nowrap"><strong>Discrete Uniform</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>DU(a, b)</code><br><small>a,b ∈ ℤ; n=b−a+1</small></td>
<td style="padding:8px 10px;color:#e2e8f0">{a, a+1, …, b}</td>
<td style="padding:8px 10px;color:#e2e8f0">1/n</td>
<td style="padding:8px 10px;color:#e2e8f0">(a+b)/2</td>
<td style="padding:8px 10px;color:#e2e8f0">(n²−1)/12</td>
<td style="padding:8px 10px;color:#e2e8f0">e<sup>at</sup>(1−e<sup>nt</sup>)/n(1−e<sup>t</sup>)</td>
<td style="padding:8px 10px;color:#e2e8f0">0</td>
<td style="padding:8px 10px;color:#e2e8f0">Max entropy on finite set; perfectly symmetric</td>
<td style="padding:8px 10px;color:#e2e8f0">Dice, lotteries, random number generation</td>
</tr>
<tr style="background-color:#1e1e1e">
<td style="border-left:4px solid #9ca3af;padding:8px 10px;font-weight:bold;color:#d1d5db;white-space:nowrap"><strong>Zipf (Zeta)</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>Zipf(s)</code><br><small>s &gt; 1; ζ(s) = Riemann zeta</small></td>
<td style="padding:8px 10px;color:#e2e8f0">{1, 2, 3, …}</td>
<td style="padding:8px 10px;color:#e2e8f0">1/(k<sup>s</sup> · ζ(s))</td>
<td style="padding:8px 10px;color:#e2e8f0">ζ(s−1)/ζ(s) if s&gt;2; else undefined</td>
<td style="padding:8px 10px;color:#e2e8f0">Finite only if s &gt; 3</td>
<td style="padding:8px 10px;color:#e2e8f0">No closed form</td>
<td style="padding:8px 10px;color:#e2e8f0">—</td>
<td style="padding:8px 10px;color:#e2e8f0">Heavy-tailed power law; rank ∝ 1/k<sup>s</sup></td>
<td style="padding:8px 10px;color:#e2e8f0">Word frequency, city sizes, web traffic</td>
</tr>
</tbody>
</table>

> **Notation:** PMF = Probability Mass Function · MGF = Moment Generating Function · C(n,k) = binomial coefficient · ζ = Riemann zeta function

---

## Continuous Distributions

<table>
<thead>
<tr style="background-color:#1e2740">
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">Distribution</th>
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">Notation</th>
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">Support</th>
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">PDF — f(x)</th>
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">CDF — F(x)</th>
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">E[X]</th>
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">Var(X)</th>
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">MGF M(t)</th>
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">Skewness</th>
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">Key Property</th>
<th style="color:#6ee7b7;padding:8px 10px;white-space:nowrap">Common Uses</th>
</tr>
</thead>
<tbody>
<tr style="background-color:#1e1a3a">
<td style="border-left:4px solid #7c6fe0;padding:8px 10px;font-weight:bold;color:#a78bfa;white-space:nowrap"><strong>Uniform</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>U(a, b)</code><br><small>a &lt; b ∈ ℝ</small></td>
<td style="padding:8px 10px;color:#e2e8f0">[a, b]</td>
<td style="padding:8px 10px;color:#e2e8f0">1/(b−a)</td>
<td style="padding:8px 10px;color:#e2e8f0">(x−a)/(b−a)</td>
<td style="padding:8px 10px;color:#e2e8f0">(a+b)/2</td>
<td style="padding:8px 10px;color:#e2e8f0">(b−a)²/12</td>
<td style="padding:8px 10px;color:#e2e8f0">(e<sup>tb</sup>−e<sup>ta</sup>)/t(b−a)</td>
<td style="padding:8px 10px;color:#e2e8f0">0</td>
<td style="padding:8px 10px;color:#e2e8f0">Max entropy on [a,b]; basis for inverse CDF sampling</td>
<td style="padding:8px 10px;color:#e2e8f0">RNG, Monte Carlo, rounding errors</td>
</tr>
<tr style="background-color:#0f2a1f">
<td style="border-left:4px solid #10b981;padding:8px 10px;font-weight:bold;color:#34d399;white-space:nowrap"><strong>Normal</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>N(μ, σ²)</code><br><small>μ ∈ ℝ, σ² &gt; 0</small></td>
<td style="padding:8px 10px;color:#e2e8f0">(−∞, +∞)</td>
<td style="padding:8px 10px;color:#e2e8f0">exp(−(x−μ)²/2σ²)/(σ√(2π))</td>
<td style="padding:8px 10px;color:#e2e8f0">Φ((x−μ)/σ)</td>
<td style="padding:8px 10px;color:#e2e8f0">μ</td>
<td style="padding:8px 10px;color:#e2e8f0">σ²</td>
<td style="padding:8px 10px;color:#e2e8f0">exp(μt+σ²t²/2)</td>
<td style="padding:8px 10px;color:#e2e8f0">0</td>
<td style="padding:8px 10px;color:#e2e8f0">CLT attractor; 68–95–99.7 rule; mean=median=mode; stable</td>
<td style="padding:8px 10px;color:#e2e8f0">Heights, scores, measurement errors</td>
</tr>
<tr style="background-color:#2a1500">
<td style="border-left:4px solid #f97316;padding:8px 10px;font-weight:bold;color:#fb923c;white-space:nowrap"><strong>Exponential</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>Exp(λ)</code><br><small>λ &gt; 0 (rate)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">[0, +∞)</td>
<td style="padding:8px 10px;color:#e2e8f0">λ e<sup>−λx</sup></td>
<td style="padding:8px 10px;color:#e2e8f0">1−e<sup>−λx</sup></td>
<td style="padding:8px 10px;color:#e2e8f0">1/λ</td>
<td style="padding:8px 10px;color:#e2e8f0">1/λ²</td>
<td style="padding:8px 10px;color:#e2e8f0">λ/(λ−t), t&lt;λ</td>
<td style="padding:8px 10px;color:#e2e8f0">2</td>
<td style="padding:8px 10px;color:#e2e8f0">Only continuous memoryless dist.; Γ(1,λ); constant hazard</td>
<td style="padding:8px 10px;color:#e2e8f0">Inter-event times, lifetimes, queues</td>
</tr>
<tr style="background-color:#2a0f1e">
<td style="border-left:4px solid #ec4899;padding:8px 10px;font-weight:bold;color:#f472b6;white-space:nowrap"><strong>Gamma</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>Γ(α, β)</code><br><small>α,β &gt; 0 (shape, rate)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">(0, +∞)</td>
<td style="padding:8px 10px;color:#e2e8f0">β<sup>α</sup> x<sup>α−1</sup> e<sup>−βx</sup>/Γ(α)</td>
<td style="padding:8px 10px;color:#e2e8f0">γ(α,βx)/Γ(α)</td>
<td style="padding:8px 10px;color:#e2e8f0">α/β</td>
<td style="padding:8px 10px;color:#e2e8f0">α/β²</td>
<td style="padding:8px 10px;color:#e2e8f0">(β/(β−t))<sup>α</sup></td>
<td style="padding:8px 10px;color:#e2e8f0">2/√α</td>
<td style="padding:8px 10px;color:#e2e8f0">Sum of α iid Exp(β); Exp=Γ(1,λ); conjugate prior for Poi λ</td>
<td style="padding:8px 10px;color:#e2e8f0">Waiting times, claim amounts, Bayesian priors</td>
</tr>
<tr style="background-color:#0a1f35">
<td style="border-left:4px solid #3b82f6;padding:8px 10px;font-weight:bold;color:#60a5fa;white-space:nowrap"><strong>Beta</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>Beta(α, β)</code><br><small>α,β &gt; 0 (shapes)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">[0, 1]</td>
<td style="padding:8px 10px;color:#e2e8f0">x<sup>α−1</sup>(1−x)<sup>β−1</sup>/B(α,β)</td>
<td style="padding:8px 10px;color:#e2e8f0">I<sub>x</sub>(α,β)</td>
<td style="padding:8px 10px;color:#e2e8f0">α/(α+β)</td>
<td style="padding:8px 10px;color:#e2e8f0">αβ/((α+β)²(α+β+1))</td>
<td style="padding:8px 10px;color:#e2e8f0">No closed form</td>
<td style="padding:8px 10px;color:#e2e8f0">2(β−α)√(α+β+1)/((α+β+2)√(αβ))</td>
<td style="padding:8px 10px;color:#e2e8f0">Lives on [0,1]; conjugate prior for Bin p; U(0,1)=Beta(1,1)</td>
<td style="padding:8px 10px;color:#e2e8f0">Proportions, A/B testing, PERT estimates</td>
</tr>
<tr style="background-color:#1f1a00">
<td style="border-left:4px solid #eab308;padding:8px 10px;font-weight:bold;color:#facc15;white-space:nowrap"><strong>Chi-Squared</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>χ²(k)</code><br><small>k ∈ ℕ (df)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">[0, +∞)</td>
<td style="padding:8px 10px;color:#e2e8f0">x<sup>k/2−1</sup>e<sup>−x/2</sup>/(2<sup>k/2</sup>Γ(k/2))</td>
<td style="padding:8px 10px;color:#e2e8f0">γ(k/2, x/2)/Γ(k/2)</td>
<td style="padding:8px 10px;color:#e2e8f0">k</td>
<td style="padding:8px 10px;color:#e2e8f0">2k</td>
<td style="padding:8px 10px;color:#e2e8f0">(1−2t)<sup>−k/2</sup>, t&lt;½</td>
<td style="padding:8px 10px;color:#e2e8f0">√(8/k)</td>
<td style="padding:8px 10px;color:#e2e8f0">Sum of k squared N(0,1); =Γ(k/2,½); χ²(k₁)+χ²(k₂)=χ²(k₁+k₂)</td>
<td style="padding:8px 10px;color:#e2e8f0">Goodness-of-fit, test of independence, S²</td>
</tr>
<tr style="background-color:#0f2010">
<td style="border-left:4px solid #22c55e;padding:8px 10px;font-weight:bold;color:#4ade80;white-space:nowrap"><strong>Student's t</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>t(ν)</code><br><small>ν &gt; 0 (df)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">(−∞, +∞)</td>
<td style="padding:8px 10px;color:#e2e8f0">Γ((ν+1)/2)(1+x²/ν)<sup>−(ν+1)/2</sup>/(√(νπ)Γ(ν/2))</td>
<td style="padding:8px 10px;color:#e2e8f0">Regularised incomplete beta</td>
<td style="padding:8px 10px;color:#e2e8f0">0 (ν&gt;1); else undef.</td>
<td style="padding:8px 10px;color:#e2e8f0">ν/(ν−2) (ν&gt;2); else undef.</td>
<td style="padding:8px 10px;color:#e2e8f0">Does not exist</td>
<td style="padding:8px 10px;color:#e2e8f0">0</td>
<td style="padding:8px 10px;color:#e2e8f0">Heavier tails than Normal; →N(0,1) as ν→∞; t(1)=Cauchy; t²(ν)=F(1,ν)</td>
<td style="padding:8px 10px;color:#e2e8f0">Small-sample inference, t-tests, regression</td>
</tr>
<tr style="background-color:#1e1e1e">
<td style="border-left:4px solid #9ca3af;padding:8px 10px;font-weight:bold;color:#d1d5db;white-space:nowrap"><strong>F-distribution</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>F(d₁, d₂)</code><br><small>d₁,d₂ &gt; 0 (df)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">[0, +∞)</td>
<td style="padding:8px 10px;color:#e2e8f0">√((d₁x)<sup>d₁</sup>d₂<sup>d₂</sup>/(d₁x+d₂)<sup>d₁+d₂</sup>)/(x B(d₁/2,d₂/2))</td>
<td style="padding:8px 10px;color:#e2e8f0">Regularised incomplete beta</td>
<td style="padding:8px 10px;color:#e2e8f0">d₂/(d₂−2), d₂&gt;2</td>
<td style="padding:8px 10px;color:#e2e8f0">2d₂²(d₁+d₂−2)/(d₁(d₂−2)²(d₂−4)), d₂&gt;4</td>
<td style="padding:8px 10px;color:#e2e8f0">Does not exist</td>
<td style="padding:8px 10px;color:#e2e8f0">Right-skewed</td>
<td style="padding:8px 10px;color:#e2e8f0">Ratio of two χ²/df; 1/F(d₁,d₂)=F(d₂,d₁); t²(ν)=F(1,ν)</td>
<td style="padding:8px 10px;color:#e2e8f0">ANOVA, regression F-test, comparing variances</td>
</tr>
<tr style="background-color:#0d2020">
<td style="border-left:4px solid #2dd4bf;padding:8px 10px;font-weight:bold;color:#5eead4;white-space:nowrap"><strong>Weibull</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>W(k, λ)</code><br><small>k,λ &gt; 0 (shape, scale)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">[0, +∞)</td>
<td style="padding:8px 10px;color:#e2e8f0">(k/λ)(x/λ)<sup>k−1</sup>exp(−(x/λ)<sup>k</sup>)</td>
<td style="padding:8px 10px;color:#e2e8f0">1−exp(−(x/λ)<sup>k</sup>)</td>
<td style="padding:8px 10px;color:#e2e8f0">λ Γ(1+1/k)</td>
<td style="padding:8px 10px;color:#e2e8f0">λ²[Γ(1+2/k)−(Γ(1+1/k))²]</td>
<td style="padding:8px 10px;color:#e2e8f0">No closed form</td>
<td style="padding:8px 10px;color:#e2e8f0">Depends on k</td>
<td style="padding:8px 10px;color:#e2e8f0">k=1→Exp; k&lt;1: ↓ hazard; k=1: flat; k&gt;1: ↑ hazard</td>
<td style="padding:8px 10px;color:#e2e8f0">Reliability, wind speed, material fatigue</td>
</tr>
<tr style="background-color:#20100d">
<td style="border-left:4px solid #f87171;padding:8px 10px;font-weight:bold;color:#fca5a5;white-space:nowrap"><strong>Log-Normal</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>LogN(μ, σ²)</code><br><small>μ ∈ ℝ, σ² &gt; 0</small></td>
<td style="padding:8px 10px;color:#e2e8f0">(0, +∞)</td>
<td style="padding:8px 10px;color:#e2e8f0">exp(−(ln x−μ)²/2σ²)/(xσ√(2π))</td>
<td style="padding:8px 10px;color:#e2e8f0">Φ((ln x−μ)/σ)</td>
<td style="padding:8px 10px;color:#e2e8f0">exp(μ+σ²/2)</td>
<td style="padding:8px 10px;color:#e2e8f0">(e<sup>σ²</sup>−1)exp(2μ+σ²)</td>
<td style="padding:8px 10px;color:#e2e8f0">Does not exist</td>
<td style="padding:8px 10px;color:#e2e8f0">(e<sup>σ²</sup>+2)√(e<sup>σ²</sup>−1)</td>
<td style="padding:8px 10px;color:#e2e8f0">ln(X)~N(μ,σ²); product CLT; mean&gt;median&gt;mode</td>
<td style="padding:8px 10px;color:#e2e8f0">Stock prices, incomes, latency, biology</td>
</tr>
<tr style="background-color:#1a1020">
<td style="border-left:4px solid #c084fc;padding:8px 10px;font-weight:bold;color:#d8b4fe;white-space:nowrap"><strong>Cauchy</strong></td>
<td style="padding:8px 10px;color:#e2e8f0"><code>Cauchy(x₀, γ)</code><br><small>x₀ ∈ ℝ (loc), γ &gt; 0 (scale)</small></td>
<td style="padding:8px 10px;color:#e2e8f0">(−∞, +∞)</td>
<td style="padding:8px 10px;color:#e2e8f0">1/(πγ[1+((x−x₀)/γ)²])</td>
<td style="padding:8px 10px;color:#e2e8f0">½+arctan((x−x₀)/γ)/π</td>
<td style="padding:8px 10px;color:#e2e8f0"><em>Undefined</em></td>
<td style="padding:8px 10px;color:#e2e8f0"><em>Undefined</em></td>
<td style="padding:8px 10px;color:#e2e8f0">Does not exist</td>
<td style="padding:8px 10px;color:#e2e8f0"><em>Undefined</em></td>
<td style="padding:8px 10px;color:#e2e8f0">t(1); ratio of two N(0,1); no mean/var/MGF; LLN &amp; CLT fail</td>
<td style="padding:8px 10px;color:#e2e8f0">Physics resonance, stress-testing estimators</td>
</tr>
</tbody>
</table>

> **Notation:** PDF = Probability Density Function · CDF = Cumulative Distribution Function · MGF = Moment Generating Function · Γ = Gamma function · B = Beta function · Φ = Standard Normal CDF · γ(·,·) = Lower Incomplete Gamma · I_x = Regularised Incomplete Beta
