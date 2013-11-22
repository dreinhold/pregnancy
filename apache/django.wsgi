import os
import sys
import site

site.addsitedir('/home/dylan/pregnancy_project/env/local/lib/python2.7/site-packages')

sys.path.append('/home/dylan/pregnancy_project/pregnancy')
#sys.path.append('/home/dylan/pregnancy_project/pregnancy/pregnancy')

os.environ['DJANGO_SETTINGS_MODULE'] = 'pregnancy.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

