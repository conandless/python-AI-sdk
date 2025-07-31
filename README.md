# <a href="https://example.com"><img src="https://via.placeholder.com/32x32/007acc/ffffff?text=AI" alt="AI SDK" align="center"></a> AI Speech Translation SDK

[![Tests](https://github.com/example/speech-translation-sdk/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/example/speech-translation-sdk/actions/workflows/test.yml)
[![Release](https://github.com/example/speech-translation-sdk/actions/workflows/release.yml/badge.svg)](https://github.com/example/speech-translation-sdk/actions/workflows/release.yml)
[![Python Versions](https://img.shields.io/badge/python-3.11%20%7C%203.12%20%7C%203.13-blue)](https://github.com/example/speech-translation-sdk)
[![PyPI version](https://img.shields.io/pypi/v/speech-translation-sdk.svg?color=blue)](https://pypi.org/project/speech-translation-sdk/)
[![Downloads](https://pepy.tech/badge/speech-translation-sdk)](https://pepy.tech/projects/speech-translation-sdk)
[![Docker](https://img.shields.io/badge/docker-ghcr.io-blue?logo=docker)](https://github.com/example/speech-translation-sdk/pkgs/container/speech-translation-sdk)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[//]: # ([![codecov]&#40;https://codecov.io/gh/example/speech-translation-sdk/graph/badge.svg?token=EXAMPLE&#41;]&#40;https://codecov.io/gh/example/speech-translation-sdk&#41;)

🌍 **Python SDK for real-time speech-to-speech translation API**  
🚀 Break down language barriers and enable seamless communication across 25+ languages

## Overview 📋

🎯 **The AI Speech Translation SDK provides a high-level API for integrating real-time speech-to-speech translation into your Python applications.**

✨ **What can this SDK do?**
- ⚡ Real-time speech-to-speech translation with near-zero latency
- 🎙️ Auto voice cloning - speak any language in YOUR voice
- 🔄 Two-way simultaneous translation for live discussions
- 🚀 Developer API/SDK for building your own apps
- 🎯 Works everywhere - Zoom, streams, events, any platform
- 🔒 Zero data storage - your conversations stay private

🔧 **This SDK focuses on making real-time translation simple and accessible:**
- 🛡️ Uses WebRTC and WebSockets under the hood
- ⚡ Abstracts away all complexity
- 🎮 Simple configuration with source/target languages
- 🎤 Supports multiple input/output adapters (microphones, speakers, files, buffers)

📊 **How it works:**
1. 🎤 Configure input/output adapters
2. 🔄 SDK handles the entire pipeline
3. 🎯 Automatic transcription, translation, and synthesis
4. 🔊 Real-time audio stream ready for playback

💡 **All with just a few lines of code!**

## Installation 📦

### From PyPI 📦
```bash
pip install speech-translation-sdk
```

### macOS SSL Certificate Setup 🔒

If you encounter SSL certificate errors on macOS like:
```
SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate
```

**Option 1: Install Python certificates** (recommended)
```zsh
/Applications/Python\ $(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")/Install\ Certificates.command
```

**Option 2: Use system certificates**
```bash
pip install pip-system-certs
```

This will configure Python to use your system's certificate store.

## Quick Start 🚀

### Real-time microphone translation 🎤

```python
from speech_translation_sdk import (SpeechTranslationSDK, Config, SourceLang, TargetLang,
                        EN, ES, DeviceManager)

sdk = SpeechTranslationSDK()
dm = DeviceManager()
mic, speaker = dm.select_devices_interactive()
cfg = Config(SourceLang(EN, mic), [TargetLang(ES, speaker)])
sdk.run(cfg)
```

⚙️ **Set your API credentials as environment variables:**
```bash
export API_KEY=your_api_key
export API_SECRET=your_api_secret
```

## Examples 💡

### File-to-file translation 📁

```python
from speech_translation_sdk import (SpeechTranslationSDK, Config, SourceLang, TargetLang,
                        FileReader, FileWriter, EN, ES)

sdk = SpeechTranslationSDK()
reader = FileReader("./speech/es.mp3")
writer = FileWriter("./es2en_out.wav")
cfg = Config(SourceLang(ES, reader), [TargetLang(EN, writer)])
sdk.run(cfg)
```

### Multiple target languages 🌐

```python
from speech_translation_sdk import (SpeechTranslationSDK, Config, SourceLang, TargetLang,
                        FileReader, FileWriter, EN, ES, FR, DE)

sdk = SpeechTranslationSDK()
config = Config(
    source=SourceLang(EN, FileReader("presentation.mp3")),
    targets=[
        TargetLang(ES, FileWriter("spanish.wav")),
        TargetLang(FR, FileWriter("french.wav")),
        TargetLang(DE, FileWriter("german.wav"))
    ]
)
sdk.run(config)
```

### Customizable output 📝

📋 **Add a transcription of the source and translated speech.**  
⚙️ **Configure output to provide:**
- 🔊 Audio only
- 📝 Transcriptions only
- 🎯 Both audio and transcriptions

```python
from speech_translation_sdk import (
    SpeechTranslationSDK,
    Config,
    SourceLang,
    TargetLang,
    FileReader,
    EN,
    ES,
)
from speech_translation_sdk.base.message import TranscriptionMessage


async def print_translation_async(msg: TranscriptionMessage):
    print(repr(msg))


def print_translation(msg: TranscriptionMessage):
    print(str(msg))


sdk = SpeechTranslationSDK()
cfg = Config(
    source=SourceLang(
        EN,
        FileReader("speech/en.mp3"),
        print_translation  # Callback for source transcriptions
    ),
    targets=[
        TargetLang(
            ES,
            # You can use only transcription without audio writer if you want
            # FileWriter("./test_output.wav"),  # Optional: audio output
            on_transcription=print_translation_async  # Callback for translated transcriptions
        )
    ],
    silent=True,  # Set to True to disable verbose logging to console
)
sdk.run(cfg)
```

#### Transcription output options: 📊

1️⃣ **Audio only** (default):
```python
TargetLang(ES, FileWriter("output.wav"))
```

2️⃣ **Transcription only**:
```python
TargetLang(ES, on_transcription=your_callback_function)
```

3️⃣ **Audio and transcription**:
```python
TargetLang(ES, FileWriter("output.wav"), on_transcription=your_callback_function)
```

💡 **The transcription callbacks receive `TranscriptionMessage` objects containing the transcribed text and metadata.**  
🔄 **Callbacks can be either synchronous or asynchronous functions.**

### Integrate with FFmpeg (streaming) 🎬

```python
import io
from speech_translation_sdk import (SpeechTranslationSDK, Config, SourceLang, TargetLang,
                        BufferReader, BufferWriter, AR, EN, RunAsPipe)

ffmpeg_cmd = [
    'ffmpeg',
    '-i', 'speech/ar.mp3',
    '-f', 's16le',      # 16-bit PCM
    '-acodec', 'pcm_s16le',
    '-ar', '48000',     # 48kHz
    '-ac', '1',         # mono
    '-'                 # output to stdout
]

pipe_buffer = RunAsPipe(ffmpeg_cmd)
es_buffer = io.BytesIO()

sdk = SpeechTranslationSDK()
reader = BufferReader(pipe_buffer)
writer = BufferWriter(es_buffer)
cfg = Config(SourceLang(AR, reader), [TargetLang(EN, writer)])
sdk.run(cfg)

print(f"Translated audio written to buffer with size: {es_buffer.getbuffer().nbytes} bytes")
with open("./ar2en_out.wav", "wb") as f:
    f.write(es_buffer.getbuffer())
```

### Using buffers 💾

```python
import io
from speech_translation_sdk import (SpeechTranslationSDK, Config, SourceLang, TargetLang,
                        BufferReader, BufferWriter, AR, EN)
from speech_translation_sdk.internal.audio import convert_any_to_pcm16

en_buffer, es_buffer = io.BytesIO(), io.BytesIO()
with open("speech/ar.mp3", "rb") as f:
    en_buffer.write(convert_any_to_pcm16(f.read()))
sdk = SpeechTranslationSDK()
reader = BufferReader(en_buffer)
writer = BufferWriter(es_buffer)
cfg = Config(SourceLang(AR, reader), [TargetLang(EN, writer)])
sdk.run(cfg)
print(f"Translated audio written to buffer with size: {es_buffer.getbuffer().nbytes} bytes")
with open("./ar2en_out.wav", "wb") as f:
    f.write(es_buffer.getbuffer())
```

### Using default audio devices 🔊

```python
from speech_translation_sdk import SpeechTranslationSDK, Config, SourceLang, TargetLang, DeviceManager, EN, ES

dm = DeviceManager()
reader, writer = dm.get_default_readers_writers()

if reader and writer:
    sdk = SpeechTranslationSDK()
    config = Config(
        source=SourceLang(EN, reader),
        targets=[TargetLang(ES, writer)]
    )
    sdk.run(config)
```

### Async API ⚡

```python
import asyncio
from speech_translation_sdk import SpeechTranslationSDK, Config, SourceLang, TargetLang, FileReader, FileWriter, EN, ES

async def translate():
    sdk = SpeechTranslationSDK()
    config = Config(
        source=SourceLang(EN, FileReader("input.mp3")),
        targets=[TargetLang(ES, FileWriter("output.wav"))]
    )
    await sdk.run(config)

asyncio.run(translate())
```

## I/O Adapters & Mixing 🔌

### Available adapters 🛠️

🎯 **The AI Speech Translation SDK provides flexible I/O adapters that can combined to:**

- 📁 **FileReader/FileWriter**: Read from and write to audio files
- 🎤 **DeviceReader/DeviceWriter**: Use microphones and speakers
- 💾 **BufferReader/BufferWriter**: Work with in-memory buffers
- 🔧 **RunAsPipe**: Run command and represent as pipe (e.g., FFmpeg stdout)

### Mixing examples 🎨

🔄 **Combine any input adapter with any output adapter:**

#### 🎤➡️📁 Microphone to file - record translations
```python
config = Config(
    source=SourceLang(EN, mic),
    targets=[TargetLang(ES, FileWriter("recording_es.wav"))]
)
```

#### 📁➡️🔊 File to speaker - play translations
```python
config = Config(
    source=SourceLang(EN, FileReader("presentation.mp3")),
    targets=[TargetLang(ES, speaker)]
)
```

#### 🎤➡️🔊📁 Microphone to multiple outputs
```python
config = Config(
    source=SourceLang(EN, mic),
    targets=[
        TargetLang(ES, speaker),  # Play Spanish through speaker
        TargetLang(ES, FileWriter("spanish.wav")),  # Save Spanish to file
        TargetLang(FR, FileWriter("french.wav"))    # Save French to file
    ]
)
```

#### 💾➡️💾 Buffer to buffer - for integration
```python
input_buffer = io.BytesIO(audio_data)
output_buffer = io.BytesIO()

config = Config(
    source=SourceLang(EN, BufferReader(input_buffer)),
    targets=[TargetLang(ES, BufferWriter(output_buffer))]
)
```

#### 🔧➡️🔊 FFmpeg pipe to speaker
```python
pipe = RunAsPipe(ffmpeg_process.stdout)
config = Config(
    source=SourceLang(EN, BufferReader(pipe)),
    targets=[TargetLang(ES, speaker)]
)
```

## Features ✨

### Real-time translation ⚡
🎯 Translate audio streams in real-time with minimal latency  
💬 Perfect for live conversations, conferences, and meetings

### Voice cloning 🗣️
🎭 Preserve the original speaker's voice characteristics in translations  
⚙️ Enable voice cloning in the configuration

### Device management 🎮
🎤 Easy device selection with interactive prompts or programmatic access:

```python
dm = DeviceManager()

# Interactive selection
mic, speaker = dm.select_devices_interactive()

# Get devices by name
mic = dm.get_mic_by_name("Blue Yeti")
speaker = dm.get_speaker_by_name("MacBook Pro Speakers")

# List all devices
input_devices = dm.get_input_devices()
output_devices = dm.get_output_devices()
```

## Supported languages 🌍

### Speech recognition languages 🎤
🇸🇦 Arabic (AR), 🇨🇳 Chinese (ZH), 🇨🇿 Czech (CS), 🇩🇰 Danish (DA), 🇳🇱 Dutch (NL), 🇬🇧 English (EN), 🇫🇮 Finnish (FI), 🇫🇷 French (FR), 🇩🇪 German (DE), 🇬🇷 Greek (EL), 🇮🇱 Hebrew (HE), 🇭🇺 Hungarian (HU), 🇮🇹 Italian (IT), 🇯🇵 Japanese (JA), 🇰🇷 Korean (KO), 🇵🇱 Polish (PL), 🇵🇹 Portuguese (PT), 🇷🇺 Russian (RU), 🇪🇸 Spanish (ES), 🇹🇷 Turkish (TR), 🇺🇦 Ukrainian (UK)

### Translation languages 🔄
🇸🇦 Arabic (AR), 🇧🇬 Bulgarian (BG), 🇨🇳 Chinese Mandarin (ZH), 🇨🇿 Czech (CS), 🇩🇰 Danish (DA), 🇳🇱 Dutch (NL), 🇬🇧 English UK (EN_GB), 🇺🇸 English US (EN_US), 🇫🇮 Finnish (FI), 🇫🇷 French (FR), 🇩🇪 German (DE), 🇬🇷 Greek (EL), 🇮🇱 Hebrew (HE), 🇭🇺 Hungarian (HU), 🇮🇩 Indonesian (ID), 🇮🇹 Italian (IT), 🇯🇵 Japanese (JA), 🇰🇷 Korean (KO), 🇵🇱 Polish (PL), 🇵🇹 Portuguese (PT), 🇧🇷 Portuguese Brazilian (PT_BR), 🇷🇴 Romanian (RO), 🇷🇺 Russian (RU), 🇸🇰 Slovak (SK), 🇪🇸 Spanish (ES), 🇲🇽 Spanish Mexican (ES_MX), 🇸🇪 Swedish (SV), 🇹🇷 Turkish (TR), 🇺🇦 Ukrainian (UK), 🇻🇳 Vietnamese (VI)

### Available language constants 📚

```python
from speech_translation_sdk import (
    # English variants - 1.5+ billion speakers (including L2)
    EN, EN_AU, EN_CA, EN_GB, EN_US,

    # Chinese - 1.3+ billion speakers
    ZH,

    # Hindi - 600+ million speakers
    HI,

    # Spanish variants - 500+ million speakers
    ES, ES_MX,

    # Arabic variants - 400+ million speakers
    AR, AR_AE, AR_SA,

    # French variants - 280+ million speakers
    FR, FR_CA,

    # Portuguese variants - 260+ million speakers
    PT, PT_BR,

    # Russian - 260+ million speakers
    RU,

    # Japanese & Korean - 200+ million speakers combined
    JA, KO,

    # Southeast Asian languages - 400+ million speakers
    ID, VI, TA, MS, FIL,

    # Germanic languages - 150+ million speakers
    DE, NL, SV, NO, DA,

    # Other European languages - 300+ million speakers
    TR, IT, PL, UK, RO, EL, HU, CS, BG, SK, FI, HR,

    # Other languages - 40+ million speakers
    AZ, HE
)
```

## Development status 🛠️

### Current status ✅
- ✅ Core SDK functionality
- ✅ GitHub Actions CI/CD
- ✅ Docker packaging
- ✅ Python 3.11, 3.12, 3.13 support
- ✅ PyPI publication (coming soon)
- ✅ Documentation site (coming soon)
- ⏳ Code coverage reporting (setup required)

### Current dev roadmap 🗺️
- ⏳ TODO: global timeout support for long-running tasks
- ⏳ TODO: support for multiple source languages in a single run
- ⏳ TODO: fine cancelling on cancel_all_tasks()
- ⏳ TODO: error handling improvements

### Build status 🏗️
- 🧪 **Tests**: Running on Python 3.11, 3.12, 3.13
- 📦 **Release**: Automated releases with Docker images
- 📊 **Coverage**: Tests implemented, reporting setup needed

## Requirements 📋

- 🐍 Python 3.11+
- 🔑 API credentials (get them at [example.com](https://example.com))

## Support 🤝

- 📚 Documentation: [https://docs.example.com](https://docs.example.com)
- 🐛 Issues: [GitHub Issues](https://github.com/example/speech-translation-sdk/issues)
- 📧 Email: support@example.com

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

© Example Corp, 2025 | 🌍 Breaking down language barriers with AI 🚀
