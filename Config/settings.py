# config/settings.py

import os
import json

class Settings:
    def __init__(self):
        # Default configuration settings
        self.project_name = "InsightOps"  # Project name
        self.version = "1.0"  # Version of the project
        self.debug_mode = True  # Set to False in production environment

        # Network configuration
        self.network_timeout = 30  # Timeout for network requests in seconds
        self.max_retries = 5  # Max retries for failed network requests
        self.server_host = "localhost"  # Server host
        self.server_port = 8080  # Server port
        self.use_ssl = False  # Whether to use SSL/TLS for communication

        # Logging configuration
        self.log_level = "DEBUG"  # Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        self.log_file_path = "logs/insightops.log"  # Log file location

        # Security configuration
        self.encryption_key = os.getenv("ENCRYPTION_KEY", "default_encryption_key")  # Encryption key for securing data
        self.auth_token = os.getenv("AUTH_TOKEN", "default_auth_token")  # Authentication token for API access

        # AI model settings
        self.ai_model_path = "ai/models"  # Path to store or load AI models
        self.ai_model_name = "system_analysis_model"  # Default AI model for system analysis

        # Health check configuration
        self.health_check_interval = 60  # Interval (in seconds) for health checks
        self.max_health_check_attempts = 3  # Max attempts for health checks before alert

        # IoT device settings
        self.iot_device_list = []  # List of IoT devices to interact with

        # Time settings
        self.timezone = "UTC"  # Default timezone for the system

    def load(self, config_file='config/config.json'):
        """
        Method to load configuration settings from a JSON file.
        If the file doesn't exist, it will fall back to default settings.
        """
        if os.path.exists(config_file):
            print(f"Loading settings from {config_file}...")
            with open(config_file, 'r') as file:
                try:
                    config_data = json.load(file)

                    # Load settings from the JSON file if they exist, else keep default values
                    self.project_name = config_data.get('project_name', self.project_name)
                    self.version = config_data.get('version', self.version)
                    self.debug_mode = config_data.get('debug_mode', self.debug_mode)

                    # Network settings
                    self.network_timeout = config_data.get('network_timeout', self.network_timeout)
                    self.max_retries = config_data.get('max_retries', self.max_retries)
                    self.server_host = config_data.get('server_host', self.server_host)
                    self.server_port = config_data.get('server_port', self.server_port)
                    self.use_ssl = config_data.get('use_ssl', self.use_ssl)

                    # Logging settings
                    self.log_level = config_data.get('log_level', self.log_level)
                    self.log_file_path = config_data.get('log_file_path', self.log_file_path)

                    # Security settings
                    self.encryption_key = config_data.get('encryption_key', self.encryption_key)
                    self.auth_token = config_data.get('auth_token', self.auth_token)

                    # AI model settings
                    self.ai_model_path = config_data.get('ai_model_path', self.ai_model_path)
                    self.ai_model_name = config_data.get('ai_model_name', self.ai_model_name)

                    # Health check settings
                    self.health_check_interval = config_data.get('health_check_interval', self.health_check_interval)
                    self.max_health_check_attempts = config_data.get('max_health_check_attempts', self.max_health_check_attempts)

                    # IoT device settings
                    self.iot_device_list = config_data.get('iot_device_list', self.iot_device_list)

                    # Time settings
                    self.timezone = config_data.get('timezone', self.timezone)

                    print("Settings loaded successfully.")

                except json.JSONDecodeError:
                    print(f"Error decoding JSON from {config_file}. Using default settings.")
                except Exception as e:
                    print(f"An error occurred while loading settings: {e}")
        else:
            print(f"Config file {config_file} not found. Using default settings.")

