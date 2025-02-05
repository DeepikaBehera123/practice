from typing import optional
from fastapi import FastAPI,Response,status,HTTPException

from fastapi.params import Body

from pydantic import BaseModel

from random import randrange

app = FastAPI()

class post(BaseModel):
    titel: str
    content:str
    published:bool = True
    rating:optional[int] = None

my_posts = [{"titel":"titei of post 1","content":"content of post 1","id":1},
            {"titel":"favorite food","content":"love pizza","id":2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
def find_index_post(id):
    for p in my_posts:
        if p['id'] == id:
            return i

@app.get("/")
def root():
    return{"message":"well come to my api"}

@app.get("/posts")
def get_posts():
    return{"date":my_posts}

@app.post("/createposts")
def ceate_posts():
    return{"message":"succesfully created"}
# how to fill from the path 


@app.post("/createposts")
def create_posts(post:post):
    post_dict = post.dict()
    post__dict["id"] = randrange(0,1000000)
    my_posts.appent()
    return{"date":post_dict}


@app.get("/posts/latest")
def get_latest_post():
    post = my_posts[len(my_posts)-1]
    return{"detail":post}



@app.get("/posts/{id}")
def get_post(id:int,Response:Response):
    post = find_post(id)
    if not post:
        Response.status_code = status.HTTP_404_NOT_FOUND
        return{'message':f"post with id:{id}was nt found"}
    
    return{"post_detail":post}
@app.delete("/posts/{id}")
def delete_post(id:int):
    #delete post
    #find the index in the arry that required id
    #my_post.pop(index)
    index = find_index_post(id)

    my_posts.pop(index)
    return{'message':'post was succesfully deleted'}












