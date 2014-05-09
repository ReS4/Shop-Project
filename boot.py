#########################
# Tornado App Launcher. #
#########################

# Setup the environment when starting Tornado.
from tornado.options import options, define
import env_setup
define("port", default=8004, help="run on the given port", type=int)

# Tornado imports etc..
import tornado
import os
# App-specific imports
from urls import url_patterns

# Your app launch code here..
if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        url_patterns,
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()