from palabra_ai import (
    SpeechTranslationSDK,
    Config,
    SourceLang,
    TargetLang,
    FileReader,
    FileWriter,
    EN,
    ES,
)
from palabra_ai.base.message import TranscriptionMessage

def print_transcription(msg: TranscriptionMessage):
    print(f"Transcription: {msg.text}")

async def print_translation_async(msg: TranscriptionMessage):
    print(f"Translation: {msg.text}")

sdk = SpeechTranslationSDK()

if __name__ == '__main__':
    cfg = Config(
        source=SourceLang(
            EN,
            FileReader("speech/en.mp3"),
            print_transcription
        ),
        targets=[
            TargetLang(
                ES,
                # you can use only transcription without audio writer if you want
                # FileWriter("./test_output.wav"),
                on_transcription=print_translation_async
            )
        ],
        silent=True,  # Set to True to disable verbose logging to console
    )
    sdk.run(cfg)
