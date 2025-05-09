from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_root():
    return { 'person_1' : {
        'name' : 'atharv',
        'lastname' : 'mahajan'
    },
    'person_2' : {
        'name' : 'kartikey',
        'lastname' : 'gupta'
    }
      }

@app.get('/blog')
def get_blogs(limit : int = 10, published : bool = True):
    if published:
        status = 'Published'
    else:
        status = 'Unpublished'

    return {'data' : f'{limit} blogs with {status} status'}


@app.get('/blog/{id}')
def get_blog(id : int):
    return {'data' : id} 


@app.get('/blog/{id}/comments')
def get_comments(id : int):
    return { f'comments for {id}': {'comment_1', 'comment_2'}}