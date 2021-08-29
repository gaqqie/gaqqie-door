import json

from qiskit import QuantumCircuit
from qiskit.compiler.assembler import assemble
from qiskit.providers import BackendV1, Job, Options

from .gaqqie_job import GaqqieJob
from ...rest import Jobbeforesubmission


class GaqqieBackend(BackendV1):
    # see https://github.com/Qiskit/qiskit-terra/blob/main/qiskit/providers/backend.py
    def __init__(self, configuration, provider: "GaqqieProvider") -> None:
        super().__init__(configuration, provider)

    @classmethod
    def _default_options(cls):
        """Return the default options
        This method will return a :class:`qiskit.providers.Options`
        subclass object that will be used for the default options. These
        should be the default parameters to use for the options of the
        backend.
        Returns:
            qiskit.providers.Options: A options object with
                default values set
        """
        return Options(shots=1024)

    # see https://github.com/Qiskit/qiskit-ibmq-provider/blob/5bc1d7a61a057894679e00784faa24bfb6c8de19/qiskit/providers/ibmq/ibmqbackend.py#L146
    def run(self, circuit: QuantumCircuit, **options) -> Job:
        """Run on the backend.
        This method that will return a :class:`~qiskit.providers.Job` object
        that run circuits. Depending on the backend this may be either an async
        or sync call. It is the discretion of the provider to decide whether
        running should  block until the execution is finished or not. The Job
        class can handle either situation.
        Args:
            circuits (QuantumCircuit or Schedule or list): An individual or a
                list of :class:`~qiskit.circuits.QuantumCircuit` or
                :class:`~qiskit.pulse.Schedule` objects to run on the backend.
                For legacy providers migrating to the new versioned providers,
                provider interface a :class:`~qiskit.qobj.QasmQobj` or
                :class:`~qiskit.qobj.PulseQobj` objects should probably be
                supported too (but deprecated) for backwards compatibility. Be
                sure to update the docstrings of subclasses implementing this
                method to document that. New provider implementations should not
                do this though as :mod:`qiskit.qobj` will be deprecated and
                removed along with the legacy providers interface.
            options: Any kwarg options to pass to the backend for running the
                config. If a key is also present in the options
                attribute/object then the expectation is that the value
                specified will be used instead of what's set in the options
                object.
        Returns:
            Job: The job object for the run
        """
        serialized_json = json.dumps(assemble(circuit, self).to_dict(), indent=2)
        request = Jobbeforesubmission(
            provider_name=self.provider().name,
            device_name=self.name(),
            instructions=serialized_json,
        )
        response = self.provider().job_api.submit_job(request)
        job = GaqqieJob(self, response)
        return job
