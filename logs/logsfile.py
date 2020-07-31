from loguru import logger
import os


info_logs_path = os.path.dirname(__file__) + '\\info.log'
error_logs_path = os.path.dirname(__file__) + '\\error.log'

# logger.remove(handler_id=None)
# 禁止控制台输出日志

logger.add(info_logs_path,
           filter=lambda x: x['level'].name > 'ERROR',
           # level='INFO',
           enqueue=True,
           rotation='00:00',
           encoding='utf-8',
           retention='30 days'
           )
logger.add(error_logs_path,
           filter='',
           level='WARNING',
           enqueue=True,
           rotation='00:00',
           encoding='utf-8',
           retention='30 days'
           )
