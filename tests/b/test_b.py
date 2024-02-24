"""Unit tests for the B discovery plugin."""

import sys

from tox_pyproject.plugins.discovery.b import BDiscoveryPlugin

if sys.version_info < (3, 10):
    from importlib_metadata import entry_points
else:
    from importlib.metadata import entry_points


def test_b_discovery_plugin_found():
    """Test that the plugin manager finds the B discovery plugin."""
    discovery_plugins = {}
    plugins = entry_points(group="tox_pyproject.plugins.discovery")
    for plugin_type in plugins:
        plugin = plugin_type.load()
        discovery_plugins[plugin_type.name] = plugin()
    assert any(
        plugin.get_name() == "B" for _, plugin in list(discovery_plugins.items())
    )


def test_b_discovery_plugin_scan_valid():
    """Test that the B discovery plugin runs."""
    bdp = BDiscoveryPlugin()
    found = bdp.scan()
    assert found == ["threshold"]
