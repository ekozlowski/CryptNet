# This file is part of CryptNet.
# 
# CryptNet is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import uuid
from datetime import datetime
from calendar import timegm
from hashlib import sha512

def int_to_bytearray(integer, length=4):
    b = bytearray(length)
    i = length-1
    while integer > 0 and i >= 0:
        b[i]=integer%256
        i -= 1
        integer = int(integer/256)
    return b


class Payload:
    """CryptNet Message Payload template"""

    payloadString = 'Default Message'

    def serialize(self):
        return bytearray(self.payloadString, 'utf-8')

    @staticmethod
    def deserialize(rawString):
        p = Payload()
        p.payloadString = rawString
        return p


class Message:
    """CryptNet Message
    
    Format: [16Bytes:msgUuid][8Bytes:timestamp][1Bytes:msgPluginIdLength][xBytes:msgPluginId][64Bytes:recipient][encrypted:[64Bytes:sender][4Bytes:payloadLength][xBytes:payload][64Bytes:signedPayloadHash]]
    """
    
    def __init__(self, recipient, sender, pluginId=None, payload=None):
        if pluginId is None:
            pluginId = ''
        elif pluginId.__len__() >= 256:
            raise TypeError('pluginId cannot be longer than 255 characters')
        if payload is None:
            payload = Payload()
        self.msgUuid = uuid.uuid4()
        self.time = datetime.utcnow()
        self.recipient = recipient
        self.sender = sender
        self.pluginId = pluginId
        self.payload = payload

    def to_bytes(self):
        b = bytearray()
        b += self.msgUuid.bytes
        b += int_to_bytearray(timegm(self.time.utctimetuple()),8)
        b += bytes([self.pluginId.__len__()])
        b += bytearray(self.pluginId, 'utf-8')
        b += self.recipient

        p = bytearray()
        p += self.sender
        pBytes = self.payload.serialize()
        p += int_to_bytearray(pBytes.__len__(),4)
        p += pBytes
        p += sha512(pBytes).digest() # Add Signing

        # Encrypt P
        b += p

        return b

    @staticmethod
    def from_bytes(byteArray):
        raise NotImplementedError('Convert Bytes to Message Object')

