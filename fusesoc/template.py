import jinja2
import yaml


class Engine(object):
    def process(self, vars, infile, outfile):
        pass


class Jinja2Engine(Engine):
    def process(self, vars, infile, outfile):
        tpl = jinja2.Template(open(infile).read())
        open(outfile,"w").write(tpl.render(vars))


def get_engine(name):
    if name == "jinja2":
        return Jinja2Engine()
    else:
        raise BaseException("Unknown template engine or engine not supported: {}".format(name))


class Variables(object):
    def __init__(self):
        self.vars = {}

    def add(self, filename):
        vars = yaml.load(open(filename).read())
        for name in vars.keys():
            if name not in self.vars:
                self.vars[name] = vars[name]

    def get(self, name):
        if name in self.vars:
            return self.vars[name]
        else:
            return {}