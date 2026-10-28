import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from feature_engineering import add_lag_features
df=add_lag_features(pd.read_csv('data/demand_history.csv')).dropna()
X=['lag_1','lag_2','lag_4','lag_8','rolling_4w','rolling_8w']; split=int(len(df)*.8)
m=RandomForestRegressor(n_estimators=150,random_state=42,n_jobs=-1).fit(df.iloc[:split][X],df.iloc[:split].demand_qty)
print('MAE:',round(mean_absolute_error(df.iloc[split:].demand_qty,m.predict(df.iloc[split:][X])),2))
