import io
from palabra_ai import (SpeechTranslationSDK, Config, SourceLang, TargetLang,
                        BufferReader, BufferWriter, AR, EN, RunAsPipe)
if __name__ == "__main__":
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
