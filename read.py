import requests
import browser_cookie3


def get_input(day: int, year: int) -> list[str]:
    cookiejar = browser_cookie3.firefox(domain_name='adventofcode.com')

    if 'session' not in {cookie.name for cookie in cookiejar}:
        raise EnvironmentError("Not authenticated on adventofcode.com")

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    r = requests.get(url, stream=True, cookies=cookiejar)
    r.raw.decode_content = True

    if r.status_code == 404:
        raise FileNotFoundError(f"No challenge found for 12/{day}/{year}")

    result: str = r.raw.read().decode('utf-8')

    output: list[str] = [line for line in result.splitlines()]

    return output


def load_from_file(filepath: str) -> list[str]:
    with open(filepath, 'r') as f:
        return f.read().splitlines()