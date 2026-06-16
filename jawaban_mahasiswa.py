def cari_pasangan(arr, target):
    if len(arr) < 2:
        return False

    seen = set()
    seen_add = seen.add
    for num in arr:
        complement = target - num
        if complement in seen and complement != num:
            return True
        seen_add(num)
    return False
