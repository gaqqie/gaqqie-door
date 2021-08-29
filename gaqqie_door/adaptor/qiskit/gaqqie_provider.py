from typing import List

from qiskit import Aer
from qiskit.providers import ProviderV1

from .gaqqie_backend import GaqqieBackend
from ...rest import Configuration, DeviceApi, JobApi, Device
from ...rest.api_client2 import ApiClient2


class GaqqieProvider(ProviderV1):
    def __init__(self) -> None:
        super().__init__()
        self._name: str = "gaqqie"
        self._url: str = None
        self._api_client: ApiClient2 = None

    def enable_account(self, url: str) -> None:
        self._url = url

    @property
    def name(self) -> str:
        return self._name

    @property
    def device_api(self) -> DeviceApi:
        return self._device_api

    @property
    def job_api(self) -> JobApi:
        return self._job_api

    def backends(self, name: str = None, **kwargs) -> List[GaqqieBackend]:
        # TODO thread safe
        if self._url is not None:
            rest_config = Configuration()
            rest_config.host = self._url

            self._api_client = ApiClient2(rest_config)
            self._device_api = DeviceApi(api_client=self._api_client)
            self._job_api = JobApi(api_client=self._api_client)
        else:
            # TODO raise Error
            pass

        # get backend information from cloud
        device = self._device_api.get_device_by_name(name)

        # create backend instance
        aer_backend = Aer.get_backend("qasm_simulator")
        config = aer_backend.configuration()
        config.backend_name = device.name
        backend = GaqqieBackend(config, self)
        return [backend]
