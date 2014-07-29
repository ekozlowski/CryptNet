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

import uuid, pickle, time

class Message:
    """CryptNet Message"""
    
    def __init__(self, msgClass=0, msgType=0, dest=None, src=None, content=None):
        self.msgUuid = str(uuid.uuid4())
        self.time = time.time()
        self.msgClass = msgClass
        self.msgType = msgType
        self.dest = dest
        self.src = src
        self.content = content

    def encryptMessage(self):
        """Creates CryptNet EncryptedMessage based on this Message instance"""
        print("Not Implemented")
    
    def serialize(self):
        return pickle.dumps(self)

class EncryptedMessage
    """CryptNet EncryptedMessage"""

    def __init__(self, msgClass=0, msgType=0, dest=None, msgUuid=None, payload=None):
        self.msgUuid = msgUuid
        self.msgClass = msgClass
        self.msgType = msgType
        self.dest = dest
        self.payload = payload

    def decryptMessage(self):
        """Creates CryptNet Message based on this EncryptedMessage instance"""
        print("Not Implemented")

    def serialize(self):
        return pickle.dumps(self)

def deserialize(pickleBytes):
    return pickle.loads(pickleBytes)
