# standard
from io import BytesIO

# third party
from PIL import Image

class Func:

    @staticmethod
    def img_file_to_bytes(file_name, format='jpeg', rich=False):
        img = Image.open(file_name)
        if rich:
            img = img.resize((800, 350))
        with BytesIO() as output:
            img.save(output, format=format)
            img_bytes = output.getvalue()
        return img_bytes
