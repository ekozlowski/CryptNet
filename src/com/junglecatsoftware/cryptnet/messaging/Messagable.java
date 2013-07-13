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

public interface Messagable {
	public void inboundMessage(Message message);
	public void outboundMessage(Message message);
}
