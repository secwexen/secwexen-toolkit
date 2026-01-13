import pytest


def test_tools_directory_exists():
    """Check if the tools package can be imported."""
    try:
        import tools
    except Exception as e:
        pytest.fail(f"Failed to import tools package: {e}")


def test_offensive_module_import():
    """Ensure offensive tools module loads."""
    try:
        import tools.offensive
    except Exception as e:
        pytest.fail(f"Failed to import offensive module: {e}")


def test_defensive_module_import():
    """Ensure defensive tools module loads."""
    try:
        import tools.defensive
    except Exception as e:
        pytest.fail(f"Failed to import defensive module: {e}")


def test_osint_module_import():
    """Ensure OSINT tools module loads."""
    try:
        import tools.osint
    except Exception as e:
        pytest.fail(f"Failed to import osint module: {e}")


def test_automation_module_import():
    """Ensure automation tools module loads."""
    try:
        import tools.automation
    except Exception as e:
        pytest.fail(f"Failed to import automation module: {e}")


def test_utils_import():
    """Ensure utils package loads correctly."""
    try:
        import utils
    except Exception as e:
        pytest.fail(f"Failed to import utils package: {e}")


def test_utils_functions_exist():
    """Check if core utility functions exist."""
    from utils import (
        log_info,
        log_warning,
        log_error,
        read_file,
        write_file,
        file_exists,
        is_valid_domain,
        is_valid_ip,
        is_valid_email,
    )

    assert callable(log_info)
    assert callable(log_warning)
    assert callable(log_error)
    assert callable(read_file)
    assert callable(write_file)
    assert callable(file_exists)
    assert callable(is_valid_domain)
    assert callable(is_valid_ip)
    assert callable(is_valid_email)
