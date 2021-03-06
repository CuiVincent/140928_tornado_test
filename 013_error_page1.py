from tornado.log import app_log

__author__ = 'cuizhe01'
import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)

class BaseHandler(tornado.web.RequestHandler):
    def send_error(self, status_code=500, **kwargs):
        reason = None
        if 'exc_info' in kwargs:
            exception = kwargs['exc_info'][1]
            if isinstance(exception, tornado.web.HTTPError) and exception.reason:
                reason = exception.reason
        try:
            if status_code == 404:
                self.render('404.html')
            elif status_code == 500:
                self.render('500.html',reason=reason)
            else:
                self.set_status(status_code, reason=reason)
                self.write_error(status_code, **kwargs)
        except Exception:
            app_log.error("Uncaught exception in write_error", exc_info=True)
        if not self._finished:
            self.finish()

class IndexHandler(BaseHandler):
    def get(self):
        raise AttributeError
        self.render('index.html')

class PageNotFoundHandler(BaseHandler):
    __err_code = 0
    def initialize(self, status_code):
       self.__err_code = status_code

    def check_xsrf_cookie(self):
        pass

    def get(self):
        raise tornado.web.HTTPError(self.__err_code)

if __name__ == '__main__':
    tornado.web.ErrorHandler = PageNotFoundHandler
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r'/', IndexHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "013_error_page1/templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()