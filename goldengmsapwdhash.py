import argparse
import base64
import hashlib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--password', dest="password", help="Put Base64 GMSA Password Here", required=True)
    args = parser.parse_args()

    if args.password:
        # Base64 dekódolás
        password_b64 = args.password
        password_bytes = base64.b64decode(password_b64)

        # NTLM hash (MD4 hash of UTF-16LE encoded password)
        nt_hash = hashlib.new('md4', password_bytes).hexdigest()
        print(f"NTLM Hash: {nt_hash}")

if __name__ == "__main__":
    main()
