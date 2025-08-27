# ข้อมูลสินค้าคงคลังเริ่มต้น
inventory = [
    ["Apple", 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

# 1. ฟังก์ชันสำหรับอัปเดตจำนวนสินค้าหลังการขาย
def update_inventory(inventory, item_name, quantity_sold):
    """ลดจำนวนสินค้าในสต็อกตามชื่อและจำนวนที่ขายไป"""
    for item in inventory:
        if item[0] == item_name:
            item[1] -= quantity_sold
            break # ออกจากลูปเมื่อเจอสินค้าแล้ว

# 2. ฟังก์ชันสำหรับคำนวณมูลค่ารวมของสินค้าทั้งหมด
def calculate_total_value(inventory):
    """คำนวณมูลค่ารวมของสินค้าทั้งหมดในสต็อก (จำนวน * ราคา)"""
    total_value = 0
    for item in inventory:
        quantity = item[1]
        price = item[2]
        total_value += quantity * price
    return total_value

# 3. ฟังก์ชันสำหรับค้นหาสินค้าที่ราคาสูงที่สุด
def find_most_expensive(inventory):
    """ค้นหาและคืนชื่อของสินค้าที่มีราคาสูงที่สุด"""
    if not inventory:
        return None # คืนค่า None ถ้าไม่มีสินค้าในสต็อก
    
    most_expensive_item = max(inventory, key=lambda item: item[2])
    return most_expensive_item[0]

# 4. ฟังก์ชันสำหรับเพิ่มสินค้าใหม่ หรืออัปเดตข้อมูลสินค้าเดิม
def add_item(inventory, item_name, quantity, price):
    """เพิ่มสินค้าใหม่ หรืออัปเดตจำนวนและราคาของสินค้าที่มีอยู่แล้ว"""
    for item in inventory:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            return # อัปเดตแล้วออกจากฟังก์ชัน
            
    # ถ้าวนลูปจนจบแล้วไม่เจอสินค้า ให้เพิ่มเป็นรายการใหม่
    inventory.append([item_name, quantity, price])

# --- ส่วนของการดำเนินการตามโจทย์ (Actions) ---

print("--- สถานะเริ่มต้น ---")
print("Inventory เริ่มต้น:", inventory)
print("-" * 25)

# 1. อัปเดตสต็อกหลังจากขายกล้วยไป 20 ลูก
print("1. ขายกล้วยไป 20 ลูก:")
update_inventory(inventory, "Banana", 20)
print("   Inventory หลังอัปเดต:", inventory)
print("-" * 25)


# 2. คำนวณมูลค่ารวมของสินค้าในสต็อก
print("2. คำนวณมูลค่ารวมของสต็อก:")
total_value = calculate_total_value(inventory)
print(f"   มูลค่ารวมของสินค้าทั้งหมด: ${total_value:.2f}")
print("-" * 25)


# 3. ค้นหาสินค้าที่แพงที่สุด
print("3. ค้นหาสินค้าที่แพงที่สุด:")
most_expensive = find_most_expensive(inventory)
print(f"   สินค้าที่แพงที่สุดคือ: {most_expensive}")
print("-" * 25)


# 4. เพิ่ม "Eggs" 30 ฟอง ราคาฟองละ $0.25
print("4. เพิ่มและอัปเดต 'Eggs':")
add_item(inventory, "Eggs", 30, 0.25)
print("   Inventory หลังจากเพิ่ม Eggs:", inventory)

#    จากนั้นอัปเดต "Eggs" เป็น 50 ฟอง ราคาฟองละ $0.30
add_item(inventory, "Eggs", 50, 0.30)
print("   Inventory หลังจากอัปเดต Eggs:", inventory)
print("-" * 25)