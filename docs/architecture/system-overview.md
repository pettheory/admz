# ADMZ - Axis Device Management Zone

## System Overview

ADMZ is an intelligent device management system for Axis cameras and IoT devices, designed specifically for Field Sales Engineers (FSEs) to streamline large-scale device deployments.

## Core Components

### 1. Device Manager
- Natural language to device configuration
- Intelligent capability discovery
- Mass deployment automation
- Error handling and troubleshooting

### 2. Analytics Agent
- Axis Object Analytics configuration
- Scene-aware recommendations
- Consultative deployment process
- Performance optimization

### 3. Secrets Manager
- Secure credential management
- Local secrets storage
- Device access control
- Audit logging

### 4. Knowledge Base
- Product specifications and capabilities
- Configuration best practices
- Troubleshooting guides
- Deployment templates

## Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Input    │───▶│ Intent Parser   │───▶│ Task Generator  │
│  (Natural Lang) │    │   (AI Agent)    │    │  (AI Planning)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                        │
                        ┌─────────────────┐             ▼
                        │ Secrets Manager │    ┌─────────────────┐
                        │ (Local, Secure) │◄───│ Task Executor   │
                        └─────────────────┘    │ (Step-by-step)  │
                                               └─────────────────┘
                                                        │
┌─────────────────┐    ┌─────────────────┐             ▼
│ Device Network  │◄───│ Device API      │◄────────Device API  │
│ (Axis Cameras)  │    │ (VAPIX)         │    │ (VAPIX/HTTP)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## Key Features

### Intelligent Device Discovery
- Automatic capability detection
- Firmware version awareness
- Hardware variant recognition
- Self-documenting API exploration

### Natural Language Configuration
- Intent-based device management
- Context-aware recommendations
- Multi-device coordination
- Human-in-the-loop approval

### Mass Deployment Support
- Bulk configuration management
- Progressive rollout capabilities
- Error recovery and rollback
- Performance monitoring

### Security-First Design
- Local credential management
- No passwords in LLM context
- Audit trail for all operations
- Network segmentation support

## Technology Stack

- **Backend:** Python with FastAPI
- **AI/ML:** Google Gemini API
- **Device Communication:** VAPIX, HTTP/HTTPS
- **Storage:** SQLite for local data
- **Documentation:** Markdown, Obsidian integration
- **Version Control:** Git with GitHub
