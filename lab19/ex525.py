if __name__ == '__main__':
    with open('ti-92_lab_19_var_29_PlaksytskyiVA_f.txt', 'r') as f_file:
        print([a for a in f_file if a.find('ab') != -1])
