import typing
from http.cookiejar import CookieJar
import requests
from browser_cookie3 import firefox, chrome, chromium, opera, opera_gx, safari, brave, edge, vivaldi
import re


def load_input(day: int, year: int, browser: str = "firefox") -> list[str]:
    """
    Loads input from selected day and year using browser's session cookie
    :param day: day from 1-25
    :param year: year when problem is from
    :param browser: firefox, chrome, chromium, opera, opera_gx, safari, brave, edge, vivaldi
    :return: newline-separated list of the input
    """

    cookiejar = get_cookies(browser)

    url = f"https://adventofcode.com/{year}/day/{day}/input"
    r = requests.get(url, stream=True, cookies=cookiejar)
    r.raw.decode_content = True

    if r.status_code == 404:
        raise FileNotFoundError(f"No challenge found for 12/{day}/{year}")

    result: str = r.raw.read().decode('utf-8')

    output: list[str] = [line for line in result.splitlines()]

    return output


def get_cookies(browser: str) -> CookieJar:
    """
    Get cookie jar from browser's session cookie
    :param browser: firefox, chrome, chromium, opera, opera_gx, safari, brave, edge, vivaldi
    :return: cookiejar
    """

    browser_list = [firefox, chrome, chromium, opera, opera_gx, safari, brave, edge, vivaldi]
    browsers = {browser.__name__: browser for browser in browser_list}

    if browser not in browsers:
        raise LookupError(f"CookieJar not found for {browser}")

    cookiejar = browsers[browser](domain_name='adventofcode.com')

    if 'session' not in {cookie.name for cookie in cookiejar}:
        raise EnvironmentError(f"Not authenticated on adventofcode.com on {browser}")

    return cookiejar


def load_from_file(filepath: str) -> list[str]:
    """
    load test input from a file
    :param filepath: path to input file
    :return: newline-separated list of the input
    """
    with open(filepath, 'r') as f:
        return f.read().splitlines()


def load_example(day: int, year: int, browser: str = "firefox", n: int = 1) -> list[str]:
    """
    Loads example input from selected day and year using browser's session cookie
    :param day: day from 1-25
    :param year: year when problem is from
    :param browser: firefox, chrome, chromium, opera, opera_gx, safari, brave, edge, vivaldi
    :param n: nth example to load
    :return: newline-separated list of the example input
    """

    cookiejar = get_cookies(browser)

    url = f"https://adventofcode.com/{year}/day/{day}"
    r = requests.get(url, stream=True, cookies=cookiejar)
    r.raw.decode_content = True

    if r.status_code == 404:
        raise FileNotFoundError(f"No challenge found for 12/{day}/{year}")

    result: str = r.raw.read().decode('utf-8')
    matches: list[str] = re.findall(r'<pre><code>(.*?)</code></pre>', result, re.DOTALL)

    if matches is None:
        raise LookupError(f"Example {n} not found")

    return matches[min(n - 1, len(matches) - 1)].splitlines()


def test_solution(day: int, year: int, *parts: typing.Callable, browser: str = "firefox") -> None:
    """
    Runs each part of solution using example and solution input and formats it nicely.
    May not work for all browsers due to permissions and cookie encryption.
    :param day: day from 1-25
    :param year: year when problem is from
    :param parts: each part to solution as a function
    :param browser: browser: firefox, chrome, chromium, opera, opera_gx, safari, brave, edge, vivaldi
    """
    example_inputs = [load_example(day, year, browser, n) for n in range(1, len(parts)+1)]
    solution_input = load_input(day, year, browser)

    def print_func_result(func: typing.Callable, input: list[str]) -> None:
        if func is None: return
        if isinstance(func, typing.Callable):
            name = ' '.join(func.__name__.split("_")).capitalize()
            print(f"{name}: {func(input)}")
            return
        raise TypeError("args must be Callable")

    print(f"{'EXAMPLE RESULTS':=^31}")
    for i, func in enumerate(parts):
        print_func_result(func, example_inputs[i])

    print(f"\n{'SOLUTION RESULTS':=^31}")
    for func in parts:
        print_func_result(func, solution_input)
