# See this guide on how to implement custom actions:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import logging


class ActionFetchEmployeeDetails(Action):
    def name(self) -> Text:
        return "action_fetch_employee_details"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        employee_id = tracker.get_slot("employee_id")
        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMjg1Mzg3LCJpYXQiOjE3Mzk2OTMzODcsImp0aSI6ImM1NmRlZDQ2ZGQ5ZDRhZmZhYTY5OWQzNDU0MTVkZWE5IiwidXNlcl9pZCI6MTI5fQ.omyw0eQdVJWWKt_3anycJf4vz8ezZqwj_RoUsJfg3rk"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        # The employee details endpoint
        url = f"http://127.0.0.1:8000/api/employee/employees/{employee_id}/"
        # Make the GET request
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            details = response.json()

            # Build a friendly multi-line string:
            lines = []
            for key, val in details.items():
                # Capitalize key or re-label as desired
                lines.append(f"{key.capitalize()}: {val}")
            # Join lines with newlines:
            formatted_details = "\n".join(lines)

            dispatcher.utter_message(text=f"Here are the employee’s details:\n\n{formatted_details}")
        else:
            dispatcher.utter_message(
                text=f"Failed to fetch employee details. "
                     f"Status code: {response.status_code}. "
                     f"Response: {response.text}"
            )

        return []


class ActionUpdateEmployeeDetails(Action):
    def name(self) -> Text:
        return "action_update_employee_details"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        employee_id = tracker.get_slot("employee_id")
        field_name = tracker.get_slot("field_name")
        field_value = tracker.get_slot("field_value")

        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMjg1Mzg3LCJpYXQiOjE3Mzk2OTMzODcsImp0aSI6ImM1NmRlZDQ2ZGQ5ZDRhZmZhYTY5OWQzNDU0MTVkZWE5IiwidXNlcl9pZCI6MTI5fQ.omyw0eQdVJWWKt_3anycJf4vz8ezZqwj_RoUsJfg3rk"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        updates = {}
        if field_name and field_value:
            updates[field_name] = field_value

        # The employee details endpoint
        url = f"http://127.0.0.1:8000/api/employee/employees/{employee_id}/"
        # Make the PUT request
        response = requests.put(url, json=updates, headers=headers)

        if response.status_code == 200:
            dispatcher.utter_message(
                text=f"Successfully updated {field_name} to {field_value} for employee {employee_id}!"
            )
            dispatcher.utter_message(text="Do you want to make any further update?")
        else:
            dispatcher.utter_message(
                text=f"Failed to update details. "
                     f"Status code: {response.status_code}. Response: {response.text}"
            )

        return []


class ActionListJobPositions(Action):
    def name(self) -> Text:
        return "action_list_job_positions"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMjg1Mzg3LCJpYXQiOjE3Mzk2OTMzODcsImp0aSI6ImM1NmRlZDQ2ZGQ5ZDRhZmZhYTY5OWQzNDU0MTVkZWE5IiwidXNlcl9pZCI6MTI5fQ.omyw0eQdVJWWKt_3anycJf4vz8ezZqwj_RoUsJfg3rk"

        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        # The job position list endpoint
        url = "http://127.0.0.1:8000/api/base/job-positions/"

        # Make the GET request
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Parse the JSON.
            data = response.json()

            # If there's a "results" array, we use that, otherwise we use the entire data
            if isinstance(data, dict) and "results" in data:
                positions = data["results"]
            else:
                positions = data  # If Horilla returns a list directly

            # 5) Build a user-friendly message.
            if not positions:
                dispatcher.utter_message(text="No job positions found.")
            else:
                lines = []
                for pos in positions:
                    pos_id = pos.get("id")
                    pos_name = pos.get("job_position")
                    dep_id = pos.get("department_id")
                    lines.append(
                        f"ID: {pos_id}, Position: {pos_name}, Department ID: {dep_id}"
                    )

                msg = "\n".join(lines)
                dispatcher.utter_message(
                    text=f"Here are the job positions:\n\n{msg}"
                )
        else:
            dispatcher.utter_message(
                text=f"Failed to list job positions. "
                     f"Status code: {response.status_code}. "
                     f"Response: {response.text}"
            )

        return []


class ActionShowLeaveTypes(Action):
    def name(self) -> Text:
        return "action_show_leave_types"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:

        # Mock list of leave types and their info
        leave_types_info = {
            "Maternity Leave": {
                "duration": "90 days",
                "pay_status": "Fully paid",
                "notes": "Available for employees who have completed at least 6 months of service."
            },
            "Sick Leave": {
                "duration": "10 days",
                "pay_status": "Paid",
                "notes": "Requires a medical note after 3 consecutive days."
            },
            "Casual Leave": {
                "duration": "6 days",
                "pay_status": "Unpaid",
                "notes": "Can be used for personal emergencies or short vacations."
            }
        }

        # Build a user-friendly reply
        response_lines = ["Here are the available Leave Types:\n"]
        for leave_name, details in leave_types_info.items():
            line = (
                f"{leave_name}\n"
                f"  Duration: {details['duration']}\n"
                f"  Pay Status: {details['pay_status']}\n"
                f"  Notes: {details['notes']}\n"
            )
            response_lines.append(line)

        # Join them into one string
        response_text = "\n".join(response_lines)

        dispatcher.utter_message(text=response_text)
        return []

