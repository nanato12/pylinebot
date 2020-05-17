from io import BytesIO
from PIL import Image

class Func:
    def save_content_from_message_id(self, message_id, file_name):
        content = self.get_message_content(message_id).content
        with open(file_name, 'wb') as content_file:
            content_file.write(content)

    def save_image_from_rich_id(self, rich_id, file_name):
        content = self.get_rich_menu_image(rich_id).content
        with open(file_name, 'wb') as content_file:
            content_file.write(content)

    def img_file_to_bytes(self, file_name, format='jpeg', rich=False):
        img = Image.open(file_name)
        if rich:
            img = img.resize((800, 350))
        with BytesIO() as output:
            img.save(output, format=format)
            img_bytes = output.getvalue()
        return img_bytes
