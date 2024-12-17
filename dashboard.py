from explainerdashboard import ExplainerDashboard
import joblib
import yaml

def load_dashboard():
    # Charger la configuration du tableau de bord à partir du fichier YAML
    with open('artifacts/dashboard.yaml', 'r') as f:
        config = yaml.safe_load(f)

    # Charger l'explainer à partir du fichier explainer.joblib
    explainer = joblib.load(config['dashboard']['explainerfile'])
    
    # Créer un tableau de bord avec la configuration YAML
    db = ExplainerDashboard(explainer, **config['dashboard']['params'])
    
    # Lancer le tableau de bord
    db.run()

if __name__ == '__main__':
    load_dashboard()
