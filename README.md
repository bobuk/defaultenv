# defaultenv

Environment and config file reader for python3.
**Warrning:** slightly magic inside. This module magically read and use environment value both from '.env' file and environment itself.

```python
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

`env` method may be used to check the value of variable.
If variable is not defined `env` method will return `None`.
If both environment variable and corresponding .env record is exist then  .env have a priority.
And yes, you can use `os.environ` instead of  `env()`, all records from .env will be exported immidiately.

Since version 0.0.2 for more convinience two classes (ENV and ENVC) was added. You can use your environment variable name without method calling.

```python
$ python
>>> from defaultenv import ENV
>>> ENV.PATH
'/usr/local/bin:/usr/local/sbin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin'
```

ENV usage removing unnesesery typing of perenthesis and quotes. In this example i've save 4 keystrokes for you. But it's not very convinient to type uppercased name everytime. Let's imagine what my pinky finger is killing me.

```python
$ python
>>> from defaultenv import ENVC as env
>>> env.shell
'/usr/local/bin/zsh'
>>> env.home
'/home/bobuk'
```

As you see ENVC convert your variable name to uppercase. What the difference between `os.environ.get('PATH', None)` and `env.path`? It's easy to calculate and the result is 21 (which is half of 42).