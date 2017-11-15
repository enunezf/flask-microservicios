# project/config.py

class BaseConfig:
    """Configuración base"""
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    """Configuración desarrollo"""
    DEBUG = True


class TestingConfig(BaseConfig):
    """Configuración de testing"""
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    """Configuración de producción"""
    DEBUG = False