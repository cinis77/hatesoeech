import os
import configparser


class Config:
    """ Get config from config file or environment variables.
    """
    config = configparser.ConfigParser()
    config.read("./config.ini")

    BOOLEAN_STATES = {'1': True, 'yes': True, 'true': True, 'on': True, True: True,
                      '0': False, 'no': False, 'false': False, 'off': False, False: False}

    @staticmethod
    def get_or_else(section, option, default_value):
        if Config._has_env(section, option):
            return os.environ.get('_'.join([section.upper(), option]))
        if Config.config.has_option(section, option):
            return Config.config.get(section, option, fallback=default_value)
        return default_value

    @staticmethod
    def getint_or_else(section, option, default_value):
        if Config._has_env(section, option):
            return Config._get_conv_env_or_else(section, option, int)
        if Config.config.has_option(section, option):
            return Config.config.getint(section, option, fallback=default_value)
        return default_value

    @staticmethod
    def getfloat_or_else(section, option, default_value):
        if Config._has_env(section, option):
            return Config._get_conv_env_or_else(section, option, float)
        if Config.config.has_option(section, option):
            return Config.config.getfloat(section, option, fallback=default_value)
        return default_value

    @staticmethod
    def getboolean_or_else(section, option, default_value):
        if Config._has_env(section, option):
            return Config._get_conv_env_or_else(section, option, Config._convert_to_boolean)
        if Config.config.has_option(section, option):
            return Config.config.getboolean(section, option, fallback=default_value)
        return default_value

    @staticmethod
    def _get_conv_env_or_else(section, option, conv):
        return conv(os.environ.get('_'.join([section.upper(), option.upper()]), None))

    @staticmethod
    def _has_env(section, option):
        return '_'.join([section.upper(), option.upper()]) in os.environ

    @staticmethod
    def _convert_to_boolean(value):
        """Return a boolean value translating from other types if necessary.
        """
        if value.lower() not in Config.BOOLEAN_STATES:
            raise ValueError('Not a boolean: %s' % value)
        return Config.BOOLEAN_STATES[value.lower()]
