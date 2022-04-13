while True:
    try:
        print("""
        ███╗   ██╗███████╗███╗   ███╗███████╗███████╗██╗███████╗
        ████╗  ██║██╔════╝████╗ ████║██╔════╝██╔════╝██║██╔════╝
        ██╔██╗ ██║█████╗  ██╔████╔██║█████╗  ███████╗██║███████╗
        ██║╚██╗██║██╔══╝  ██║╚██╔╝██║██╔══╝  ╚════██║██║╚════██║
        ██║ ╚████║███████╗██║ ╚═╝ ██║███████╗███████║██║███████║
        ╚═╝  ╚═══╝╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝╚═╝╚══════╝
                    Dev : D O R T R O 乂\n\n
        """)
        decenc = input("Press 1 to encode\nPress 2 to decode\n").lower()
    
        if decenc == "1":
            cipher = input("Type your message to encode:\n")

            l = []
            e = ""
            if " " in cipher:
                cipher = cipher.replace(" ", "-")
            else:
                pass
            for i in cipher:
                n = ord(i) * len(cipher) * 2
                l.append(hex(n))
            for i in l:
                n = i[::-1].split('x0')
                news = "".join(n)
                e += news
            print(f"Cipher: {e[::-1]}")
        elif decenc == "2":
            cipher = input("Type your message to decode:\n")

            f = cipher[::-1]
            pure = []
            hexx = []
            last = ""
            for i in range(0, len(f), 3):
                pure.append(f[i:i+3])

            for i in pure:
                hexx.append(i[::-1])

            for i in hexx:
                last += chr(int(i, 16) // len(hexx) // 2)

            if "-" in last:
                last = last.replace("-", " ")

            print(f"Message : {last}")
        else:
            pass

        while True:
            try:
                loop = input("Want to Encode/Decode next text?\n[y/n]: ").lower()
                if loop == "n" or loop == "y":
                    break
                print("Invalid input!")
            except Exception as e:
                print(e)
        if loop == "n":
            break
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')
    except Exception as e:
        print(e)
