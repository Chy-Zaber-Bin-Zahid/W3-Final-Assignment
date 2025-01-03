from controllers.add_controller import add_route
from controllers.getSingle_controller import getSingle_route
from controllers.getAll_controller import getAll_route
from controllers.deleteSingle_controller import deleteSingle_route
from controllers.deleteAll_controller import deleteAll_route
from controllers.edit_controller import edit_route


def routes(app):
    add_route(app)
    getSingle_route(app)
    getAll_route(app)
    deleteSingle_route(app)
    deleteAll_route(app)
    edit_route(app)
