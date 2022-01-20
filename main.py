from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from crawler import Crawler


app = FastAPI()
templates = Jinja2Templates(directory="templates")


async def handle_render(request: Request, page = None):
    crawler = Crawler()
    await crawler.setup()
    path = f"{page}" if page else None
    data = crawler.get_template_data(path)
    data["request"] = request
    return templates.TemplateResponse("index.html", data)

@app.get("/favicon.ico")
def render_svg():
    f = open("logo.svg", "r")
    svg = f.read()
    return svg

@app.get("/raw/{page}")
async def raw_page_root(request: Request, page: str):
    crawler = Crawler()
    await crawler.setup()
    path = f"{page}"
    data = crawler.page_content(path)
    return data


@app.get("/raw/{dir}/{page}")
async def raw_page(request: Request, dir: str, page: str):
    crawler = Crawler()
    await crawler.setup()
    path = f"{dir}/{page}"
    print(path)
    data = crawler.page_content(path)
    return data

@app.get("/")
async def render_default(request: Request):
    return await handle_render(request)

@app.get("/{page}")
async def render_page(request: Request, page: str):
    return await handle_render(request, page)


@app.get("/{dir}/{page}")
async def render_page(request: Request, dir: str, page: str):
    path = f"{dir}/{page}"
    print(path)
    return await handle_render(request, path)
