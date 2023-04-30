from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them"""
    industries_list = read(path)
    set_industries = set()
    for industries in industries_list:
        if industries["industry"] != "":
            set_industries.add(industries["industry"])
    return set_industries


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry"""
    return [
        filtered_industries
        for filtered_industries in jobs
        if filtered_industries["industry"] == industry
    ]
