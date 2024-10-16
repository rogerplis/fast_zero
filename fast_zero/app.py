from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserSchema

app = FastAPI()


@app.get('/', response_model=Message, status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Hello World'}


@app.post('/users/', response_model=UserSchema, status_code=HTTPStatus.CREATED)
def create_user(user: UserSchema):
    return user