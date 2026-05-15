from typing import Any, Awaitable, Callable, Optional, Type, Union

from nestipy.common import Module
from nestipy.dynamic_module import DynamicModule

from .jwt_builder import ConfigurableModuleClass, JwtOption
from .jwt_service import JwtService


@Module(providers=[JwtService], exports=[JwtService], is_global=True)
class JwtModule(ConfigurableModuleClass):
    @classmethod
    def for_root(cls, option: Optional[JwtOption] = None) -> DynamicModule:
        dynamic_module: DynamicModule = cls.register(
            option or JwtOption(secret="nestipy_secret_key")
        )
        if option and option.is_global:
            dynamic_module.is_global = option.is_global
        return dynamic_module

    @classmethod
    def for_root_async(
        cls,
        value: Optional[JwtOption] = None,
        factory: Optional[Callable[..., Union[Awaitable[Any], Any]]] = None,
        existing: Optional[Union[Type, str]] = None,
        use_class: Optional[Type] = None,
        inject: Optional[list] = None,
        imports: Optional[list] = None,
        extras: Optional[dict] = None,
    ) -> DynamicModule:
        return cls.register_async(
            value=value,
            factory=factory,
            existing=existing,
            use_class=use_class,
            inject=inject,
            imports=imports,
            extras=extras,
        )
