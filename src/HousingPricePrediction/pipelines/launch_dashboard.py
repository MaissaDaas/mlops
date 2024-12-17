from explainerdashboard import ExplainerDashboard

# Load the dashboard from the configuration file
ExplainerDashboard.from_config("artifacts/dashboard.yaml").run()