# Measuring Muscle Better Than a Human Expert

*Device-normalised geometry for muscle architecture measurement in B-mode ultrasound*

Preprint on a fully automated pipeline for measuring pennation angle, fascicle length
and muscle thickness from B-mode ultrasound across six scanner layouts.

**Read it:** https://cdowning-pdf.github.io/umud-muscle-architecture/

> **Status:** preprint, not peer reviewed. A manuscript version is being prepared for
> submission to the *Journal of Biomechanics*.

## Result

Scores below are **error** measurements — like golf, lower is better. Each number is
how far a measurement sits from the consensus of seven expert raters.

| | |
|---|---|
| UMUD Challenge, final standing | **Top 5.5%** — 38th of 690 teams |
| This pipeline, error vs. 7-expert consensus | **0.196** |
| One human expert, same measure | 0.259 |

The pipeline measures closer to a seven-rater expert consensus than an individual
expert does. Two components are derived rather than fitted, and are the ones expected
to transfer:

- **Lateral anisotropy correction.** Two of six scanner layouts export horizontally
  resampled screenshots, so pixels are not square and every angle read in pixel
  coordinates is wrong. Corrected from published aperture specifications.
- **Convergence-corrected fascicle length.** Extending fascicle fragments to both
  aponeuroses is exact only when they are parallel; when they converge by half-angle
  *h* the chord is inflated by 1/(1 − cot²γ·tan²*h*). A bisector-referenced estimator
  removes the convergence dependence, so one calibration constant transfers between
  anatomically distinct datasets.

Colton Downing · University of Southern California · November 2026
