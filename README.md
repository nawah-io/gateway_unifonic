# Nawah Gateway for Unifonic SMS
This repo is a [Nawah](https://github.com/nawah-io/nawah_docs) Package that allows developers to integrate [Unifonic SMS](https://www.unifonic.com/SMS) into Nawah apps using Gateway Controller.

## How-to
1. From your app directory run: `nawah packages add gateway_unifonic`
2. Add `unifonic` Var to `nawah_app.py` App Config:
```python
vars = {
	'unifonic': {'sid': 'UNIFONIC_SID'}
}
```
3. `unifonic` gateway requires following args:
   1. `phone`: Target phone number using international format with prefixed `+`. Type `str`.
   2. `content`: Message body. Type `str`.
4. `unifonic` gateway accepts optional arg, namely `unifonic_auth`, replicating `unifonic` value in `vars Config Attr` for dynamic Unifonic API credentials.
5. Use `unifonic` gateway using Nawah Gateway Controller:
```python
from nawah.gateway import Gateway

Gateway.send(gateway='unifonic', phone=phone, content=content)
```