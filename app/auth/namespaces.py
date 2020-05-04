""""""

from flask_restplus import Namespace, fields


class UserNamespace:
    """"""

    ns = Namespace('user')

    login_model = ns.model('LoginModel',
                           {'username': fields.String(required=True),
                            'password': fields.String(required=True)})

    registration_model = ns.model('RegisterModel',
                                  {'username': fields.String(required=True),
                                   'password': fields.String(required=True),
                                   'email': fields.String(required=True)})
