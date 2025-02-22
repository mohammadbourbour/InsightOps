# main.py

from IOT import Iot
from Servers import Servers
from Utils.logger import Logger
from AI.system_analysis import SystemAnalysis
from Monitoring.health_check import HealthCheck

class InsightOps:
    def __init__(self):
        self.iot = Iot()
        self.servers = Servers()
        self.logger = Logger()
        self.system_analysis = SystemAnalysis()
        self.health_check = HealthCheck()

    def run(self):
        self.logger.log("Starting InsightOps...")
        self.health_check.check_health()
        self.iot.setup_devices()
        self.servers.connect_to_servers()
        self.system_analysis.analyze_system()

if __name__ == "__main__":
    insight_ops = InsightOps()
    insight_ops.run()
