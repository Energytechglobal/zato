"""migrate_from_411a1ddb_to_5a7b9403

Revision ID: 00ad4c118b99
Revises: 0028a_934259d2a3b7
Create Date: 2017-12-14 15:29:40.477831

"""

# Revision identifiers, used by Alembic.
revision = '0031_00ad4c118b99'
down_revision = '0030_0d1ac9c22670'

from alembic import context, op
import sqlalchemy as sa

# Zato
from zato.common.odb import model

# Pass this as a naming_convention= kwarg to batch_alter_table() in order to
# resolve unnamed constraint exceptions with SQLite. This is the default
# format used by PostgreSQL, it is likely if there are other databases to
# be supported, we will need to mimic their default naming behaviour by
# dynamically switching this at runtime, according to the driver in use.
naming_convention = {
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
}

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sms_twilio',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_internal', sa.Boolean(), nullable=False),
    sa.Column('account_sid', sa.String(length=200), nullable=False),
    sa.Column('auth_token', sa.String(length=200), nullable=False),
    sa.Column('default_from', sa.String(length=200), nullable=True),
    sa.Column('default_to', sa.String(length=200), nullable=True),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], [u'cluster.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'cluster_id')
    )
    op.create_table('cache',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_default', sa.Boolean(), nullable=False),
    sa.Column('cache_type', sa.String(length=45), nullable=False),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], [u'cluster.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'cluster_id')
    )
    op.create_table('cache_builtin',
    sa.Column('cache_id', sa.Integer(), nullable=False),
    sa.Column('max_size', sa.Integer(), nullable=False),
    sa.Column('max_item_size', sa.Integer(), nullable=False),
    sa.Column('extend_expiry_on_get', sa.Boolean(), nullable=False),
    sa.Column('extend_expiry_on_set', sa.Boolean(), nullable=False),
    sa.Column('sync_method', sa.String(length=20), nullable=False),
    sa.Column('persistent_storage', sa.String(length=40), nullable=False),
    sa.ForeignKeyConstraint(['cache_id'], [u'cache.id'], ),
    sa.PrimaryKeyConstraint('cache_id')
    )
    op.create_table('cache_memcached',
    sa.Column('cache_id', sa.Integer(), nullable=False),
    sa.Column('servers', sa.Text(), nullable=False),
    sa.Column('is_debug', sa.Boolean(), nullable=False),
    sa.Column('extra', sa.LargeBinary(length=20000), nullable=True),
    sa.ForeignKeyConstraint(['cache_id'], [u'cache.id'], ),
    sa.PrimaryKeyConstraint('cache_id')
    )
    op.create_table('pubsub_topic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_internal', sa.Boolean(), nullable=False),
    sa.Column('last_pub_time', sa.BigInteger(), nullable=True),
    sa.Column('max_depth_gd', sa.Integer(), nullable=False),
    sa.Column('max_depth_non_gd', sa.Integer(), nullable=False),
    sa.Column('current_depth_gd', sa.Integer(), nullable=False),
    sa.Column('gd_depth_check_freq', sa.Integer(), nullable=False),
    sa.Column('has_gd', sa.Boolean(), nullable=False),
    sa.Column('is_api_sub_allowed', sa.Boolean(), nullable=False),
    sa.Column('hook_service_id', sa.Integer(), nullable=True),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], [u'cluster.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['hook_service_id'], [u'service.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pubsub_topic', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.create_index('pubsb_tp_clust_idx', ['cluster_id'], unique=False)
        batch_op.create_index('pubsb_tp_id_idx', ['cluster_id', 'id'], unique=True)
        batch_op.create_index('pubsb_tp_name_idx', ['cluster_id', 'name'], unique=True)

    op.create_table('pubsub_endpoint',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('is_internal', sa.Boolean(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('endpoint_type', sa.String(length=40), nullable=False),
    sa.Column('last_seen', sa.BigInteger(), nullable=True),
    sa.Column('last_pub_time', sa.BigInteger(), nullable=True),
    sa.Column('last_sub_time', sa.BigInteger(), nullable=True),
    sa.Column('last_deliv_time', sa.BigInteger(), nullable=True),
    sa.Column('role', sa.String(length=40), nullable=False),
    sa.Column('tags', sa.Text(), nullable=True),
    sa.Column('topic_patterns', sa.Text(), nullable=True),
    sa.Column('pub_tag_patterns', sa.Text(), nullable=True),
    sa.Column('message_tag_patterns', sa.Text(), nullable=True),
    sa.Column('service_id', sa.Integer(), nullable=True),
    sa.Column('security_id', sa.Integer(), nullable=True),
    sa.Column('ws_channel_id', sa.Integer(), nullable=True),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], [u'cluster.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['security_id'], [u'sec_base.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['service_id'], [u'service.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['ws_channel_id'], [u'channel_web_socket.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cluster_id', 'name'),
    sa.UniqueConstraint('cluster_id', 'security_id'),
    sa.UniqueConstraint('cluster_id', 'service_id'),
    sa.UniqueConstraint('cluster_id', 'ws_channel_id')
    )
    with op.batch_alter_table('pubsub_endpoint', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.create_index('pubsb_endp_clust_idx', ['cluster_id'], unique=False)
        batch_op.create_index('pubsb_endp_id_idx', ['cluster_id', 'id'], unique=True)
        batch_op.create_index('pubsb_endp_name_idx', ['cluster_id', 'name'], unique=True)

    op.create_table('pubsub_sub',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('is_internal', sa.Boolean(), nullable=False),
    sa.Column('creation_time', sa.BigInteger(), nullable=False),
    sa.Column('sub_key', sa.String(length=200), nullable=False),
    sa.Column('pattern_matched', sa.Text(), nullable=False),
    sa.Column('deliver_by', sa.Text(), nullable=True),
    sa.Column('ext_client_id', sa.Text(), nullable=True),
    sa.Column('is_durable', sa.Boolean(), nullable=False),
    sa.Column('has_gd', sa.Boolean(), nullable=False),
    sa.Column('active_status', sa.String(length=200), nullable=False),
    sa.Column('is_staging_enabled', sa.Boolean(), nullable=False),
    sa.Column('delivery_method', sa.String(length=200), nullable=False),
    sa.Column('delivery_data_format', sa.String(length=200), nullable=False),
    sa.Column('delivery_endpoint', sa.Text(), nullable=True),
    sa.Column('last_interaction_time', sa.BigInteger(), nullable=True),
    sa.Column('last_interaction_type', sa.String(length=200), nullable=True),
    sa.Column('last_interaction_details', sa.Text(), nullable=True),
    sa.Column('delivery_batch_size', sa.Integer(), nullable=False),
    sa.Column('wrap_one_msg_in_list', sa.Boolean(), nullable=False),
    sa.Column('delivery_max_size', sa.Integer(), nullable=False),
    sa.Column('delivery_max_retry', sa.Integer(), nullable=False),
    sa.Column('delivery_err_should_block', sa.Boolean(), nullable=False),
    sa.Column('wait_sock_err', sa.Integer(), nullable=False),
    sa.Column('wait_non_sock_err', sa.Integer(), nullable=False),
    sa.Column('hook_service_id', sa.Integer(), nullable=True),
    sa.Column('out_http_method', sa.Text(), nullable=True),
    sa.Column('amqp_exchange', sa.Text(), nullable=True),
    sa.Column('amqp_routing_key', sa.Text(), nullable=True),
    sa.Column('files_directory_list', sa.Text(), nullable=True),
    sa.Column('ftp_directory_list', sa.Text(), nullable=True),
    sa.Column('sms_twilio_from', sa.Text(), nullable=True),
    sa.Column('sms_twilio_to_list', sa.Text(), nullable=True),
    sa.Column('smtp_subject', sa.Text(), nullable=True),
    sa.Column('smtp_from', sa.Text(), nullable=True),
    sa.Column('smtp_to_list', sa.Text(), nullable=True),
    sa.Column('smtp_body', sa.Text(), nullable=True),
    sa.Column('smtp_is_html', sa.Boolean(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('endpoint_id', sa.Integer(), nullable=True),
    sa.Column('out_job_id', sa.Integer(), nullable=True),
    sa.Column('out_http_soap_id', sa.Integer(), nullable=True),
    sa.Column('out_smtp_id', sa.Integer(), nullable=True),
    sa.Column('out_amqp_id', sa.Integer(), nullable=True),
    sa.Column('ws_sub_id', sa.Integer(), nullable=True),
    sa.Column('ws_channel_id', sa.Integer(), nullable=True),
    sa.Column('server_id', sa.Integer(), nullable=True),
    sa.Column('cluster_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cluster_id'], [u'cluster.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['endpoint_id'], [u'pubsub_endpoint.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['hook_service_id'], [u'service.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['out_amqp_id'], [u'out_amqp.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['out_http_soap_id'], [u'http_soap.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['out_job_id'], [u'job.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['out_smtp_id'], [u'email_smtp.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['server_id'], [u'server.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['topic_id'], [u'pubsub_topic.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['ws_channel_id'], [u'channel_web_socket.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['ws_sub_id'], [u'web_socket_sub.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pubsub_sub', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.create_index('pubsb_sub_clust_endpt_idx', ['cluster_id', 'endpoint_id', 'topic_id'], unique=False)
        batch_op.create_index('pubsb_sub_clust_idx', ['cluster_id'], unique=False)
        batch_op.create_index('pubsb_sub_clust_subk', ['cluster_id', 'sub_key'], unique=True)
        batch_op.create_index('pubsb_sub_id_idx', ['cluster_id', 'id'], unique=True)

    op.create_table('pubsub_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pub_msg_id', sa.String(length=200), nullable=False),
    sa.Column('pub_correl_id', sa.String(length=200), nullable=True),
    sa.Column('in_reply_to', sa.String(length=200), nullable=True),
    sa.Column('ext_client_id', sa.Text(), nullable=True),
    sa.Column('group_id', sa.Text(), nullable=True),
    sa.Column('position_in_group', sa.Integer(), nullable=True),
    sa.Column('pattern_matched', sa.Text(), nullable=False),
    sa.Column('pub_time', sa.BigInteger(), nullable=False),
    sa.Column('ext_pub_time', sa.BigInteger(), nullable=True),
    sa.Column('expiration_time', sa.BigInteger(), nullable=True),
    sa.Column('last_updated', sa.BigInteger(), nullable=True),
    sa.Column('data', sa.Text(), nullable=False),
    sa.Column('data_prefix', sa.Text(), nullable=False),
    sa.Column('data_prefix_short', sa.String(length=200), nullable=False),
    sa.Column('data_format', sa.String(length=200), nullable=False),
    sa.Column('mime_type', sa.String(length=200), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('priority', sa.Integer(), nullable=False),
    sa.Column('expiration', sa.Integer(), nullable=False),
    sa.Column('has_gd', sa.Boolean(), nullable=False),
    sa.Column('published_by_id', sa.Integer(), nullable=False),
    sa.Column('topic_id', sa.Integer(), nullable=True),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], [u'cluster.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['published_by_id'], [u'pubsub_endpoint.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['topic_id'], [u'pubsub_topic.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pubsub_message', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.create_index('pubsb_msg_id_idx', ['cluster_id', 'id'], unique=True)
        batch_op.create_index('pubsb_msg_inreplyto_id_idx', ['cluster_id', 'in_reply_to'], unique=False)
        batch_op.create_index('pubsb_msg_pubmsg_id_idx', ['cluster_id', 'pub_msg_id'], unique=True)

    op.create_table('web_socket_cli_ps_keys',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('sub_key', sa.Text(), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], [u'web_socket_client.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['cluster_id'], [u'cluster.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('web_socket_cli_ps_keys', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.create_index('wscl_psk_cli', ['cluster_id', 'client_id'], unique=False)
        batch_op.create_index('wscl_psk_sk', ['cluster_id', 'sub_key'], unique=False)

    op.create_table('pubsub_endp_topic',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('pattern_matched', sa.Text(), nullable=False),
    sa.Column('last_pub_time', sa.BigInteger(), nullable=False),
    sa.Column('pub_msg_id', sa.String(length=200), nullable=False),
    sa.Column('pub_correl_id', sa.String(length=200), nullable=True),
    sa.Column('in_reply_to', sa.String(length=200), nullable=True),
    sa.Column('ext_client_id', sa.Text(), nullable=True),
    sa.Column('endpoint_id', sa.Integer(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], [u'cluster.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['endpoint_id'], [u'pubsub_endpoint.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['topic_id'], [u'pubsub_topic.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pubsub_endp_topic', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.create_index('pubsb_endpt_clsendtp_idx', ['cluster_id', 'endpoint_id', 'topic_id'], unique=True)
        batch_op.create_index('pubsb_endpt_clust_idx', ['cluster_id'], unique=False)
        batch_op.create_index('pubsb_endpt_id_idx', ['cluster_id', 'id'], unique=True)
        batch_op.create_index('pubsb_endpt_msgid_idx', ['cluster_id', 'pub_msg_id'], unique=True)

    op.create_table('pubsub_endp_msg_queue',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('creation_time', sa.BigInteger(), nullable=False),
    sa.Column('delivery_count', sa.Integer(), nullable=False),
    sa.Column('last_delivery_time', sa.BigInteger(), nullable=True),
    sa.Column('has_gd', sa.Boolean(), nullable=False),
    sa.Column('is_in_staging', sa.Boolean(), nullable=False),
    sa.Column('is_deliverable', sa.Boolean(), nullable=False),
    sa.Column('delivery_status', sa.Text(), nullable=False),
    sa.Column('delivery_time', sa.BigInteger(), nullable=True),
    sa.Column('pub_msg_id', sa.String(length=200), nullable=False),
    sa.Column('endpoint_id', sa.Integer(), nullable=True),
    sa.Column('topic_id', sa.Integer(), nullable=False),
    sa.Column('subscription_id', sa.Integer(), nullable=True),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id', 'pub_msg_id'], [u'pubsub_message.cluster_id', u'pubsub_message.pub_msg_id'], ondelete=u'CASCADE', name='pubsub_enms_msg_fkey'),
    sa.ForeignKeyConstraint(['cluster_id'], [u'cluster.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['endpoint_id'], [u'pubsub_endpoint.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['subscription_id'], [u'pubsub_sub.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['topic_id'], [u'pubsub_topic.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pubsub_endp_msg_queue', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.create_index('pubsb_enms_q_endp_idx', ['cluster_id', 'endpoint_id'], unique=False)
        batch_op.create_index('pubsb_enms_q_endptp_idx', ['cluster_id', 'endpoint_id', 'topic_id'], unique=False)
        batch_op.create_index('pubsb_enms_q_id_idx', ['cluster_id', 'id'], unique=True)
        batch_op.create_index('pubsb_enms_q_pubmid_idx', ['cluster_id', 'pub_msg_id'], unique=True)
        batch_op.create_index('pubsb_enms_q_subs_idx', ['cluster_id', 'subscription_id'], unique=False)

    op.create_table('pubsub_endp_msg_q_inter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entry_timestamp', sa.BigInteger(), nullable=False),
    sa.Column('inter_type', sa.String(length=200), nullable=False),
    sa.Column('inter_details', sa.Text(), nullable=True),
    sa.Column('queue_id', sa.Integer(), nullable=False),
    sa.Column('cluster_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cluster_id'], [u'cluster.id'], ondelete=u'CASCADE'),
    sa.ForeignKeyConstraint(['queue_id'], [u'pubsub_endp_msg_queue.id'], ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('pubsub_endp_msg_q_inter', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.create_index('pubsb_enms_qi_endptp_idx', ['cluster_id', 'queue_id'], unique=False)
        batch_op.create_index('pubsb_enms_qi_id_idx', ['cluster_id', 'id'], unique=True)

    op.drop_table('delivery_payload')
    op.drop_table('delivery_history')
    op.drop_table('delivery_def_out_wmq')
    op.drop_table('delivery')
    op.drop_table('delivery_def_base')
    op.drop_table('pub_sub_consumer')
    op.drop_table('pub_sub_producer')
    op.drop_table('pub_sub_topic')

    with op.batch_alter_table('http_soap', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.add_column(sa.Column('cache_expiry', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('cache_id', sa.Integer(), nullable=True))
        batch_op.create_index('path_host_conn_act_clus_idx', ['url_path', 'host', 'connection', 'soap_action', 'cluster_id'], unique=True)
        batch_op.create_foreign_key('http_soap_cache_id_fkey', 'cache', ['cache_id'], ['id'], ondelete=u'CASCADE')

    with op.batch_alter_table('web_socket_client', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.add_column(sa.Column('cluster_id', sa.Integer(), nullable=False))
        batch_op.drop_index('wscl_cli_ext_i_idx')
        batch_op.create_index('wscl_cli_ext_i_idx', ['cluster_id', 'ext_client_id'], unique=False)
        batch_op.drop_index('wscl_cli_ext_n_idx')
        batch_op.create_index('wscl_cli_ext_n_idx', ['cluster_id', 'ext_client_name'], unique=False)
        batch_op.drop_index('wscl_pr_addr_idx')
        batch_op.create_index('wscl_pr_addr_idx', ['cluster_id', 'peer_address'], unique=False)
        batch_op.drop_index('wscl_pr_fqdn_idx')
        batch_op.create_index('wscl_pr_fqdn_idx', ['cluster_id', 'peer_fqdn'], unique=False)
        batch_op.drop_index('wscl_pub_client_idx')
        batch_op.create_index('wscl_pub_client_idx', ['cluster_id', 'pub_client_id'], unique=True)
        batch_op.create_foreign_key('web_socket_client_cluster_id_fkey', 'cluster', ['cluster_id'], ['id'], ondelete=u'CASCADE')

    with op.batch_alter_table('web_socket_sub', schema=None, naming_convention=naming_convention) as batch_op:
        batch_op.add_column(sa.Column('cluster_id', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('ext_client_id', sa.Text(), nullable=False))
        batch_op.add_column(sa.Column('sub_key', sa.Text(), nullable=False))
        batch_op.create_index('wssub_extcli_idx', ['cluster_id', 'ext_client_id'], unique=True)
        batch_op.create_index('wssub_subkey_chan_idx', ['cluster_id', 'sub_key', 'channel_id'], unique=True)
        batch_op.create_index('wssub_subkey_idx', ['cluster_id', 'sub_key'], unique=True)
        batch_op.drop_index('wssub_channel_idx')
        batch_op.create_index('wssub_channel_idx', ['cluster_id', 'channel_id'], unique=False)
        batch_op.drop_index('wssub_patt_idx')
        batch_op.drop_index('wssub_patt_is_idx')
        batch_op.drop_constraint('web_socket_sub_server_id_fkey', type_='foreignkey')
        batch_op.drop_constraint('web_socket_sub_client_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key('web_socket_sub_cluster_id_fkey', 'cluster', ['cluster_id'], ['id'], ondelete=u'CASCADE')
        batch_op.drop_column('is_durable')
        batch_op.drop_column('has_gd')
        batch_op.drop_column('is_by_channel')
        batch_op.drop_column('pattern')
        batch_op.drop_column('server_id')
        batch_op.drop_column('client_id')
        batch_op.drop_column('is_by_ext_id')


def downgrade():
    raise NotImplementedError
