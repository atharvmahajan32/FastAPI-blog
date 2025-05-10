from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional



app = FastAPI()

class Blog(BaseModel):
    id: int
    title: str
    Content: str
    published: Optional[bool] = Field(default=None)

@app.get('/')
def get_root():
    return { 'person_1' : {
        'name' : 'atharv',
        'lastname' : 'mahajan'
    },
    'person_2' : {
        'name' : 'kartikey',
        'lastname' : 'gupta'
    },
    'person_3+4' : {
        'name' : 'samyak',
        'lastname' : 'jain'
    }
      }

@app.get('/blog')
def get_blogs(limit : int = 10, published : bool = True, sort: Optional[str] = None):
    if published:
        status = 'Published'
    else:
        status = 'Unpublished'

    return {'data' : f'{limit} blogs with {status} status'}


@app.get('/blog/{id}')
def get_specific_blog(id : int):
    return {'data' : id} 


@app.get('/blog/{id}/comments')
def get_comments(id : int):
    return { f'comments for {id}': {'comment_1', 'comment_2'}}


@app.post('/blog')
def create_blog( request : Blog):
    return {'data': f'the created blog has the title {request.title} and has the content {request.Content}' }