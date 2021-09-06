from aiohttp import web 

async def sample(request):
    return web.Response(text="async server is python")

app=web.application()
app.add_route([web.get('/',sample)])
web.run_app(app)