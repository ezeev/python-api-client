## Requirements.
Python 2.7 and later.

## Setuptools
You can install the bindings via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install
```

Or you can install from Github via pip:

```sh
pip install git+https://github.com/ezeev/wavefront-api-client.git
```

To use the bindings, import the pacakge:

```python
import wavefront_api_client
```

## Manual Installation
If you do not wish to use setuptools, you can download the latest release.
Then, to use the bindings, import the package:

```python
import path.to.swagger_client
```

## Getting Started

```
import wavefront_api_client as wave_api

base_url = 'https://YOUR_INSTANCE.wavefront.com'
api_key = 'YOUR_API_TOKEN'

client = wave_api.ApiClient(host=base_url, header_name='Authorization', header_value='Bearer ' + api_key)

# instantiate the metric API
metric_api = wave_api.MetricApi(client)
response = metric_api.get_metric_details("cpu.usage.idle")

print response


# instantiate the source API


```