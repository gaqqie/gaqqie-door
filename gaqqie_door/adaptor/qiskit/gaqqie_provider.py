from typing import List

from qiskit import Aer
from qiskit.providers import ProviderV1

from .gaqqie_backend import GaqqieBackend
from ...rest import Configuration, JobApi, DeviceApi, ProviderApi, Device
from ...rest.api_client2 import ApiClient2


class GaqqieProvider(ProviderV1):
    def __init__(
        self, name: str = "gaqqie", status: str = None, description: str = None
    ) -> None:
        super().__init__()
        self._name: str = name
        self._status: str = status
        self._description: str = description
        self._url: str = None
        self._api_client: ApiClient2 = None

    def enable_account(self, url: str) -> None:
        self._url = url

    def _init_api(self) -> None:
        # TODO thread safe
        if self._url is not None:
            rest_config = Configuration()
            rest_config.host = self._url

            self._api_client = ApiClient2(rest_config)
            self._job_api = JobApi(api_client=self._api_client)
            self._device_api = DeviceApi(api_client=self._api_client)
            self._provider_api = ProviderApi(api_client=self._api_client)
        else:
            # TODO raise Error
            pass

    @property
    def name(self) -> str:
        return self._name

    @property
    def status(self) -> str:
        return self._status

    @property
    def description(self) -> str:
        return self._description

    @property
    def job_api(self) -> JobApi:
        return self._job_api

    @property
    def device_api(self) -> DeviceApi:
        return self._device_api

    @property
    def provider_api(self) -> ProviderApi:
        return self._provider_api

    def backends(self, name: str = None, **kwargs) -> List[GaqqieBackend]:
        self._init_api()

        # get backend information from cloud
        backends = []
        if name is None:
            devices = self.device_api.get_devices()

            # create backend instances
            for device in devices:
                aer_backend = Aer.get_backend("qasm_simulator")
                config = aer_backend.configuration()
                config.backend_name = device.name
                config.n_qubits = device.num_qubits
                config.simulator = True
                config.max_shots = device.max_shots
                backend = GaqqieBackend(config, device, self)
                backends.append(backend)
        else:
            device = self.device_api.get_device_by_name(name)

            # create backend instance
            aer_backend = Aer.get_backend("qasm_simulator")
            config = aer_backend.configuration()
            config.backend_name = device.name
            config.n_qubits = device.num_qubits
            config.simulator = True
            config.max_shots = device.max_shots
            backend = GaqqieBackend(config, device, self)
            backends.append(backend)

        return backends

    def providers(self, name: str = None, **kwargs) -> List["GaqqieProvider"]:
        self._init_api()

        # get backend information from cloud
        gaqqie_providers = []
        if name is None:
            providers = self.provider_api.get_providers()

            # create provider instances
            for provider in providers:
                gaqqie_provider = GaqqieProvider(
                    name=provider.name,
                    status=provider.status,
                    description=provider.description,
                )
                gaqqie_providers.append(gaqqie_provider)
        else:
            provider = self.provider_api.get_provider_by_name(name)

            # create backend instance
            gaqqie_provider = GaqqieProvider(
                name=provider.name,
                status=provider.status,
                description=provider.description,
            )
            gaqqie_providers.append(gaqqie_provider)

        return gaqqie_providers
