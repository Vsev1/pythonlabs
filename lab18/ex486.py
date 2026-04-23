if __name__ == '__main__':
    with open('ti-92_lab_18_var_29_PlaksytskyiVA_f.txt', 'r') as f_file, \
            open('ti-92_lab_18_var_29_PlaksytskyiVA_g.txt', 'r') as g_file, \
            open('ti-92_lab_18_var_29_PlaksytskyiVA_h.txt', 'w') as h_file:
        h_file.write(f_file.read() + '\n' + g_file.read())
