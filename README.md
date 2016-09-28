# defaultenv

Environment and config file reader for python.
**Warrning:** slightly magic inside. This module magically read and use environment value both from '.env' file and environment itself.

```
$ echo "MY_VAL='test'" > .env
$ python
>>> from defaultenv import env
>>> env('PATH')
'/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin'
>>> env('TEST')
>>> env('MY_VAL')
'test'
>>> import os; os.environ['MY_VAL']
'test'

```

So, use `env` method to check the value of variable. If variable is not defined `env` method will return `None`.
