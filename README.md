# HR/Employee Assistant Chatbot 

_By [Spyros Mavromatis](https://github.com/spymavro) & [Eirini-Garyfalia Kyriakou](https://github.com/eirkyr)_

---
## Overview
This project is a **Task-Oriented Dialog System Prototype** designed to assist employees and HR personnel with essential HR-related tasks. The chatbot is built using **[Rasa](https://rasa.com/)**, an open-source conversational AI framework, and integrates with **Horilla HRMS**, a free and open-source Human Resource Management System (HRMS). Horilla provides a comprehensive solution for managing employees, payroll, policies, leave, and more.

The chatbot mainly supports retrieving employee details, updating employee information, and listing available job positions, by interacting with Horilla's API. It also displays leave types and handles HR policy inquiries and provides direct HR contact details using predefined responses.

---

## Domain and Motivation
So, the HR/Employee Assistant Chatbot is designed for **Human Resources (HR) and Employee Support**. It serves as a task-oriented dialog system that streamlines HR-related interactions such as:
- Retrieving employee details
- Updating employee information
- Listing available job positions
- Displaying leave types
- Providing company policies and HR contact details

In today’s fast-paced work environment, quick and efficient access to HR information is crucial. The HR/Employee Assistant Chatbot was developed to:

- **Streamline Employee Interactions:** Automate routine tasks (e.g., fetching employee details, updating records etc.) to reduce manual workload.
- **Enhance Efficiency:** Provide instant, accurate responses to HR-related queries.
- **Improve Accessibility:** Enable employees to access important HR information at any time, thereby supporting self-service.

**Why Horilla HRMS?**
Horilla is an open-source HRMS that offers a robust set of features for managing employee data. Its API allows seamless integration with external systems, making it an ideal choice for this project. You can access Horilla's source code and documentation on its [GitHub repository](https://github.com/horilla-opensource/horilla?tab=readme-ov-file).

---
## Implemented Scenarios & Functionalities
Firstly, the chatbot supports several key scenarios, organized into main intents:
### 1. General Conversation & Greeting
- To maintain a natural conversation flow, the chatbot includes these core **intents**:
  - `greet`
  - `goodbye`
  - `thanks`
  - `affirm`
  - `deny`
  - `mood_great`
  - `mood_unhappy`
  - `bot_challenge`
  - `provide_name`
_(and additional basic conversation intents)_

- **Functionality:**
  - Initiates conversation with a friendly greeting.
  - Acknowledges user names.
  - Handles polite exchanges (thanks, goodbye).

- **Files Involved:**  
  - **nlu.yml:** Contains training examples for these general intents.  
  - **domain.yml:** Defines responses (e.g., `utter_greet`, `utter_goodbye`, `utter_thanks`, etc.).  
  - **rules.yml:** Maps these intents to the appropriate utterances in a rule-based fashion.


### 2. Scenario A: Company Policies (Predefined Responses)
- **Description**: Employees can inquire about various company policies directly from the chatbot. The responses are predefined and do not require API interactions.
- **Workflow**:
  1. The user asks about a specific policy (e.g., code of conduct, remote work policy).
  2. The chatbot responds with detailed information stored in predefined responses (`utter_` responses).
- **Policies Covered:**
  - **Code of Conduct:** Professional behavior expectations and ethics standards.
  - **Information Security:** Guidelines on protecting company data and security protocols.
  - **Remote Work:** Rules for remote work, security measures, and communication expectations.
  - **Data Privacy:** Compliance with GDPR/CCPA and data handling practices.
  - **Device Usage:** Proper use of company-provided and personal devices.
  - **IT Support:** How to report technical issues and request assistance.
  - **NDA Policy:** Rules on sharing confidential company information.
  - **Software Use:** Approved software usage and restrictions.
  - **Internet Usage:** Appropriate internet use policies during work hours.

- **Files Involved:**
  - `domain.yml`: Defines intents and `utter_` responses for each policy (e.g., `utter_code_of_conduct`, `utter_information_security`, etc.).
  - `rules.yml`: Maps each policy-related intent to the correct `utter_` response.
  - `nlu.yml`: Provides training examples for policy-related intents.

This scenario highlights the chatbot’s ability to deliver quick, consistent policy responses without relying on external APIs.

### 3. Scenario B: Fetch Employee Details 
- **Description**: Employees can request their personal and work-related details, such as name, department, job position, and more.
- **Workflow**:
  1. The user provides their employee ID.
  2. The chatbot triggers the `action_fetch_employee_details` action, which makes a GET request to Horilla's API.
  3. The employee's details are fetched, formatted, and displayed to the user.
- **Files Involved**:
  - `nlu.yml`: Defines the `fetch_employee_details` intent with examples that include an `employee_id` entity.
  - `domain.yml`: Includes the `action_fetch_employee_details` action in the actions list.
  - `stories.yml`: Contains stories such as "Name, ID and Details" and "Original Fetch Employee Details" that demonstrate this flow.
  - `rules.yml`: Contains rules mapping the `fetch_employee_details` intent to the `action_fetch_employee_details` action.
  - `actions.py`: Implements the `ActionFetchEmployeeDetails` class which handles the API call and response formatting.

### 4. Scenario C: Update employee Details
- **Description**: This scenario allows employees (or HR personnel) to update an employee’s information.
- **Workflow**:
  1. The user provides their employee ID along with the field name and the new value.
  2. Chatbot processes the update request via an API call (`action_update_employee_details`).
  3. A confirmation message is sent back to the user.
- **Files Involved**:
  - `nlu.yml`: Contains training examples for the `update_employee_details` intent, including entities for `employee_id`, `field_name`, and `field_value`.
  - `domain.yml`: Lists the `action_update_employee_details` action.
  - `stories.yml`: Includes stories such as "Name, ID and Update Details", "Further Updates", and "Original Update Employee Details" that depict the update flow.
  - `actions.py`: Implements the `ActionUpdateEmployeeDetails` class which sends the PUT request to Horilla's API and handles the response.
  
### 5. Scenario D: List Job Positions
- **Description**: Lists available job positions by fetching data from the Horilla API. 
- **Workflow**:
  1. The user invokes the intent to list job positions.
  2. The chatbot calls the `action_list_job_positions` action.
  3. A list of available job positions is retrieved from the API and presented in a user-friendly format.
- **Files Involved**:
  - `nlu.yml`: Contains the `list_job_positions` intent examples.
  - `domain.yml`: Includes the `action_list_job_positions` action.
  - `stories.yml`: Contains a story for listing job positions.
  - `actions.py`: Implements the `ActionListJobPositions` class which handles the API call and message formatting. 
  
### 6. Scenario E: Show Leave Types (Mocked Data)
- **Description:**: Displays different leave types (e.g., Maternity, Sick, Casual) using mocked data within the chatbot.

- **Workflow:**
  1. The user asks about leave types.
  2. The chatbot responds with a preformatted list including details like duration, pay status, and notes.
  
- **Files Involved:**  
  - **nlu.yml:** Contains the `ask_leave_types` intent.
  - **domain.yml:** Lists the `action_show_leave_types` action.
  - **stories.yml:** Includes the story or rule flow for leave types.
  - **rules.yml:** Maps the `ask_leave_types` intent to the `action_show_leave_types` action.
  - **actions.py:** Implements the `ActionShowLeaveTypes` class that returns the mocked leave types data.


### 7. Scenario F: Contact with HR (without API)
- **Description:** Employees can request HR contact details for various queries, such as payroll issues or feedback submissions without needing an API call.

- **Main Intents Involved:**
  - `ask_contact_hr`

- **Workflow**
  1. The user asks how to contact HR.
  2. The chatbot immediately replies with a predefined message that includes HR email and phone number.

- **Response Provided:**
  - "You can contact HR at hr@company.com or call +1-234-567-890."

- **Files Involved:**
  - `nlu.yml`: Defines the `ask_contact_hr` intent with training examples.
  - `domain.yml`: Includes the `utter_ask_contact_hr` response.
  - `rules.yml`: Maps the `ask_contact_hr` intent to the `utter_ask_contact_hr` response.

This scenario demonstrates how the chatbot handles direct HR contact inquiries using predefined responses without API interactions. 

---
## Data Sources & Integrations

The HR/Employee Assistant Chatbot leverages multiple data sources and integrations to deliver accurate, real-time HR information while ensuring a smooth conversational experience. Below are the key components and how they interact:

### Horilla HRMS API
- **Employee Details & Updates:**  
  - **Endpoints:**  
    - **Fetch Employee Details:**  
      `http://127.0.0.1:8000/api/employee/employees/{employee_id}/`
    - **Update Employee Details:**  
      Same endpoint is used with an HTTP PUT request.
  - **Purpose:**  
    Enables real-time retrieval and updating of employee information.
  - **Authentication:**  
    Uses a JWT token (passed in the HTTP header as `Authorization: Bearer <token>`) for secure API access.

- **Job Positions:**  
  - **Endpoint:**  
    `http://127.0.0.1:8000/api/base/job-positions/`
  - **Purpose:**  
    Dynamically fetches a list of job positions within the organization, ensuring users receive the most up-to-date information.

### Mocked Data for Leave Types
- **Description:**  
  - Leave types such as Maternity, Sick, and Casual are provided as mocked data within the chatbot (via the `ActionShowLeaveTypes` action).
- **Purpose:**  
  - Demonstrates handling of static data when API integration is not implemented or necessary for that particular function.

### Database Integration
- **Database:**  
  - Horilla HRMS utilizes PostgreSQL for backend data storage.
- **Purpose:**  
  - Ensures persistent and reliable storage of employee records, job positions, and policy information.
- **Setup:**  
  - PostgreSQL is installed and managed locally (using Homebrew on macOS), with appropriate roles and databases configured to support the HRMS.

### Rasa Integration
- **Custom Actions:**  
  - Implemented in `actions.py`, these actions (e.g., `ActionFetchEmployeeDetails`, `ActionUpdateEmployeeDetails`, and `ActionListJobPositions`) directly call Horilla HRMS API endpoints to fetch or update data.
- **Dialog Management:**  
  - Rasa's NLU and Core components process user messages, extract entities (such as `employee_id`, `field_name`, and `field_value`), and trigger the corresponding actions based on defined stories and rules.


---

## Error Handling and Robustness

The HR/Employee Assistant Chatbot has been designed with robust error handling mechanisms and extensive training data to ensure a smooth user experience, even when unexpected issues occur. Below are the key measures implemented, along with examples extracted from our YAML and Python files:

### 1. API Response Error Handling

Custom actions that interact with the Horilla HRMS API include checks on the HTTP response status. If an API call fails, the chatbot provides a clear error message to the user.

#### a. Fetching Employee Details
In the `ActionFetchEmployeeDetails` action (in `actions.py`), the following code handles API errors:
```python
if response.status_code == 200:
    # Process and format the employee details
else:
    dispatcher.utter_message(
        text=f"Failed to fetch employee details. Status code: {response.status_code}. Response: {response.text}"
    )
 ```   
**Example Error Message:**
"Failed to fetch employee details. Status code: 404. Response: Not Found"
#### b. Updating Employee Details
In the ActionUpdateEmployeeDetails action, error handling during a PUT request is implemented as follows:
```python
if response.status_code == 200:
    dispatcher.utter_message(
        text=f"Successfully updated {field_name} to {field_value} for employee {employee_id}!"
    )
    dispatcher.utter_message(text="Do you want to make any further update?")
else:
    dispatcher.utter_message(
        text=f"Failed to update details. Status code: {response.status_code}. Response: {response.text}"
    )
 ```
**Example Error Message:**
"Failed to update details. Status code: 400. Response: Bad Request"

#### c. Listing Job Positions
In the ActionListJobPositions action, error handling is done as follows:
```python
if response.status_code == 200:
    # Process and list job positions
else:
    dispatcher.utter_message(
        text=f"Failed to list job positions. Status code: {response.status_code}. Response: {response.text}"
    )
 ```
**Example Error Message:**
"Failed to list job positions. Status code: 500. Response: Internal Server Error"

### 2. Robust NLU Training Data
The NLU training data in nlu.yml includes diverse examples to handle variations in user input. This improves the system's ability to correctly identify intents and extract entities, even when users phrase their requests in multiple ways.

Examples:

- **Greetings**: "hey", "hello", "hi there", "good morning", "good evening"
- **Expressions of Thanks**: "Thanks", "thank you very much", "No, thanks", "no, thank you"
- **Negative or Cancellation Phrases**: "No", "I don't want to make more updates", "no, thanks"

### 3. Rule-Based Response Handling
Rules defined in rules.yml ensure that conversation flows remain predictable. For example, the following rule handles HR contact inquiries:
```yaml
- rule: Ask contact HR
  steps:
    - intent: ask_contact_hr
    - action: utter_ask_contact_hr
 ```
This mapping guarantees that, regardless of variations in user phrasing, the chatbot consistently responds with the correct HR contact details.

### 4. Fallback and User Guidance
While a dedicated fallback policy (e.g., using a FallbackClassifier) is not explicitly detailed in the current configuration, the system still provides robust guidance by:

- **Prompting for Missing Information:**
If required details (such as the employee ID) are missing, the chatbot prompts the user to provide them.
- **Clear Error Messages:**
When API calls fail, the chatbot returns clear error messages to help the user understand the issue.
- **Graceful Conversation Closure:**
Responses like utter_no_more_updates ensure that conversations can end smoothly when no further action is needed.

---
## Challenges & How They Were Addressed

1. **API Integration:**
   - **Challenge:**  
     Integrating with Horilla's API required a deep understanding of its authentication mechanism (Bearer Token) and endpoint structure.
   - **Solution:**  
     - We added the JWT token in the `Authorization` header in our custom action implementations (e.g., `ActionFetchEmployeeDetails`, `ActionUpdateEmployeeDetails`, and `ActionListJobPositions` in `actions.py`).
     - This token is securely passed with each API request to ensure authenticated access.
     - The endpoint URLs were carefully configured according to Horilla HRMS documentation, ensuring that data is fetched and updated correctly.

2. **Incomplete User Information:**
   - **Challenge:**  
     Users may not always provide all necessary details (such as employee ID, field name, or field value) in their initial message.
   - **Solution:**  
     - We designed the conversation flows in `stories.yml` and `rules.yml` to handle missing information by prompting the user for the required details.
     - For example, if the employee ID is missing, the bot responds with, “Please provide the ID of your account.”
     - This ensures that the required data is collected before proceeding with API calls, minimizing errors.

3. **Interaction of Files in Rasa:**
   - **Challenge:**  
     Coordinating multiple configuration files (like `nlu.yml`, `domain.yml`, `stories.yml`, and `rules.yml`) can be complex, as each file plays a specific role in the system.
   - **Solution:**  
     - We maintained a clear and organized project structure where:
       - `nlu.yml` contains comprehensive training examples for intent recognition.
       - `domain.yml` defines intents, entities, slots, responses, and actions.
       - `stories.yml` outlines the dialogue flows for various scenarios.
       - `rules.yml` ensures predictable responses for rule-based interactions.
     - Regular integration testing was performed to ensure consistency across these files, ensuring that modifications in one file do not adversely affect the overall system functionality.
---
## Setup & Credentials 

### Prerequisites
Before starting, we ensure that we have the following installed on your system:
- **Python 3.8 or higher**
  - Python versions **3.10.12** (for Rasa) and **3.9.10** (for Horilla)
- **PostgreSQL** (for Horilla HRMS)
- **Git** (for cloning repositories)

### Set Up Directories & Virtual Environments
1. **Install `pyenv` and `pyenv-virtualenv`** (macOS):
```bash
   brew install pyenv-virtualenv
```
2.1 **Create a project directory for the Rasa chatbot**
```bash
mkdir /Users/user/my-rasa-project
cd /Users/user/my-rasa-project
```
2.2 **Create a virtual environment for Rasa**
```bash
pyenv virtualenv 3.10.12 my-rasa-project-venv
pyenv local my-rasa-project-venv
```

3.1 **Create a project directory for Horilla**
```bash
mkdir /Users/user/horilla-project
cd /Users/user/horilla-project
```
3.2 **Create a virtual environment for Horilla**
```bash
pyenv virtualenv 3.9.10 horilla-venv
pyenv local horilla-venv
```

### Project Structure
1. **RASA**

1.1 **Install Rasa**

```bash
pip install rasa
```
1.2 **Initialize Rasa project**
```bash
rasa init
```
2. **HORILLA**

2.1 **Clone the Horilla repository**
```bashgit 
cd /Users/user/horilla-project
clone https://github.com/horilla-opensource/horilla.git
```
2.2 **Install required dependencies**
```bashgit 
cd horilla
pip install -r requirements.txt
```
3. **PostgreSQL**

3.1 **Database Configuration**
```bashgit
brew install postgresql
brew services start postgresql
brew services list
psql -d postgres
```

```bashgit
CREATE ROLE horilla LOGIN PASSWORD 'create_your_password';

CREATE DATABASE horilla_main OWNER horilla;
```


3.2 **Environment Configuration**

Rename the Provided Environment File & Edit the .env File
```bashgit
mv .env.dist .env
nano .env
```

Update the File with Your Database Configuration
```dotenv
# Set "DEBUG=False" for production environments
DEBUG=True

# Django Secret Key (generate your own if needed)
SECRET_KEY=django-insecure-j8op9)1q8$1&@^s&p*_0%d#pr@w9qj@lo=3#@d=a(^@9@zd@%j

# Allowed Hosts (for development)
ALLOWED_HOSTS=localhost,127.0.0.1

# Time Zone
TIME_ZONE=Europe/Athens

# Database URL: Format is postgresql://<DB_USER>:<DB_PASSWORD>@<DB_HOST>:<DB_PORT>/<DB_NAME>
DATABASE_URL=

# Additional DB credentials (if used by initialization scripts)
DB_INIT_PASSWORD=
DB_ENGINE=django.db.backends.postgresql
DB_NAME=horilla_main
DB_USER=horilla
DB_PASSWORD=
DB_HOST=localhost
DB_PORT=5432
```

Generate a New Django Secret Key
- To generate a new key, we run the following in Python (e.g., via Google Colab or a local shell):

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```
- We replace the SECRET_KEY in .env file with the new key


4. **MIGRATIONS & SERVER RUN**

4.1 **Apply Horilla migrations**

```bash
cd /Users/user/horilla-project/horilla
python3 manage.py makemigrations
python3 manage.py migrate
```
4.2 **Create a Horilla user (insert username, password etc)**
```bash
python3 manage.py createhorillauser
```

4.3 **Then run the server**
```bash
python3 manage.py runserver
```
Access it at http://127.0.0.1:8000/

### Bearer Token Retrieval
**To authenticate from your Rasa chatbot or any REST client, you’ll need a Bearer token. For example:**
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"username": "your_username_from_horilla_user", "password": "your_password_from_horilla_user"}' \
  http://127.0.0.1:8000/api/auth/login/
```
This returns an access token in JSON, which you can use in your Rasa actions.py

---
## Example Runs

<details> <summary>Example 1: Fetching Employee Details</summary>

- User: “hello there”

- Bot: “Hi, I’m Rasa’s HR Assistant. What's your name?”

- User: "I'm Oddo"

- Bot: "Nice to meet you, Odoo! What can I do for you?"

- User: “Please provide my account details.”

- Bot: “Please provide the ID of your personal account.”

- User: “The ID of my account is 2.”

- Bot:

```yaml
Here are the employee’s details:
Id: 2
Job_position_name: Odoo Dev
Job_position_id: 1
Employee_work_info_id: 1
Employee_bank_details_id: None
Badge_id: PEP01
Employee_first_name: Michael
Employee_last_name: Brown
Employee_profile: /media/employee/profile/allgo-an-app-for-plus-size-people-Akaz9xK_f2M-unsplash.jpg
Email: michael.brown@horilla.com
Phone: 9876540001
Address: None
Country: None
State: None
City: None
Zip: None
Dob: None
Gender: male
Qualification: None
Experience: None
Marital_status: single
Children: None
Emergency_contact: None
Emergency_contact_name: None
Emergency_contact_relation: None
Is_active: True
Additional_info: None
Is_from_onboarding: False
Is_directly_converted: False
Employee_user_id: 3
```

</details> <details> <summary>Examples 2: Updating Employee Details</summary>

**Example 1:** 

- User: “Hi" 

- Bot: “Hi, I’m Rasa’s HR Assistant. What's your name?”

- User: "My name is Benjamin"

- Bot: "Nice to meet you, Benjamin! What can I do for you?"

- User: “ I want to update my account details”

- Bot: “Please provide the ID of the employee and the update you want to make.”

- User: “I want to change the phone for employee 11 to 6934987643”

- Bot: “Successfully updated phone to 6934987643 for employee 11! Do you want to make any further update?”

- User: "yes please"

- Bot: "Please provide the ID of the employee and the update you want to make."

- User: "I would like change the address for employee 11 to 12 Finley Street"

- Bot: Successfully updated address to 12 Finley Street for employee 11! Do you want to make any further update?

- User: "I am good, thanks"

- Bot: "If you need anything else, let me know."


**Example 2: (Fenching & Updating)** 

- User: “Hi" 

- Bot: “Hi, I’m Rasa’s HR Assistant. What's your name?”

- User: "My name is Scarlett"

- Bot: "Nice to meet you, Scarlett! What can I do for you?"

- User: “Show details for employee 34”

- Bot: 

```yaml
Here are the employee’s details:
Id: 34
Job_position_name: Social Media Coordinator
Job_position_id: 10
Employee_work_info_id: 33
Employee_bank_details_id: None
Badge_id: PEP37
Employee_first_name: Scarlett
Employee_last_name: Martinez
Employee_profile: None
Email: scarlett.martinez@horilla.com
Phone: 9876540037
Address: None
Country: None
State: None
City: None
Zip: None
Dob: None
Gender: female
Qualification: None
Experience: None
Marital_status: single
Children: None
Emergency_contact: None
Emergency_contact_name: None
Emergency_contact_relation: None
Is_active: True
Additional_info: None
Is_from_onboarding: False
Is_directly_converted: False
Employee_user_id: 35
```
- User: "I want to update the marital_status for employee 34 to married"

- Bot: "Successfully updated marital_status to married for employee 34! Do you want to make any further update?"

- User: “No I don't want to make any other update”

- Bot: “If you need anything else, let me know.”

- User: "Show details for employee 34" (validation)

- Bot:
```yaml
Here are the employee’s details:
Id: 34
Job_position_name: Social Media Coordinator
Job_position_id: 10
Employee_work_info_id: 33
Employee_bank_details_id: None
Badge_id: PEP37
Employee_first_name: Scarlett
Employee_last_name: Martinez
Employee_profile: None
Email: scarlett.martinez@horilla.com
Phone: 9876540037
Address: None
Country: None
State: None
City: None
Zip: None
Dob: None
Gender: female
Qualification: None
Experience: None
Marital_status: married
Children: None
Emergency_contact: None
Emergency_contact_name: None
Emergency_contact_relation: None
Is_active: True
Additional_info: None
Is_from_onboarding: False
Is_directly_converted: False
Employee_user_id: 35
```

- User: "Thanks you"

- Bot: "If you need anything else, let me know."


</details> <details> <summary>Example 3: Show Leave Types</summary>

- User: “hi”

- Bot: "Hi, I’m Rasa’s HR Assistant. What's your name?"

- User: "my name is Spyros"

- Bot: "Nice to meet you, Spyros! What can I do for you?"

- User: "What leave types can I request?"

- Bot: 

```yaml
Here are the available Leave Types:
Maternity Leave
  Duration: 90 days
  Pay Status: Fully paid
  Notes: Available for employees who have completed at least 6 months of service.

Sick Leave
  Duration: 10 days
  Pay Status: Paid
  Notes: Requires a medical note after 3 consecutive days.

Casual Leave
  Duration: 6 days
  Pay Status: Unpaid
  Notes: Can be used for personal emergencies or short vacations.
```


</details> <details> <summary>Examples 4: List Job positions</summary>

- User: "Hi!"

- Bot: "Hi, I’m Rasa’s HR Assistant. What's your name?"

- User: "My name is Spyros"

- Bot: Nice to meet you, Spyros! What can I do for you?

- User: "I'd like to see the company's job positions"

- Bot:
```yaml
Here are the job positions:
ID: 1, Position: Odoo Dev, Department ID: 1
ID: 2, Position: Django Dev, Department ID: 1
ID: 3, Position: Sales Man, Department ID: 2
ID: 4, Position: Training and Development Coordinator, Department ID: 3
ID: 5, Position: Compensation and Benefits Specialist, Department ID: 3
ID: 6, Position: Recruiter, Department ID: 3
ID: 7, Position: Marketing Specialist, Department ID: 4
ID: 8, Position: Digital Marketing Specialist, Department ID: 4
ID: 9, Position: Content Creator, Department ID: 4
ID: 10, Position: Social Media Coordinator, Department ID: 4
ID: 11, Position: Chief Financial Officer (CFO), Department ID: 5
ID: 12, Position: Financial Analyst, Department ID: 5
ID: 13, Position: Accounts Payable Clerk, Department ID: 5
ID: 14, Position: Tax Accountant, Department ID: 5
ID: 15, Position: System Admin, Department ID: 1
ID: 16, Position: React Dev, Department ID: 1
ID: 17, Position: Flutter Dev, Department ID: 1
ID: 18, Position: Sales Representative, Department ID: 2
ID: 19, Position: Sales Manage, Department ID: 2
```
- User: Thanks!

- Bot: If you need anything else, let me know.

- User: Bye

- Bot: Goodbye! Take care.

</details>

<details> <summary>Example 5: Policies & HR Support</summary>

- User: “Hi”

- Bot: “Hi, I’m Rasa’s HR Assistant. What's your name?”

- User: "I'm Oddo"

- Bot: "Nice to meet you, Odoo! What can I do for you?"

- User: “How do I get IT support?”

- Bot: “The IT Support Policy provides guidelines for receiving technical support. Employees must submit a support ticket through the IT service desk for technical issues. High-impact issues are prioritized, and hardware issues should be reported to IT.”

- User: “Tell me about the non-disclosure agreement.”

- Bot: “The Non-Disclosure Agreement (NDA) Policy protects confidential company information. Employees must not share proprietary, confidential, or trade secret information with external parties. Violating the NDA may lead to legal consequences and termination.”

- User: "Is there a number I can call to speak with Human Resources?"

- Bot: "You can contact HR at hr@company.com or call +1-234-567-890."

- User: "thanks!"

- Bot: “If you need anything else, let me know.”

- User: "bye"

- Bot: “Bye”

</details>

---

## Dialog Policy Experimentation (Bonus)

### a. Changes Made
- **TEDPolicy Adjustments:**  
  Increased `max_history` to 5 and raised the number of training `epochs` to 100 in the `config.yml` to better capture multi-turn conversation context.
- **RulePolicy Introduction:**  
  Added a `RulePolicy` to handle simple, rule-based responses (e.g., greetings, thanks, HR contact inquiries) for more predictable behavior.
- **NLU Training Data Refinement:**  
  Expanded and diversified training examples in `nlu.yml` to improve intent recognition and entity extraction accuracy.

### b. Reasons for Modifications
- **Enhanced Context Management:**  
  The adjustments to TEDPolicy parameters were aimed at allowing the model to consider more conversation history, thereby improving the handling of multi-turn dialogues.
- **Predictability and Consistency:**  
  Introducing a RulePolicy ensured that well-defined intents received consistent responses, reducing unexpected fallback occurrences.
- **Improved Accuracy in Intent Detection:**  
  Refining the NLU training data was crucial to reducing misclassifications, ensuring that the chatbot better understands user input variations.

### c. Observed Results and Insights
- **Improved Intent Recognition:**  
  The chatbot now demonstrates higher accuracy in understanding user inputs, leading to smoother interactions.
- **Reduced Fallbacks:**  
  The incorporation of rule-based policies has minimized fallback triggers, resulting in fewer interruptions during conversations.
- **Enhanced User Experience:**  
  Users experienced more natural and contextually aware interactions, with the system effectively prompting for missing information and maintaining coherent multi-turn dialogues.
- **Iterative Improvements:**  
  Continuous testing and user feedback have shown that these modifications significantly improved dialog flow. Further fine-tuning of policy parameters and training data is expected to yield even better performance.
---
## Conclusion & Future Improvements

The HR/Employee Assistant Chatbot successfully demonstrates how conversational AI can streamline HR operations by providing instant access to employee details, updating records, listing job positions, displaying leave types, and delivering company policy information—all integrated seamlessly with Horilla HRMS. Throughout the project, robust error handling, comprehensive NLU training, and effective dialog policies have been implemented to ensure a smooth and user-friendly experience.

### Key Achievements:
- **Seamless API Integration:**  
  Real-time retrieval and updating of employee data using Horilla's API.
- **Robust Error Handling:**  
  Clear error messages and fallback mechanisms ensure resilience during API failures or ambiguous user input.
- **Effective Dialog Management:**  
  The combination of TEDPolicy, RulePolicy, and enriched NLU training data has improved multi-turn conversation handling and overall intent recognition.
- **User-Centric Design:**  
  The chatbot provides structured interactions that guide users through each HR task efficiently.

### Future Improvements:
- **Enhanced Security:**  
  Implement secure storage and dynamic retrieval of API tokens (e.g., via environment variables or a secrets manager) to further protect sensitive data.
- **Expanded Functionalities:**  
  - Integrate additional HR tasks such as payroll inquiries, performance reviews, and onboarding processes.
  - Implement real-time updates for leave types by integrating with live data sources rather than relying on mocked data.
- **Improved Dialog Policies:**  
  - Experiment with further fine-tuning of TEDPolicy and RulePolicy parameters.
  - Explore additional fallback strategies and context retention techniques to further enhance user interactions.
- **User Feedback Integration:**  
  - Develop mechanisms for gathering and analyzing user feedback to continually refine the chatbot’s performance.
  - Implement iterative improvements based on observed user behavior and satisfaction levels.
- **Multilingual Support:**  
  Extend the chatbot's capabilities to support multiple languages, catering to a global workforce.

Overall, the project lays a strong foundation for a comprehensive HR assistant solution, and ongoing improvements will help ensure it meets the evolving needs of modern HR environments.

---
## Thank you for using the HR/Employee Assistant Chatbot!!!

We appreciate you taking the time to explore our project. If you have any questions, feedback, or suggestions, please feel free to open an issue or contribute to our repository. Your insights help us improve and better serve your HR needs.

**Happy chatting and streamlining HR processes!**

**Contributors:**  
- [Spyros Mavromatis](https://github.com/spymavro) (7115182300020) (spyros.mauromatis@gmail.com)
- [Eirini-Garyfalia Kyriakou](https://github.com/eirkyr) (7115182300016) (irinikiriakou8@gmail.com)
