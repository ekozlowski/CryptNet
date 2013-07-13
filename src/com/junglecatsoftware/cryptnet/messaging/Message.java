/* 
 * Copyright 2012 Bryan Wyatt
 * 
 * This file is part of CryptNet.
 *  
 * CryptNet is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * CryptNet is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License
 * along with CryptNet.  If not, see <http://www.gnu.org/licenses/>.
 */

package com.junglecatsoftware.cryptnet.messaging;

import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.util.UUID;

public class Message {
	private static byte[] messageType = {(byte)0,(byte)0,(byte)0};
	private UUID messageID;
	
	public Message(){
		this(UUID.randomUUID());
	}
	
	public Message(UUID messageID){
		this.messageID = messageID;
	}
	
	public byte[] getByteArray(){
		byte[] messageIDBytes = getBytesFromUUID(messageID);
		byte[] buffer = new byte[messageType.length + messageIDBytes.length];
		System.arraycopy(messageType, 0, buffer, 0, messageType.length);
		System.arraycopy(messageIDBytes, 0, buffer, messageType.length, messageIDBytes.length);
		return buffer;
	}
	
	public static byte[] getBytesFromUUID(UUID uuid){
		byte[] bytes = new byte[16];
		ByteBuffer buffer = ByteBuffer.wrap(bytes);
		buffer.order(ByteOrder.BIG_ENDIAN);
		buffer.putLong(uuid.getMostSignificantBits());
		buffer.putLong(uuid.getLeastSignificantBits());
		return bytes;
	}
	
}
