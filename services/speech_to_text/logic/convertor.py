import pathlib
from faster_whisper import WhisperModel


class Convertor:
    def speech_to_text(self, file_path):
        audio_file = pathlib.Path(file_path)
        transcription_result = self._transcribe_audio(audio_file, device="cpu", compute_type="float32")

        text = ""
        for segment in transcription_result:
            # print(f"[{segment.start:.2f} - {segment.end:.2f}] {segment.text}")
            text += segment.text
        return text


    def _transcribe_audio(self, file_path, model_size="small", device="cuda", compute_type="float16"):
        # Initialize the Whisper model
        model = WhisperModel(model_size, device=device, compute_type=compute_type)

        # Transcribe the audio file
        segments, info = model.transcribe(file_path)
        return segments