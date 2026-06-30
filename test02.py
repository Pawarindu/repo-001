ef parse_client_blob(raw):
    # Expect exactly 8-byte header + 32-byte X + 32-byte Y
    if len(raw) != 72:
        return None
    magic, cb_key = struct.unpack('<II', raw[:8])