from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents"""

    with open(path, "r", encoding="utf8") as file:
        jobs = csv.DictReader(file)
        jobs_list = []
        for row in jobs:
            jobs_list.append(row)

    return jobs_list


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them"""
    jobs_data = read(path)
    set_jobs_types = set()
    for row in jobs_data:
        set_jobs_types.add(row["job_type"])
    return set_jobs_types


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type"""
    return [
        filtered_jobs
        for filtered_jobs in jobs
        if filtered_jobs["job_type"] == job_type
    ]
