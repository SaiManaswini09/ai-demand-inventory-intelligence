def add_lag_features(df):
    df=df.sort_values(['plant','material','week']).copy()
    g=df.groupby(['plant','material'])['demand_qty']
    for lag in (1,2,4,8): df[f'lag_{lag}']=g.shift(lag)
    df['rolling_4w']=g.transform(lambda s:s.shift(1).rolling(4).mean())
    df['rolling_8w']=g.transform(lambda s:s.shift(1).rolling(8).mean())
    return df
