import json


class Dict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__getitem__


def callback(data):
    d = json.dumps(data)
    print("SIZE", len(d.encode("utf-8")))
    return d


def get_callback(callback_data):
    return json.loads(callback_data)
