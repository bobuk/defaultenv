import os, sys, ast, os.path

__env_timestamp__ = 0.0
__fname__ = '.env'

def read_env_file(fname = __fname__):
    if os.path.exists(fname):
        with open(fname, 'r') as fl:
            cont = ""
            for num, line in enumerate(fl):
                line = cont + line.lstrip()
                line = line.strip()
                if '#' in line:
                    line = line.split('#', 1)[0].strip()
                if line.endswith('\\'):
                    cont = line[:-1]
                    continue
                if len(line) > 1:
                    if '=' not in line:
                        sys.stderr.write('Err in .env, line ' + str(num) + ': ' + line + '\n')
                    key, val = line.split('=')
                    key = key.strip().upper()
                    val = val.strip()
                    try:
                        val = ast.literal_eval(val)
                    except: pass

                    os.environ[key] = str(val)
                cont = ""
        __env_timestamp__ = os.path.getmtime(fname)

def env(key, default = None):
    try:
        if os.path.getmtime(__fname__) > __env_timestamp__:
            read_env_file()
    except:
        pass
    key = os.environ[key] if key in os.environ else None
    if default and key and callable(default):
        return default(key)

    return key if key else default
        

        

class EnvObj:
    def __init__(self, capitalize = False):
        self.capitalize = capitalize
        self.default = {}

    def defaults(self, **params):
        self.default = params if not self.capitalize else {k.upper(): v for k,v in params.items()}
        return self
    def __getattr__(self, name):
        if self.capitalize:
            name = name.upper()
        return env(name, default = self.default.get(name, None))

ENV = EnvObj()
ENVC = EnvObj(capitalize = True)
