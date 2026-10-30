PRIORITAS = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
KANAN = {'^'}  # ^ asosiatif kanan

def infix_ke_postfix(ekspresi):
    stack, output = [], []
    for t in ekspresi.replace(" ", ""):
        if t.isalnum():                  # operand -> langsung ke output
            output.append(t)
        elif t == '(':                   # kurung buka -> push
            stack.append(t)
        elif t == ')':                   # kurung tutup -> pop sampai '('
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()                  # buang '('
        else:                            # operator
            while (stack and stack[-1] != '(' and
                   (PRIORITAS[stack[-1]] > PRIORITAS[t] or
                    (PRIORITAS[stack[-1]] == PRIORITAS[t] and t not in KANAN))):
                output.append(stack.pop())
            stack.append(t)
    while stack:                         # sisa stack -> output
        output.append(stack.pop())
    return ' '.join(output)


# ---------- PROGRAM UTAMA (pakai input) ----------
print("=== INFIX -> POSTFIX ===")
print("Contoh: A + (B * C - (D / E ^ F) * G) * H")
print("Operator: + - * / ^   |   Ketik 'q' untuk keluar\n")

while True:
    teks = input("Infix   : ")
    if teks.lower() == "q":
        break

    # cek kurung seimbang
    if teks.count("(") != teks.count(")"):
        print("Input tidak valid (kurung tidak seimbang)\n")
        continue

    # cek karakter: hanya huruf/angka, operator, dan kurung
    salah = False
    for c in teks.replace(" ", ""):
        if not c.isalnum() and c not in PRIORITAS and c not in "()":
            salah = True
    if salah:
        print("Input tidak valid (ada karakter yang tidak dikenali)\n")
        continue

    try:
        print("Postfix :", infix_ke_postfix(teks), "\n")
    except (KeyError, IndexError):
        print("Input tidak valid\n")
