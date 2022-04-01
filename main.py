from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from crawler import Crawler


app = FastAPI()

app.mount("/favicons", StaticFiles(directory="favicons"), name="favicons")
app.mount("/images", StaticFiles(directory="images"), name="images")

templates = Jinja2Templates(directory="templates")


async def handle_render(request: Request, page=None):
    crawler = Crawler()
    await crawler.setup()
    path = f"{page}" if page else None

    try:
        data = crawler.get_template_data(path)
        data["request"] = request
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

    return templates.TemplateResponse("index.html", data)


async def handle_raw_request(request: Request, page=None):
    crawler = Crawler()
    await crawler.setup()
    path = f"{page}" if page else None

    try:
        data = crawler.page_content(path)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

    return data


@app.get("/raw/{page}")
async def raw_page_root(request: Request, page: str):
    return await handle_raw_request(request, page)


@app.get("/raw/{dir}/{page}")
async def raw_page(request: Request, dir: str, page: str):
    path = f"{dir}/{page}"
    return await handle_raw_request(request, path)


@app.get("/")
async def render_default(request: Request):
    return await handle_render(request)


@app.get("/{page}")
async def render_page(request: Request, page: str):
    return await handle_render(request, page)


@app.get("/{dir}/{page}")
async def render_page(request: Request, dir: str, page: str):
    path = f"{dir}/{page}"
    return await handle_render(request, path)
