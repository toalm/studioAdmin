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


def _check_if_user_has_access_to_feature(user: 'User',  # NOQA
                                         feature_name: str):
    return False


def can_access_feature(feature_name: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            log.info('inside the Can access decorator')
            if not request:
                raise SyntaxError('This decorator can only be used with views')
            if not _check_if_user_has_access_to_feature(user=request.user,
                                                        feature_name=feature_name):
                raise NotAllowedAccessError("Not allowed to access")
            func(request, args, kwargs)

        return wrapper

    return decorator


@can_access_feature(feature_name='test')
def get_gallery_view(request: str,
                     view_name: str) -> None:
    log.info('Inside this')


if __name__ == '__main__':
    get_gallery_view(request=None,
                     view_name='test')
