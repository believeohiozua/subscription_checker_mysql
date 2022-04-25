ALTER TABLE t_budgets
ADD COLUMN a_percent DECIMAL(10,2) AFTER a_amount_spent;

UPDATE t_budgets SET
  a_percent = (a_amount_spent/a_budget_amount)*100;

-- UPDATE t_budgets
-- --  (a_shop_id, a_month, a_budget_amount, a_amount_spent)
-- SET a_month='2020-06-01' where a_shop_id=1 --(1, '2020-06-01', 930.00, 725.67),
-- SET a_month='2020-06-01' where a_shop_id=1 --(2, '2020-06-01', 990.00, 886.63),
-- SET a_month='2020-06-01' where a_shop_id=1 --(3, '2020-06-01', 650.00, 685.91),
-- SET a_month='2020-06-01' where a_shop_id=1 --(4, '2020-06-01', 740.00, 746.92),
-- SET a_month='2020-06-01' where a_shop_id=1 --(5, '2020-06-01', 630.00, 507.64),
-- SET a_month='2020-06-01' where a_shop_id=1 --(6, '2020-06-01', 640.00, 946.32),
-- SET a_month='2020-06-01' where a_shop_id=1 --(7, '2020-06-01', 980.00, 640.16),
-- SET a_month='2020-06-01' where a_shop_id=1 --(8, '2020-06-01', 790.00, 965.64),
-- SET a_month='2020-06-01' where a_shop_id=1 --(1, '2020-07-01', 960.00, 803.67),
-- SET a_month='2020-06-01' where a_shop_id=1 --(2, '2020-07-01', 670.00, 715.64),
-- SET a_month='2020-06-01' where a_shop_id=1 --(3, '2020-07-01', 890.00, 580.81),
-- SET a_month='2020-06-01' where a_shop_id=1 --(4, '2020-07-01', 590.00, 754.93),
-- SET a_month='2020-06-01' where a_shop_id=1 --(5, '2020-07-01', 870.00, 505.12),
-- SET a_month='2020-06-01' where a_shop_id=1 --(6, '2020-07-01', 700.00, 912.30),
-- SET a_month='2020-06-01' where a_shop_id=1 --(7, '2020-07-01', 990.00, 805.15),
-- SET a_month='2020-06-01' where a_shop_id=1 --(8, '2020-07-01', 720.00, 504.25);
