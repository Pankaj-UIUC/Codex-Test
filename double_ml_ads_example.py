"""
Evaluate the effect of an ad tactic while accounting for confounders.

This workshop example mimics ad measurement with user-level features.
It estimates the causal impact of showing a tailored ad (``tactic``) on
whether a user converts. Age, prior engagement, and device type confound
both the ad assignment and the outcome. Double Machine Learning (DML)
separates these influences to recover the treatment effect.

Run with ``python double_ml_ads_example.py``.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from doubleml import DoubleMLData, DoubleMLPLR

# ---------------------------------------------------------------------------
# 1. Simulate realistic ad data
# ---------------------------------------------------------------------------
np.random.seed(123)
n_obs = 2000
age = np.random.normal(loc=35, scale=10, size=n_obs)
prior_clicks = np.random.poisson(lam=2, size=n_obs)
is_mobile = np.random.binomial(1, 0.6, size=n_obs)

# Probability of receiving the targeted tactic depends on confounders
logit_t = (
    0.1 * (age - age.mean())
    + 0.2 * prior_clicks
    + 0.3 * is_mobile
    + np.random.normal(size=n_obs)
)
prob_t = 1 / (1 + np.exp(-logit_t))
tactic = np.random.binomial(1, prob_t)

# Outcome: conversion depends on tactic and confounders
true_ate = 0.4
baseline_y = (
    0.05 * age - 0.02 * prior_clicks + 0.1 * is_mobile + np.random.normal(size=n_obs)
)
conversion = true_ate * tactic + baseline_y

data = pd.DataFrame(
    {
        "y": conversion,
        "tactic": tactic,
        "age": age,
        "prior_clicks": prior_clicks,
        "is_mobile": is_mobile,
    }
)

# ---------------------------------------------------------------------------
# 2. Wrap the data for DoubleML
# ---------------------------------------------------------------------------
dml_data = DoubleMLData(
    data, y_col="y", d_cols="tactic", x_cols=["age", "prior_clicks", "is_mobile"]
)

# ---------------------------------------------------------------------------
# 3. ML models for nuisance functions
# ---------------------------------------------------------------------------
ml_l = RandomForestRegressor(n_estimators=200, max_depth=5, random_state=123)
ml_m = RandomForestRegressor(n_estimators=200, max_depth=5, random_state=123)

# ---------------------------------------------------------------------------
# 4. Estimate treatment effect via DoubleMLPLR
# ---------------------------------------------------------------------------
dml_plr = DoubleMLPLR(dml_data, ml_l, ml_m, n_folds=5)
dml_plr.fit()

# ---------------------------------------------------------------------------
# 5. Show results
# ---------------------------------------------------------------------------
print("True ATE:", true_ate)
print("Estimated ATE:", round(dml_plr.coef[0], 3))
print("Std. Error:", round(dml_plr.se[0], 3))
