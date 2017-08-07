


with open("filesystem.img", "rb") as fs:
    offset = 0
    buffer = b""
    image = b""
    writing = False
    counter = 0

    def flush_image():
        global counter, image, writing
        with open("image{}.jpg".format(counter), "wb") as jpg:
            jpg.write(image)
            image = b""
            writing = False
            counter += 1

    while True:
        buffer = fs.read(2)
        offset += 2

        if not buffer:
            if writing:
                print("[!] ERROR: EOF while still reading image, flushing anyways!")
                flush_image()
            else:
                print("[+] Done!")
            break

        if buffer == b"\xFF\xD8":
            print("[+] Found JPG header at {}".format(hex(offset)))
            writing = True
            image += buffer
            continue

        if writing and buffer == b"\xFF\xD9":
            print("[+] Found JPG EOF at {}".format(hex(offset)))
            image += buffer
            flush_image()
            continue

        if writing:
            image += buffer




