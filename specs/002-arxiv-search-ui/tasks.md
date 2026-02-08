---
description: "Task list for arXiv Search UI feature implementation"
---

# Tasks: arXiv Search UI

**Input**: Design documents from `specs/002-arxiv-search-ui/`
**Prerequisites**: plan.md, spec.md, data-model.md, research.md

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 [P] Create the project structure as defined in `plan.md`.
- [X] T002 [P] Initialize a Python project and add `arxiv` and `customtkinter` to `requirements.txt`.
- [X] T003 [P] Set up `pytest` for testing.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [X] T004 Implement the basic main window in `src/ui/main_window.py`.
- [X] T005 Implement the arXiv search logic in `src/search/arxiv_search.py` to connect to the arXiv API.
- [X] T006 Implement the CSV exporter in `src/utils/csv_exporter.py`.

---

## Phase 3: User Story 1 - Basic Search and Display (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to be able to type keywords into a search box, initiate a search, and see the results displayed on the screen.

**Independent Test**: The user can input a search query, and the UI displays matching results.

### Implementation for User Story 1

- [X] T007 [US1] Create the keyword search input field in the main window.
- [X] T008 [US1] Implement the logic to trigger a search when the user presses enter in the search box.
- [X] T009 [US1] Implement the display of search results in the main window.
- [X] T010 [US1] Implement the logic to clear the search and display all results.
- [X] T011 [US1] Implement the display of a loading indicator during search.

---

## Phase 4: User Story 2 - Advanced Filtering (Priority: P2)

**Goal**: As a user, I want to refine my search using a time range, author's name, and specify the maximum number of papers to retrieve.

**Independent Test**: The user can apply various filters (time range, author, paper limit) and see the results update accordingly.

### Implementation for User Story 2

- [X] T012 [P] [US2] Create input fields for time range, author, and max results in the main window.
- [X] T013 [US2] Implement the logic to include the filter parameters in the search query.
- [X] T014 [US2] Implement the logic to update the search results when filters are changed.
- [X] T015 [P] [US2] Implement input validation for the date and max results fields.

---

## Phase 5: User Story 3 - Export Search Results (Priority: P2)

**Goal**: As a user, I want to be able to save the displayed search results to a CSV file.

**Independent Test**: The user can perform a search and then successfully export the displayed results.

### Implementation for User Story 3

- [X] T016 [US3] Create an "Export to CSV" button in the main window.
- [X] T017 [US3] Implement the logic to call the `csv_exporter` with the current search results.

---

## Phase 6: User Story 4 - Default Display (Priority: P3)

**Goal**: As a user, when I open the application, I want to see a list of recent or popular papers.

**Independent Test**: The user can launch the application and see a pre-populated list of papers.

### Implementation for User Story 4

- [X] T018 [US4] Implement the logic to perform a default search for recent or popular papers on application startup.
- [X] T019 [US4] Display the default search results in the main window.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T020 [P] Implement Traditional Chinese localization for all UI elements and messages.
- [X] T021 [P] Write unit tests for the search logic.
- [X] T022 [P] Write unit tests for the CSV exporter.
- [X] T023 [P] Write UI tests for the main window.
- [X] T024 [P] Final code cleanup and refactoring.
- [X] T025 [P] Update `README.md` with final instructions.
