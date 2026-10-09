"""
Chain validation — didactic example.

Shows the shape of a chain validator: given a resolved list of
servers, check depth, identity, and authentication.

The production implementation adds descriptor integrity verification,
capability drift detection, and correlation with tool invocation
logs. Those are proprietary.
"""

from dataclasses import dataclass


@dataclass
class Server:
    name: str
    has_pinned_identity: bool
    is_authenticated: bool


def validate_chain(servers, safe_depth=5):
    """Return a list of (severity, message) issues for a resolved chain."""
    issues = []

    if len(servers) > safe_depth:
        issues.append(("HIGH", f"chain depth {len(servers)} > {safe_depth}"))

    for s in servers:
        if not s.has_pinned_identity:
            issues.append(("CRITICAL", f"{s.name}: no pinned identity"))
        if not s.is_authenticated:
            issues.append(("HIGH", f"{s.name}: not authenticated"))

    return issues


if __name__ == "__main__":
    chain = [
        Server("gateway", has_pinned_identity=True, is_authenticated=True),
        Server("kyc", has_pinned_identity=True, is_authenticated=True),
        Server("billing", has_pinned_identity=False, is_authenticated=True),
        Server("external", has_pinned_identity=False, is_authenticated=False),
    ]

    for severity, message in validate_chain(chain):
        print(f"[{severity}] {message}")
