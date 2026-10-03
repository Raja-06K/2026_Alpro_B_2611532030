# ==============================================================================
# Program Jam Pasir Kristal Palindromik Berbingkai
# ==============================================================================

print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK (PEKAN 5) ===")

# Input nilai N dari pengguna
n_1234 = int(input("Masukkan ukuran skala jam pasir (N): "))

# ------------------------------------------------------------------------------
# 1. BINGKAI ATAS
# ------------------------------------------------------------------------------
print("#", end="")
for k_1234 in range(4 * n_1234 + 5):
    print("=", end="")
print("#")

# ------------------------------------------------------------------------------
# 2. FASE 1: JAM PASIR ATAS (Mundur dari N ke 1)
# ------------------------------------------------------------------------------
for baris_1234 in range(n_1234, 0, -1):
    # Sisi kiri: Bingkai dan padding
    print("| ", end="")
    
    # Spasi penyeimbang kiri
    for s_1234 in range(2 * (n_1234 - baris_1234)):
        print(" ", end="")
        
    # Deret angka mundur (baris -> 1)
    for a_1234 in range(baris_1234, 0, -1):
        print(a_1234, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju (1 -> baris)
    for a_1234 in range(1, baris_1234 + 1):
        print("", a_1234, end="")
        
    # Spasi penyeimbang kanan
    for s_1234 in range(2 * (n_1234 - baris_1234)):
        print(" ", end="")
        
    # Sisi kanan: Padding dan bingkai
    print(" |")

# ------------------------------------------------------------------------------
# 3. FASE 2: POROS TITIK PUSAT (Nol / Singularity)
# ------------------------------------------------------------------------------
print("|", end="")
for s_1234 in range(2 * n_1234 + 1):
    print(" ", end="")

print("<*>", end="")

for s_1234 in range(2 * n_1234 + 1):
    print(" ", end="")
print("|")

# ------------------------------------------------------------------------------
# 4. FASE 3: JAM PASIR BAWAH (Maju dari 1 ke N)
# ------------------------------------------------------------------------------
for baris_1234 in range(1, n_1234 + 1):
    # Sisi kiri: Bingkai dan padding
    print("| ", end="")
    
    # Spasi penyeimbang kiri
    for s_1234 in range(2 * (n_1234 - baris_1234)):
        print(" ", end="")
        
    # Deret angka mundur (baris -> 1)
    for a_1234 in range(baris_1234, 0, -1):
        print(a_1234, end=" ")
        
    # Poros kristal tengah
    print("<*>", end="")
    
    # Deret angka maju (1 -> baris)
    for a_1234 in range(1, baris_1234 + 1):
        print("", a_1234, end="")
        
    # Spasi penyeimbang kanan
    for s_1234 in range(2 * (n_1234 - baris_1234)):
        print(" ", end="")
        
    # Sisi kanan: Padding dan bingkai
    print(" |")

# ------------------------------------------------------------------------------
# 5. BINGKAI BAWAH
# ------------------------------------------------------------------------------
print("#", end="")
for k_1234 in range(4 * n_1234 + 5):
    print("=", end="")
print("#")