import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log(response, req_payload=None):
    logger.info(f'REQUEST METHOD: {response.request.method}')
    logger.info(f'REQUEST URL: {response.url}')
    logger.info(f'REQUEST HEADERS: {response.request.headers}')
    logger.info(f'REQUEST BODY: {req_payload}\n')
    logger.info(f'STATUS CODE: {response.status_code}')
    logger.info(f'RESPONSE TIME: {response.elapsed.total_seconds() * 1000:.0f} ms\n')
    logger.info(f'RESPONSE HEADERS: {response.headers}')
    logger.info(f'RESPONSE BODY: {response.text}\n')
