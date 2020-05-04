""""""

from http import HTTPStatus

from app.exceptions import NotFoundError, UnauthorizedError, ValidationError
from app.namespaces import ErrorNs
from app.login import login


@ErrorNs.ns.errorhandler(NotFoundError)
@ErrorNs.ns.marshal_with(ErrorNs.error_model, code=HTTPStatus.NOT_FOUND)
def not_found_error_handler(e):
    """Обработчик для ошибки NotFoundError"""

    return {'message': f'Resource {e} not found'}, HTTPStatus.NOT_FOUND


@login.unauthorized_handler
@ErrorNs.ns.errorhandler(UnauthorizedError)
@ErrorNs.ns.marshal_with(ErrorNs.error_model, code=HTTPStatus.UNAUTHORIZED)
def unauthorized_error_handler(e):
    """Обработчик для ошибки UnauthorizedError"""

    return {'message': e}, HTTPStatus.UNAUTHORIZED


@ErrorNs.ns.errorhandler(ValidationError)
@ErrorNs.ns.marshal_with(ErrorNs.error_model, code=HTTPStatus.CONFLICT)
def validation_error_handler(e):
    """Обработчик для ошибки ValidationError"""

    return {'message': e}, HTTPStatus.CONFLICT
