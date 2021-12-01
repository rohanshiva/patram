# My First Experiment

Blah blah



check it out


what are we talking about


damn

# Getting Started

The frontend is a Svelte app that is served by a FastAPI server.

Simply look at the `[main.py](http://main.py)` file and notice there are two additional frontend specific code blocks:

```jsx
app.mount("/svelte", StaticFiles(directory="svelte/public", html=True), name="build")
```

This line mounts the Svelte app statically under the `/svelte` route.

```jsx
@app.get("/{full_path:path}")
def render_svelte(request: Request, full_path: str):
    return FileResponse("svelte/public/index.html")
```

This last route, at the bottom of the router ensures that when any route is visited, e.g. `/experiment/1234` that the `index.html` file is rendered and the Svelte app will take care of routing on the frontend.

The rest of the logic is just dummy routes made to emulate the backend you have.

# Local Development

To make changes to the app locally, you will do so in the context of a FastAPI server using uvicorn.

Create a virtual environment in the root directory locally `python3 -m venv .venv`.

Activate this vitrual environment with `source .venv/bin/activate`.

Install the dependencies for the virtual environment with `pip install -r requirements.txt`.

To make changes to the frontend, enter the `svelte` directory and start the development server with `npm run dev`. (You may need to run `npm run i` first).

Finally, serve the svelte frontend with uvicorn using `uvicorn main:app --reload` from the root directory.

Change something in any Svelte file (or in the backend) and the app should automatically reload.

# Deployment

When you are ready to push the app to production in a Deta Micro, use the following steps:

- Build the frontend from within the `svelte` directory by running `npm run build`
- Deploy the entire application from the root app directory with `deta new` . (Make sure you have the `.detaignore` file).
