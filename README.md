# Device-Normalised Geometry for Muscle Architecture Measurement in B-Mode Ultrasound

Technical report on a fully automated pipeline for measuring pennation angle, fascicle
length and muscle thickness from B-mode ultrasound across six scanner layouts.

**Read it:** https://cdowning-pdf.github.io/umud-muscle-architecture/

## Summary

| | |
|---|---|
| UMUD Challenge, final standing | 38 / 690 teams (top 5.5%) |
| Movement, provisional → final | +50 places |
| Benchmark score vs. 7-rater consensus | 0.196 |
| One human expert, same benchmark | 0.259 |

The pipeline measures closer to a seven-rater expert consensus than an individual
expert does. Two components are derived rather than fitted, and are the ones we
expect to transfer:

- **Lateral anisotropy correction.** Two of six scanner layouts export horizontally
  resampled screenshots, so pixels are not square and every angle read in pixel
  coordinates is wrong. Corrected from published aperture specifications.
- **Convergence-corrected fascicle length.** Extending fascicle fragments to both
  aponeuroses is exact only when they are parallel; when they converge by half-angle
  *h* the chord is inflated by 1/(1 − cot²γ·tan²*h*). A bisector-referenced estimator
  removes the convergence dependence, so one calibration constant transfers between
  anatomically distinct datasets.

Colton Downing · University of Southern California · November 2026
