import easyocr

reader = easyocr.Reader(['en'])

def extract_text_from_image(path):

    result = reader.readtext(path)

    text = " ".join(
        [item[1] for item in result]
    )

    return text