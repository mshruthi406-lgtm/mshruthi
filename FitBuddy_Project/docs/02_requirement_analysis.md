# Phase 2 – Requirement Analysis

## Functional Requirements
| ID | Requirement |
|---|---|
| FR1 | Accept user name and user ID |
| FR2 | Accept age and weight |
| FR3 | Accept fitness goal |
| FR4 | Accept low/medium/high intensity |
| FR5 | Generate a structured 7-day plan |
| FR6 | Generate a nutrition/recovery tip |
| FR7 | Store user and plan information |
| FR8 | Accept feedback |
| FR9 | Produce an updated plan |
| FR10 | Display original and updated plans |
| FR11 | Provide an all-users/admin page |
| FR12 | Expose FastAPI documentation |

## Non-Functional Requirements
- Simple responsive UI
- Input validation
- Persistent local database
- Environment variable for API key
- Clear modular Python code
- Local deployment using Uvicorn

## Inputs
Name, user ID, age, weight, goal, intensity, feedback.

## Outputs
7-day plan, nutrition tip, updated plan, confirmation message, admin records.

## Constraints
The application is a student project/demo. Fitness content should not be treated as medical diagnosis or treatment.
