from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs"""
    jobs_list = read(path)
    set_max_salary = set()
    for salary in jobs_list:
        if salary["max_salary"].isnumeric():
            set_max_salary.add(int(salary["max_salary"]))
    return max(set_max_salary)


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs"""
    jobs_list = read(path)
    set_min_salary = set()
    for salary in jobs_list:
        if salary["min_salary"].isnumeric():
            set_min_salary.add(int(salary["min_salary"]))
    return min(set_min_salary)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job"""
    try:
        min_salary = int(job["min_salary"])
        max_salary = int(job["max_salary"])
        salaries = int(salary)
        if min_salary > max_salary:
            raise ValueError
        return min_salary <= salaries <= max_salary
    except (ValueError, TypeError, KeyError) as error:
        raise ValueError from error


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range"""
    filtered_salary = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                filtered_salary.append(job)
        except ValueError:
            pass
    return filtered_salary
