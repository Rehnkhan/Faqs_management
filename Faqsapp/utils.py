from googletrans import Translator
from googletrans import LANGUAGES
import logging

logger = logging.getLogger(__name__)

translator = Translator()

def translate_text(lang: str, text: str,retries=3) -> str:
    if lang not in LANGUAGES:
        return f"Error: Unsupported language '{lang}'"

    translator = Translator()
    for attempt in range(retries):
        try:
            translation = translator.translate(text, dest=lang)
            return translation.text
        except Exception as e:
            logger.error(f"Translation Error ({lang}): {e}")
            if attempt < retries - 1:
                continue  # Retry
            return text  # Fallback to original text if translation fails