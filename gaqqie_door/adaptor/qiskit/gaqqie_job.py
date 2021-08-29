from typing import Optional

from qiskit.providers import Backend, JobV1, JobStatus
from qiskit.providers.ibmq.runtime import ResultDecoder
from qiskit.result import Result

from ...rest import Job


class GaqqieJob(JobV1):
    def __init__(self, backend: Backend, job: Job, **kwargs) -> None:
        """Initializes the asynchronous job.
        Args:
            backend: the backend used to run the job.
            job_id: a unique id in the context of the backend used to run
                the job.
            kwargs: Any key value metadata to associate with this job.
        """
        super().__init__(backend, job.id, **kwargs)
        self._job = job

    def submit(self):
        """Submit the job to the backend for execution."""
        pass

    def result(self, timeout: Optional[float] = None, wait: float = 5) -> Result:
        """Return the results of the job."""
        self.wait_for_final_state(timeout, wait)
        response = self.backend().provider().job_api.get_result_by_job_id(self.job_id())
        if response.results:
            result_dict = ResultDecoder.decode(response.results)
            result_obj = Result.from_dict(result_dict)
            return result_obj
        else:
            return None

    def status(self) -> JobStatus:
        """Return the status of the job, among the values of ``JobStatus``."""
        self._job = self.backend().provider().job_api.get_job_by_id(self.job_id())
        if self._job.status == "QUEUED":
            status = JobStatus.QUEUED
        elif self._job.status == "RUNNING":
            status = JobStatus.RUNNING
        elif self._job.status == "SUCCEEDED":
            status = JobStatus.DONE
        elif self._job.status == "CANCELLED":
            status = JobStatus.CANCELLED
        elif self._job.status == "FAILED":
            status = JobStatus.ERROR
        else:
            raise ValueError(f"receive unsupported status={self._job.status}.")

        return status
