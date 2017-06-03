import urllib.request # will need to prefix with module name
import http as h # import as different name if you need to
from cgi import * # imports everything; might lead to namespace collisions and larger memory footprint
from marshal import version as v # import specific function (under different name if you need to)

handler = urllib.request.FTPHandler # urllib.request
status = h.HTTPStatus.CONTINUE # http
form = FieldStorage() # cgi
version = v # marshal