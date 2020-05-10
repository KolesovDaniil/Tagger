from http import HTTPStatus

from flask_restplus import Resource
from flask_login import login_required

from app.texts import views
from app.texts.namespaces import TextNamespace
from app.namespaces import ErrorNs


@TextNamespace.ns.route('')
class TextAll(Resource):
    @TextNamespace.ns.expect(TextNamespace.texts_parser)
    @TextNamespace.ns.response(HTTPStatus.OK, HTTPStatus.OK.phrase,
                               model=TextNamespace.get_text_all_model)
    @TextNamespace.ns.marshal_with(fields=TextNamespace.get_text_all_model)
    @login_required
    def get(self):
        """Get all texts"""

        params = TextNamespace.texts_parser.parse_args()

        return views.get_texts(params), HTTPStatus.OK

    @TextNamespace.ns.expect(TextNamespace.add_expect_model)
    @TextNamespace.ns.response(HTTPStatus.CREATED, HTTPStatus.CREATED.phrase,
                               model=TextNamespace.add_response_model)
    @TextNamespace.ns.response(HTTPStatus.BAD_REQUEST, HTTPStatus.BAD_REQUEST.phrase,
                               model=ErrorNs.error_model)
    @TextNamespace.ns.marshal_with(fields=TextNamespace.add_response_model)
    def post(self):
        """Add new text"""

        return views.add_text(TextNamespace.ns.payload), HTTPStatus.CREATED


@login_required
@TextNamespace.ns.route('/<int:id>')
@TextNamespace.ns.doc({'id': 'Text id'})
@TextNamespace.ns.response(HTTPStatus.NOT_FOUND, HTTPStatus.NOT_FOUND.phrase,
                           model=ErrorNs.error_model)
class TextById(Resource):
    @TextNamespace.ns.response(HTTPStatus.OK, HTTPStatus.OK.phrase,
                               model=TextNamespace.get_text_model)
    @login_required
    @TextNamespace.ns.marshal_with(fields=TextNamespace.get_text_model)
    def get(self, id):
        """Get text"""

        views.check_text_existing(id)

        return views.get_text(id), HTTPStatus.OK

    @TextNamespace.ns.expect(TextNamespace.update_expect_model)
    @TextNamespace.ns.response(HTTPStatus.NO_CONTENT, HTTPStatus.NO_CONTENT.phrase)
    @TextNamespace.ns.response(HTTPStatus.BAD_REQUEST, HTTPStatus.BAD_REQUEST.phrase,
                               model=ErrorNs.error_model)
    @login_required
    def patch(self, id):
        """Update text"""

        views.check_text_existing(id)
        views.update_text(id, TextNamespace.ns.payload)

        return {}, HTTPStatus.NO_CONTENT

    @TextNamespace.ns.response(HTTPStatus.NO_CONTENT, HTTPStatus.NO_CONTENT.phrase)
    @login_required
    def delete(self, id):
        """Delete text"""

        views.check_text_existing(id)
        views.delete_text(id)

        return {}, HTTPStatus.NO_CONTENT


@TextNamespace.ns.route('/tags',
                        doc={'description': 'Get tags without Log In and saving text'})
class TextTags(Resource):
    @TextNamespace.ns.expect(TextNamespace.tags_expect_model)
    @TextNamespace.ns.response(HTTPStatus.OK, HTTPStatus.OK.phrase,
                               model=TextNamespace.tags_response_model)
    @TextNamespace.ns.marshal_with(fields=TextNamespace.tags_response_model)
    def get(self):
        """Get tags"""

        text = TextNamespace.ns.payload['text']

        return {'tags': views.get_tags(text)}, HTTPStatus.OK
