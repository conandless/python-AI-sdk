# Installation Guide

This guide will help you install and set up the AI Speech Translation SDK.

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Installation Methods

### Method 1: From Source (Development)

1. Clone the repository:
   ```bash
   git clone https://github.com/example/speech-translation-sdk.git
   cd speech-translation-sdk
   ```

2. Install in development mode:
   ```bash
   pip install -e .
   ```

### Method 2: From PyPI (Production)

```bash
pip install speech-translation-sdk
```

### Method 3: From GitHub Releases

Download the latest wheel file from [Releases](https://github.com/example/speech-translation-sdk/releases):

```bash
# For Python 3.11
pip install https://github.com/example/speech-translation-sdk/releases/download/v0.2.4/speech_translation_sdk-0.2.4-py3-none-any.whl
```

### Method 4: Using Docker

```bash
# Pull the Docker image
docker pull ghcr.io/example/speech-translation-sdk:latest

# Run the container
docker run ghcr.io/example/speech-translation-sdk:latest

# Or use in your Dockerfile
FROM ghcr.io/example/speech-translation-sdk:latest
```

## Verification

After installation, verify that the SDK is working correctly:

```python
from speech_translation_sdk import SpeechTranslationSDK, EN, ES

# This should not raise any errors
sdk = SpeechTranslationSDK()
print("✅ SDK installed successfully!")
```

## Configuration

### Environment Variables

Set your API credentials as environment variables:

```bash
export API_KEY=your_api_key
export API_SECRET=your_api_secret
```

### API Credentials

You'll need to obtain API credentials from the service provider. These are required for authentication with the translation service.

## Quick Start

1. Install the SDK (see methods above)
2. Set up your API credentials
3. Explore the [examples](https://github.com/example/speech-translation-sdk/tree/main/examples) directory

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure you've installed the package correctly
2. **SSL Certificate Errors**: On macOS, you may need to install certificates
3. **Audio Device Issues**: Ensure your microphone and speakers are properly configured

### Getting Help

- Check [GitHub Issues](https://github.com/example/speech-translation-sdk/issues)
- Email: support@example.com