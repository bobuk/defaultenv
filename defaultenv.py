import typing
import os, sys, ast, os.path, pathlib

__env_timestamp__ = 0.0
__fname__ = ".env"


def read_env_file(fname:str =__fname__) -> None:
    if os.path.exists(fname):
        with open(fname, "r") as fl:
            cont: str = ""
            num: int
            line: str
            for num, line in enumerate(fl):
                line = cont + line.lstrip()
                line = line.strip()
                if "#" in line:
                    line = line.split("#", 1)[0].strip()
                if line.endswith("\\"):
                    cont = line[:-1]
                    continue
                if len(line) > 1:
                    if "=" not in line:
                        sys.stderr.write(
                            "Err in {fname} line {num}: {line}\n".format_map(locals())
                        )
                    key: str
                    val: str
                    key, val = line.split("=")
                    key = key.strip().upper()
                    val = val.strip()
                    try:
                        val = ast.literal_eval(val)
                    except:
                        pass

                    os.environ[key] = str(val)
                cont = ""
        __env_timestamp__ = os.path.getmtime(fname)


def load_env_file() -> None:
    try:
        if os.path.getmtime(__fname__) > __env_timestamp__:
            read_env_file()
    except:
        pass


def env(key:str, default: typing.Optional[typing.Any] = None):
    load_env_file()

    key = os.environ[key] if key in os.environ else ""
    if not key:
        return default(key) if callable(default) else default
    if default and callable(default):
        return default(key)
    return key


def auto_default(val: str) -> typing.Union[str, int, typing.List[pathlib.Path], pathlib.Path]:
    if not val:
        return val
    if val.isdigit():
        return int(val)
    if val.startswith("/"):
        if ":" in val:
            return [pathlib.Path(_) for _ in val.split(":")]
        return pathlib.Path(val)
    return val

class EnvObj:

    def __init__(self, capitalize=False):
        self.capitalize: bool = capitalize
        self.default: typing.Dict = {}
        self.default_default = None

    def defaults(self, **params):
        self.default = params if not self.capitalize else {
            k.upper(): v for k, v in params.items()
        }
        return self

    def pretty_good_defaults(self):
        self.default_default = auto_default
        return self

    def __getattr__(self, name: str) -> typing.Union[str, int, typing.List[pathlib.Path], pathlib.Path]:
        if self.capitalize:
            name = name.upper()
        return env(name, default=self.default.get(name, self.default_default))


ENV = EnvObj()
ENVC = EnvObj(capitalize=True)
ENVCD = EnvObj(capitalize=True).pretty_good_defaults()
