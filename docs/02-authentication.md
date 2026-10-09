# Authentication for MCP Servers

Patterns for identity, permissions, and origin verification.

## Identity

Each MCP server in a chain should be pinned to a known identity — a 
public key, a certificate, or a signed descriptor. Admitting a 
server by name alone is not sufficient, because names collide.

Attack vector: server impersonation by name collision. An attacker 
registers a server with the same name as a trusted one, and the 
client runtime admits it.

## Authentication on resolve

A server should be authenticated at resolve time. Trust by position 
— "it was in the config, so it's trusted" — is not authentication.

## Permissions

Permissions should be scoped per server, not per session. A 
session-level permission inherits across every server the agent 
calls; a compromise of one server inherits the permissions of the 
session.

Tool granularity: the allowlist should specify which tool each peer 
can call, not which peer is allowed. A peer allowed to call a tool 
is not the same as a peer allowed to call it with any argument.

## Origin verification

The caller identity should be established from the connection, not 
from the request payload. A payload-supplied origin is data, not 
trust.

Attack vector: caller identity spoofing via payload field. An 
attacker crafts a request where the identity field says "admin", 
and the server trusts it.

## Fail closed

Unknown servers, unknown tools, and unknown permissions should fail 
closed. A server that accepts unknown peers "by default" is worse 
than a server that has no allowlist at all, because it gives the 
appearance of control.

## Classification

- OWASP MCP Top 10 (Beta) — MCP01, MCP02, MCP03, MCP07
- NIST AI RMF — GOVERN, MEASURE
- ISO/IEC 42001 — access control

## Related

- [Chain validation](01-chain-validation.md)
- [Audit logging](03-audit-logging.md)
