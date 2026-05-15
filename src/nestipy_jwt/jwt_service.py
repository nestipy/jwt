import json
from typing import Annotated, Any, Iterable

from jwt import PyJWT
from jwt.types import Options
from nestipy.common import Injectable
from nestipy.ioc import Inject

from .jwt_builder import JWT_OPTION_TOKEN, JwtOption


@Injectable()
class JwtService(PyJWT):
    _options: Annotated[JwtOption, Inject(JWT_OPTION_TOKEN)]

    def __init__(self):
        super().__init__()

    def generate_token(
        self,
        payload: dict[str, Any],
        key: str | bytes | None = None,
        algorithm: str | None = None,
        headers: dict[str, Any] | None = None,
        json_encoder: type[json.JSONEncoder] | None = None,
        sort_headers: bool = True,
    ):
        return super().encode(
            payload,
            key or self._options.secret,
            algorithm or self._options.algorithms[0]
            if len(self._options.algorithms) > 0
            else "HS256",
            headers,
            json_encoder,
            sort_headers,
        )

    def verify(
        self,
        jwt: str | bytes,
        key: str | bytes | None = None,
        algorithms: list[str] | None = None,
        options: Options | None = None,
        verify: bool | None = None,
        detached_payload: bytes | None = None,
        audience: str | Iterable[str] | None = None,
        issuer: str | None = None,
        leeway: str | None = None,
    ) -> Any:
        return super().decode(
            jwt,
            key or self._options.secret,
            algorithms or self._options.algorithms or ["HS256"],
            options,
            verify,
            detached_payload,
            audience,
            issuer,
            leeway,
        )
