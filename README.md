# Measuring Muscle Better Than a Human Expert



Technical report on a fully automated pipeline for measuring pennation angle, fascicle length
and muscle thickness from B-mode ultrasound across six scanner layouts.

**Read it:** https://cdowning-pdf.github.io/umud-muscle-architecture/

## Result

Scores below are **error** measurements, like golf, lower is better. Each number is how far a measurement sits from the consensus of seven expert raters.

| | |
|---|---|
| **My model** | **0.196** |
| One human expert (leave-one-out median) | 0.264, 35% higher |
| DL_Track_US, the standard tool in this field | 0.331, 69% higher |
| SMA, earlier automated method | 0.409, 109% higher |

The pipeline measures closer to a seven-rater expert consensus than an individual
expert does, and closer than DL_Track_US, the established open-source tool for this
task. All methods are scored on the same 35 images against the same consensus. Two components are derived rather than fitted, and are the ones expected
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
