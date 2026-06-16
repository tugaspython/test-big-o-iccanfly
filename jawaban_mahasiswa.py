 def cari_pasangan(arr: Iterable[float], target: float) -> bool:
     """True jika ada dua elemen (indeks berbeda) di arr yang jumlahnya == target."""
     seen = set()
     for x in arr:
         if (target - x) in seen:
             return True
         seen.add(x)
     return False
