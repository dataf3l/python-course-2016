import cherrypy
import matlab.engine
from matlab.engine import MatlabExecutionError

print("Please wait...")
eng = matlab.engine.start_matlab()

def to_string(item):
    str(item)

class HelloWorld(object):
    
    def index(self):
        a = open("form.html","r")
        form = a.read()
        a.close()
        return form

    @cherrypy.expose
    def run_command(self,command="gcd(80.0, 100.0, nargout=3)"):
        global eng
        try:
            results_obj = eval("eng." + command)
        except MatlabExecutionError:
            return "Bad command:" + command
        results_str = str(results_obj)
        html = " " + results_str
        return "<h1>Results are</h1>" + html
    index.exposed = True

print("Server Starting...")
cherrypy.quickstart(HelloWorld())
