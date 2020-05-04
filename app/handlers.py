""""""

from app.exceptions import NotFoundError
from app.namespaces import ErrorNs


@ErrorNs.ns.error_handlers(NotFoundError)
@ErrorNs.ns.marshal_with(ErrorNs.error_model)
def not_found_error_handler(e):
    """Обработчик для ошибки NotFoundError"""

    return {'message': f'Resource {e} not found'}
