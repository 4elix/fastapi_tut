from fastapi import FastAPI, HTTPException
from typing import Optional, List, Dict
from pydantic import BaseModel

app = FastAPI()


class User(BaseModel):
    id: int
    name: str
    age: int


class Post(BaseModel):
    id: int
    title: str
    body: str
    author: User


class PostCreate(BaseModel):
    title: str
    body: str
    author_id: int


users = [
    {'id': 1, 'name': 'Jon', 'age': 28},
    {'id': 2, 'name': 'Alex', 'age': 25},
    {'id': 3, 'name': 'Sten', 'age': 31},
]

posts = [
    {'id': 1, 'title': 'News 1', 'body': 'Text 1', 'author': users[0]},
    {'id': 2, 'title': 'News 2', 'body': 'Text 2', 'author': users[0]},
    {'id': 3, 'title': 'News 3', 'body': 'Text 3', 'author': users[1]},
    {'id': 4, 'title': 'News 4', 'body': 'Text 4', 'author': users[1]},
    {'id': 5, 'title': 'News 5', 'body': 'Text 5', 'author': users[2]},
    {'id': 6, 'title': 'News 6', 'body': 'Text 6', 'author': users[2]},
]


# @app.get('/items')  # http://127.0.0.1:8000/items
# async def get_items() -> List[Post]:
#     post_objects = []
#     for post in posts:
#         post_objects.append(Post(id=post['id'], title=post['title'], body=post['body']))
#
#     return post_objects


@app.get('/items')
async def get_items() -> List[Post]:
    return [Post(**post) for post in posts]


@app.get('/item/{id}')  # http://127.0.0.1:8000/item/1
async def get_item(id: int) -> Post:
    for post in posts:
        if post['id'] == id:
            return Post(**post)

    raise HTTPException(status_code=404, detail='Post not found')


@app.get('/search')  # http://127.0.0.1:8000/search?post_id=2
async def search(post_id: Optional[int] = None) -> Dict[str, Optional[Post]]:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return {'data': Post(**post)}
        raise HTTPException(status_code=404, detail='Post not found')
    else:
        return {'data': None}


@app.post('/items/add')
async def add_item(post: PostCreate) -> Post:
    author = next((user for user in users if user['id'] == post.author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail='User not found')

    new_post_id = len(posts) + 1
    new_post = {
        'id': new_post_id,
        'title': post.title,
        'body': post.body,
        'author': author
    }
    posts.append(new_post)

    return Post(**new_post)