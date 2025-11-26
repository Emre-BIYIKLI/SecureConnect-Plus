# SecureConnect+  
**Uçtan Uca Şifrelemeli Çok Platformlu Sohbet ve Uzaktan Erişim Sistemi**  
Ahmet Yesevi Üniversitesi – Bilgisayar Mühendisliği 2025 Güz Dönemi Projesi  
Öğrenci: Emre BIYIKLI | Danışman: Doç. Dr. Mevlüt Aksoy

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org)
[![Flutter](https://img.shields.io/badge/Flutter-3.19%2B-blue)](https://flutter.dev)
[![React](https://img.shields.io/badge/React-18%2B-blue)](https://reactjs.org)

## Özellikler
- Uçtan uca şifreleme (X25519 + AES-256-GCM + HMAC-SHA256)
- Gerçek zamanlı şifreli sohbet (WebSocket)
- Şifreli dosya transferi
- Güvenli uzaktan masaüstü kontrolü (ekran paylaşımı + fare/klavye)
- Masaüstü (Python/PyQt5), Mobil (Flutter), Web (Next.js) platform desteği
- Firebase Authentication & Firestore
- 2FA ve JWT tabanlı oturum yönetimi

## Proje Durumu
🚧 Geliştirme aşamasında – İlk prototip 1 hafta içinde hazır!

## Klasör Yapısı
SecureConnect-Plus/
├── backend/          # FastAPI + WebSocket sunucusu
├── desktop/          # PyQt5 masaüstü istemci
├── mobile/           # Flutter mobil uygulama
├── web/              # Next.js web paneli
├── shared/           # Ortak kriptografi modülleri
├── docs/             # Proje dokümantasyonu
└── README.md

## Kurulum (yakında detaylı gelecek)
```bash
# backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

Lisans: MIT © 2025 Emre BIYIKLI

