from api.resource.account import AccountApi,AccountsApi,AccountRegisterApi, AccountAuthApi
from api.resource.login import loginApi, authorizationApi

def init_routes(api):
    #계정 api
    api.add_resource(AccountApi, '/account/<string:user_id>')
    api.add_resource(AccountsApi, '/accounts')
    api.add_resource(AccountRegisterApi, '/account')
    api.add_resource(AccountAuthApi, '/accountMailAuth')

    #로그인api
    api.add_resource(loginApi, '/login')
    #토큰인증 api
    api.add_resource(authorizationApi, '/authorization')
