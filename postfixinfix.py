prioritas = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}


# 1. ubah infix jadi postfix
def infix_ke_postfix(token):
    output = []   # hasil postfix
    stack = []    # tempat operator disimpan sementara

    for t in token:
        if t == "(":
            stack.append(t)
        elif t == ")":
            # keluarkan operator sampai ketemu "("
            while stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()   # buang "("
        elif t in prioritas:
            # keluarkan operator di stack yang prioritasnya lebih tinggi
            # (kalau sama, juga dikeluarkan, kecuali operator barunya ^
            #  karena pangkat dihitung dari kanan: 2 ^ 3 ^ 2 = 2 ^ (3 ^ 2))
            while stack and stack[-1] != "(":
                atas = prioritas[stack[-1]]
                if atas > prioritas[t] or (atas == prioritas[t] and t != "^"):
                    output.append(stack.pop())
                else:
                    break
            stack.append(t)
        else:
            output.append(t)   # angka langsung masuk output

    # sisa operator di stack dikeluarkan semua
    while stack:
        output.append(stack.pop())
    return output


# 2. hitung hasil postfix
def hitung_postfix(token):
    stack = []

    for t in token:
        if t in prioritas:
            b = stack.pop()   # angka kedua
            a = stack.pop()   # angka pertama
            if t == "+":
                stack.append(a + b)
            elif t == "-":
                stack.append(a - b)
            elif t == "*":
                stack.append(a * b)
            elif t == "/":
                stack.append(a / b)
            else:
                stack.append(a ** b)   # pangkat
        else:
            stack.append(float(t))   # angka masuk stack
    return stack[0]


# 3. cek postfix valid (operand harus tepat 1 lebih banyak dari operator)
def cek_postfix(token):
    jumlah = 0   # jumlah operand yang "menunggu" operator
    for t in token:
        if t in ("(", ")"):
            raise ValueError("kurung tidak seimbang")
        elif t in prioritas:
            jumlah = jumlah - 1   # operator memakai 2 operand, menghasilkan 1
            if jumlah < 1:
                raise ValueError("operand kurang")
        else:
            jumlah = jumlah + 1   # operand (angka atau huruf)
    if jumlah != 1:
        raise ValueError("operator kurang")


# 4. cek apakah semua operand berupa angka (kalau huruf, tidak bisa dihitung)
def semua_angka(token):
    for t in token:
        if t not in prioritas:
            try:
                float(t)
            except:
                return False
    return True


# program utama
print("=== INFIX -> POSTFIX ===")
print("Pisahkan dengan spasi, contoh: ( 2 + 3 ) * 4  atau  A + B * C")
print("Ketik 'q' untuk keluar\n")

while True:
    teks = input("Infix   : ")
    if teks == "q":
        break

    try:
        token = teks.split()
        postfix = infix_ke_postfix(token)
        cek_postfix(postfix)
        print("Postfix :", " ".join(postfix))

        # kalau semua operand angka, hasilnya sekalian dihitung
        if semua_angka(postfix):
            print("Hasil   :", hitung_postfix(postfix))
        print()
    except:
        print("Input tidak valid\n")
