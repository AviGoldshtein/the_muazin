from faster_whisper import WhisperModel
from tempfile import NamedTemporaryFile
from services.speech_to_text.logic.logger import Logger
import os


class Convertor:
    def __init__(self):
        self.logger = Logger.get_logger(name=__name__)

    def speech_to_text(self, audio_file_bytes):
        try:
            with NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                temp_file.write(audio_file_bytes)
                temp_file.flush()

            transcription_result = self._transcribe_audio(file_path=temp_file.name, device="cpu", compute_type="float32")

            self.logger.info(f"the process of transcription was successfully for file: {temp_file.name}")
            os.remove(temp_file.name)
            return "".join([segment.text for segment in transcription_result])
        except Exception as e:
            self.logger.error(f"error while transcribing file: {temp_file.name},\n{e}")

    def _transcribe_audio(self, file_path, model_size="small", device="cuda", compute_type="float16"):
        model = WhisperModel(model_size, device=device, compute_type=compute_type)

        segments, info = model.transcribe(file_path)
        return segments