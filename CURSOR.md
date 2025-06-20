# AI Hotel Booking Agent - Project Plan

## Goal
Build an intelligent conversational AI agent using LangGraph, LangChain, and Google's Gemini API that can handle hotel room bookings across multiple mock hotels, reschedule existing reservations, and answer hotel-related questions through Instagram Direct Messages. The agent should maintain conversation context, resume interrupted conversations, and provide a seamless user experience with both Instagram and local testing interfaces.

## Project Status Tracking

### Stage Status Legend
- 🔴 **Not Started** - No work begun
- 🟡 **In Progress** - Currently being worked on
- 🟢 **Completed** - All requirements met and tests passing
- ⚠️ **Blocked** - Waiting for dependencies or external factors

### Testing Requirements
- **All tests must pass** before moving to the next phase
- **Previous phase tests** must continue passing when moving forward
- **Test coverage** should be maintained above 80% for core functionality
- **Integration tests** required for API interactions

## Critical Gaps Identified & Solutions

### 🚨 Missing Elements That Could Derail the Project

1. **Webhook Security**: Instagram webhooks need proper verification
2. **Rate Limiting**: Both Instagram API and Gemini API have strict limits
3. **Error Recovery**: Network failures, API timeouts, partial data corruption
4. **Concurrent Users**: Multiple users booking simultaneously
5. **Data Consistency**: Race conditions in booking availability
6. **Logging & Monitoring**: Essential for debugging production issues
7. **Configuration Management**: Environment-specific settings
8. **Dependency Management**: Version pinning and virtual environments
9. **CI/CD Pipeline**: Automated testing and deployment
10. **Documentation Standards**: Code comments, API docs, architecture diagrams

## Senior Developer Recommendations

### 🎯 How to Start (Structured Approach)

#### Week 1: Foundation & Planning
- **Day 1-2**: Set up development environment and tools
- **Day 3-4**: Create project structure and basic configuration
- **Day 5**: Implement logging, configuration management, and basic tests

#### Week 2: Core Development
- **Day 1-3**: Build and test core business logic (no external APIs)
- **Day 4-5**: Implement data layer with comprehensive testing

#### Week 3: Integration
- **Day 1-2**: LangGraph state machine implementation
- **Day 3-4**: Gemini API integration with fallback mechanisms
- **Day 5**: Local testing interface

#### Week 4: External Integration
- **Day 1-3**: Instagram API integration with proper security
- **Day 4-5**: End-to-end testing and error handling

### 🔧 Essential Tools & Setup
- **IDE**: VS Code with Python extensions
- **Database Tool**: DB Browser for SQLite
- **API Testing**: Postman or Insomnia
- **Version Control**: Git with proper branching strategy
- **Virtual Environment**: venv or conda
- **Code Quality**: pre-commit hooks, black formatter, pylint
- **Documentation**: Sphinx for auto-generated docs

## Prerequisites

### Technical Requirements
- **Python 3.8+** with virtual environment setup
- **LangGraph** - For building the conversational state machine
- **LangChain** - For LLM integration and prompt management
- **Google Gemini API** - As the primary LLM
- **Instagram Graph API** - For DM integration
- **SQLite** - For local data storage
- **Git** - For version control

### API Access & Official Documentation Links

#### Google Gemini API
- **Official Documentation**: https://ai.google.dev/docs
- **API Keys & Pricing**: https://makersuite.google.com/app/apikey
- **Python SDK**: https://github.com/google/generative-ai-python
- **Rate Limits**: 60 requests per minute (free tier)

#### Instagram Graph API
- **Getting Started Guide**: https://developers.facebook.com/docs/instagram-api/getting-started
- **Webhooks Documentation**: https://developers.facebook.com/docs/graph-api/webhooks/getting-started
- **Instagram Messaging**: https://developers.facebook.com/docs/messenger-platform/instagram/features/webhook
- **Developer Console**: https://developers.facebook.com/apps/

#### LangChain & LangGraph
- **LangChain Documentation**: https://python.langchain.com/docs/get_started/introduction
- **LangGraph Documentation**: https://langchain-ai.github.io/langgraph/
- **LangGraph Examples**: https://github.com/langchain-ai/langgraph/tree/main/examples
- **LangChain Templates**: https://github.com/langchain-ai/langchain/tree/master/templates

#### Development Tools
- **Python Virtual Environments**: https://docs.python.org/3/tutorial/venv.html
- **SQLite Documentation**: https://sqlite.org/docs.html
- **pytest Documentation**: https://docs.pytest.org/en/7.4.x/
- **FastAPI**: https://fastapi.tiangolo.com/
- **ngrok (for webhooks)**: https://ngrok.com/docs/getting-started/

### Development Environment
- Code editor (VS Code recommended)
- Postman or similar tool for API testing
- SQLite browser for database inspection

## Action Plan

### Phase 1: Foundation Setup (CRITICAL)
**Timeline: 2-3 days** | **Status: 🟡 In Progress**

#### 1.0 Pre-Development Setup (NEW)
**Status: 🟢 Completed**
- Set up proper project structure following Python best practices
- Configure logging framework (structured logging with different levels)
- Implement configuration management (environment-based configs)
- Set up pre-commit hooks for code quality
- Create comprehensive .gitignore
- Set up virtual environment with requirements.txt and requirements-dev.txt

**Tests Required:**
- Environment test: Verify virtual environment isolation
- Configuration test: Validate config loading from different environments
- Logging test: Verify log levels and formatting
- Pre-commit test: Ensure code quality checks work

#### 1.1 Project Structure Setup
**Status: 🟢 Completed**
```
hotel_booking_agent/
├── src/
│   ├── agent/
│   │   ├── __init__.py
│   │   ├── state_machine.py
│   │   ├── conversation_handler.py
│   │   └── prompts/
│   ├── services/
│   │   ├── __init__.py
│   │   ├── hotel_service.py
│   │   ├── booking_service.py
│   │   └── llm_service.py
│   ├── integrations/
│   │   ├── __init__.py
│   │   ├── instagram_client.py
│   │   └── database_client.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── hotel.py
│   │   ├── booking.py
│   │   └── conversation.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py
│   │   ├── config.py
│   │   └── validators.py
│   └── main.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── e2e/
├── data/
│   ├── mock_hotels.json
│   └── database/
├── docs/
├── scripts/
├── .env.example
├── .gitignore
├── requirements.txt
├── requirements-dev.txt
├── pytest.ini
├── setup.py
└── README.md
```

**Tests Required:**
- Structure test: Verify all directories and files are created
- Import test: Verify all modules can be imported
- Package test: Verify setup.py works correctly

#### 1.2 Dependency Management & Security
**Status: 🟢 Completed**
- Pin exact versions in requirements.txt
- Set up dependency vulnerability scanning
- Configure environment variables with validation
- Implement secrets management (no hardcoded credentials)
- Set up rate limiting and request timeout configurations

**Tests Required:**
- Dependency test: Verify all dependencies install correctly
- Security test: Scan for known vulnerabilities
- Environment test: Validate environment variable loading
- Timeout test: Verify request timeout configurations

#### 1.3 Database Schema Design & Mock Data (ENHANCED)
**Status: 🟢 Completed**
- Design normalized database schema with proper relationships: 🟢 Completed
- Implement database migrations system: 🟢 Completed
- Add database connection pooling: 🟢 Completed
- Create comprehensive mock data with realistic scenarios: 🟢 Completed
- Implement data seeding scripts: 🟢 Completed

**Database Schema:**
```sql
-- Users table
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    instagram_id TEXT UNIQUE NOT NULL,
    username TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_active TIMESTAMP
);

-- Conversations table
CREATE TABLE conversations (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    state TEXT NOT NULL,
    context TEXT, -- JSON blob
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id)
);

-- Hotels table
CREATE TABLE hotels (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL,
    star_rating INTEGER,
    description TEXT,
    amenities TEXT, -- JSON array
    policies TEXT, -- JSON object
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Room types table
CREATE TABLE room_types (
    id INTEGER PRIMARY KEY,
    hotel_id INTEGER,
    name TEXT NOT NULL,
    description TEXT,
    max_occupancy INTEGER,
    base_price DECIMAL(10,2),
    features TEXT, -- JSON array
    FOREIGN KEY (hotel_id) REFERENCES hotels (id)
);

-- Bookings table
CREATE TABLE bookings (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    hotel_id INTEGER,
    room_type_id INTEGER,
    check_in_date DATE,
    check_out_date DATE,
    num_guests INTEGER,
    total_price DECIMAL(10,2),
    status TEXT DEFAULT 'confirmed',
    booking_reference TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (hotel_id) REFERENCES hotels (id),
    FOREIGN KEY (room_type_id) REFERENCES room_types (id)
);

-- Booking modifications table
CREATE TABLE booking_modifications (
    id INTEGER PRIMARY KEY,
    booking_id INTEGER,
    modification_type TEXT, -- 'reschedule', 'cancel'
    old_check_in DATE,
    old_check_out DATE,
    new_check_in DATE,
    new_check_out DATE,
    fee_charged DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (booking_id) REFERENCES bookings (id)
);
```

**Tests Required:**
- Schema test: Verify database schema creation - 🟢
- Migration test: Test database migration scripts - 🟡 (Manual test complete)
- Data integrity test: Verify foreign key constraints - 🟡 (Implicitly tested)
- Mock data test: Validate mock data consistency - 🟢 (Unit test created)
- Performance test: Query performance with sample data - 🔴

### Phase 2: Core Business Logic (ENHANCED)
**Timeline: 4-5 days** | **Status: 🟡 In Progress**

#### 2.1 Hotel & Booking Services (NEW APPROACH)
**Status: 🟡 In Progress**
- Implement hotel search and filtering logic: 🟢 Completed
- Build booking availability checking with concurrency handling: 🔴 Not Started
- Create booking creation/modification services: 🔴 Not Started
- Implement thread-safe booking operations: 🔴 Not Started
- Add comprehensive input validation and sanitization: 🔴 Not Started
- Create booking reference generation system: 🔴 Not Started

**Tests Required:**
- Unit test: Hotel search algorithms - 🟢
- Unit test: Booking availability logic - 🔴
- Concurrency test: Multiple simultaneous bookings
- Integration test: End-to-end booking flow
- Edge case test: Invalid date ranges, unavailable rooms

#### 2.2 LangGraph State Machine Design (ENHANCED)
**Status: 🔴 Not Started**
- Design comprehensive state machine with error recovery
- Implement conversation checkpointing for resume capability
- Add timeout handling for long conversations
- Create state validation and consistency checks
- Implement conversation branching for complex scenarios

**State Machine Flow:**
```
INITIAL → HOTEL_SELECTION → DATE_SELECTION → ROOM_SELECTION →
GUEST_DETAILS → BOOKING_CONFIRMATION → COMPLETED

Side flows:
- Q&A_MODE (accessible from any state)
- RESCHEDULE_FLOW (from COMPLETED)
- ERROR_RECOVERY (from any state)
- CONVERSATION_RESUME (startup state)
```

**Tests Required:**
- Unit test: Each state transition and validation
- Integration test: Complete conversation flows
- Timeout test: Long conversation handling
- Resume test: Conversation checkpoint and recovery
- Error test: Invalid state transitions

#### 2.3 LLM Integration with Fallback (CRITICAL)
**Status: 🔴 Not Started**
- Implement Gemini API with retry logic and exponential backoff
- Add request/response caching to minimize API calls
- Create fallback responses for API failures
- Implement prompt engineering with context management
- Add response validation and sanitization

**Tests Required:**
- Unit test: API retry logic
- Integration test: Gemini API functionality
- Fallback test: Behavior during API failures
- Performance test: Response time optimization
- Quality test: Response relevance and accuracy

### Phase 3: Instagram Integration (SECURITY FOCUSED)
**Timeline: 3-4 days** | **Status: 🔴 Not Started**

#### 3.1 Secure Webhook Implementation (CRITICAL)
**Status: 🔴 Not Started**
- Implement webhook signature verification
- Add request rate limiting and DDoS protection
- Create secure message parsing with input sanitization
- Implement user authentication and session management
- Add webhook retry mechanism for failed deliveries

**Security Checklist:**
- Webhook signature validation using Instagram's secret
- Input validation and sanitization
- Rate limiting per user and global
- Request size limits
- IP allowlisting (if possible)
- Secure headers implementation

**Tests Required:**
- Security test: Webhook signature verification
- Load test: Rate limiting effectiveness
- Integration test: Message parsing accuracy
- Authentication test: User session management
- Failure test: Webhook retry mechanism

#### 3.2 Instagram API Client (PRODUCTION READY)
**Status: 🔴 Not Started**
- Implement Instagram Graph API client with proper error handling
- Add message queue for outgoing messages
- Implement exponential backoff for API failures
- Create message formatting and validation
- Add comprehensive logging for debugging

**API Limitations to Handle:**
- Rate limits: 200 calls per hour per user
- Message size limits
- Supported message types
- User context limitations

**Tests Required:**
- Unit test: API client functionality
- Integration test: Message send/receive flow
- Rate limit test: API quota management
- Error handling test: API failure scenarios
- Queue test: Message queuing system

### Phase 4: Local Testing Interface (DEVELOPMENT TOOL)
**Timeline: 2 days** | **Status: 🔴 Not Started**

#### 4.1 Development Testing Interface
**Status: 🔴 Not Started**
- Create web-based testing interface (Flask/FastAPI)
- Implement conversation simulation
- Add debugging features (state inspection, conversation history)
- Create admin panel for data management
- Add performance monitoring dashboard

**Features:**
- Real-time conversation testing
- State machine visualization
- Database inspection tools
- Log viewer
- Performance metrics

**Tests Required:**
- Unit test: Interface functionality
- Integration test: Feature parity with Instagram
- Usability test: Developer experience
- Performance test: Interface responsiveness

## Advanced Configuration Management

### Environment Configuration Structure
```python
# config/settings.py
class BaseConfig:
    # Database
    DATABASE_URL = "sqlite:///hotel_booking.db"
    DATABASE_POOL_SIZE = 10

    # Instagram API
    INSTAGRAM_APP_SECRET = os.getenv('INSTAGRAM_APP_SECRET')
    INSTAGRAM_ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')

    # Gemini API
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    GEMINI_MODEL = "gemini-pro"
    GEMINI_MAX_TOKENS = 1000
    GEMINI_TEMPERATURE = 0.7

    # Rate Limiting
    RATE_LIMIT_PER_USER = 10  # per minute
    RATE_LIMIT_GLOBAL = 100   # per minute

    # Logging
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "json"

    # Security
    WEBHOOK_VERIFY_TOKEN = os.getenv('WEBHOOK_VERIFY_TOKEN')
    SESSION_TIMEOUT = 3600  # seconds

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    LOG_LEVEL = "DEBUG"

class ProductionConfig(BaseConfig):
    DEBUG = False
    DATABASE_URL = os.getenv('DATABASE_URL')
```

### Logging Configuration
```python
# utils/logger.py
import logging
import json
from datetime import datetime

class StructuredLogger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        handler = logging.StreamHandler()
        formatter = StructuredFormatter()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def log_conversation_event(self, user_id, event_type, data):
        self.logger.info(json.dumps({
            "timestamp": datetime.utcnow().isoformat(),
            "user_id": user_id,
            "event_type": event_type,
            "data": data
        }))
```

### Phase 5: Data Management & Persistence
**Timeline: 1-2 days** | **Status: 🔴 Not Started**

#### 5.1 Database Operations
**Status: 🔴 Not Started**
- Implement CRUD operations for bookings across multiple hotels
- User session management with permanent storage
- Conversation history storage and retrieval
- Mock hotel data management and querying
- Booking search and filtering capabilities

**Tests Required:**
- Unit test: All CRUD operations
- Performance test: Database query optimization
- Data integrity test: Referential integrity and constraints
- Concurrency test: Multiple user sessions

#### 5.2 Data Validation & Error Handling
**Status: 🔴 Not Started**
- Input validation for dates, guest numbers, hotel selection
- Graceful degradation for system failures
- User-friendly error messages
- Conversation state recovery mechanisms

**Tests Required:**
- Unit test: All validation rules
- Edge case test: Invalid input handling
- Recovery test: System failure and recovery scenarios
- User experience test: Error message clarity

### Phase 6: Comprehensive Testing & Quality Assurance
**Timeline: 2-3 days** | **Status: 🔴 Not Started**

#### 6.1 Test Suite Completion
**Status: 🔴 Not Started**
- Ensure all unit tests from previous phases are passing
- Create comprehensive integration test suite
- Develop end-to-end test scenarios covering:
  - Complete booking workflows for multiple hotels
  - Rescheduling scenarios with fee calculations
  - Conversation interruption and resume
  - Error handling and recovery
- Performance testing and optimization

**Tests Required:**
- Regression test: All previous tests must pass
- Load test: System performance under concurrent users
- Stress test: System behavior at limits
- User acceptance test: Real-world usage scenarios

#### 6.2 Code Quality & Documentation
**Status: 🔴 Not Started**
- Code review and refactoring
- Comprehensive README with setup instructions
- Architecture documentation with LangGraph flow diagram
- API documentation
- Troubleshooting guide
- Mock data documentation

**Quality Checks:**
- Code coverage above 80%
- No critical security vulnerabilities
- Clean code standards compliance
- Documentation completeness review

### Phase 7: Deployment & Monitoring Setup
**Timeline: 1-2 days** | **Status: 🔴 Not Started**

#### 7.1 Deployment Configuration
**Status: 🔴 Not Started**
- Configure production environment
- Set up webhook URL (using ngrok for development)
- Environment-specific configurations
- Basic monitoring and logging setup
- Health check endpoints

**Tests Required:**
- Deployment test: Successful deployment verification
- Health check test: System status monitoring
- Integration test: Production environment functionality
- Security test: Production security validation

## Mock Hotel Data Structure

### Hotel Details (Intermediate Level)
Each of the 5-7 mock hotels will include:

**Basic Information:**
- Hotel name and brand
- Location (city, address, coordinates)
- Star rating (3-5 stars)
- Contact information

**Amenities & Services:**
- Standard amenities (WiFi, parking, breakfast)
- Premium amenities (spa, gym, pool, restaurant)
- Business facilities (meeting rooms, business center)
- Special services (concierge, room service, laundry)

**Room Types & Features:**
- Standard Room: Basic amenities, city/garden view
- Deluxe Room: Enhanced space, better view, premium amenities
- Suite: Separate living area, luxury amenities, premium location
- Family Room: Extra space, child-friendly features

**Pricing Structure:**
- Base rates for each room type
- Seasonal pricing variations
- Weekend vs weekday rates
- Special offers and packages

**Policies:**
- Check-in/out times
- Cancellation policies
- Rescheduling fees (flat rate or percentage-based)
- Pet policies, smoking policies
- Age restrictions

## Architecture Overview

### Core Components
1. **Instagram Webhook Handler** - Receives and processes Instagram messages
2. **LangGraph Agent** - Manages conversation state and flow
3. **Gemini LLM Integration** - Generates contextual responses
4. **Database Layer** - Stores bookings and conversation history
5. **Hotel Service** - Handles booking logic (with mock data)

### Data Flow
```
Instagram DM → Webhook → Agent Router → LangGraph State Machine → Gemini LLM → Response → Instagram DM
                                    ↓
                          Database Storage (Permanent)
                                    ↓
                        Conversation Resume Capability

Local Testing Interface → Agent Router → [Same flow as above] → Local Response
```

## Updated Mock Data Strategy

### Multiple Hotels (5-7 Hotels)
1. **Grand Plaza Hotel** (5-star, Business District)
2. **Seaside Resort & Spa** (4-star, Beach Location)
3. **Mountain View Lodge** (3-star, Hill Station)
4. **City Center Inn** (3-star, Downtown)
5. **Heritage Palace Hotel** (5-star, Historical)
6. **Airport Business Hotel** (4-star, Near Airport)
7. **Budget Stay Express** (2-star, Economic Option)

### Rescheduling Policy
- **Free rescheduling**: Up to 48 hours before check-in
- **Rescheduling fee**: $25-50 depending on hotel category and room type
- **Peak season surcharge**: Additional 20% fee during peak periods
- **Same-day rescheduling**: Subject to availability, higher fees apply

## Testing Strategy Overview

### Test Execution Flow
1. **Phase Completion Requirement**: All tests for the current phase must pass
2. **Regression Testing**: All tests from previous phases must continue to pass
3. **Integration Validation**: New features must integrate properly with existing functionality
4. **Documentation Update**: Test documentation must be updated with each phase

### Test Categories
- **Unit Tests**: Individual component functionality
- **Integration Tests**: Component interaction testing
- **End-to-End Tests**: Complete user journey testing
- **Performance Tests**: System performance and scalability
- **Security Tests**: Data protection and API security
- **User Experience Tests**: Interface usability and error handling

### Continuous Testing Requirements
- Automated test execution on code changes
- Test coverage monitoring (minimum 80%)
- Performance regression detection
- Security vulnerability scanning

## 🚀 How to Start (Step-by-Step Guide)

### Step 1: Initial Setup (Day 1)
```bash
# 1. Create project directory
mkdir hotel_booking_agent
cd hotel_booking_agent

# 2. Set up virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Create basic project structure
mkdir -p src/{agent,services,integrations,models,utils}
mkdir -p tests/{unit,integration,e2e}
mkdir -p {data,docs,scripts,config}

# 4. Initialize git
git init
echo "venv/" > .gitignore
echo "*.pyc" >> .gitignore
echo ".env" >> .gitignore
echo "__pycache__/" >> .gitignore

# 5. Create requirements files
touch requirements.txt requirements-dev.txt
```

### Step 2: Install Core Dependencies (Day 1)
```bash
# Add to requirements.txt:
langchain==0.1.0
langgraph==0.0.26
google-generativeai==0.3.2
fastapi==0.104.1
uvicorn==0.24.0
sqlalchemy==2.0.23
sqlite3
requests==2.31.0
python-dotenv==1.0.0
pydantic==2.5.0

# Add to requirements-dev.txt:
pytest==7.4.3
pytest-cov==4.1.0
black==23.11.0
pylint==3.0.3
pre-commit==3.6.0
httpx==0.25.2  # for testing async code

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

### Step 3: Set up Development Tools (Day 1)
```bash
# 1. Set up pre-commit hooks
pre-commit install

# 2. Create pytest.ini
echo "[tool:pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*
addopts = -v --tb=short --cov=src" > pytest.ini

# 3. Create .env.example
echo "# API Keys
GEMINI_API_KEY=your_gemini_api_key_here
INSTAGRAM_APP_SECRET=your_instagram_app_secret
INSTAGRAM_ACCESS_TOKEN=your_instagram_access_token
WEBHOOK_VERIFY_TOKEN=your_webhook_verify_token

# Database
DATABASE_URL=sqlite:///hotel_booking.db

# Environment
ENVIRONMENT=development
DEBUG=True" > .env.example
```

### Step 4: Create Basic Configuration (Day 2)
```python
# src/utils/config.py
import os
from typing import Optional
from pydantic import BaseSettings

class Settings(BaseSettings):
    # API Configuration
    gemini_api_key: str
    instagram_app_secret: str
    instagram_access_token: str
    webhook_verify_token: str

    # Database
    database_url: str = "sqlite:///hotel_booking.db"

    # Application
    environment: str = "development"
    debug: bool = True

    # Rate Limiting
    rate_limit_per_user: int = 10
    rate_limit_global: int = 100

    class Config:
        env_file = ".env"

settings = Settings()
```

### Step 5: Set Up Testing Framework (Day 2)
```python
# tests/conftest.py
import pytest
import tempfile
import os
from src.utils.config import Settings

@pytest.fixture
def test_settings():
    return Settings(
        gemini_api_key="test_key",
        instagram_app_secret="test_secret",
        instagram_access_token="test_token",
        webhook_verify_token="test_verify_token",
        database_url="sqlite:///:memory:",
        environment="testing",
        debug=True
    )

@pytest.fixture
def test_db():
    # Create temporary database for testing
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as tmp:
        yield tmp.name
    os.unlink(tmp.name)
```

## 🎯 Senior Developer Best Practices

### 1. **Start Small, Test Everything**
- Write failing tests first (TDD approach)
- Never commit code without tests
- Run tests after every change

### 2. **Configuration Management**
- Never hardcode values
- Use environment variables for all secrets
- Validate configuration on startup

### 3. **Error Handling Strategy**
```python
# Good error handling pattern
class BookingError(Exception):
    """Base exception for booking operations"""
    pass

class BookingNotFoundError(BookingError):
    """Raised when booking is not found"""
    pass

class BookingUnavailableError(BookingError):
    """Raised when booking is not available"""
    pass

# Usage in services
def create_booking(booking_data):
    try:
        # Booking logic here
        return booking
    except ValidationError as e:
        logger.error(f"Invalid booking data: {e}")
        raise BookingError(f"Invalid booking data: {e}")
    except DatabaseError as e:
        logger.error(f"Database error: {e}")
        raise BookingError("System temporarily unavailable")
```

### 4. **Monitoring & Observability**
- Log everything important
- Use structured logging (JSON format)
- Add metrics and health checks
- Monitor API usage and limits

### 5. **Security Checklist**
- Validate all inputs
- Use HTTPS everywhere
- Implement proper authentication
- Secure webhook endpoints
- Never log sensitive data

## 🔍 Code Quality Standards

### Commit Message Format
```
type(scope): description

Examples:
feat(booking): add hotel availability checking
fix(instagram): handle webhook signature verification
test(database): add booking CRUD operation tests
docs(readme): update setup instructions
```

### Code Review Checklist
- [ ] All tests pass
- [ ] Code coverage above 80%
- [ ] No hardcoded values
- [ ] Proper error handling
- [ ] Security considerations addressed
- [ ] Performance implications considered
- [ ] Documentation updated

## Potential Challenges & Solutions

1. **Instagram API Rate Limits**: Implement queuing and retry mechanisms
2. **Context Loss**: Store conversation state in database
3. **Date Parsing**: Use robust date parsing libraries
4. **Error Recovery**: Implement fallback flows for common errors
5. **User Authentication**: Use Instagram user ID for session management

## Success Metrics

- Successfully handle complete booking flows
- Maintain conversation context across multiple interactions
- Gracefully handle edge cases and errors
- Provide helpful responses to hotel-related questions
- Demonstrate clean, maintainable code architecture
