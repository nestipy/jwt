from nestipy.common import Module
from nestipy.core import AppKey
from nestipy.ioc import ModuleProviderDict

from app_controller import AppController
from app_service import AppService
from auth_guard import AuthGuard
from nestipy_jwt import JwtModule


@Module(
    imports=[
        JwtModule.for_root(),
    ],
    controllers=[AppController],
    providers=[
        AppService,
        ModuleProviderDict(
            token=AppKey.APP_GUARD,
            use_class=AuthGuard
        )
    ]
)
class AppModule:
    ...
