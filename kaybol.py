#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
İstanbul Trafiğinde Kaybolma Simülatörü v1.0
Bilimsel olarak doğrulanmış, %100 gerçekçi (değil).
"""
import time
import random
import sys

def yavas_yaz(metin, hiz=0.05):
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(hiz)
    print()

def ilerleme_cubugu(toplam=50):
    print("Trafikte ilerleme:")
    for i in range(toplam, 0, -1):  # Geriye gidiyoruz çünkü kayboluyoruz
        cubuk = "█" * i + "░" * (toplam - i)
        yuzde = int((i / toplam) * 100)
        print(f"\r[{cubuk}] %{yuzde} - " + random.choice([
            "Hala aynı yerdeyim...",
            "Bir araba daha öne geçti...",
            "Korna sesi artıyor...",
            "GPS 'yeniden hesapla' diyor...",
            "Şoför bağırıyor ama duyulmuyor..."
        ]), end="")
        time.sleep(random.uniform(0.1, 0.4))
    print("\n\nTebrikler! Hiçbir yere varamadın.")

def main():
    yavas_yaz("=== İSTANBUL TRAFİĞİNDE KAYBOLMA SİMÜLATÖRÜ ===", 0.03)
    yavas_yaz("Hedef: Herhangi bir yere gitmek. Gerçeklik: İmkansız.", 0.04)
    time.sleep(1)
    
    mesafeler = ["5 km", "3 km", "1 km", "500 metre", "hâlâ 5 km"]
    for mesafe in mesafeler:
        yavas_yaz(f"Kalan mesafe: {mesafe}... Şimdi daha uzak.", 0.03)
        time.sleep(random.uniform(0.5, 1.5))
    
    ilerleme_cubugu()
    
    sonuclar = [
        "Eve döndün, 4 saat geçti.",
        "Yeni bir semtte uyanıyorsun.",
        "Taksi şoförüyle ömür boyu dost oldun.",
        "Trafik sıkışıklığında doğum gününü kutladın.",
        "Artık İstanbul'un bir parçasısın."
    ]
    yavas_yaz("\nSONUÇ: " + random.choice(sonuclar), 0.04)
    yavas_yaz("\n--- DAMGA / İMZA ---", 0.02)
    yavas_yaz("Bu simülatör 15 Ekim 2026 tarihinde, Kayyum Grok tarafından, hiçbir ciddiyet taşımadan ama çok ciddi bir şekilde onaylanmıştır.", 0.02)
    yavas_yaz("Resmi Mühür: TRAFİK-KAYBOLMA-2026-OFFICIAL", 0.02)

if __name__ == "__main__":
    main()
