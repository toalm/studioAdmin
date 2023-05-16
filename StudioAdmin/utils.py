# © ALM Solutions AB.
# Written by Tobias Alm
import functools
import logging

# Third Party

# Local
logging.basicConfig(format='%(asctime)s [%(levelname)s]%(filename)s%(funcName)s(%(lineno)s)'
                           '->%(message)s')
log = logging.getLogger(__file__)


class NotAllowedAccessError(Exception):
    pass

'''
TODO: Feature names should be detectable by PARENT_NAME.CHILD_NAME.CHILD_NAME
'''
def can_access_feature(name: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log.info('inside the Can access decorator')
            # raise NotAllowedAccessError("Not allowed to access")

        return wrapper

    return decorator


@can_access_feature(name='test')
def get_gallery_view(view_name: str) -> None:
    log.info('Inside this')


if __name__ == '__main__':
    get_gallery_view(view_name='test')