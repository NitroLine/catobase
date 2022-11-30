import boto3
from config import DB_REGION_NAME, DB_ENDPOINT_URL, AWS_ACCESS_KEY_ID, AWS_PRIVATE_KEY


class FakeTable:
    table_status = "ALREADY ACTIVE"


def create_series_table():
    ydb_docapi_client = boto3.resource('dynamodb',
                                       region_name=DB_REGION_NAME,
                                       endpoint_url=DB_ENDPOINT_URL,
                                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                                       aws_secret_access_key=AWS_PRIVATE_KEY)
    try:
        ydb_docapi_client.create_table(
            TableName='docapitest/replica',  # Series — имя таблицы
            KeySchema=[
                {
                    'AttributeName': 'key',
                    'KeyType': 'HASH'  # Ключ партицирования
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'key',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'value',
                    'AttributeType': 'N'  # Строка
                },
            ]
        )
        ydb_docapi_client.create_table(
            TableName='docapitest/catnames',  # Series — имя таблицы
            KeySchema=[
                {
                    'AttributeName': 'name_id',
                    'KeyType': 'HASH'  # Ключ партицирования
                },
                {
                    'AttributeName': 'author',
                    'KeyType': 'RANGE'  # Ключ сортировки
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name_id',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'  # Строка
                },
                {
                    'AttributeName': 'author',
                    'AttributeType': 'S'  # Строка
                },
            ]
        )
    except ydb_docapi_client.meta.client.exceptions.ResourceInUseException:
        pass
    table = ydb_docapi_client.Table('docapitest/replica')
    table.put_item(
        Item={
            'key': 0,
            'value': 1,
        }
    )
    return table


if __name__ == '__main__':
    series_table = create_series_table()
    print("Table status:", series_table.table_status)
