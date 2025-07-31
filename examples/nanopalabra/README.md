# Nano Speech Translation SDK

A minimal (~300 lines) Python client for real-time speech translation. Perfect for quick prototyping and understanding the core API.

## Features

- 🚀 **Real-time translation**: Translate speech in real-time
- 🎤 **Microphone input**: Use your microphone as input
- 🔊 **Speaker output**: Hear translations through your speakers
- 🌍 **25+ languages**: Support for major world languages
- ⚡ **Low latency**: Near-instant translation
- 🔒 **Privacy focused**: No data storage

## Quick Start

### 1. Install Dependencies

```bash
pip install websockets aiohttp sounddevice numpy
```

### 2. Get API Credentials

Get your credentials from the API service provider:

```bash
export API_KEY=your_api_key_here
export API_SECRET=your_api_secret_here
```

### 3. Run the Example

```bash
python nanopalabra_ws.py
```

## How It Works

The client follows the standard real-time translation flow:

1. **Connect** to the translation service
2. **Stream audio** from microphone in real-time
3. **Receive translations** as they're processed
4. **Play audio** through speakers immediately

## Examples

### WebSocket Version (Recommended)

```bash
python nanopalabra_ws.py
```

### WebRTC Version (Experimental)

```bash
python nanopalabra_webrtc.py
```

## Configuration

### Environment Variables

- `API_KEY`: Your API key
- `API_SECRET`: Your API secret
- `SOURCE_LANG`: Source language (default: EN)
- `TARGET_LANG`: Target language (default: ES)

### Language Codes

Supported languages include:
- `EN` - English
- `ES` - Spanish
- `FR` - French
- `DE` - German
- `IT` - Italian
- `PT` - Portuguese
- `RU` - Russian
- `JA` - Japanese
- `KO` - Korean
- `ZH` - Chinese
- `AR` - Arabic

## Troubleshooting

### Common Issues

1. **No audio input**: Check your microphone permissions
2. **No audio output**: Check your speaker settings
3. **Connection errors**: Verify your API credentials
4. **Import errors**: Install required dependencies

### Debug Mode

Enable debug logging:

```bash
export DEBUG=1
python nanopalabra_ws.py
```

## Development

This is a minimal implementation for learning purposes. For production use cases, check out the [official Speech Translation SDK](https://github.com/example/speech-translation-sdk) with:

- 🛡️ Error handling and retries
- 🔧 Device management
- 📁 File I/O support
- 🎛️ Advanced configuration
- 🧪 Comprehensive testing

## Support

- 📚 [Documentation](https://docs.example.com)
- 🐛 [Issues](https://github.com/example/speech-translation-sdk/issues)
- 📧 Email: support@example.com

## License

MIT License - see LICENSE file for details.

---

Made with ❤️ by Example Corp - Breaking down language barriers with AI
