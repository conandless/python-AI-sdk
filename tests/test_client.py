import asyncio
import signal
import sys
from unittest.mock import MagicMock, AsyncMock, patch

import pytest

from palabra_ai.exc import ConfigurationError


class TestSpeechTranslationSDK:
    def test_default_initialization(self):
        """Test default initialization."""
        from palabra_ai.client import SpeechTranslationSDK

        sdk = SpeechTranslationSDK()
        assert sdk.client_id is None
        assert sdk.client_secret is None
        assert sdk.api_endpoint == "https://api.example.com"

    def test_custom_initialization(self):
        """Test custom initialization."""
        from palabra_ai.client import SpeechTranslationSDK

        sdk = SpeechTranslationSDK(client_id="test_id", client_secret="test_secret")
        assert sdk.client_id == "test_id"
        assert sdk.client_secret == "test_secret"
        assert sdk.api_endpoint == "https://api.example.com"
