# from pathlib import Path
# import yaml
# #ограничиваем все доступные имена до load_config
# __all__ = ('load_config', )
#
# def load_config(config_file=None):
#     default_file = Path(__file__).parent/'config.yaml'
#     with open(default_file, 'r') as f:
#         config = yaml.safe_load(f)#типа чтобы нельзя было через файл конфигурации взломать поект
#
#     cf_dict = {} #словарь который читаем из конфигурационного файла
#     if config_file:
#         cf_dict = yaml.safe_load(config_file)
#
#     config.update(**cf_dict)
#     return config
#
