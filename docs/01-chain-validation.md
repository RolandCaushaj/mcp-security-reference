# Chain Validation

Why trust propagation across MCP servers is the primary security 
concern in multi-server agent architectures.

## The problem

When an agent calls an MCP server, and that server calls another, 
trust becomes transitive. The agent trusts the first server; the 
first server trusts the second; the second reaches a tool. A 
compromise at any node in the chain reaches every node downstream.

This is not a new problem in distributed systems, but it has 
specific properties in MCP:

- Servers are resolved at runtime, not at deploy time
- Descriptors can change between resolve and use
- The client runtime, not the operator, resolves the chain
- A single name collision can substitute an attacker-controlled server

## The perimeter

The perimeter of an MCP deployment is not the system. It is the 
chain the system trusts.

A clean web pentest says nothing about what the chain can be made 
to do. A firewall rule does not see the chain. The trust is inside 
the protocol flow.

## What to validate

For each node in the chain:

- **Identity** — is the server pinned to a known identity, or 
  admitted by name?
- **Authentication** — is the server authenticated on resolve, or 
  trusted by position?
- **Integrity** — is the server descriptor verified, or accepted 
  as declared?
- **Capability** — which tools does it expose at resolve time, and 
  are they the same at use time?

## Patterns

**Pin identity, not name.** A server should be identified by a 
cryptographic property (key, certificate), not by a string that can 
collide.

**Verify on resolve, not on declaration.** Configuration says what 
should be. The runtime says what is. Audit the runtime.

**Cap chain depth.** Each additional server adds attack surface. A 
chain depth threshold is a practical control, not a theoretical 
limit.

**Scope permissions per server, not per session.** A session-level 
permission inherits across every server the agent calls. A 
server-level permission does not.

## Classification

Findings against chain validation typically map to:

- OWASP MCP Top 10 (Beta) — MCP01, MCP03, MCP04
- MITRE ATLAS — AML.T0051
- NIST AI RMF — MEASURE
- ISO/IEC 42001 — operational controls

## Related

- [Authentication](02-authentication.md)
- [Audit logging](03-audit-logging.md)
- [Threat models](04-threat-models.md)
