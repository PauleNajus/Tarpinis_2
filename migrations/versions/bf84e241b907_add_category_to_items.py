"""Add category to Items

Revision ID: bf84e241b907
Revises: 35208eedc4fb
Create Date: 2024-06-27 10:43:39.216503

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf84e241b907'
down_revision = '35208eedc4fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(), nullable=False, server_default='default_category'))

    # Insert sample data in smaller chunks
    op.execute("""
        INSERT INTO "Products" (name, description, price, quantity, category) VALUES 
        ('Apple', 'Fresh red apples', 0.5, 100, 'Fruits'),
        ('Banana', 'Fresh yellow bananas', 0.3, 150, 'Fruits'),
        ('Carrot', 'Fresh orange carrots', 0.4, 200, 'Vegetables'),
        ('Broccoli', 'Fresh green broccoli', 0.8, 120, 'Vegetables'),
        ('Strawberry', 'Fresh red strawberries', 1.0, 50, 'Berries');
    """)
    op.execute("""
        INSERT INTO "Products" (name, description, price, quantity, category) VALUES 
        ('Blueberry', 'Fresh blueberries', 1.2, 60, 'Berries'),
        ('Chicken Breast', 'Fresh chicken breast', 3.5, 80, 'Meat'),
        ('Salmon Fillet', 'Fresh salmon fillet', 5.0, 70, 'Fish'),
        ('Milk', 'Fresh milk', 1.1, 90, 'Dairy'),
        ('Cheese', 'Fresh cheese', 2.5, 60, 'Dairy');
    """)
    op.execute("""
        INSERT INTO "Products" (name, description, price, quantity, category) VALUES 
        ('Yogurt', 'Fresh yogurt', 1.0, 100, 'Dairy'),
        ('Bread', 'Fresh bread', 1.5, 75, 'Bakery'),
        ('Croissant', 'Fresh croissant', 1.8, 80, 'Bakery'),
        ('Eggs', 'Fresh eggs', 2.0, 100, 'Dairy'),
        ('Tomato', 'Fresh tomatoes', 0.6, 150, 'Vegetables');
    """)
    op.execute("""
        INSERT INTO "Products" (name, description, price, quantity, category) VALUES 
        ('Cucumber', 'Fresh cucumbers', 0.5, 130, 'Vegetables'),
        ('Lettuce', 'Fresh lettuce', 0.7, 90, 'Vegetables'),
        ('Orange', 'Fresh oranges', 0.9, 110, 'Fruits'),
        ('Grapes', 'Fresh grapes', 2.2, 70, 'Fruits'),
        ('Avocado', 'Fresh avocados', 1.5, 60, 'Fruits');
    """)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('Products', schema=None) as batch_op:
        batch_op.drop_column('category')

    # Remove sample data
    op.execute("""
        DELETE FROM "Products" WHERE name IN (
            'Apple', 'Banana', 'Carrot', 'Broccoli', 'Strawberry', 'Blueberry', 
            'Chicken Breast', 'Salmon Fillet', 'Milk', 'Cheese', 'Yogurt', 
            'Bread', 'Croissant', 'Eggs', 'Tomato', 'Cucumber', 'Lettuce', 
            'Orange', 'Grapes', 'Avocado'
        );
    """)
    # ### end Alembic commands ###