from bookStore.auth import auth


def initialize_route(api):
    api.add_resource(auth.Auth, '/auth')
