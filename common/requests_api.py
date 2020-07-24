import requests
from common.readConfig import WRConfigFile
from logs.logsfile import logger


conf = WRConfigFile().read_conf
url_head = conf('requests_setting', 'url_head')
if url_head == '':
    logger.info('configfile.ini文件没有配置[requests_setting][url_head]')
    logger.error('configfile.ini文件没有配置[requests_setting][url_head]')


@logger.catch()
def auto_get(url=None, params=None, headers=None, allow_redirects=True, timeout=3):
    all_url = str(url_head) + str(url)
    try:
        logger.info('开始请求接口:{all_url}', all_url=all_url)
        get_response = requests.get(url=all_url, headers=headers, params=params, allow_redirects=allow_redirects, timeout=timeout)
        logger.success('接口请求成功，等待返回数据。请求URL:{get_response_url}', get_response_url=get_response.url)
    except BaseException as e:
        logger.warning('接口请求时发生异常:{all_url},异常:{e}', all_url=all_url, e=e)
    else:
        logger.success('接口请求执行成功，返回数据:{get_response}', get_response=get_response.content)
        return get_response.text
    finally:
        logger.info('接口执行完毕')


@logger.catch()
def auto_post(url=None, data=None, headers=None, allow_redirects=True, timeout=3):
    all_url = str(url_head) + str(url)
    try:
        logger.info('开始请求接口:{all_url}', all_url=all_url)
        post_response = requests.post(url=all_url, headers=headers, data=data, allow_redirects=allow_redirects, timeout=timeout)
        logger.success('接口请求成功，等待返回数据。请求URL:{post_response_url}', post_response_url=post_response.url)
    except BaseException as e:
        logger.warning('接口请求时发生异常:{all_url},异常:{e}', all_url=all_url, e=e)
    else:
        logger.success('接口请求执行成功，返回数据:{post_response}', post_response=post_response.json())
        return post_response.json()
    finally:
        logger.info('接口执行完毕')


if __name__ == '__main__':
    params = {'stu_name': '小黑'}
    auto_get(url='/api/user/stu_info', params=params)
    auto_get(url='/index.php?s=/5&page_id=17')
    data = {'username': 'niuhanyang', 'passwd': 'aA123456'}
    auto_post(url='/api/user/login', data=data)


