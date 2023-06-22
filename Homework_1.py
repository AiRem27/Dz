# def pal(s):
#     if len(s)<=1:
#         return True
#     if s[0]!=s[-1]:
#         return False
#     return pal(s[1:-1])
# print(pal("шабабабабабаш"))

def is_palindrome(str):
    return str == str[::-1]

result = is_palindrome("лепсспел")
print(result)  # True

result = is_palindrome("helloworld")
print(result)  # False