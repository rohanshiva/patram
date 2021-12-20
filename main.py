from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from crawler import Crawler


app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/raw/{page}")
def raw_page_root(request: Request, page: str):
    crawler = Crawler()
    path = f"{page}"
    data = crawler.page_content(path)
    return data


@app.get("/raw/{dir}/{page}")
def raw_page(request: Request, dir: str, page: str):
    crawler = Crawler()
    path = f"{dir}/{page}"
    data = crawler.page_content(path)
    return data


@app.get("/")
def render_home(request: Request):
    return RedirectResponse("/intro")


@app.get("/{page}")
def render_page(request: Request, page: str):
    crawler = Crawler()
    path = f"/{page}"
    data = crawler.get_template_data(path)
    data["request"] = request
    f = open("logo.svg", "r")
    data["svg"] = f.read()
    return templates.TemplateResponse("index.html", data)


@app.get("/{dir}/{page}")
def render_page(request: Request, dir: str, page: str):
    crawler = Crawler()
    path = f"{dir}/{page}"
    data = crawler.get_template_data(path)
    data["request"] = request
    f = open("logo.svg", "r")
    data["svg"] = f.read()
    return templates.TemplateResponse("index.html", data)
