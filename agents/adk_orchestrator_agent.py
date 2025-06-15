"""
ADK-Powered Orchestrator Agent
Enterprise-grade financial analysis coordination using ADK framework
"""
from .adk_base_agent import ADKAgent
import requests
import json
import asyncio
from typing import Dict, Any

class ADKOrchestratorAgent(ADKAgent):
    def __init__(self):
        super().__init__(
            name="adk_orchestrator_agent", 
            description="ADK-powered financial analysis orchestrator with enterprise workflow management",
            capabilities=[
                "multi_agent_coordination",
                "financial_analysis_workflow", 
                "data_aggregation",
                "report_synthesis",
                "adk_workflow_management",
                "enterprise_orchestration"
            ],
            version="2.0"
        )
        self.agent_endpoints = {
            'data_gathering': 'http://localhost:9001/',
            'quantitative_analysis': 'http://localhost:9002/', 
            'qualitative_analysis': 'http://localhost:9003/',
            'report_generation': 'http://localhost:9004/'
        }
    
    async def process_task(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """ADK-compliant financial analysis orchestration"""
        # Handle both string and dict payloads
        if isinstance(payload, str):
            query = payload
        else:
            query = payload.get('query', payload.get('message', str(payload)))
        
        # Store query in ADK memory
        self.update_memory("current_query", query)
        self.update_memory("workflow_start", True)
        
        # ADK workflow orchestration with enterprise features
        workflow_steps = [
            ("data_gathering", {
                "query": query, 
                "task": "adk_gather_financial_data",
                "adk_context": "financial_analysis_workflow"
            }),
            ("quantitative_analysis", {
                "query": query, 
                "task": "adk_quantitative_analysis",
                "adk_context": "financial_analysis_workflow"
            }), 
            ("qualitative_analysis", {
                "query": query, 
                "task": "adk_qualitative_analysis",
                "adk_context": "financial_analysis_workflow"
            }),
            ("report_generation", {
                "query": query, 
                "task": "adk_generate_report",
                "adk_context": "financial_analysis_workflow"
            })
        ]
        
        results = {}
        workflow_metadata = {
            "total_steps": len(workflow_steps),
            "completed_steps": 0,
            "failed_steps": 0,
            "adk_orchestration": True
        }
        
        for step_name, step_payload in workflow_steps:
            print(f"🤖 ADK Step {len(results)+1}: {step_name} for query: {query}")
            
            try:
                # ADK agent-to-agent communication
                result = await self._call_adk_agent(step_name, step_payload)
                results[step_name] = result
                workflow_metadata["completed_steps"] += 1
                
                # Update ADK memory with step results
                self.update_memory(f"step_{step_name}", result)
                
            except Exception as e:
                workflow_metadata["failed_steps"] += 1
                return {
                    "agent": self.name,
                    "error": f"ADK workflow failed at {step_name}: {str(e)}",
                    "completed_steps": list(results.keys()),
                    "workflow_metadata": workflow_metadata,
                    "adk_orchestration": True
                }
        
        # ADK final report synthesis
        final_report = await self._synthesize_adk_results(results, query)
        
        # Update ADK memory
        self.update_memory("workflow_complete", True)
        self.update_memory("final_report", final_report)
        
        return {
            "agent": self.name,
            "task": "adk_financial_analysis_orchestration",
            "query": query,
            "workflow_results": results,
            "final_report": final_report,
            "workflow_metadata": workflow_metadata,
            "adk_capabilities_used": self.capabilities,
            "adk_orchestration": True,
            "enterprise_features": {
                "workflow_tracking": True,
                "error_handling": True,
                "memory_management": True,
                "agent_coordination": True
            }
        }
    
    async def _call_adk_agent(self, agent_name: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        """ADK-compliant agent communication with enterprise features"""
        endpoint = self.agent_endpoints.get(agent_name)
        if not endpoint:
            raise ValueError(f"ADK agent {agent_name} not found in registry")
        
        # ADK message format with enterprise metadata
        adk_message = {
            "message": {
                "role": "user", 
                "parts": [{"text": json.dumps(payload)}]
            },
            "adk_metadata": {
                "sender": self.name,
                "sender_id": self.agent_id,
                "capabilities_required": ["financial_analysis"],
                "priority": "high",
                "workflow_context": "financial_analysis",
                "adk_version": self.adk_version,
                "enterprise_mode": True
            }
        }
        
        # Make ADK agent call with timeout and retry logic
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.post(endpoint, json=adk_message, timeout=30)
                response.raise_for_status()
                return response.json()
            except Exception as e:
                if attempt == max_retries - 1:
                    raise e
                await asyncio.sleep(1)  # Brief retry delay
    
    async def _synthesize_adk_results(self, results: Dict[str, Any], query: str) -> Dict[str, Any]:
        """ADK-powered result synthesis with enterprise intelligence"""
        
        # Extract data from ADK agent responses
        report_data = results.get('report_generation', {})
        if isinstance(report_data, dict) and 'messages' in report_data and len(report_data['messages']) > 1:
            agent_response = report_data['messages'][-1]
            if isinstance(agent_response, dict) and 'parts' in agent_response and agent_response['parts']:
                try:
                    parsed_report = json.loads(agent_response['parts'][0]['text'])
                    
                    # Enhance with ADK enterprise features
                    enhanced_report = {
                        "adk_synthesis": True,
                        "enterprise_grade": True,
                        "executive_summary": parsed_report.get('executive_summary', 'ADK analysis completed'),
                        "investment_recommendation": parsed_report.get('investment_recommendation', 'See detailed analysis'),
                        "financial_highlights": parsed_report.get('financial_highlights', {}),
                        "key_findings": parsed_report.get('key_findings', []),
                        "confidence_level": parsed_report.get('confidence_level', 'Medium'),
                        "adk_workflow_steps": list(results.keys()),
                        "query_processed": query,
                        "adk_orchestrator": self.name,
                        "synthesis_metadata": {
                            "agents_coordinated": len(results),
                            "data_sources_integrated": 4,
                            "adk_version": self.adk_version,
                            "enterprise_features": True
                        }
                    }
                    
                    return enhanced_report
                    
                except json.JSONDecodeError:
                    pass
        
        # ADK fallback synthesis
        return {
            "adk_synthesis": True,
            "enterprise_grade": True,
            "summary": f"ADK enterprise workflow completed for: {query}",
            "recommendation": "Analysis completed using ADK framework with enterprise features",
            "adk_agents_coordinated": list(results.keys()),
            "raw_results": results,
            "orchestrator_metadata": {
                "adk_version": self.adk_version,
                "enterprise_mode": True,
                "workflow_success": True
            }
        } 