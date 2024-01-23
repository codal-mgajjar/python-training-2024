from io import StringIO, BytesIO

#read in StringIO
data = StringIO("hello")
print(data.read())

#write in StringIO
data.write(" World")
data.seek(0)
print(data.read())

# Retreive full file
print(data.getvalue())

#close IO stream
data.close()
print(data.closed)


#bytes IO
stream_str = BytesIO(b"JournalDev Python: \x00\x01")
print(stream_str.getvalue())
