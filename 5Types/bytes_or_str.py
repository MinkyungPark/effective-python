# bytes or str 인스턴스를 받아 항상 str 리턴
def to_str(bytes_or_str):
    if isinstance(bytes_or_str, bytes):
        value = bytes_or_str.decode("utf-8")
    else:
        value = bytes_or_str
    return value


# bytes or str 인스턴스를 받아 항상 bytes 리턴
def to_bytes(bytes_or_str):
    if isinstance(bytes_or_str, str):
        value = bytes_or_str.encode("utf-8")
    else:
        value = bytes_or_str
    return value


print(repr(to_str(b"foo")))  # 'foo'
print(repr(to_str("bar")))  # 'bar'
print(repr(to_str(b"\xed\x95\x9c")))  # '한'

print(repr(to_bytes(b"foo")))  # b'foo'
print(repr(to_bytes("bar")))  # b'bar'
print(repr(to_bytes("한")))  # b'\xed\x95\x9c'