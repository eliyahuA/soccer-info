"""Client module for Soccer Football Info API."""
from .httpclient import SyncHTTPClient, AsyncHTTPClient
from .base_client import SyncClient, AsyncClient

__all__ = ['SyncHTTPClient', 'AsyncHTTPClient', 'SyncClient', 'AsyncClient']
