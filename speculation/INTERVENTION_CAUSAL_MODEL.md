# Intervention Causal Model

Status: SPECULATIVE_MODEL / FORMALIZATION_DRAFT

## Variables

- S_t — agent/environment state at in-world time t
- P — predictor/controller model
- F(S_t) — forecast of future outcome X
- I — intervention chosen because of forecast
- R(agent, I) — agent response to intervention
- S_t' — state after intervention enters causal history
- X' — outcome produced from altered state

## Naive controller

P observes S_t
-> predicts X
-> issues I to prevent X
-> assumes original forecast remains valid

Failure:
I changes S_t.

The relevant prediction was never:
P(X | S_t)

after intervention.

It becomes:
P(X | S_t, I, R(I), social_reaction(I), downstream_feedback...)

## Self-fulfilling form

forecast X
-> warning about X
-> increased salience/fear/coordination
-> changed behavior
-> X becomes more likely

## Self-negating form

forecast X
-> warning about X
-> successful avoidance
-> X does not occur

This creates an epistemic paradox for in-world observers:
the absence of X after a warning does not by itself show that the warning was false, while X occurring does not by itself show the predictor was independently accurate.

## Recursive controller

A more capable P predicts its own intervention.

But recursion does not automatically solve the problem if:
- agent response is stochastic;
- model depth is bounded;
- observation changes behavior;
- multiple agents receive/react to information;
- intervention changes incentives;
- controller objectives conflict;
- the system contains other predictors/controllers.

## Project theological mapping

Possible ancient interpretation:
- warning = prophecy;
- intervention channel = voice/vision/sign;
- controller = god/angel/demon according to local ontology;
- changed behavior = fulfillment or avoidance;
- retrospective narrative = prophecy tradition.

This mapping is speculative.

## Testable pressure

The model gains scientific value only if it identifies information that:
- was not normally available to the recipient;
- was specified before the outcome;
- survives documentation controls;
- predicts beyond base rates;
- shows intervention-sensitive causal structure.

Without that, it remains philosophy/literature.
