# CRUD in depth: Advanced querying and filtering with ORMs

# Filtering with complex conditions
from sqlalchemy import func, or_, and_
from my_flask_app.app import db
session = db.session

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    last_purchase_date = db.Column(db.DateTime)
    is_vip = db.Column(db.Boolean, default=False)
    city = db.Column(db.String(100))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    total_amount = db.Column(db.Float, nullable=False)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Float, nullable=False)


# Basic filtering is the foundation of data retrieval, 
# allowing developers to pinpoint exact information within a database. 

active_customers = session.query(Customer).filter(Customer.is_active == True).all()
# This query retrieves all customers who are currently active, 
# demonstrating a straightforward filtering condition.

# the ORM translates your intent into a SQL query that efficiently retrieves only those customer records where the is_active attribute is set to True.

# Complex filtering with logical operators allows developers to navigate the intricacies of data and extract precise results. 

# For example, suppose you need to pinpoint customers who are either "active" 
# and have made a purchase within the last 30 days, or who hold the esteemed "VIP" status. 

from datetime import datetime, timedelta

thirty_days_ago = datetime.now() - timedelta(days=30)
customers = session.query(Customer).filter(
    or_(
        and_(Customer.is_active == True, Customer.last_purchase_date >= thirty_days_ago),
        Customer.is_vip == True
    )
).all()

# The or_() function ensures that records matching either of the two main conditions are included
# while the and_() function ensures that both sub-conditions within the first main condition are satisfied.

# ORMs seamlessly navigate these relationships, allowing you to express this query with ease:
orders = session.query(Order).join(Customer).filter(Customer.city == 'New York').all()

# Here, the join() operation establishes a connection between the Order and Customer tables, 
# enabling filtering based on the city attribute of the Customer entity.

# Sorting results
# ORMs offer user-friendly ways to sort data based on various criteria, 
# ensuring that the information is presented logically and in a way that makes sense to users. 

# To retrieve a list of customers sorted alphabetically by their names, you can use the order_by() method:
sorted_customers = session.query(Customer).order_by(Customer.last_name).all()

# The ORM translates this instruction into an SQL ORDER BY clause, 
# ensuring that the retrieved customer records are arranged in ascending order based on the last_name column. 

#  To obtain the latest orders first, a slight modification to the order_by() clause achieves the desired outcome:
orders = session.query(Order).order_by(Order.order_date.desc()).all()

# ORMs excel at sorting on multiple columns, allowing for the establishment of data hierarchies. 
# For example, you can easily categorize customers first by their city, 
# and then alphabetically by last name within each city:
customers = session.query(Customer).order_by(Customer.city, Customer.last_name).all()

# Aggregating data
# ORMs equip developers with powerful aggregation functions 
# like count, sum, avg, min, and max, enabling the extraction of valuable insights.

# To ascertain the total number of orders in your system, 
# a simple aggregation query using the count() function achieves the desired result:
total_orders = session.query(func.count(Order.id)).scalar()

# The ORM translates this into an SQL COUNT query, 
# returning a single scalar value representing the total count of order records. 

# Calculating averages unveils central tendencies within your data.
# Determining the average order value provides valuable business intelligence.
avg_order_value = session.query(func.avg(Order.total_amount)).scalar()

# This query efficiently computes the average of the total_amount column across all order records, furnishing a concise summary statistic.

# Grouping and aggregating data unveils patterns. 
# Suppose you need to calculate the total sales for each product in your inventory. 
# ORMs facilitate such grouping and aggregation operations with remarkable ease:


product_sales = session.query(
    OrderItem.product_id, func.sum(OrderItem.quantity * OrderItem.unit_price).label('total_sales')
).group_by(OrderItem.product_id).all()

# This query groups order items by their product_id, 
# calculates the total sales for each group by summing the product of quantity and unit_price
# and labels the result as total_sales.
# The output provides a breakdown of sales figures for each product, enabling data-driven decision-making.

# Need to retrieve a customer from the databaseand update their name
customer = session.query(Customer).filter_by(id=1).first()
if customer:
    customer.name = "New Name"
    session.commit()    