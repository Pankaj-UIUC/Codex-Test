## Double Machine Learning Workshop Example

Double Machine Learning (DML) uses modern machine learning models to control for
large sets of confounding variables when estimating causal effects. By splitting
the data and cross-fitting the models, DML delivers unbiased estimates and valid
confidence intervals even when using flexible learners. This methodology is
popular in economics and Ads Measurement to quantify the incremental impact of
showing ads to users with many observed features.

`double_ml_example.py` provides a short demonstration of Double Machine
Learning. Run the script with:

```bash
python double_ml_example.py
```

It simulates data and estimates the average treatment effect of a treatment on
an outcome using random forests for the nuisance functions.


## Ads Tactic Effectiveness Example

`double_ml_ads_example.py` mimics user-level ad measurement. It estimates the
lift from a targeted ad tactic while controlling for age, prior engagement, and
device type.

Run the script with:

```bash
python double_ml_ads_example.py
```

