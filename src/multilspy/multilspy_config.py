"""
Configuration parameters for Multilspy.
"""
import os
import pathlib
from enum import Enum
from dataclasses import dataclass
from pathlib import PurePath


class Language(str, Enum):
    """
    Possible languages with Multilspy.
    """

    CSHARP = "csharp"
    PYTHON = "python"
    RUST = "rust"
    JAVA = "java"
    TYPESCRIPT = "typescript"
    JAVASCRIPT = "javascript"
    PHP = "php"

    def __str__(self) -> str:
        return self.value

@dataclass
class MultilspyConfig:
    """
    Configuration parameters
    """
    code_language: Language
    static_root: str = str(PurePath(os.path.abspath(os.path.dirname(__file__))))
    language_server_dir: str = pathlib.Path.home()
    trace_lsp_communication: bool = False

    @classmethod
    def from_dict(cls, env: dict):
        """
        Create a MultilspyConfig instance from a dictionary
        """
        import inspect
        return cls(**{
            k: v for k, v in env.items() 
            if k in inspect.signature(cls).parameters
        })