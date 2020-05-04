""""""

from flask_restplus import Namespace, fields


class ErrorNs:
    """"""

    ns = Namespace('')

    error_model = ns.model('ErrorModel',
                           {'message': fields.String()})
