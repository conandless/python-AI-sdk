import io
from palabra_ai import (SpeechTranslationSDK, Config, SourceLang, TargetLang,
                        BufferReader, BufferWriter, AR, EN)
from palabra_ai.internal.audio import convert_any_to_pcm16

if __name__ == "__main__":
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