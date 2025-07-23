from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

# Get the API key from the environment variable
api_key = os.getenv("API_KEY")
domain = os.getenv("DOMAIN")

"""
Function to get all open tickets assigned to the current agent
"""
def get_tickets():

  r = requests.get("https://"+ domain +".freshdesk.com/api/v2/tickets?filter=new_and_my_open", auth = (api_key, 'X'))

  if r.status_code == 200:
    print("Request processed successfully, the response is given below")

    # format the response to json
    response = json.loads(r.content)
    
    # First get the current agent info to get their ID
    agent_info = requests.get("https://"+ domain +".freshdesk.com/api/v2/agents/me", auth = (api_key, 'X'))
    current_agent_id = None
    if agent_info.status_code == 200:
      current_agent = json.loads(agent_info.content)
      current_agent_id = current_agent.get('id')
      print(f"Current agent: {current_agent.get('name')} (ID: {current_agent_id})")
    
    # Filter for tickets assigned to current agent and open status
    if current_agent_id:
      assigned_open_tickets = [ticket for ticket in response if ticket.get('status') == 2 and ticket.get('agent_id') == current_agent_id]
    else:
      # Fallback: just filter for open tickets
      assigned_open_tickets = [ticket for ticket in response if ticket.get('status') == 2]
    
    print(f"Found {len(assigned_open_tickets)} open tickets assigned to current agent out of {len(response)} total tickets:")
    print(json.dumps(assigned_open_tickets, indent=4))

  else:
    print(f"Failed to read tickets, status code: {r.status_code}")
    print("Response content:")
    print(r.content)