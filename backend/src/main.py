from fastapi import FastAPI, HTTPException
import boto3
from uuid import uuid1
from config import DB_REGION_NAME, DB_ENDPOINT_URL, AWS_PRIVATE_KEY, AWS_ACCESS_KEY_ID
from models import InfoOutputDto, CatOutputDto, CreateOutputDto, CatName

app = FastAPI()


@app.get("/")
async def root():
    return {"description": "Котобаза.", "type": "api"}


@app.get("/api/info", response_model=InfoOutputDto)
async def server_info():
    return {"backend_version": "0.0.1", "replica_id": "idk"}


@app.get("/api/cats", response_model=CatOutputDto)
async def names():
    ydb_docapi_client = boto3.resource('dynamodb',
                                       region_name=DB_REGION_NAME,
                                       endpoint_url=DB_ENDPOINT_URL,
                                       aws_access_key_id=AWS_ACCESS_KEY_ID,
                                       aws_secret_access_key=AWS_PRIVATE_KEY)
    table = ydb_docapi_client.Table('docapitest/catnames')
    response = table.scan()
    return {"cat_names": response["Items"], "count": response["Count"]}


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
    return {"created_id": name_id}
