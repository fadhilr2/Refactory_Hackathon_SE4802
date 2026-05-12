## ADDED Requirements

### Requirement: Flat Directory Structure
The system SHALL have a flat root directory structure consisting of three main folders (`cli/`, `pipeline/`, and `inference/`). 

#### Scenario: Verify root structure
- **WHEN** the repository is initialized
- **THEN** the root directory contains exactly three main folders: `cli/`, `pipeline/`, and `inference/`.

### Requirement: CLI Directory
The system SHALL use the `cli/` directory to contain the command-line interface logic.

#### Scenario: Verify CLI directory existence
- **WHEN** the repository structure is applied
- **THEN** a directory named `cli/` is created at the root.

### Requirement: Pipeline Directory
The system SHALL use the `pipeline/` directory to handle data ingestion, tracking, and extraction processes.

#### Scenario: Verify Pipeline directory existence
- **WHEN** the repository structure is applied
- **THEN** a directory named `pipeline/` is created at the root.

### Requirement: Inference Directory
The system SHALL use the `inference/` directory to manage local AI processing.

#### Scenario: Verify Inference directory existence
- **WHEN** the repository structure is applied
- **THEN** a directory named `inference/` is created at the root.
