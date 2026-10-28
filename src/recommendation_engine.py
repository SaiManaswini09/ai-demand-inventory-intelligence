def recommend(on_hand,forecast_4w,safety_stock):
    qty=max(0,forecast_4w+safety_stock-on_hand)
    risk='High' if on_hand<forecast_4w*.65 else ('Medium' if on_hand<forecast_4w+safety_stock else 'Low')
    return {'risk':risk,'recommended_order_qty':qty,'action':'ORDER' if qty else 'MONITOR / REALLOCATE'}
