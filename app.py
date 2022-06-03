

input_text = Element("input_text")

op = Element("output")

def clear(*args, **kwargs):
    input_text.clear()

def count(*args, **kwargs):
    number = len(input_text.value)
    op.write(number)
    