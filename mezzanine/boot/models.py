from . import mixinto


def extensible_meta(module_name):
    class ExtensibleMeta(type):
        def __new__(cls, name, bases, attrs):
            model_name = ".".join((module_name, name))
            real_meta = bases[0].__class__
            extra_bases = tuple(mixinto.registry[model_name])
            mixinto.registry[model_name] = None
            return real_meta.__new__(real_meta, name, bases + extra_bases, attrs)
    return ExtensibleMeta
