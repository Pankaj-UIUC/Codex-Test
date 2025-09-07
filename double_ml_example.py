"""
A short, self-contained example that introduces Double Machine Learning (DML).

DML is a framework for estimating causal effects with machine learning while
correcting for bias from high-dimensional confounders. By cross-fitting the
machine learning models, it avoids overfitting and yields valid statistical
inference. The approach is widely used in economics and online advertising to
measure the incremental effect of showing ads to users who have rich feature
vectors.

This script is intended for a workshop. It keeps the code and explanation
simple, yet it showcases the key ideas:
    1. Generate synthetic data with a known treatment effect.
    2. Create a ``DoubleMLData`` object.
    3. Specify machine learning models for the nuisance functions.
    4. Estimate the treatment effect using ``DoubleMLPLR`` (partially linear
       regression model).
    5. Report the estimated Average Treatment Effect (ATE).

Run the script with ``python double_ml_example.py``.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from doubleml import DoubleMLData, DoubleMLPLR

# ---------------------------------------------------------------------------
# 1. Simulate data
# ---------------------------------------------------------------------------
np.random.seed(42)
n_obs = 500
x1 = np.random.normal(size=n_obs)
x2 = np.random.normal(size=n_obs)
# Treatment is a function of the covariates plus some noise
# so that x1 and x2 are confounders.
d = 0.5 * x1 + 0.3 * x2 + np.random.normal(size=n_obs)
# Outcome depends on treatment and covariates
true_ate = 1.0
y = true_ate * d + 0.5 * x1 - 0.5 * x2 + np.random.normal(size=n_obs)

data = pd.DataFrame({'y': y, 'd': d, 'x1': x1, 'x2': x2})

# ---------------------------------------------------------------------------
# 2. Wrap the data for DoubleML
# ---------------------------------------------------------------------------
dml_data = DoubleMLData(data, y_col='y', d_cols='d', x_cols=['x1', 'x2'])

# ---------------------------------------------------------------------------
# 3. Choose ML models for the nuisance functions
#    (outcome regression and treatment regression)
# ---------------------------------------------------------------------------
ml_l = RandomForestRegressor(n_estimators=100, max_depth=3, random_state=42)
ml_m = RandomForestRegressor(n_estimators=100, max_depth=3, random_state=42)

# ---------------------------------------------------------------------------
# 4. Estimate the treatment effect via DoubleMLPLR
# ---------------------------------------------------------------------------
dml_plr = DoubleMLPLR(dml_data, ml_l, ml_m, n_folds=5)
dml_plr.fit()

# ---------------------------------------------------------------------------
# 5. Present the result
# ---------------------------------------------------------------------------
print("True ATE:", true_ate)
print("Estimated ATE:", round(dml_plr.coef[0], 3))
print("Std. Error:", round(dml_plr.se[0], 3))
