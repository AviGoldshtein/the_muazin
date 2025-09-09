from faster_whisper import WhisperModel
from tempfile import NamedTemporaryFile
import os


class Convertor:
    def speech_to_text(self, audio_file_bytes):
        with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(audio_file_bytes)
            temp_file.flush()

        transcription_result = self._transcribe_audio(file_path=temp_file.name, device="cpu", compute_type="float32")

        text = ""
        for segment in transcription_result:
            text += segment.text

        os.remove(temp_file.name)
        return text


    def _transcribe_audio(self, file_path, model_size="small", device="cuda", compute_type="float16"):
        # Initialize the Whisper model
        model = WhisperModel(model_size, device=device, compute_type=compute_type)

        # Transcribe the audio file
        print(file_path)
        segments, info = model.transcribe(file_path)
        return segments