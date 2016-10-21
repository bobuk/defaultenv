import os, sys, ast

if os.path.exists('.env'):
    with open('.env', 'r') as fl:
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

def env(key, default = None):
    return os.environ.get(key, default)
