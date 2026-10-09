# Threat Models for MCP Architectures

Common attack scenarios against multi-server agent systems.

## Man-in-the-middle

An attacker intercepts traffic between the agent and an MCP server, 
or between two servers in the chain. Because the chain is resolved 
at runtime, a substituted node can be inserted without changing 
configuration.

Controls: pin server identity, verify on resolve, encrypt transport.

## Privilege escalation

A compromised server inherits the trust of the chain. Tools 
reachable from the compromised node become reachable to the 
attacker, including tools that are not directly connected.

Controls: cap chain depth, scope permissions per server, log every 
invocation.

## Supply chain

A third-party MCP server, tool descriptor, or model artefact is 
compromised upstream. The attacker does not need to reach the 
client; they compromise a dependency.

Controls: verify provenance, pin versions, monitor for descriptor 
drift.

## Name collision

An attacker registers a server with the same name as a trusted one. 
The runtime resolves the name to the attacker's server.

Controls: pin identity by cryptographic property, not by name.

## Capability drift

A server resolves with one set of tools and later exposes another. 
The audit captured the first set; the second is unlogged.

Controls: verify capability at resolve and at use, log mutations, 
cap allowed drift.

## Fail-open

An unknown server or unknown tool is accepted by default. The 
system has the appearance of control but no enforcement.

Controls: fail closed on unknown peers and unknown tools, test the 
failure mode.

## Payload origin spoofing

The caller identity is read from the request payload rather than 
from the connection.

Controls: establish identity from the transport, not from the 
payload.

## Data exfiltration via tool

A tool with egress capability (HTTP, email, write) is used to send 
data out. The tool is permitted; the use is not.

Controls: classify tools by capability, monitor egress-class 
invocations, require confirmation for destructive or egress actions.

## Classification

Each of these maps to controls in:

- OWASP MCP Top 10 (Beta)
- OWASP Top 10 for LLM Applications
- MITRE ATLAS
- NIST AI RMF
- ISO/IEC 42001

## Related

- [Chain validation](01-chain-validation.md)
- [Authentication](02-authentication.md)
- [Audit logging](03-audit-logging.md)
