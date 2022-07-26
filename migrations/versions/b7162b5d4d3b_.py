"""empty message

Revision ID: b7162b5d4d3b
Revises: bb2df01d9bb6
Create Date: 2022-07-26 12:39:39.623189

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b7162b5d4d3b'
down_revision = 'bb2df01d9bb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_current_auction_datetime', table_name='current_auction')
    op.drop_table('current_auction')
    op.drop_index('ix_auction_datetime', table_name='auction')
    op.drop_table('auction')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auction',
    sa.Column('aid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('sellerName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('cropName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('sellerId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('cropId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('variety', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('minPrice', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('datetime', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['cropId'], ['crops.cropId'], name='auction_ibfk_1'),
    sa.ForeignKeyConstraint(['sellerId'], ['user.uid'], name='auction_ibfk_2'),
    sa.PrimaryKeyConstraint('aid'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_auction_datetime', 'auction', ['datetime'], unique=False)
    op.create_table('current_auction',
    sa.Column('aid', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('sellerName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('cropName', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('sellerId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('cropId', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('variety', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('minPrice', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('datetime', mysql.DATETIME(), nullable=False),
    sa.ForeignKeyConstraint(['cropId'], ['crops.cropId'], name='current_auction_ibfk_1'),
    sa.ForeignKeyConstraint(['sellerId'], ['user.uid'], name='current_auction_ibfk_2'),
    sa.PrimaryKeyConstraint('aid'),
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_current_auction_datetime', 'current_auction', ['datetime'], unique=False)
    # ### end Alembic commands ###
