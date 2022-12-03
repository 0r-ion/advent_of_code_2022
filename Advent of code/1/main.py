def main():
    file = open('data.txt', 'r')
    most = 0
    temp = 0
    for line in file:
        if line != '\n':
            try:
                temp += int(line)
            except:
                continue
        else:
            if temp >= most:
                most = temp
            temp = 0
    print(most)
            

if __name__ == '__main__':
    main()
    # print(f"exit code:{main()}")
