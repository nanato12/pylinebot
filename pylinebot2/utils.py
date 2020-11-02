#  Copyright 2020 nanato12

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

"""pylinebot.utils module."""

from io import BytesIO

from PIL import Image


def img_file_to_bytes(
    file_name: str, format: str = "jpeg", rich: bool = False
) -> bytes:
    img: Image = Image.open(file_name)
    if rich:
        img = img.resize((800, 350))
    with BytesIO() as output:
        img.save(output, format=format)
        img_bytes: bytes = output.getvalue()
    return img_bytes
