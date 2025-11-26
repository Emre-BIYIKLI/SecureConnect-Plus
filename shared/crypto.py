# shared/crypto.py
# SecureConnect+ Uçtan Uca Şifreleme Motoru v0.1
# X25519 + AES-256-GCM + HMAC-SHA256

from cryptography.hazmat.primitives.asymmetric import x25519
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os
import base64

class SecureConnectCrypto:
    @staticmethod
    def generate_keypair():
        private_key = x25519.X25519PrivateKey.generate()
        public_key = private_key.public_key()
        
        private_bytes = private_key.private_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PrivateFormat.Raw,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_bytes = public_key.public_bytes(
            encoding=serialization.Encoding.Raw,
            format=serialization.PublicFormat.Raw
        )
        return base64.b64encode(private_bytes).decode(), base64.b64encode(public_bytes).decode()

    @staticmethod
    def derive_shared_secret(private_key_b64: str, peer_public_key_b64: str) -> bytes:
        private_key = x25519.X25519PrivateKey.from_private_bytes(base64.b64decode(private_key_b64))
        peer_public = x25519.X25519PublicKey.from_public_bytes(base64.b64decode(peer_public_key_b64))
        
        shared_secret = private_key.exchange(peer_public)
        
        derived = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=None,
            info=b'SecureConnect+ handshake',
        ).derive(shared_secret)
        return derived

    @staticmethod
    def encrypt_message(key: bytes, message: str) -> str:
        aesgcm = AESGCM(key)
        iv = os.urandom(12)
        ciphertext = aesgcm.encrypt(iv, message.encode(), None)
        return base64.b64encode(iv + ciphertext).decode()

    @staticmethod
    def decrypt_message(key: bytes, encrypted_b64: str) -> str:
        data = base64.b64decode(encrypted_b64)
        iv = data[:12]
        ciphertext = data[12:]
        aesgcm = AESGCM(key)
        plaintext = aesgcm.decrypt(iv, ciphertext, None)
        return plaintext.decode()
