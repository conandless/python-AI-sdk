from palabra_ai import (SpeechTranslationSDK, Config, SourceLang, TargetLang,
                        DeviceManager, EN, ES)

sdk = SpeechTranslationSDK()

if __name__ == "__main__":
    dm = DeviceManager()
    mic, speaker = dm.select_devices_interactive()
    cfg = Config(SourceLang(EN, mic), [TargetLang(ES, speaker)])
    sdk.run(cfg)
