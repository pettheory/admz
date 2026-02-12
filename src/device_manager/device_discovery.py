"""
Device Discovery Module

Implements intelligent device discovery using VAPIX APIs and 
self-documenting features for comprehensive capability detection.
"""

import asyncio
import aiohttp
import requests
from typing import Dict, List, Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class DeviceInfo:
    """Device information and capabilities"""
    ip_address: str
    model: str
    firmware_version: str
    hardware_id: str
    capabilities: Dict[str, any]
    last_updated: str

class DeviceDiscovery:
    """
    Intelligent device discovery using VAPIX APIs and 
    self-documenting features.
    """
    
    def __init__(self, credentials_manager):
        self.credentials_manager = credentials_manager
        self.discovered_devices = {}
        
    async def discover_device(self, ip_address: str) -> Optional[DeviceInfo]:
        """
        Discover device capabilities and information.
        
        Args:
            ip_address: Device IP address
            
        Returns:
            DeviceInfo object or None if discovery fails
        """
        try:
            # Get credentials for device
            credentials = self.credentials_manager.get_credentials(ip_address)
            
            # Basic device info
            device_info = await self._get_basic_device_info(ip_address, credentials)
            
            # Capability discovery
            capabilities = await self._discover_capabilities(ip_address, credentials)
            
            # Create DeviceInfo object
            return DeviceInfo(
                ip_address=ip_address,
                model=device_info.get('model', 'Unknown'),
                firmware_version=device_info.get('firmware_version', 'Unknown'),
                hardware_id=device_info.get('hardware_id', 'Unknown'),
                capabilities=capabilities,
                last_updated=datetime.now().isoformat()
            )
            
        except Exception as e:
            print(f"Device discovery failed for {ip_address}: {e}")
            return None
    
    async def _get_basic_device_info(self, ip_address: str, credentials: Dict) -> Dict:
        """Get basic device information using device info CGI"""
        try:
            # Try device info CGI first
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"http://{ip_address}/axis-cgi/basicdeviceinfo.cgi",
                    auth=aiohttp.BasicAuth(credentials['username'], credentials['password']),
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        # Fallback to parameter CGI
                        return await self._get_device_info_fallback(ip_address, credentials)
                        
        except Exception as e:
            print(f"Failed to get device info for {ip_address}: {e}")
            return {}
    
    async def _discover_capabilities(self, ip_address: str, credentials: Dict) -> Dict:
        """Discover device capabilities using multiple methods"""
        capabilities = {}
        
        # Method 1: Swagger API (newer devices)
        swagger_caps = await self._discover_via_swagger(ip_address, credentials)
        capabilities.update(swagger_caps)
        
        # Method 2: Parameter CGI (all devices)
        param_caps = await self._discover_via_parameters(ip_address, credentials)
        capabilities.update(param_caps)
        
        # Method 3: Feature probing (experimental)
        probe_caps = await self._discover_via_probing(ip_address, credentials)
        capabilities.update(probe_caps)
        
        return capabilities
    
    async def _discover_via_swagger(self, ip_address: str, credentials: Dict) -> Dict:
        """Discover capabilities via Swagger API (newer devices)"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    f"http://{ip_address}/axis-cgi/openapi.json",
                    auth=aiohttp.BasicAuth(credentials['username'], credentials['password']),
                    timeout=aiohttp.ClientTimeout(total=10)
                ) as response:
                    if response.status == 200:
                        openapi_spec = await response.json()
                        return self._parse_swagger_capabilities(openapi_spec)
                    else:
                        return {}
                        
        except Exception:
            return {}
    
    def _parse_swagger_capabilities(self, openapi_spec: Dict) -> Dict:
        """Parse Swagger/OpenAPI specification for capabilities"""
        capabilities = {}
        
        # Extract available endpoints
        if 'paths' in openapi_spec:
            for path, methods in openapi_spec['paths'].items():
                if 'analytics' in path:
                    capabilities['analytics_api'] = True
                if 'motion' in path:
                    capabilities['motion_detection'] = True
                if 'audio' in path:
                    capabilities['audio_api'] = True
                    
        # Extract available components
        if 'components' in openapi_spec and 'schemas' in openapi_spec['components']:
            for schema_name, schema in openapi_spec['components']['schemas'].items():
                if 'analytics' in schema_name.lower():
                    capabilities['analytics_schemas'] = True
                    
        return capabilities
    
    async def _get_device_info_fallback(self, ip_address: str, credentials: Dict) -> Dict:
        """Fallback method to get device info via parameter CGI"""
        # TODO: Implement parameter CGI fallback
        return {}
    
    async def _discover_via_parameters(self, ip_address: str, credentials: Dict) -> Dict:
        """Discover capabilities via parameter CGI"""
        # TODO: Implement parameter-based discovery
        return {}
    
    async def _discover_via_probing(self, ip_address: str, credentials: Dict) -> Dict:
        """Discover capabilities via feature probing"""
        # TODO: Implement feature probing
        return {}
