Career Profile Intelligence Platform

Overview

This application enables analysts, recruiters, and managers to analyze LinkedIn profile data of professionals based on the visibility level granted by their own LinkedIn accounts. It supports batch processing, profile metadata extraction, and structured storage, with a frontend dashboard and an extensible API backend.

Goals
	•	Analyze and store career progression, job history, education, and activity of individuals from LinkedIn.
	•	Support batch operations, profile metadata extraction, and visual rendering.
	•	Design a secure, scalable system using React for frontend, Flask for backend, and PostgreSQL for storage.

⸻

Architecture

Frontend
	•	Framework: React
	•	Views: Search input, profile selection modal, dashboard with timeline and table views
	•	Table Interactivity: Sorting, filtering, export options
	•	Status feedback: Toast messages for actions (e.g. delete, fetch complete)
	•	Settings page for LinkedIn token management

Backend
	•	Framework: Flask
	•	API Documentation: OpenAPI Spec (OAS)
	•	Database: PostgreSQL
	•	Containerization: Single Docker container
	•	Future extensibility for OAuth2 and token scopes

Data Model
	•	Profile
	•	Name, LinkedIn URL (clickable)
	•	Last updated timestamp
	•	Job history (with metadata: role type, company name, size, company URL)
	•	Education history
	•	Extracted skills, endorsements, and summary box fields
	•	Engagement level score
	•	User-defined tags (profile level only)
	•	Slowly Changing Dimensions (SCD) versioning of profile data

Batch Processing
	•	Upload list of names or LinkedIn URLs
	•	Preview selection UI for disambiguation (e.g. “John Smith”)
	•	Job queue with progress tracker
	•	Post-batch summary: total profiles processed

⸻

Features

MVP
	•	Search and select profiles by name
	•	Process batch LinkedIn profiles
	•	Display structured profile data (job, education, skills, activity)
	•	Timeline and tabular views
	•	Export profiles to CSV/Excel/JSON
	•	View LinkedIn engagement level
	•	User-defined tagging and tag-based filtering
	•	Store last updated timestamp per profile
	•	Settings page for token input
	•	Health check endpoint
	•	Internal logging of key actions
	•	Delete profile functionality

Deferred/Post-MVP
	•	OAuth2 login (e.g., Google)
	•	Email-based allowlist filtering post-login
	•	Scoped token and RBAC
	•	Error handling display and retry logs
	•	Search history
	•	Profile insights via NLP (e.g., promotion detection)
	•	Side-by-side profile comparison
	•	Pagination
	•	Accessibility features and dark mode
	•	Public developer token access

⸻

Data Handling
	•	Store only processed data, not raw LinkedIn responses
	•	Classify roles (full-time, volunteer, internship) using metadata
	•	LinkedIn activity fully fetched if accessible
	•	Store profile version history using SCD design pattern
	•	Secure token storage and user-specific configuration

⸻

Error Handling Strategy
	•	Backend logs for each fetch, deletion, and tag assignment
	•	Frontend toasts for success/failure feedback
	•	Validate LinkedIn URL format before processing
	•	Rate limiting according to LinkedIn’s public access guidelines
	•	Health check API for token, DB, and connection validation

⸻

Testing Plan
	•	Unit tests for API endpoints (CRUD, token validation, batch fetch)
	•	Integration tests for profile processing pipeline
	•	Frontend E2E tests for search, selection, and dashboard flow
	•	Manual tests for tag filtering, CSV export, and deletion
	•	Load tests for batch processing and timeline rendering

⸻

Deployment
	•	Backend served via Docker container
	•	React app built and deployed via standard CI/CD pipeline
	•	Database hosted on a cloud-managed PostgreSQL service

⸻

Notes
	•	All users currently operate under a shared LinkedIn token
	•	Only one authenticated user in MVP
	•	Token is entered manually through the settings page
	•	Search input should support common name collisions and preview selection