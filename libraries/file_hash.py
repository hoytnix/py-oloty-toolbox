import hashlib

def file_checksum(fp):
    try:
        with open(fp, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except: # File does not exist yet.
        return ""