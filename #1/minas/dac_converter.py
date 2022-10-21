def dac_converter(no: int):
    digit_no = 1024/no
    print('digit no ', digit_no)
    final_op = 5/digit_no
    str_final = str(round(final_op, 2))
    print('final output :', str_final)


in_no = input('Enter no: ')
no = int(in_no)
dac_converter(no)

