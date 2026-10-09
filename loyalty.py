# Автор: Карпенко Єгор Віталійович, група З-41

def loyalty_points(amount: float, is_member: bool = False) -> int:
    """
    Обчислює кількість балів лояльності.
    - 1 бал за кожні повні 20 грн.
    - Учасник програми отримує подвійні бали (x2).
    - amount < 0 викликає ValueError.
    """
    if amount < 0:
        raise ValueError("Сума покупки не може бути від'ємною")
    
    base_points = int(amount // 20)
    
    if is_member:
        return base_points * 2
    
    return base_points
