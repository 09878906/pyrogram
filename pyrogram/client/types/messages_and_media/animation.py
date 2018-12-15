# Pyrogram - Telegram MTProto API Client Library for Python
# Copyright (C) 2017-2018 Dan Tès <https://github.com/delivrance>
#
# This file is part of Pyrogram.
#
# Pyrogram is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pyrogram is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from struct import pack

from pyrogram.api import types
from pyrogram.api.core import Object
from .photo_size import PhotoSize
from ...ext.utils import encode


class Animation(Object):
    """This object represents an animation file (GIF or H.264/MPEG-4 AVC video without sound).

    Args:
        file_id (``str``):
            Unique identifier for this file.

        width (``int``):
            Animation width as defined by sender.

        height (``int``):
            Animation height as defined by sender.

        duration (``int``):
            Duration of the animation in seconds as defined by sender.

        thumb (:obj:`PhotoSize <pyrogram.PhotoSize>`, *optional*):
            Animation thumbnail.

        file_name (``str``, *optional*):
            Animation file name.

        mime_type (``str``, *optional*):
            Mime type of a file as defined by sender.

        file_size (``int``, *optional*):
            File size.

        date (``int``, *optional*):
            Date the animation was sent in Unix time.
    """

    ID = 0xb0700025

    def __init__(self, file_id: str, width: int, height: int, duration: int, *,
                 thumb=None, file_name: str = None, mime_type: str = None, file_size: int = None, date: int = None,
                 client=None, raw=None):
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
        self.date = date
        self.width = width
        self.height = height
        self.duration = duration

        self._client = client
        self._raw = raw

    @staticmethod
    def parse(client, animation: types.Document, video_attributes: types.DocumentAttributeVideo,
              file_name: str) -> "Animation":
        return Animation(
            file_id=encode(
                pack(
                    "<iiqq",
                    10,
                    animation.dc_id,
                    animation.id,
                    animation.access_hash
                )
            ),
            width=getattr(video_attributes, "w", 0),
            height=getattr(video_attributes, "h", 0),
            duration=getattr(video_attributes, "duration", 0),
            thumb=PhotoSize.parse(client, animation.thumb),
            mime_type=animation.mime_type,
            file_size=animation.size,
            file_name=file_name,
            date=animation.date,
            client=client,
            raw=animation
        )
