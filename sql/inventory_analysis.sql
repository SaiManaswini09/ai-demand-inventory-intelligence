-- Priority procurement actions
SELECT plant, material, category, supplier, stockout_risk, on_hand_qty,
       forecast_4w_qty, recommended_order_qty, excess_value
FROM procurement_recommendations
ORDER BY CASE stockout_risk WHEN 'High' THEN 1 WHEN 'Medium' THEN 2 ELSE 3 END,
         recommended_order_qty DESC;

-- Working-capital opportunity
SELECT category, SUM(excess_value) AS excess_inventory_value
FROM procurement_recommendations
GROUP BY category ORDER BY excess_inventory_value DESC;
