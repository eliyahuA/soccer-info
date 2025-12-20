"""Client module for Soccer Football Info API."""
from soccer_info.client.sync.httpclient import HTTPClient
from soccer_info.client.async_.async_httpclient import AsyncHTTPClient
from soccer_info.client.sync.client import Client
from soccer_info.client.async_.async_client import AsyncClient

__all__ = ['HTTPClient', 'AsyncHTTPClient', 'Client', 'AsyncClient']
