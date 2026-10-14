# Clarias Bio-Economic Sperm Pooling

### Python Implementation for Computational Reproducibility

**Associated Manuscript:**  
Beyond the Traditional 1:10 Breeding Ratio: A Bio-Economic Algorithm for Dynamic Sperm Pooling in Clarias Hatcheries

**Journal:** Animals (MDPI)  
**Manuscript ID:** animals-4654775  
**Research Unit:** Animal Genomics and Bioresource Research Unit, Faculty of Science, Kasetsart University, Thailand

## Overview

This repository contains a reconstructed Python implementation of the mathematical and bio-economic modeling framework described in the associated manuscript.

The computational framework evaluates sperm motility compensation, male broodstock requirements, economic costs, longitudinal simulations, and five-year net present value (NPV) projections for Clarias hatcheries.

## Biological Data Source

The biological parameters were derived primarily from previously published research:

Rey et al. (2025), *Aquaculture*.  
https://doi.org/10.1016/j.aquaculture.2024.741646

Additional hatchery production parameters were informed by historical records from Betagro Public Company Limited (2021–2023), as described in the manuscript.

## Python Scripts

- `compensation.py`: Sperm motility compensation and breeding-ratio calculations.
- `economics.py`: Bio-economic costs and financial break-even analysis.
- `longitudinal.py`: Longitudinal modeling of sperm motility and broodstock requirements.
- `NPV.py`: Five-year net present value calculations.
- `model.py`: Shared mathematical and economic model functions.

## Reproducibility Status

This code was reconstructed from the manuscript equations and reported parameters. It is not independently verified as the original code used during the study.

Some computational assumptions and reported outputs require further validation before this repository can be considered a fully reproducible implementation.

## Data Availability

The biological source data are described in the published study by Rey et al. The computational implementation is provided in this repository. Availability of underlying hatchery records is subject to applicable data access restrictions.

## Citation

Please cite the associated manuscript once publication details become available, together with the archived software release DOI when assigned.

## Contact

Animal Genomics and Bioresource Research Unit  
Faculty of Science, Kasetsart University, Thailand
