def func(a):
    if '' in a:
        a[a.index('')] = '0'
    return a

if __name__ == '__main__':
    with open('ti-92_lab_20_var_29_PlaksytskyiVA_f.txt', 'r') as f_file, \
            open('ti-92_lab_20_var_29_PlaksytskyiVA_g.txt', 'w') as g_file:

        file_read = open('ti-92_lab_20_var_29_PlaksytskyiVA_f.txt', 'r').readlines()

        x_list = [a[:a.index('x')].replace(' ', '').replace('+', '') for a in file_read]
        y_list = [a[a.index('x') + 1: a.index('y')].replace(' ', '').replace('+', '') for a in file_read]
        z_list = [a[a.index('y') + 1: a.index('=')].replace(' ', '').replace('+', '') for a in file_read]

        x_list = [int(i) for i in func(x_list)]
        y_list = [int(i) for i in func(y_list)]
        z_list = [int(i) for i in func(z_list)]

        g_file.write("{:d}, {:d}, {:d}\n".format(x_list[0], y_list[0], z_list[0]))
        for i, j, k in zip(x_list[1:], y_list[1:], z_list[1:]):
            if (x_list[0] / i) == (y_list[0] / j) or (i / x_list[0]) == (j / y_list[0]):
                g_file.write("{:d}, {:d}, {:d}\n".format(i, j, k))