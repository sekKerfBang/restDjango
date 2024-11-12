from dataclasses import dataclass
import requests
from getpass import getpass
import pathlib
import json


@dataclass
class JWTClient:
    '''
    Utilise le décorateur dataclass pour simplifier la construction de la classe JWTClient.
    '''
    access: str = None
    refresh: str = None
    # Assurez-vous que cela correspond à votre configuration de SimpleJWT
    header_type: str = "Bearer"
    # Assumons que DRF s'exécute sur localhost:8000
    base_endpoint: str = "http://localhost:8000/api/"
    # Ce chemin de fichier est potentiellement peu sécurisé
    cred_path: pathlib.Path = pathlib.Path("creds.json")
    
    def __post_init__(self):
        if self.cred_path.exists():
            # Vérifiez si des crédentiels sont stockés et essayez de les utiliser
            try:
                data = json.loads(self.cred_path.read_text())
            except Exception:
                print('Erreur lors de la lecture du fichier des crédentiels.')
                data = None
            if data is None:
                self.clear_tokens()
                self.perform_auth()
            else:
                self.access = data.get('access')
                self.refresh = data.get('refresh')
                token_verified = self.verify_token()
                if not token_verified:
                    refreshed = self.perform_refresh()
                    if not refreshed:
                        print("Données invalides, veuillez vous reconnecter.")
                        self.clear_tokens()
                        self.perform_auth()
        else:
            # Aucun fichier de crédentiels trouvé, exécutez le processus de connexion
            self.perform_auth()
    
    def get_headers(self, header_type=None):
        '''
        En-têtes par défaut pour les requêtes HTTP incluant le token JWT.
        '''
        _type = header_type or self.header_type   
        token = self.access
        if not token:
            return {}
        return {
            "Authorization": f"{_type} {token}"
        } 
        
    def perform_auth(self):
        '''
        Simple méthode d'authentification sans exposer les mots de passe lors de la collecte.
        '''    
        endpoint = f'{self.base_endpoint}token/'
        print(endpoint)
        username = input('Quel est votre nom ?\n')
        password = getpass('Quel est votre mot de passe ?\n')
        r = requests.post(endpoint, json={'username': username, 'password': password})
        if r.status_code != 200:
            self.clear_tokens()
            print("Erreur d'authentification :", r.json()) 
            return False
        refresh_data = r.json()
        if 'access' not in refresh_data:
            self.clear_tokens()
            print("Aucun token d'accès trouvé.")
            return False
        self.access = refresh_data.get('access')
        self.refresh = refresh_data.get('refresh')
        self.write_creds(refresh_data)
        return True 
    
    def write_creds(self, data):
        '''
        Écrit les données des tokens dans un fichier JSON sécurisé.
        '''
        self.cred_path.write_text(json.dumps(data))
    
    def clear_tokens(self):
        '''
        Supprime les tokens stockés et le fichier de crédentiels s'il existe.
        '''
        self.access = None
        self.refresh = None
        if self.cred_path.exists():
            self.cred_path.unlink()  # Supprime le fichier
    
    def verify_token(self):
        '''
        Vérifie si le token d'accès est valide (ajoutez votre logique ici si nécessaire).
        '''
        # Exemple simplifié : dans la réalité, vous devriez vérifier l'expiration du token
        return bool(self.access)
    
    def perform_refresh(self):
        '''
        Tente de rafraîchir le token d'accès à l'aide du token de rafraîchissement.
        '''
        if not self.refresh:
            return False
        endpoint = f'{self.base_endpoint}/token/refresh/'
        r = requests.post(endpoint, json={'refresh': self.refresh})
        if r.status_code != 200:
            return False
        refresh_data = r.json()
        self.access = refresh_data.get('access')
        if self.access:
            self.write_creds({'access': self.access, 'refresh': self.refresh})
            return True
        return False
    
    def list(self, endpoint=None, limit=3):
        '''
        Requête à une vue DRF nécessitant l'authentification SimpleJWT.
        '''
        if not self.access:
            raise Exception("Aucun token d'accès, veuillez vous authentifier.")
        headers = self.get_headers()
        if endpoint is None or self.base_endpoint not in str(endpoint):
            endpoint = f"http://127.0.0.1:8000/product/list-product/?limit={limit}"
        r = requests.get(endpoint, headers=headers)
        if r.status_code != 200:
            raise Exception(f"Requête non complétée {r.text}")
        data = r.json()
        return data

if __name__ == "__main__":
    '''
    Exemple d'utilisation de la classe JWTClient.
    '''        
    client = JWTClient()
    try:
        lookup_1_data = client.list(limit=5)
        results = lookup_1_data.get('results', [])
        print(lookup_1_data)
        next_url = lookup_1_data.get('next')
        print("Première recherche - Nombre de résultats :", len(results))
        if next_url:
            lookup_2_data = client.list(endpoint=next_url)
            results += lookup_2_data.get('results', [])
            print("Deuxième recherche - Nombre total de résultats :", len(results))
    except Exception as e:
        print("Erreur :", e)
