def generate_primes(n):
    """
    ฟังก์ชันนี้จะค้นหาจำนวนเฉพาะทั้งหมดที่น้อยกว่าหรือเท่ากับ n
    และคืนค่ากลับเป็นสตริงที่คั่นด้วยเครื่องหมาย ", "
    """
    # สร้างลิสต์ว่างสำหรับเก็บจำนวนเฉพาะ
    primes = []

    # วนลูปตั้งแต่ 2 ถึง n เพื่อตรวจสอบทีละตัวเลข
    for num in range(2, n + 1):
        is_prime = True
        # ตรวจสอบว่า num เป็นจำนวนเฉพาะหรือไม่
        # โดยหารด้วยตัวเลขตั้งแต่ 2 จนถึงรากที่สองของ num
        # หากหารลงตัว แสดงว่าไม่ใช่จำนวนเฉพาะ
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        
        # ถ้า is_prime ยังเป็น True แสดงว่าเป็นจำนวนเฉพาะ ให้เพิ่มลงในลิสต์
        if is_prime:
            primes.append(num)
            
    # แปลงลิสต์ของตัวเลขเป็นสตริง และคั่นด้วย ", "
    return ", ".join(map(str, primes))

# ตัวอย่างการใช้งานตามโจทย์
print(f"generate_primes(10) # Output: \"{generate_primes(10)}\"")
print(f"generate_primes(20) # Output: \"{generate_primes(20)}\"")
print(f"generate_primes(1)  # Output: \"{generate_primes(1)}\"")
print(f"generate_primes(2)  # Output: \"{generate_primes(2)}\"")