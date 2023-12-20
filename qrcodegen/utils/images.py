import base64
import io
import logging

import qrcode

logger = logging.getLogger(__name__)


def to_b64(b: bytes) -> str:
    try:
        encoded = base64.b64encode(b)
        decoded = encoded.decode("utf-8")
        return decoded
    except Exception as e:
        logger.error(e)
        return ""


def generate_qr_code(text: str) -> str:
    st = io.BytesIO()
    img = qrcode.make(text)
    img.save(st, "PNG")
    st.seek(0)
    byte_img = st.read()
    st.close()

    return byte_img
