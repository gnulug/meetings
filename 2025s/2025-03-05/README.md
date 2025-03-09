# Rigorous Benchmarking in Reasonable Time

## Part 1: benchmark selection and subsetting

[_Subsetting the SPEC CPU2006 benchmark suite_ by Phansalkar et al. 2007](https://doi.org/10.1145/1241601.1241616) shows an example of benchmark subsetting. Table 1 shows features used or each benchmark. Figure 5 shows PCA. Figure 6 shows a dendrogram of hierarchical clsutering.

[_BenchSubset: A framework for selecting benchmark subsets based on consensus clustering_ by Zhan et al. 2021](https://doi.org/10.1002/int.22791) synthesizes prior subsetting works to create a general best-practice.

## Part 2: measuring

[_Producing Wrong Data Without Doing Anything Obviously Wrong!_ by Mytkowicz e tal. 2009](https://doi.org/10.1145/1508284.1508275). Incredible paper.

[Reproducible benchmarking in Linux-based environments from Julia developers](https://github.com/JuliaCI/BenchmarkTools.jl/blob/4db27210d43abf2c55226366f3a749afe1d64951/doc/linuxtips.md)

You may need to use [_Setuid demystified_ by Chen et al. 2002](https://people.eecs.berkeley.edu/~daw/papers/setuid-usenix02.pdf) to safely implement benchmark procedures at a user-level.

[_Stepping Towards Noiseless Linux Environment_ by Akkan, Lang, and Liebrock 2012](https://doi.org/10.1145/2318916.2318925)

## Part 3: how to aggregate statistics

[_How to not lie with statistics; The correct way to summarize benchmark results_ by Flemming and Wallace 1986](https://doi.org/10.1145/5666.5673) explains why arithmetic mean of speedup ratios can be misleading and change based on what one is normalizing to (Tables III and IV). It shows how geometric mean is robust to rescaling (Tables V and VI).

[_Characterizing computer performance with a single number_ by Smith 1988](https://doi.org/10.1145/63039.63043) argues for harmonic mean. In my view, geometric mean is best for speedup ratios whereas harmonic mean is best for combining rates.

[_The Harmonic or Geometric Mean: Does it Really Matter?_ by Citron, Huraney, and Gnadrey 2006](https://doi.org/10.1145/1186736.1186738) documents the War of the Means.

## Part 4: Quantifying uncertainty

[_SoK: Benchmarking Flaws in Systems Security_ by Kouwe et al. 2019](https://doi.org/10.1109/EuroSP.2019.00031) samples literature to find that most empirical performance claims do not include any measure of uncertainty (B4) and also count the number of claims that use the wrong mean (B5).

[_War of the Benchmark Means: Time for a Truce_ by Mashey 2004](https://doi.org/10.1145/1040136.1040137). While this discusses the war of the means, I brought it up to show that program runtimes are right-skewed and possibly log-normal. Errors can be more accurately estimated from this.

In probability theory, a probability distribution is [infinitely divisible (Wikipedia)](https://en.wikipedia.org/wiki/Infinite_divisibility_(probability)) if it can be expressed as the probability distribution of the sum of an arbitrary number of independent and identically distributed (i.i.d.) random variables. The characteristic function of any infinitely divisible distribution is then called an infinitely divisible characteristic function.

What distribution do you think program runtimes are ([on Sam's Bluesky](https://bsky.app/profile/samgrayson.me/post/3lggsguu4lc23))?

[Uncertainty quantification (Wikipedia)](https://en.wikipedia.org/wiki/Uncertainty_quantification) is the science of quantitative characterization and estimation of uncertainties in both computational and real world applications.

In probability theory and statistics, [the gamma distribution (Wikipdia)](https://en.wikipedia.org/wiki/Gamma_distribution) is a versatile two-parameter family of continuous probability distributions.

Statistical significance is logically independent of clinical relevance according to Figure 2 of [_Confidence Interval or P-Value?_ by Prel et al. 2009](https://doi.org/10.3238/arztebl.2009.0335).
