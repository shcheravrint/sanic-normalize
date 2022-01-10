from sanic import Sanic, response
from sanic.views import HTTPMethodView
from sanic.response import text,json

app = Sanic(name='normalize')



# @app.route("/")
# async def home(request):
#    return response.text("Hello Sanic")


class SimpleAsyncView(HTTPMethodView):

    async def get(self, request):
        return text('I am async get method')

    async def post(self, request):
        data = request.json
        response = {dataentry['name']: [value for key, value in dataentry.items() if 'val' in key.lower()][0] for dataentry in data}
        return json(response)

    async def put(self, request):
        return text('I am async put method')


app.add_route(SimpleAsyncView.as_view(), '/async')

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=8000, debug=True) # 'debug' param auto-reloads server when code is changed