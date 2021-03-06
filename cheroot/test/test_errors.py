"""Test suite for ``cheroot.errors``."""

import platform

import pytest

from cheroot import errors


SYS_PLATFORM = platform.system()
IS_WINDOWS = SYS_PLATFORM == 'Windows'
IS_LINUX = SYS_PLATFORM == 'Linux'
IS_MACOS = SYS_PLATFORM == 'Darwin'


@pytest.mark.parametrize(
    'err_names,err_nums',
    (
        (('', 'some-nonsense-name'), []),
        (
            ('EPROTOTYPE', 'EAGAIN', 'EWOULDBLOCK',
             'WSAEWOULDBLOCK', 'EPIPE'),
            (91, 11, 32) if IS_LINUX else
            (32, 35, 41) if IS_MACOS else
            (32, 10041, 11, 10035) if IS_WINDOWS else
            ()
        ),
    ),
)
def test_plat_specific_errors(err_names, err_nums):
    """Test that plat_specific_errors retrieves correct err num list."""
    actual_err_nums = errors.plat_specific_errors(*err_names)
    assert len(actual_err_nums) == len(err_nums)
    assert sorted(actual_err_nums) == sorted(err_nums)
