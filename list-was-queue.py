import boto.sqs
import boto.sqs.queue
from boto.sqs.message import Message
from boto.sqs.connection import SQSConnection
from boto.exception import SQSError

conn = boto.sqs.connect_to_region("us-east-1", aws_access_key_id='AKIAJ2BJXBF74J
PNZKCQ', aws_secret_access_key='mJyTlfZ+ZnDp5oe1tief0KpSqlUg52pIh4Fz2bOd')

rs = conn.get_all_queues()
for q in rs:
        print q.id

#irland is in eu-west-1 region
myconn = boto.sqs.connect_to_region("eu-west-1", aws_access_key_id='AKIAJ2BJXBF7
4JPNZKCQ', aws_secret_access_key='mJyTlfZ+ZnDp5oe1tief0KpSqlUg52pIh4Fz2bOd')

rs = myconn.get_all_queues()
for q in rs:
        print q.id