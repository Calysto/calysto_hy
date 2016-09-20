'''
A Hy Lang kernel for Jupyter based on MetaKernel.
'''
from __future__ import print_function

import __future__  # NOQA

import ast
import sys
import traceback

from hy.version import __version__ as hy_version
from hy.macros import _hy_macros, load_macros
from hy.lex import tokenize
from hy.compiler import hy_compile, _compile_table, load_stdlib
from hy.core import language

from .version import __version__

from metakernel import MetaKernel

class CalystoHy(MetaKernel):
    '''
    '''
    implementation = 'hy'
    implementation_version = __version__
    language = 'hy'
    language_version = hy_version
    banner = 'Hy is a wonderful dialect of Lisp that’s embedded in Python.'
    language_info = {
        'name': 'hy',
        'mimetype': 'text/x-hylang',
        'codemirror_mode': {
            'name': 'hy'
        },
        'pygments_lexer': 'lisp'
    }
    kernel_json = {
        "argv": [sys.executable,
                 "-m", "calysto_hy",
                 "-f", "{connection_file}"],
        "display_name": "Calysto Hy",
        "language": "hy",
        "codemirror_mode": "hy",
        "name": "calysto_hy"
    }
    identifier_regex = r'\\?[\w\.][\w\.\?\!\-\>\<]*'
    function_call_regex = r'\(([\w\.][\w\.\?\!\-\>\>]*)[^\)\()]*\Z'
    magic_prefixes = dict(magic='%', shell='!', help='?')
    help_suffix = None

    def __init__(self, *args, **kwargs):
        '''
        Create the hy environment
        '''
        super(CalystoHy, self).__init__(*args, **kwargs)
        load_stdlib()
        [load_macros(m) for m in ['hy.core', 'hy.macros']]
        self.env = {}
        if "str" in dir(__builtins__):
            self.env.update({key: getattr(__builtins__, key)
                             for key in dir(__builtins__)})
        if "keys" in dir(__builtins__):
            self.env.update(__builtins__)
        self.env["raw_input"] = self.raw_input
        self.env["read"] = self.raw_input
        self.env["input"] = self.raw_input

    def do_execute_direct(self, code):
        '''
        '''
        retval = None
        #### try to parse it:
        try:
            tokens = tokenize(code)
            _ast = hy_compile(tokens, '__console__', root=ast.Interactive)
            code = compile(_ast, "In [%s]" % self.execution_count, mode="single")
            retval = eval(code, self.env)
        except Exception as e:
            self.Error(traceback.format_exc())
            self.kernel_resp.update({
                "status": "error",
                'ename' : e.__class__.__name__,   # Exception name, as a string
                'evalue' : e.__class__.__name__,  # Exception value, as a string
                'traceback' : [], # traceback frames as strings
            })
            return None
        return retval

    def get_completions(self, info):
        txt = info["help_obj"]
        matches = [word for word in self.env if word.startswith(txt)]
        for p in list(_hy_macros.values()) + [_compile_table]:
            p = filter(lambda x: isinstance(x, str), p.keys())
            p = [x.replace('_', '-') for x in p]
            matches.extend([
                x for x in p
                if x.startswith(txt) and x not in matches
            ])
        return matches