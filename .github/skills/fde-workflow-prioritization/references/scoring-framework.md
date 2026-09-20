# Value × Feasibility Scoring Framework v1

Use whole-number component ratings from 1 to 5. Calculate weighted scores to one decimal place. Scores organize discussion; they are not objective truth.

## Value score

| Component | Weight | Rating guidance |
|---|---:|---|
| Business impact | 50% | 1 = local inconvenience; 5 = material decision, control, customer, financial, or deadline impact |
| Frequency / volume | 30% | 1 = rare and small; 5 = frequent, high-volume, or continuously recurring |
| Reach | 20% | 1 = one individual; 5 = multiple teams or enterprise-wide |

```text
Value = impact × 0.50 + frequency_volume × 0.30 + reach × 0.20
```

## Feasibility score

| Component | Weight | Rating guidance |
|---|---:|---|
| Data readiness | 30% | 1 = unknown/unavailable; 5 = accessible, governed, understood |
| Rule/process clarity | 25% | 1 = contradictory/implicit; 5 = bounded and validated |
| Owner readiness | 20% | 1 = no accountable Owner; 5 = Owner and approvers engaged |
| Technical feasibility | 15% | 1 = major unknown dependencies; 5 = bounded and compatible with current environment |
| Compliance readiness | 10% | 1 = unresolved critical concern; 5 = permitted path and controls identified |

```text
Feasibility = data × 0.30 + clarity × 0.25 + owner × 0.20
              + technical × 0.15 + compliance × 0.10
```

## AI Fit

Rate separately from feasibility:

| Rating | Meaning |
|---:|---|
| 1 | Deterministic routing/calculation; ordinary automation is preferable |
| 2 | Limited AI value; mostly workflow, data, or rule automation |
| 3 | AI assists one bounded step with Human Gate |
| 4 | Material unstructured interpretation, fuzzy matching, explanation, or knowledge retrieval |
| 5 | AI is central to a bounded workflow and can be evaluated with clear controls |

AI Fit never overrides a missing Owner, prohibited data use, or a High Risk control gap.

## Risk

- `Low`: reversible, limited scope, no sensitive decision or unresolved access issue.
- `Medium`: meaningful operational impact, personal/sensitive data, or important Human Gate requiring controls.
- `High`: unapproved data use, regulatory/control implications, automated high-stakes decision, unclear accountability, or material production dependency.

Record mitigations separately. An unmitigated High Risk candidate cannot be `Now`.

## Evidence Confidence

- `High`: multiple consistent sources plus a documented measure or approved supporting evidence reference.
- `Medium`: one specific recent case with credible reported or estimated baseline.
- `Low`: generic statements, unresolved contradictions, or missing scope/baseline/Owner.

## Recommendation rules

Apply in this order:

1. `Park` when Value ≤ 2.0 or a critical dependency makes progress currently impossible.
2. `Improve without AI` when AI Fit ≤ 2 and Value > 2.0.
3. `Now` when Value ≥ 4.0, Feasibility ≥ 3.0, AI Fit ≥ 3, risk is not unmitigated High, and Evidence Confidence is Medium or High.
4. `Validate` for remaining potentially valuable candidates that need evidence, data, Owner, risk, or solution validation.

Within each class, sort by Value descending, then Feasibility descending, then Evidence Confidence. Do not create an overall pseudo-precise rank across recommendation classes.
