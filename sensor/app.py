import falcon

from .events import MyResource

api = application = falcon.API()

events = MyResource()
api.add_route('/events', events)

