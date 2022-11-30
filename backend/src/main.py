from fastapi import FastAPI, HTTPException
import boto3
from uuid import uuid1
from config import DB_REGION_NAME, DB_ENDPOINT_URL, AWS_PRIVATE_KEY, AWS_ACCESS_KEY_ID, BACKEND_VERSION
from models import InfoOutputDto, CatOutputDto, CreateOutputDto, CatName

app = FastAPI()

ydb_docapi_client = boto3.resource('dynamodb',
                                   region_name=DB_REGION_NAME,
                                   endpoint_url=DB_ENDPOINT_URL,
                                   aws_access_key_id=AWS_ACCESS_KEY_ID,
                                   aws_secret_access_key=AWS_PRIVATE_KEY)

table = ydb_docapi_client.Table('docapitest/replica')
response = table.update_item(Key={'key': 0},
                             ReturnValues="UPDATED_NEW",
                             ExpressionAttributeValues={":inc": 1},
                             UpdateExpression='ADD value :inc',)
replica_id = response['Attributes'].get('value', 0)

@app.get("/")
async def root():
    return {"description": "Котобаза.", "type": "api"}


@app.get("/api/info", response_model=InfoOutputDto)
async def server_info():
    return {"backend_version": BACKEND_VERSION, "replica_id": replica_id}


@app.get("/api/cats", response_model=CatOutputDto)
async def names():
    ydb_docapi_client = boto3.resource('dynamodb',
                                       region_name=DB_REGION_NAME,
                                       endpoint_url=DB_ENDPOINT_URL,
                                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                                       aws_secret_access_key=AWS_PRIVATE_KEY)
    table = ydb_docapi_client.Table('docapitest/catnames')
    items = []
    scan_kwargs = {}
    done = False
    start_key = None
    response = {}
    while not done:
        if start_key:
            scan_kwargs['ExclusiveStartKey'] = start_key
        response = table.scan(**scan_kwargs)
        items += response.get('Items', [])
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None
    return {"cat_names": items, "count": response.get("Count", 0)}


@app.post("/api/cats", response_model=CreateOutputDto)
async def name_add(cat: CatName):
    ydb_docapi_client = boto3.resource('dynamodb',
                                       region_name=DB_REGION_NAME,
                                       endpoint_url=DB_ENDPOINT_URL,
                                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                                       aws_secret_access_key=AWS_PRIVATE_KEY)
    table = ydb_docapi_client.Table('docapitest/catnames')
    name_id = uuid1().hex
    table.put_item(
        Item={
            'name_id': name_id,
            'name': cat.name,
            'author': cat.author
        }
    )
    return {"created_id": name_id, "replica_id": replica_id, "backend_version": BACKEND_VERSION}
