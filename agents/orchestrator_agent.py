from utils.a2a_client import A2AClient
import json

AGENT_ADDRESSES = {
    "data_gathering_agent": "http://localhost:9001/",
    "quantitative_analysis_agent": "http://localhost:9002/",
    "qualitative_analysis_agent": "http://localhost:9003/",
    "report_generation_agent": "http://localhost:9004/",
}

class OrchestratorAgent:
    def __init__(self):
        self.name = "orchestrator_agent"
        self.description = "Project Manager for the financial research team"
    
    async def execute(self, payload):
        """Orchestrate the multi-agent workflow"""
        query = payload.get('query', '')
        
        # Step 1: Data Gathering
        print(f"Step 1: Gathering data for query: {query}")
        data_client = A2AClient(AGENT_ADDRESSES["data_gathering_agent"])
        data_task = data_client.send_task({"query": query})
        data_result = self.extract_result(data_task)
        
        # Step 2: Quantitative Analysis
        print("Step 2: Performing quantitative analysis")
        quant_client = A2AClient(AGENT_ADDRESSES["quantitative_analysis_agent"])
        quant_task = quant_client.send_task({"query": query, "data": data_result})
        quant_result = self.extract_result(quant_task)
        
        # Step 3: Qualitative Analysis
        print("Step 3: Performing qualitative analysis")
        qual_client = A2AClient(AGENT_ADDRESSES["qualitative_analysis_agent"])
        qual_task = qual_client.send_task({"query": query, "data": data_result})
        qual_result = self.extract_result(qual_task)
        
        # Step 4: Report Generation
        print("Step 4: Generating final report")
        report_client = A2AClient(AGENT_ADDRESSES["report_generation_agent"])
        report_task = report_client.send_task({
            "query": query,
            "data_analysis": data_result,
            "quantitative_analysis": quant_result,
            "qualitative_analysis": qual_result
        })
        final_report = self.extract_result(report_task)
        
        return {
            "orchestrator": self.name,
            "workflow_completed": True,
            "query": query,
            "final_report": final_report,
            "workflow_steps": [
                {"step": 1, "agent": "data_gathering_agent", "status": "completed"},
                {"step": 2, "agent": "quantitative_analysis_agent", "status": "completed"},
                {"step": 3, "agent": "qualitative_analysis_agent", "status": "completed"},
                {"step": 4, "agent": "report_generation_agent", "status": "completed"}
            ]
        }
    
    def extract_result(self, task):
        """Extract result from task response"""
        if task and task.get("state") == "COMPLETED":
            try:
                result_text = task["messages"][-1]["parts"][0]["text"]
                return json.loads(result_text)
            except:
                return {"error": "Failed to parse result"}
        return {"error": "Task failed or incomplete"}

# Create instance
orchestrator_agent = OrchestratorAgent() 