import streamlit as st
import json
from utils.a2a_client import A2AClient

st.set_page_config(page_title="MAS Control Room", layout="wide")

st.title("Financial Research Multi-Agent System 🤖")
st.caption("Powered by A2A Multi-Agent Communication")

# --- A2A Client Setup ---
ORCHESTRATOR_URL = "http://localhost:9000/"
try:
    a2a_client = A2AClient(remote_agent_url=ORCHESTRATOR_URL)
except Exception as e:
    st.error(f"Failed to initialize A2A client. Is the Orchestrator server running? Error: {e}")
    st.stop()

# --- Session State ---
if "messages" not in st.session_state:
    st.session_state.messages = []
if "activity_log" not in st.session_state:
    st.session_state.activity_log = ["Awaiting query..."]

# --- UI Layout ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Chat")
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            if message["role"] == "assistant" and isinstance(message["content"], dict):
                st.json(message["content"])
            else:
                st.markdown(message["content"])

    if prompt := st.chat_input("e.g., Analyze NVIDIA's stock performance and recent news"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("The agent team is working..."):
                st.session_state.activity_log = ["▶️ User query sent to Orchestrator Agent."]
                
                # Update activity log
                st.session_state.activity_log.append("✅ Orchestrator received task and is planning.")
                st.session_state.activity_log.append("➡️ Delegating tasks to specialist agents...")
                
                # Send task to orchestrator
                final_task = a2a_client.send_task({"query": prompt})

                if final_task and final_task.get("state") == "COMPLETED":
                    response_json_str = final_task["messages"][-1]["parts"][0]["text"]
                    st.session_state.activity_log.append("✅ Final report received. Task complete.")
                    try:
                        # Pretty print the final JSON output from the orchestrator
                        final_report_obj = json.loads(response_json_str)
                        st.json(final_report_obj)
                        st.session_state.messages.append({"role": "assistant", "content": final_report_obj})
                    except json.JSONDecodeError:
                        st.markdown(response_json_str) # Fallback for non-json text
                        st.session_state.messages.append({"role": "assistant", "content": response_json_str})
                else:
                    error_message = f"Task failed. Last known state: {final_task.get('state', 'Unknown') if final_task else 'No response'}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})
                    st.session_state.activity_log.append(f"❌ {error_message}")
                st.rerun()

with col2:
    st.subheader("Agent Activity Log")
    log_placeholder = st.empty()
    log_content = "\n".join(st.session_state.activity_log)
    log_placeholder.text_area("Log", log_content, height=500, disabled=True)

# --- Sidebar with System Status ---
with st.sidebar:
    st.header("System Status")
    
    # Check if agents are running
    agent_status = {
        "Orchestrator (9000)": "http://localhost:9000/",
        "Data Gathering (9001)": "http://localhost:9001/",
        "Quantitative (9002)": "http://localhost:9002/",
        "Qualitative (9003)": "http://localhost:9003/",
        "Report Generation (9004)": "http://localhost:9004/",
    }
    
    for agent_name, url in agent_status.items():
        try:
            import requests
            response = requests.get(f"{url}.well-known/agent.json", timeout=2)
            if response.status_code == 200:
                st.success(f"✅ {agent_name}")
            else:
                st.error(f"❌ {agent_name}")
        except:
            st.error(f"❌ {agent_name}")
    
    st.header("Quick Actions")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.session_state.activity_log = ["Awaiting query..."]
        st.rerun()
    
    st.header("Example Queries")
    st.markdown("""
    - Analyze NVIDIA's stock performance
    - Compare AMD vs Intel financials
    - Research Tesla's latest earnings
    - What factors affect semiconductor stocks?
    - Analyze Apple's market position
    """)

# --- Footer ---
st.markdown("---")
st.markdown("**Instructions:** Start all agent servers first, then run this Streamlit app. Enter a financial research query above to begin!") 