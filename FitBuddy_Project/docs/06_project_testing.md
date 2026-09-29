# Phase 6 – Project Testing

## Test Cases

| Test ID | Test | Expected Result |
|---|---|---|
| T01 | Open `/` | Home form loads |
| T02 | Submit valid profile | 7-day plan page loads |
| T03 | Submit missing required field | Browser/backend validation prevents invalid submission |
| T04 | Generate same user ID again | Existing user/plan is refreshed |
| T05 | Submit feedback for valid ID | Updated plan and confirmation appear |
| T06 | Submit feedback for unknown ID | Error page appears |
| T07 | Open `/view-all-users` | Stored users and plans are listed |
| T08 | Delete a user | User and plan are removed |
| T09 | Open `/docs` | FastAPI Swagger documentation loads |
| T10 | Run without API key | Demo fallback keeps the workflow usable |

## Automated Tests
`tests/test_app.py` covers:
- Home page
- Plan generation
- Feedback update

Run:
```bash
pytest
```

## Acceptance Criteria
The application should start locally, accept a valid profile, generate a plan, persist it, process feedback, and display stored records.
