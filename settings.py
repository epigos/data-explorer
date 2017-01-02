import tornado
import tornado.template
import os
from tornado.options import define, options

# Make filepaths relative to settings.
path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=9011, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")

tornado.options.parse_command_line()

settings = {}
settings['debug'] = options.debug
settings['static_path'] = path(ROOT, 'static')
settings['template_loader'] = tornado.template.Loader(path(ROOT, 'templates'))

if options.config:
    tornado.options.parse_config_file(options.config)
