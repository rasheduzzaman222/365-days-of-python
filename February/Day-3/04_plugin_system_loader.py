import importlib

def load_plugin(module_name):
    try:
        module = importlib.import_module(module_name)
        return module
    except ImportError:
        return None


if __name__ == "__main__":
    plugin = load_plugin("math")
    if plugin:
        print(plugin.sqrt(16))
