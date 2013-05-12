def open(fileName, mode):
    return FileObject()

class FileObjectState:
    OPEN = 0
    CLOSED = 1

class FileObject:

    state = FileObjectState.CLOSED

    def __init__(self):
        state = FileObjectState.OPEN

    def readline(self):
        resultString = "02 00 01 00 00 00 00 00 00"
        return resultString

    def close(self):
        state = FileObjectState.CLOSED
