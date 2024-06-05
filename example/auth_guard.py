from typing import Union, Awaitable, Annotated


from nestipy.common import Injectable, CanActivate, HttpException, HttpStatusMessages, HttpStatus
from nestipy.core import ExecutionContext
from nestipy.ioc import Inject

from nestipy_jwt import JwtService


@Injectable()
class AuthGuard(CanActivate):
    jwt: Annotated[JwtService, Inject()]

    def can_activate(self, context: "ExecutionContext") -> Union[Awaitable[bool], bool]:
        req = context.switch_to_http().get_request()
        bearer = req.headers.get("authorization", "").replace("Bearer ", "")
        try:
            data = self.jwt.decode(bearer)
            print(data)
            return True
        except Exception as e:
            raise HttpException(HttpStatus.UNAUTHORIZED, HttpStatusMessages.UNAUTHORIZED, str(e))
