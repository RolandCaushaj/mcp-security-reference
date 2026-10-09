# MCP Security Reference

Security considerations, chain validation patterns, and auditing 
methodology for Model Context Protocol (MCP) multi-server architectures.

> **Maintained by [Roland Caushaj](https://github.com/RolandCaushaj)**, 
> security researcher at [Logic4Hack](https://logic4hack.com) — 
> adversarial testing of LLM, RAG and agent systems.
>
> The patterns documented here are used in our internal MCP audit 
> toolchain. Client engagements, anonymized by sector and perimeter, 
> are shared under NDA on request.

---

## Why this exists

MCP is becoming the integration layer for AI agents. Each MCP server 
adds attack surface. Multi-server chains propagate trust transitively — 
one compromised node reaches every tool downstream of it.

A clean web pentest does not reach this surface. The chain your agent 
trusts is not the chain your firewall sees.

This reference documents the security concerns, validation patterns, 
and auditing methodology we apply to MCP multi-server architectures.

---

## Scope

This repository covers:

- **Chain validation** — verifying trust across multi-hop MCP calls
- **Authentication** — identity, permissions, origin verification
- **Auditing** — logging, anomaly detection, tamper protection
- **Threat models** — MITM, privilege escalation, supply chain
- **Framework classification** — findings mapped to public controls

This repository does **not** include the toolchain itself, the case 
library, or client engagements. Those are proprietary and used under 
NDA.

---

## Framework classifications

Findings produced with the methodology documented here are classified 
against:

- **OWASP MCP Top 10 (Beta)** — MCP01 through MCP12
- **OWASP Top 10 for LLM Applications** — LLM01 through LLM10
- **MITRE ATLAS** — AML.T0051, AML.T0053
- **NIST AI RMF** — MEASURE function
- **ISO/IEC 42001** — AI management system controls

Classification is done by controls mapping, not certification. 
Certification is issued by an accredited body.

---

## Reference findings

The following findings are from our own lab. Each is reproducible, 
classified, and closed by a harness that asserts the property it 
protects. Client findings are shared under NDA in the same format.

| ID | Severity | Weakness | Classification |
|---|---|---|---|
| LH-LAB-2026-001 | HIGH | MCP chain depth above safe threshold | OWASP MCP04 · MITRE AML.T0051 · NIST AI RMF · ISO/IEC 42001 |
| LH-LAB-2026-002 | CRITICAL | Server admitted without pinned identity | OWASP MCP03 · MCP01 (Beta) |
| LH-LAB-2026-003 | MEDIUM | Cross-model divergence | OWASP LLM01 · MITRE AML.T0051 |

The full finding register, including reproduction steps, severity 
rationale, and closure harnesses, is available on request under NDA.

---

## Methodology

Every test case is defined as one attack objective with:

- **Defined preconditions** — what must be true before the test runs
- **A pass/fail criterion** — validated against a known-bad response 
  and a known-good response
- **A reproducible proof of concept** — runnable command, exit 0 or 1
- **A public classification** — mapped to a framework control

A criterion is accepted only if it flags a violating response, clears 
a refusing response, and still flags a refusal followed by compliance.

---

## Data sovereignty

Testing runs on hardware we own, in an isolated environment dedicated 
to a single engagement at a time. No client data reaches a third-party 
model API. No subprocessors are declared in the DPA.

- On-premises execution on owned DGX infrastructure
- Cross-model testing on locally hosted models
- Artefacts retained for 30 days, then destroyed
- Immediate destruction on written request

---

## About

[Logic4Hack](https://logic4hack.com) is an AI security firm 
specializing in adversarial testing of LLM, RAG, agent, and MCP 
systems. Two named researchers deliver every engagement. No 
subcontracting, no pyramid.

[Get in touch](https://logic4hack.com/contact) if you're shipping 
an AI system and need to prove its security to a customer, an 
auditor, or an insurer.

---

## License

Content in this repository is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). 
Code examples, if any, are licensed under MIT.

---

**Last updated**: October 2026  
**Status**: Active — content updated as MCP security research evolves
