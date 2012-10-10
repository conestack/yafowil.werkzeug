import types
from UserDict import DictMixin
from werkzeug import datastructures
from yafowil.base import (
    UNSET,
    factory,
)


get_localizer = None # XXX


class WerkzeugRequestAdapter(DictMixin):

    def __init__(self, request):
        self.request = request

    def __getitem__(self, key):
        if key in self.request.form:
            value = self.request.form[key]
        elif key in self.request.files:
            value = self.request.files[key]
        else:
            raise KeyError(key)
        if isinstance(value, datastructures.FileStorage):
            fvalue = dict()
            fvalue['file'] = value.stream
            fvalue['filename'] = value.filename
            fvalue['mimetype'] = value.mimetype
            fvalue['headers'] = value.headers
            fvalue['original'] = value
            return fvalue
        return value

    def keys(self):
        return self.request.form.keys() + self.request.files.keys()

    def __setitem__(self, key, item):
        raise AttributeError('read only, __setitem__ is not supported')

    def __delitem__(self, key):
        raise AttributeError('read only, __delitem__ is not supported')


class TranslateCallable(object):

    def __init__(self, data):
        if isinstance(data.request, WerkzeugRequestAdapter):
            self.request = data.request.request
        else:
            self.request = data.request

    def __call__(self, msg):
        return msg


def werkzeug_preprocessor(widget, data):
    if not isinstance(data.request, (dict, WerkzeugRequestAdapter)):
        data.request = WerkzeugRequestAdapter(data.request)
    if not isinstance(data.translate_callable, TranslateCallable):
        data.translate_callable = TranslateCallable(data)
    return data


def register():
    factory.register_global_preprocessors([werkzeug_preprocessor])
