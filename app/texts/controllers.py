from http import HTTPStatus

from flask_restplus import Resource

from app.texts import views
from app.texts.namespaces import TextNamespace
from app.namespaces import ErrorNs


@TextNamespace.ns.route('')
class TextAll(Resource):
    """"""

    @TextNamespace.ns.expect(TextNamespace.texts_parser)
    @TextNamespace.ns.response(HTTPStatus.OK, HTTPStatus.OK.phrase,
                               model=TextNamespace.get_text_all_model)
    def get(self):
        return views.get_texts()

    @TextNamespace.ns.expect(TextNamespace.post_model, validate=True)
    @TextNamespace.ns.response(HTTPStatus.CREATED, HTTPStatus.CREATED.phrase,
                               model=TextNamespace.post_response_model)
    def post(self):
        return {'id': views.add_text()}


@TextNamespace.ns.route('/<int:id>')
@TextNamespace.ns.doc({'id': 'Text id'})
@TextNamespace.ns.response(HTTPStatus.NOT_FOUND, HTTPStatus.NOT_FOUND.phrase,
                           model=ErrorNs.error_model)
class TextById(Resource):
    """"""

    @TextNamespace.ns.response(HTTPStatus.OK, HTTPStatus.OK.phrase,
                               model=TextNamespace.get_text_model)
    def get(self, id):
        pass

    @TextNamespace.ns.expect(TextNamespace.post_model)
    def patch(self, id):
        pass

    def delete(self, id):
        pass
