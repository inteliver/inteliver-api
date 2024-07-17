from enum import Enum
import os
from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings


class AppEnvEnum(str, Enum):
    DEVELOPMENT = "development"
    STAGING = "staging"
    PRODUCTION = "production"


class BaseAppSettings(BaseSettings):
    app_name: str = Field("ai-service-template", alias="CONFIG_APP_NAME")
    app_api_host: str = Field("127.0.0.1", alias="CONFIG_APP_API_HOST")
    app_api_port: int = Field(8080, alias="CONFIG_APP_API_PORT")
    app_running_env: AppEnvEnum = Field(
        AppEnvEnum.DEVELOPMENT, alias="CONFIG_APP_RUNNING_ENV"
    )

    openapi_docs_url: str = Field("/docs", alias="CONFIG_FASTAPI_DOCS_URL")
    openapi_json_url: str = Field("/openapi.json", alias="CONFIG_FASTAPI_OPENAPI_URL")
    gradio_interface_enable: bool = Field(True, alias="CONFIG_GRADIO_INTERFACE_ENABLE")
    gradio_interface_url: str = Field("/ui", alias="CONFIG_GRADIO_INTERFACE_URL")

    eureka_discovery_url: str = Field("127.0.0.1", alias="CONFIG_EUREKA_DISCOVERY_URL")
    eureka_discovery_enable: bool = Field(False, alias="CONFIG_EUREKA_DISCOVERY_ENABLE")


class DevelopmentSettings(BaseAppSettings):
    # example of a database url that has different env variable names and
    # default value in different running env settings
    # database_url: str = Field(..., env="DEV_DB_URL")
    pass


class StagingSettings(BaseAppSettings):
    # example of a database url that has different env variable names and
    # default value in different running env settings
    # database_url: str = Field(..., env="STAGING_DB_URL")
    app_api_host: str = Field("0.0.0.0", alias="CONFIG_APP_API_HOST")
    eureka_discovery_enable: bool = Field(True, alias="CONFIG_EUREKA_DISCOVERY_ENABLE")


class ProductionSettings(BaseAppSettings):
    # example of a database url that has different env variable names and
    # default value in different running env settings
    # database_url: str = Field(..., env="PROD_DB_URL")
    app_api_host: str = Field("0.0.0.0", alias="CONFIG_APP_API_HOST")
    gradio_interface_enable: bool = Field(False, alias="CONFIG_GRADIO_INTERFACE_ENABLE")


@lru_cache
def get_settings():
    env = AppEnvEnum(os.getenv("CONFIG_APP_RUNNING_ENV", "development"))
    if env == AppEnvEnum.DEVELOPMENT:
        return DevelopmentSettings()
    elif env == AppEnvEnum.STAGING:
        return StagingSettings()
    elif env == AppEnvEnum.PRODUCTION:
        return ProductionSettings()
    else:
        raise ValueError("Invalid environment specified")


settings = get_settings()
