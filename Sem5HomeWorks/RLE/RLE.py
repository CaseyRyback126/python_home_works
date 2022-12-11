# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.


my_text = 'AAaaaAdddLLkkKKfffffffKKDDnnrRR'


def encode_rle(ss: str):
    str_code = ''
    prev_char = ''
    count = 1
    for char in ss:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code


str_coder = encode_rle(my_text)
print(str_coder)

my_text2 = '2V5q6g3Q5s7D4p'


def decoding_rle(ss: str):
    count = ''
    str_decode = ''
    for char in ss:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode


str_decoder = decoding_rle(my_text2)
print(str_decoder)
