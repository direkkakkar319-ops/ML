from xgboost import XGBRegressor
import shap
import matplotlib.pyplot as plt

# train an XGBoost model
X, y = shap.datasets.california()
model = XGBRegressor().fit(X, y)

# explain the model's predictions using SHAP
# (same syntax works for LightGBM, CatBoost, scikit-learn, transformers, Spark, etc.)
explainer = shap.Explainer(model)
shap_values = explainer(X)

shap.plots.waterfall(shap_values[0], show=False)
plt.savefig("waterfall.png", bbox_inches="tight", dpi=150)
plt.close()

shap.plots.force(shap_values[0], matplotlib=True, show=False)
plt.savefig("force_single.png", bbox_inches="tight", dpi=150)
plt.close()

force_plot = shap.plots.force(shap_values[:500])
shap.save_html("force_all.html", force_plot)