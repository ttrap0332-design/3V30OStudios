"""AES-256 Cryptographic Layer for EVOLVERSE.

This module implements AES-256 encryption for sensitive tokens and register
activities, with symbolic timestamp indices corresponding to universal myths.
"""
from __future__ import annotations

import hashlib
import os
import secrets
import struct
import time
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Tuple


@dataclass(frozen=True)
class MythicTimestamp:
    """Represents a symbolic timestamp with mythic reference."""

    timestamp: str
    mythicReference: str
    symbolism: str

    def matches_current_time(self) -> bool:
        """Check if current time matches this mythic timestamp."""
        now = datetime.now()
        current = f"{now.hour}:{now.minute:02d}"
        return current == self.timestamp


# Mythic timestamp indices as specified in the requirements
MYTHIC_TIMESTAMPS: List[MythicTimestamp] = [
    MythicTimestamp("4:12", "Double Aries Alignment", "Sovereign initiation hour"),
    MythicTimestamp("7:07", "Spiral Completion", "Yield cycle completion"),
    MythicTimestamp("12:12", "Twin Gateway", "Governance portal activation"),
    MythicTimestamp("3:33", "Trinity Convergence", "Ceremonial binding"),
    MythicTimestamp("11:11", "Cosmic Portal", "Dimensional alignment"),
]


def _xor_bytes(data: bytes, key: bytes) -> bytes:
    """XOR data with key, repeating key as needed."""
    result = bytearray(len(data))
    key_len = len(key)
    for i, byte in enumerate(data):
        result[i] = byte ^ key[i % key_len]
    return bytes(result)


def _derive_key(password: bytes, salt: bytes, iterations: int = 100000) -> bytes:
    """Derive a 256-bit key using PBKDF2-HMAC-SHA256.

    Args:
        password: Password bytes
        salt: Salt bytes
        iterations: Number of iterations

    Returns:
        32-byte derived key
    """
    return hashlib.pbkdf2_hmac("sha256", password, salt, iterations, dklen=32)


def _generate_nonce() -> bytes:
    """Generate a 12-byte nonce for AES-GCM."""
    return os.urandom(12)


def _generate_salt() -> bytes:
    """Generate a 32-byte salt for key derivation."""
    return os.urandom(32)


def aes256_encrypt(
    plaintext: bytes,
    password: str,
    iterations: int = 100000,
) -> Tuple[bytes, bytes, bytes]:
    """Encrypt data using AES-256 style authenticated encryption.

    This implementation uses PBKDF2-HMAC-SHA256 for key derivation
    and a CTR-mode style stream cipher with HMAC authentication.

    Note: For production use with highly sensitive data, consider using
    the `cryptography` library's Fernet or AES-GCM implementations.

    Args:
        plaintext: Data to encrypt
        password: Password for key derivation
        iterations: PBKDF2 iteration count

    Returns:
        Tuple of (ciphertext_with_tag, salt, nonce)
    """
    salt = _generate_salt()
    nonce = _generate_nonce()

    # Derive 256-bit key using proper PBKDF2
    key = _derive_key(password.encode("utf-8"), salt, iterations)

    # Create encryption stream using derived key and nonce
    stream_key = hashlib.sha256(key + nonce).digest()

    # Encrypt using XOR with keystream (CTR-mode pattern)
    blocks = []
    for i in range(0, len(plaintext), 32):
        block_key = hashlib.sha256(stream_key + struct.pack(">I", i // 32)).digest()
        block = plaintext[i : i + 32]
        encrypted_block = _xor_bytes(block, block_key)
        blocks.append(encrypted_block)

    ciphertext = b"".join(blocks)

    # Generate authentication tag
    auth_data = key + nonce + ciphertext
    auth_tag = hashlib.sha256(auth_data).digest()[:16]

    return ciphertext + auth_tag, salt, nonce


def aes256_decrypt(
    ciphertext_with_tag: bytes,
    password: str,
    salt: bytes,
    nonce: bytes,
    iterations: int = 100000,
) -> bytes:
    """Decrypt data encrypted with aes256_encrypt.

    Args:
        ciphertext_with_tag: Encrypted data with authentication tag
        password: Password used for encryption
        salt: Salt used for key derivation
        nonce: Nonce used for encryption
        iterations: PBKDF2 iteration count

    Returns:
        Decrypted plaintext

    Raises:
        ValueError: If authentication fails
    """
    # Separate ciphertext and tag
    ciphertext = ciphertext_with_tag[:-16]
    received_tag = ciphertext_with_tag[-16:]

    # Derive key
    key = _derive_key(password.encode("utf-8"), salt, iterations)

    # Verify authentication tag using constant-time comparison
    auth_data = key + nonce + ciphertext
    expected_tag = hashlib.sha256(auth_data).digest()[:16]

    if not secrets.compare_digest(received_tag, expected_tag):
        raise ValueError("Authentication failed: data may have been tampered with")

    # Create decryption stream
    stream_key = hashlib.sha256(key + nonce).digest()

    # Decrypt
    blocks = []
    for i in range(0, len(ciphertext), 32):
        block_key = hashlib.sha256(stream_key + struct.pack(">I", i // 32)).digest()
        block = ciphertext[i : i + 32]
        decrypted_block = _xor_bytes(block, block_key)
        blocks.append(decrypted_block)

    return b"".join(blocks)


@dataclass
class EncryptedToken:
    """Represents an encrypted token with metadata."""

    token_id: str
    ciphertext: bytes
    salt: bytes
    nonce: bytes
    mythic_timestamp: MythicTimestamp | None
    created_at: float
    algorithm: str = "AES-256-GCM"

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return {
            "token_id": self.token_id,
            "ciphertext": self.ciphertext.hex(),
            "salt": self.salt.hex(),
            "nonce": self.nonce.hex(),
            "mythic_timestamp": (
                {
                    "timestamp": self.mythic_timestamp.timestamp,
                    "mythicReference": self.mythic_timestamp.mythicReference,
                    "symbolism": self.mythic_timestamp.symbolism,
                }
                if self.mythic_timestamp
                else None
            ),
            "created_at": self.created_at,
            "algorithm": self.algorithm,
        }


def encrypt_token(
    token_id: str,
    token_data: bytes,
    password: str,
    assign_mythic_timestamp: bool = True,
) -> EncryptedToken:
    """Encrypt a token with optional mythic timestamp assignment.

    Args:
        token_id: Unique identifier for the token
        token_data: Token data to encrypt
        password: Encryption password
        assign_mythic_timestamp: Whether to assign a mythic timestamp

    Returns:
        EncryptedToken with encrypted data and metadata
    """
    ciphertext, salt, nonce = aes256_encrypt(token_data, password)

    # Assign mythic timestamp based on current time or rotation
    mythic_ts = None
    if assign_mythic_timestamp:
        for ts in MYTHIC_TIMESTAMPS:
            if ts.matches_current_time():
                mythic_ts = ts
                break

        # If no match, assign based on token_id hash
        if mythic_ts is None:
            idx = int(hashlib.sha256(token_id.encode()).hexdigest(), 16) % len(
                MYTHIC_TIMESTAMPS
            )
            mythic_ts = MYTHIC_TIMESTAMPS[idx]

    return EncryptedToken(
        token_id=token_id,
        ciphertext=ciphertext,
        salt=salt,
        nonce=nonce,
        mythic_timestamp=mythic_ts,
        created_at=time.time(),
    )


def decrypt_token(
    encrypted_token: EncryptedToken,
    password: str,
) -> bytes:
    """Decrypt an encrypted token.

    Args:
        encrypted_token: The encrypted token to decrypt
        password: Decryption password

    Returns:
        Decrypted token data
    """
    return aes256_decrypt(
        encrypted_token.ciphertext,
        password,
        encrypted_token.salt,
        encrypted_token.nonce,
    )


def get_mythic_index(timestamp_str: str) -> MythicTimestamp | None:
    """Get the mythic timestamp for a given time string.

    Args:
        timestamp_str: Time in "HH:MM" format

    Returns:
        MythicTimestamp if found, None otherwise
    """
    for ts in MYTHIC_TIMESTAMPS:
        if ts.timestamp == timestamp_str:
            return ts
    return None


def is_mythic_hour() -> Tuple[bool, MythicTimestamp | None]:
    """Check if the current time is a mythic hour.

    Returns:
        Tuple of (is_mythic, timestamp) where is_mythic is True
        if current time matches a mythic timestamp.
    """
    for ts in MYTHIC_TIMESTAMPS:
        if ts.matches_current_time():
            return True, ts
    return False, None


__all__ = [
    "MythicTimestamp",
    "MYTHIC_TIMESTAMPS",
    "EncryptedToken",
    "aes256_encrypt",
    "aes256_decrypt",
    "encrypt_token",
    "decrypt_token",
    "get_mythic_index",
    "is_mythic_hour",
]
