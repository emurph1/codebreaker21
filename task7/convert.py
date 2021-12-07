import uuid
import binascii
x = uuid.UUID('{4da468db-1daa-481c-9be7-d9feee42a436}')

bytesx = x.bytes

# get the length of uuid and then convert to hex
# print(len(bytesx))

magic_start = bytes.fromhex("1553DC11") # uint32 = 4 bytes
cmd_param = bytes.fromhex("1700") # uint16 = 2 bytes
cmd_length = bytes.fromhex("0002") # size_t
cmd_data = bytes.fromhex("0002") # uint16 = 2 bytes
uuid_param = bytes.fromhex("1708") # uint16 = 2 bytes
uuid_length = bytes.fromhex("0010") # size_t but it is uint16 = 2 bytes
uuid = bytesx 
magic_end = bytes.fromhex("E38A5B8C")

everything = magic_start + cmd_param + cmd_length + cmd_data + uuid_param + uuid_length + uuid + magic_end

print(everything.hex())
