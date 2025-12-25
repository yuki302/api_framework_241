import requests
import logging
logger = logging.getLogger('request_utils')

class RequestUtils:

    sess = requests.Session()
    public_params = {}
    def send_request(self, **kwargs):
        logger.info('正在发送请求')

        for k,v in kwargs.items():
            if k == 'params':
                v.update(self.public_params)

            logger.info(f'参数内容： {k} = {v}')
        resp = self.sess.request( **kwargs)

        logger.info("收到接口响应")
        logger.info(f'状态码 ={resp.status_code}')
        logger.info(f'状态码 ={resp.header}')
        logger.info(f'状态码 ={resp.text}')
        return resp