"""
ADK (Agent Development Kit) Base Agent Implementation
Enterprise-grade agent framework for Financial MAS
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional
import asyncio
import json
import uuid
import time
from datetime import datetime

class ADKAgent(ABC):
    """
    Base ADK Agent class that provides enterprise-grade agent capabilities
    All Financial MAS agents inherit from this ADK foundation
    """
    
    def __init__(self, name: str, description: str, capabilities: List[str], version: str = "1.0"):
        self.name = name
        self.description = description
        self.capabilities = capabilities
        self.version = version
        self.adk_version = "1.0"
        self.state = "idle"
        self.memory = {}
        self.execution_history = []
        self.agent_id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.last_activity = None
        
    @abstractmethod
    async def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        ADK-compliant task processing method
        Must be implemented by all ADK agents
        """
        pass
    
    async def execute(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        ADK execution framework with enterprise features
        """
        execution_id = str(uuid.uuid4())
        start_time = time.time()
        
        # Update ADK state
        self.state = "processing"
        self.last_activity = datetime.now().isoformat()
        
        try:
            # Log execution start
            self._log_execution(execution_id, "started", payload)
            
            # Process task using ADK framework
            result = await self.process_task(payload)
            
            # Add ADK metadata to result
            adk_result = {
                **result,
                "adk_metadata": {
                    "agent_id": self.agent_id,
                    "agent_name": self.name,
                    "execution_id": execution_id,
                    "adk_version": self.adk_version,
                    "capabilities_used": self.capabilities,
                    "execution_time": time.time() - start_time,
                    "state": "completed",
                    "timestamp": datetime.now().isoformat()
                }
            }
            
            # Update state and log
            self.state = "completed"
            self._log_execution(execution_id, "completed", adk_result)
            
            return adk_result
            
        except Exception as e:
            # ADK error handling
            self.state = "error"
            error_result = {
                "error": str(e),
                "agent": self.name,
                "adk_metadata": {
                    "agent_id": self.agent_id,
                    "execution_id": execution_id,
                    "adk_version": self.adk_version,
                    "state": "error",
                    "execution_time": time.time() - start_time,
                    "timestamp": datetime.now().isoformat()
                }
            }
            
            self._log_execution(execution_id, "error", error_result)
            return error_result
    
    def get_capabilities(self) -> List[str]:
        """Return ADK agent capabilities"""
        return self.capabilities
    
    def get_state(self) -> str:
        """Return current ADK agent state"""
        return self.state
    
    def get_adk_info(self) -> Dict[str, Any]:
        """Return comprehensive ADK agent information"""
        return {
            "agent_id": self.agent_id,
            "name": self.name,
            "description": self.description,
            "capabilities": self.capabilities,
            "version": self.version,
            "adk_version": self.adk_version,
            "state": self.state,
            "created_at": self.created_at,
            "last_activity": self.last_activity,
            "execution_count": len(self.execution_history),
            "memory_size": len(self.memory)
        }
    
    def _log_execution(self, execution_id: str, status: str, data: Dict[str, Any]):
        """Log ADK execution for monitoring and debugging"""
        log_entry = {
            "execution_id": execution_id,
            "status": status,
            "timestamp": datetime.now().isoformat(),
            "data_size": len(str(data))
        }
        self.execution_history.append(log_entry)
        
        # Keep only last 100 executions
        if len(self.execution_history) > 100:
            self.execution_history = self.execution_history[-100:]
    
    def update_memory(self, key: str, value: Any):
        """Update ADK agent memory"""
        self.memory[key] = {
            "value": value,
            "timestamp": datetime.now().isoformat()
        }
    
    def get_memory(self, key: str) -> Optional[Any]:
        """Retrieve from ADK agent memory"""
        if key in self.memory:
            return self.memory[key]["value"]
        return None 