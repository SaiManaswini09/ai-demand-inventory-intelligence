# AI Demand & Inventory Intelligence

Predictive + prescriptive supply-chain analytics portfolio project.

## Business problem
A multi-plant manufacturer faces stockouts, excess inventory, and inconsistent material planning. This project combines demand history, inventory, forecasting features, and transparent recommendation logic to identify future shortages, working-capital opportunities, and replenishment actions.

## What it demonstrates
- 96 weeks of synthetic demand across 60 materials and 4 plants
- Python feature engineering and Random Forest forecasting example
- 4-week demand forecasts and forecast-accuracy metric
- Stockout-risk classification and recommended order quantities
- Excess-inventory / working-capital analysis
- SQL analysis
- Dependency-free interactive GitHub Pages dashboard

## Architecture
`Synthetic ERP-style data → feature engineering → forecasting → inventory risk → recommendation engine → executive dashboard`

## Repository
```text
data/       demand, inventory and material master
outputs/    forecasts and procurement recommendations
src/        feature engineering, ML and recommendation logic
sql/        business analysis queries
notebooks/  exploratory analysis
index.html  interactive GitHub Pages dashboard
```

## Recommendation logic
`Recommended Order = max(0, 4-Week Forecast + Safety Stock - On-Hand Inventory)`

All data is synthetic and created solely for portfolio demonstration. It contains no confidential employer, supplier, customer, or commercial information.
