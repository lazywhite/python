# 1.from a.b import c -> both a.__init__ and b.__init__ 
# will both be executed ,then <import a >will not execute
# a.__init__ any more

# 2.from a import * , will not import name.startswith('_')
# 3.from __future__ import absolute_import
#      import string ## will try to import 'string' standard library
#      not .string
# 4. relative import can only use like this <from . import m>
#      it won't work if parts of package are executed as script
# 5. import importlib; importlib.import_module('name':str)
#        path = importlib.import_module('os.path')
