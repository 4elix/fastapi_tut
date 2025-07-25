from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()


@app.get('/')
async def home() -> dict[str, str]:
    return {'data': 'message'}


@app.get('/contacts')
async def contacts() -> int:
    return 33


posts = [
    {'id': 1, 'title': 'News 1', 'body': 'Text 1'},
    {'id': 2, 'title': 'News 2', 'body': 'Text 2'},
    {'id': 3, 'title': 'News 3', 'body': 'Text 3'},
    {'id': 4, 'title': 'News 4', 'body': 'Text 4'},
    {'id': 5, 'title': 'News 5', 'body': 'Text 5'},
    {'id': 6, 'title': 'News 6', 'body': 'Text 6'},
]


@app.get('/items')  # http://127.0.0.1:8000/items
async def get_items() -> list:
    return posts


@app.get('/item/{id}')  # http://127.0.0.1:8000/item/1
async def get_item(id: int) -> dict:
    for post in posts:
        if post['id'] == id:
            return post

    raise HTTPException(status_code=404, detail='Post not found')


@app.get('/search')  # http://127.0.0.1:8000/search?post_id=2
async def search(post_id: Optional[int] = None) -> dict:
    if post_id:
        for post in posts:
            if post['id'] == post_id:
                return post
        raise HTTPException(status_code=404, detail='Post not found')
    else:
        return {'data': 'Not post id provided'}
