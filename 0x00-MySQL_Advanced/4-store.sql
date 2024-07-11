-- creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
-- for each row in orders
FOR EACH ROW
UPDATE items
-- set quantity = quantity minus number attribute/column in orders
SET quantity = quantity - NEW.number
-- only update if the name of item is similar to item_name of orders
WHERE name = NEW.item_name
