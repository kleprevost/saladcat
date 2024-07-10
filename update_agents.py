import requests
import json
import time

# Configuration
HASHTOPOLIS_URL = 'http://hashtopolisip:myport/api/user.php'
API_KEY = 'hashtopoliskey'
TASK_ID = ''  # Replace with the actual task ID you want to assign agents to
UPDATE_INTERVAL = 5  # Time interval in seconds between updates

# Headers for the API request
headers = {
    'Content-Type': 'application/json'
}

# Test function to check API connection
def test_connection():
    payload = {
        "section": "test",
        "request": "connection"
    }
    response = requests.post(
        HASHTOPOLIS_URL,
        headers=headers,
        data=json.dumps(payload)
    )
    print(response.text)
    return response.json()

# Function to get all agents
def get_all_agents():
    payload = {
        'section': 'agent',
        'request': 'listAgents',
        'accessKey': API_KEY
    }
    response = requests.post(
        HASHTOPOLIS_URL,
        headers=headers,
        data=json.dumps(payload)
    )
    print("Get All Agents Response:", response.text)
    return response.json()

# Function to get details of an agent
def get_agent_details(agent_id):
    payload = {
        'section': 'agent',
        'request': 'get',
        'agentId': agent_id,
        'accessKey': API_KEY
    }
    response = requests.post(
        HASHTOPOLIS_URL,
        headers=headers,
        data=json.dumps(payload)
    )
    print(f"Get Agent {agent_id} Details Response:", response.text)
    return response.json()

# Function to mark agent as trusted
def mark_agent_as_trusted(agent_id):
    payload = {
        'section': 'agent',
        'request': 'setTrusted',
        'agentId': agent_id,
        'trusted': True,
        'accessKey': API_KEY
    }
    response = requests.post(
        HASHTOPOLIS_URL,
        headers=headers,
        data=json.dumps(payload)
    )
    print("Mark Agent as Trusted Response:", response.text)
    return response.json()

# Function to set error handling for agent
def set_error_handling(agent_id):
    payload = {
        'section': 'agent',
        'request': 'setErrorFlag',
        'agentId': agent_id,
        'ignoreErrors': 1,
        'accessKey': API_KEY
    }
    response = requests.post(
        HASHTOPOLIS_URL,
        headers=headers,
        data=json.dumps(payload)
    )
    print("Set Error Handling Response:", response.text)
    return response.json()

# Function to assign agent to a task
def assign_agent_to_task(agent_id, task_id):
    payload = {
        'section': 'task',
        'request': 'taskAssignAgent',
        'agentId': agent_id,
        'taskId': task_id,
        'accessKey': API_KEY
    }
    response = requests.post(
        HASHTOPOLIS_URL,
        headers=headers,
        data=json.dumps(payload)
    )
    print(f"Assign Agent {agent_id} to Task {task_id} Response:", response.text)
    return response.json()

# Function to update agents
def update_agents():
    # Get all agents
    agents = get_all_agents()
    
    # Check if the response is valid
    if agents.get('response') != 'OK':
        print(f"Error retrieving agents: {agents.get('message')}")
        return
    
    # Iterate through agents and perform required operations
    for agent in agents.get('agents', []):
        agent_details = get_agent_details(agent['agentId'])
        if agent_details.get('response') == 'OK':
            # Mark agent as trusted if not already trusted
            if not agent_details.get('isTrusted', False):
                print(f"Marking agent {agent['name']} (ID: {agent['agentId']}) as trusted.")
                response = mark_agent_as_trusted(agent['agentId'])
                if response.get('response') == 'OK':
                    print(f"Agent {agent['name']} successfully marked as trusted.")
                else:
                    print(f"Failed to mark agent {agent['name']} as trusted: {response.get('message')}")
            
            # Set error handling for the agent
            print(f"Setting error handling for agent {agent['name']} (ID: {agent['agentId']}).")
            response = set_error_handling(agent['agentId'])
            if response.get('response') == 'OK':
                print(f"Error handling for agent {agent['name']} successfully set.")
            else:
                print(f"Failed to set error handling for agent {agent['name']}: {response.get('message')}")
            
            # Assign agent to a specific task
            print(f"Assigning agent {agent['name']} (ID: {agent['agentId']}) to task {TASK_ID}.")
            response = assign_agent_to_task(agent['agentId'], TASK_ID)
            if response.get('response') == 'OK':
                print(f"Agent {agent['name']} successfully assigned to task {TASK_ID}.")
            else:
                print(f"Failed to assign agent {agent['name']} to task {TASK_ID}: {response.get('message')}")

# Main function
def main():
    # Test API connection
    test_response = test_connection()
    if test_response.get('response') != 'SUCCESS':
        print(f"Error connecting to API: {test_response.get('message')}")
        return
    
    # Continuously update agents every 5 seconds
    while True:
        update_agents()
        time.sleep(UPDATE_INTERVAL)

if __name__ == "__main__":
    main()
