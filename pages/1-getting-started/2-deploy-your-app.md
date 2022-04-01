# Deploy your app

[Install the Deta CLI](https://docs.deta.sh/docs/micros/getting_started#configuring--installing-the-deta-cli)

## Logging in to Deta via the CLI
Once you've sucessfully installed the CLI, you need to login to Deta.

From a Terminal, type `deta login` 

This command will open your browser and authenticate your CLI through Deta's web application.

Upon a successful login, you are ready to start building Micros.

## Creating your micro for Patram
To create a micro, navigate to your root project dir.
```bash
cd patram
```
Now, run the following command to create a new Python Micro.
```bash
deta new --python patram
```
The CLI should respond with something like this:
```
{
    "name": "patram",
    "runtime": "python3.7",
    "endpoint": "https://<path>.deta.dev",
    "visor": "enabled",
    "http_auth": "enabled"
}
```
Visit the endpoint and your site is now deployed! 🎉

## Updating your app

Once you've got your app [deployed on a Deta micro](/getting-started/deploy-your-app), you can simply add new pages and run the following command.
```bash
deta deploy
```
