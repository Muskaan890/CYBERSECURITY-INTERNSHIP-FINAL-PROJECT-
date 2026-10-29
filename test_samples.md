# Sample Test Cases

Run `python phishing_checker.py` (or `python3 phishing_checker.py`) and try each URL.

| No. | Sample URL | Expected warning signs |
|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs |
| 2 | `http://192.0.2.10/account` | IP address hostname; HTTP |
| 3 | `http://example.com@sample.invalid/login` | `@` symbol; HTTP |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Hostname has 5 or more segments |
| 5 | `https://xn--example.invalid/` | Punycode marker |

## How to record results
For each test, write:
- Actual output: [paste what your program displayed]
- Status: PASS if the expected warning signs appeared; otherwise investigate and record FAIL.

These are illustrative test URLs. Do not visit suspicious links just to test them; the program only needs the text.
