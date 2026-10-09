# Audit Logging for MCP

What to capture, why, and how to protect it.

## Why

Audit logs are the difference between an incident you can 
reconstruct and an incident you can only describe. For vendor 
assessment under DORA, they are evidence.

The register of information required by DORA Articles 28–44 asks 
for documented evidence of ICT controls. An append-only audit log 
is one such control.

## What to capture

- **Every server resolve** — with identity, authentication state, 
  and descriptor hash
- **Every tool invocation** — with caller, tool name, and arguments
- **Every permission decision** — including denials, not just grants
- **Every chain mutation** — server added, removed, or replaced
- **Every tamper event** — descriptor changed between resolve and use

The denial log matters as much as the approval log. An attack that 
is blocked is a signal; an attack that is not logged is not a signal.

## Tamper protection

A log that can be edited after the fact is not evidence.

- Append-only storage
- Cryptographic chaining (each entry hashes the previous)
- Off-system retention or write-once storage
- Periodic integrity check with recorded hash

## Retention

For DORA-relevant engagements, retention should be defined by 
contract. The default in our engagements is 30 days after delivery, 
with immediate destruction on written request.

## What not to log

- Credentials, tokens, API keys
- Raw model prompts containing client data
- Personal data beyond what is necessary for the audit

Log the fact of an invocation, not the full content.

## Classification

- NIST AI RMF — MEASURE, MANAGE
- ISO/IEC 42001 — operational control
- DORA Article 28-44 — register of information

## Related

- [Chain validation](01-chain-validation.md)
- [Authentication](02-authentication.md)
