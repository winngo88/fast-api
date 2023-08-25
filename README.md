# FastAPI BASIC
![Image not found](media/schema.png?raw=true "From Amigoscode channel")
## Insstallation
- Install FastAPI  
    ```
    pip install fastapi
    ```
- Install Uvicorn server ([an Asynchronous Server Gateway Interface - ASGI](https://asgi.readthedocs.io/en/latest/))  
    ```
    pip install "uvicorn[standard]"
    ```

## Run server  
```
uvicorn main:app --reload #main is module, app is an instance of FastAPI
```

## How to user
### GET
```
@app.get("</api/version/object_want_to_get>")
async def func_get_name():
    <...>
```
### POST
```
@app.post("</app/version/object_want_to_post>")
async def fun_post_name(para: ObjectType):
    <...>
```
### DELETE
```
@app.delete("</app/version/object_want_to_delete/{conditon_para}>")
async def fun_delete_name(condition_para: ParaType):
    if condition_para == <...>:
        <...>
```

## [HTTP response status codes indicate](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
!["HTTP Response Status Codes"](media/http_status_codes.png?raw=true "HTTP Response Codes")
## Notes 
- Practice makes perfect :smiley:

## Tham khảo
https://www.youtube.com/watch?v=GN6ICac3OXY