import marshal
import dis
with open("./__pycache__/hello_chai.cpython-313.pyc","rb") as f:
    f.read(16)
    code_obj = marshal.load(f)

dis.dis(code_obj)