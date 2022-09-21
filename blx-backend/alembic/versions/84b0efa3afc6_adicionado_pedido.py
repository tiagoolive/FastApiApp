"""Adicionado Pedido

Revision ID: 84b0efa3afc6
Revises: 56964c6dbec6
Create Date: 2022-09-21 10:01:46.081902

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84b0efa3afc6'
down_revision = '56964c6dbec6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pedido',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('local_entrega', sa.String(), nullable=True),
    sa.Column('tipo_entrega', sa.String(), nullable=True),
    sa.Column('observacao', sa.String(), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('produto_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['produto_id'], ['produto.id'], name='fk_pedido_produto'),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], name='fk_pedido_usuario'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_pedido_id'), ['id'], unique=False)

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pedido', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_pedido_id'))

    op.drop_table('pedido')
    # ### end Alembic commands ###
