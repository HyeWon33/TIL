# def add(foo, bar):
#     out = {}
#     for key in foo:
#         out[key] = foo[key] + bar[key]
#     return out

# def subtract(foo, bar):
#     out = {}
#     for key in foo:
#         if key in bar:
#             out[key] = foo[key] - bar[key]
#     return out

# def multiply(foo, bar):
#     out = {}
#     for key in foo:
#         if key in bar:
#             out[key] = foo[key] * bar[key]
#     return out

# def divide(foo, bar):
#     out = {}
#     for key in foo:
#         if key in bar:
#             out[key] = foo[key] / bar[key]
#     return out            


#연습문제
def add(foo, bar):
    return {fkey: foo[fkey] + bar[fkey] for fkey in foo if fkey in bar}
