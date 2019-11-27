import json

import falcon
from datetime import datetime

class MyResource(object):

    def on_get(self, req, resp):
	
        now = datetime.now() 
        date_time = now.strftime("%Y/%m/%d, %H:%M:%S")
		
        doc = { 'up': date_time }

        # Create a JSON representation of the resource
        resp.body = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200