"""jooj

Revision ID: 259f8e025057
Revises: d90bdbc5b549
Create Date: 2022-09-09 15:55:05.496379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '259f8e025057'
down_revision = 'd90bdbc5b549'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produto', sa.Column('jooj', sa.String(), nullable=True))
    op.add_column('produto', sa.Column('usuario_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'produto', 'usuario', ['usuario_id'], ['id'])
    op.drop_column('produto', 'tamanhos')
    op.add_column('usuario', sa.Column('senha', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'senha')
    op.add_column('produto', sa.Column('tamanhos', sa.VARCHAR(), nullable=True))
    op.drop_constraint(None, 'produto', type_='foreignkey')
    op.drop_column('produto', 'usuario_id')
    op.drop_column('produto', 'jooj')
    # ### end Alembic commands ###
