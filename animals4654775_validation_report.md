# Computational validation report — animals-4654775

**Input:** `Clarias-Bioeconomic-Sperm-Pooling-main.zip` (GitHub repository snapshot supplied by authors).

**Scope:** Static inspection and execution of five Python files; numerical cross-check against Tables 1 and 2 in `animals-4654775.docx`. This report does not certify the scripts as the code originally used by the authors.

## Execution

- `python -m py_compile *.py`: PASS.
- `python compensation.py`, `python economics.py`, `python longitudinal.py`, `python NPV.py`: PASS, each produced its named PNG at 300 dpi.
- `requirements.txt` lists NumPy, pandas, Matplotlib, seaborn; only NumPy and Matplotlib appear to be imported by the inspected scripts.

## Reproduced model outputs

| Scenario | Males (ceil function) | Net profit per cycle (THB) | 5-year NPV (THB) | Matches Table 1? |
|---|---:|---:|---:|---|
| Ideal | 10 | 166,500 | 1,994,359 | Yes |
| Microscopic | 25 | 164,250 | 1,967,408 | Yes |
| Visual | 58 | 159,300 | 1,908,116 | Yes |
| Random | 115 | 150,750 | 1,805,703 | Yes |
| Traditional (uncompensated) | 10 | 72,975 (hard-coded) | 874,104 | Numerically yes, not independently derived |

## Substantive concerns needing resolution before a finalized reproducibility release

1. **Visual male-count inconsistency:** Equation with a ceiling function yields `ceil(100/10 * 70 / 12.27) = 58`. Table 2 reports **57** while Table 1 profits imply **58**. Amend the manuscript or explain why a different rounding convention is used.
2. **Traditional-case circularity:** `UNCOMPENSATED_PROFIT = 72975` is entered as a published result in `model.py`; the underlying hatching/revenue model does not independently derive it. Supply input assumptions/data and the complete calculation, or disclose that this is a reported input.
3. **Unverified longitudinal decline:** `longitudinal.py` chooses `r = 0.25/year` as an illustrative assumption, not a measured value. The script plots **10 years**, while Methods 2.3.4 mentions a **5-year** trajectory (the Figure 3 caption mentions 10 years). Harmonize time horizon and label assumptions clearly.
4. **Model scope:** `economics.py` uses a simplified revenue and cost formula with no independently implemented motility-to-hatching calibration or fixed-cost term. Reconcile this with the full methodology before calling it a complete verification of Figure 4 or break-even threshold.
5. **Figure 5 frequency:** The script plots cumulative NPV by year (0–5), while manuscript discusses 15 production cycles. The annual values represent three discounted cycles per year. Explain this aggregation in the figure caption and README.
6. **Software provenance:** `model.py` explicitly states these scripts are *reconstructions*, not the original author source. Keep this provenance in the README and any Zenodo metadata unless the original analysis workflow can be independently substantiated.

## Release recommendation

Use GitHub as a **draft** and postpone a final Zenodo release until the author team resolves these discrepancies, documents inputs/code dependencies, and approves the source package. A future release may accurately be described as a **reconstructed Python implementation** if original scripts are unavailable.
