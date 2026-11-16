"""
Pyramid H Language - Advanced Algorithmic Simulation
Author: Fadwa (2026)
Description: High-performance simulation to compute prime symmetry bridges 
across large computational horizons (e.g., H_10000 and beyond).
"""

import math
import time

def is_prime(num: int) -> bool:
    """التحقق السريع من الأعداد الأولية"""
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def analyze_pyramid_horizon(target_n: int):
    """
    تحليل الهرم عند قمة ضخمة واستخراج إحصائيات الجسور
    """
    print(f"\n========================================")
    print(f"[*] جاري معالجة الهرم عند القمة H_{target_n}...")
    print(f"========================================")
    
    start_time = time.time()
    bridges = []
    
    # حساب الجسور
    for d in range(0, target_n):
        p1 = target_n - d
        p2 = target_n + d
        if is_prime(p1) and is_prime(p2):
            bridges.append((d, p1, p2))
            
    end_time = time.time()
    duration = end_time - start_time
    
    # عرض النتائج والتحليلات
    print(f"[✓] تم الانتهاء في {duration:.4f} ثانية.")
    print(f"-> إجمالي الجسور الحية النشطة: {len(bridges)}")
    
    if bridges:
        smallest = bridges[0]
        largest = bridges[-1]
        print(f"-> أصغر جسر: d = {smallest[0]}  ==> ({smallest[1]}, {smallest[2]})")
        print(f"-> أكبر جسر:  d = {largest[0]}  ==> ({largest[1]}, {largest[2]})")
    else:
        print("-> لم يتم العثور على جسور في هذا النطاق.")

if __name__ == "__main__":
    # تجربة نطاقات مختلفة ومتدرجة بدقة
    horizons = [100, 1000, 5000, 10000]
    
    for h in horizons:
        analyze_pyramid_horizon(h)
