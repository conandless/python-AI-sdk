from palabra_ai import (SpeechTranslationSDK, Config, SourceLang, TargetLang,
                        FileReader, FileWriter, EN, ES)

sdk = SpeechTranslationSDK()

if __name__ == "__main__":
    reader = FileReader("./speech/es.mp3")
    writer = FileWriter("./es2en_out.wav")
    cfg = Config(SourceLang(ES, reader), [TargetLang(EN, writer)])
    sdk.run(cfg)
