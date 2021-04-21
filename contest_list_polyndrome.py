# поиск палиндрома

def check_poly(c):
    if c != c[::-1]:  # -1 здесь шаг строки: от конца к началу
        return False
    else:
        return True


arg = "ANNA"
print(check_poly(arg))