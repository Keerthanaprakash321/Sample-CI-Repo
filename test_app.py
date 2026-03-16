# This is a simple test to ensure the CI pipeline passes
def test_always_passes():
    assert True

def test_environment_version():
    import sys
    # This confirms we are actually running on Python 3.13 as requested in Task 2
    assert sys.version_info.major == 3
    assert sys.version_info.minor == 13
