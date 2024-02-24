"""Discover B files to analyze."""

from tox_pyproject.config import Config


class BDiscoveryPlugin():
    """Discover B files to analyze."""

    def get_name(self) -> str:
        """Get name of discovery type."""
        return "B"

    def scan(self) -> list[str]:
        """Scan package looking for B files."""
        config = Config()
        b_files: list[str] = []
        b_files.append(config.default_level)

        return b_files
