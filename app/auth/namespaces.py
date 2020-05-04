""""""

from flask_restplus import Namespace, fields


class AuthNamespace:
    """"""

    ns = Namespace('auth')

    login_model = ns.model('LoginModel',
                           {'username': fields.String(required=True),
                            'password': fields.String(required=True)})
