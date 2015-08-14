def pytest_love(report):
    if report.when == 'call':
        if hasattr(report, 'wasxfail'):
            if report.skipped:
                return "xfailed", "x", "xfail"
            elif report.failed:
                return "xpassed", "p", "XPASS"
        if report.passed:
            letter = u"\U0001F49A ".encode('utf8')
        elif report.skipped:
            letter = u"\U0001F49B ".encode('utf8')
        elif report.failed:
            letter = u"\U0001F494 ".encode('utf8')
        return report.outcome, letter, report.outcome.upper()
