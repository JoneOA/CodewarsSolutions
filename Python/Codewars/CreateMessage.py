def create_message(s):
    xs = [s]
    def wrapper(other=''):
        if not other:
            return ' '.join(xs)
        xs.append(other)
        return wrapper
    return wrapper

print(create_message("World")("Hello")("hraf")("FAFDFAD"))