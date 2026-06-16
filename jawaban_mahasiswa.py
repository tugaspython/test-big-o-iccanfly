def cari_pasangan(arr, target):
    seen = set()
    for num in arr:
        complement = target - num
        if complement in seen and complement != num:
            return True
        seen.add(num)
    return False
